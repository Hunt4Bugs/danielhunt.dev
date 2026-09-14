"""Markdown documents: front matter plus named body sections, read and written losslessly.

A document is front matter (YAML between `---` fences) and a body. The body is an optional H1
followed by `## `-delimited sections. Nothing here knows about concepts or contracts; it is the
file format only.
"""

from __future__ import annotations

import os
import re
import tempfile

import yaml

from .errors import DhError

FENCE = "---"
H1_RE = re.compile(r"^# (.+)$")
H2_RE = re.compile(r"^## (.+)$")
# A fenced code block can contain lines that look like headings; track them so a `## ` inside
# ```...``` is never mistaken for a section boundary.
CODE_FENCE_RE = re.compile(r"^(```|~~~)")


class Document:
    """One markdown file, parsed into front matter, an H1, and ordered body sections."""

    def __init__(self, path, front_matter=None, h1=None, sections=None, preamble=""):
        self.path = path
        self.front_matter = front_matter if front_matter is not None else {}
        self.h1 = h1
        # Ordered mapping of verbatim heading text -> raw section text (no trailing blank lines).
        self.sections = sections if sections is not None else {}
        # Text between the H1 and the first `## ` heading. Rare, preserved so round-trips are
        # lossless.
        self.preamble = preamble

    # -- reading ---------------------------------------------------------------

    @classmethod
    def parse(cls, text, path=None):
        front, body = cls._split_front_matter(text, path)
        h1, preamble, sections = cls._split_body(body)
        return cls(path=path, front_matter=front, h1=h1, sections=sections, preamble=preamble)

    @classmethod
    def read(cls, path):
        with open(path, "r", encoding="utf-8") as handle:
            return cls.parse(handle.read(), path=path)

    @staticmethod
    def _split_front_matter(text, path):
        lines = text.split("\n")
        if not lines or lines[0].strip() != FENCE:
            return {}, text
        for index in range(1, len(lines)):
            if lines[index].strip() == FENCE:
                raw = "\n".join(lines[1:index])
                try:
                    front = yaml.safe_load(raw) or {}
                except yaml.YAMLError as exc:
                    raise DhError(f"{path or '<text>'}: front matter is not valid YAML: {exc}")
                if not isinstance(front, dict):
                    raise DhError(f"{path or '<text>'}: front matter is not a mapping")
                return front, "\n".join(lines[index + 1 :])
        raise DhError(f"{path or '<text>'}: front matter fence is never closed")

    @staticmethod
    def _split_body(body):
        h1 = None
        preamble_lines = []
        sections = {}
        current = None
        current_lines = []
        in_code = False

        for line in body.split("\n"):
            if CODE_FENCE_RE.match(line):
                in_code = not in_code

            if not in_code:
                h1_match = H1_RE.match(line)
                if h1_match and h1 is None and current is None:
                    h1 = h1_match.group(1).strip()
                    continue
                h2_match = H2_RE.match(line)
                if h2_match:
                    if current is not None:
                        sections[current] = "\n".join(current_lines).strip("\n")
                    current = h2_match.group(1).strip()
                    current_lines = []
                    continue

            if current is None:
                preamble_lines.append(line)
            else:
                current_lines.append(line)

        if current is not None:
            sections[current] = "\n".join(current_lines).strip("\n")

        return h1, "\n".join(preamble_lines).strip("\n"), sections

    # -- section values --------------------------------------------------------

    def get_section(self, name):
        return self.sections.get(name)

    def set_section(self, name, text):
        self.sections[name] = text.strip("\n") if text else ""

    def section_bullets(self, name):
        """Return one value per `- ` bullet, or [] when the section is absent or empty."""
        raw = self.sections.get(name)
        if not raw:
            return []
        out = []
        for line in raw.split("\n"):
            stripped = line.strip()
            if stripped.startswith("- "):
                out.append(stripped[2:].strip())
        return out

    def section_prose(self, name):
        """Return the section's text with generated-marker comments stripped."""
        raw = self.sections.get(name)
        if raw is None:
            return None
        kept = [ln for ln in raw.split("\n") if not ln.strip().startswith("<!--")]
        return "\n".join(kept).strip("\n")

    # -- writing ---------------------------------------------------------------

    def render(self, key_order=None, section_order=None):
        parts = []
        if self.front_matter:
            parts.append(FENCE)
            parts.append(dump_front_matter(self.front_matter, key_order))
            parts.append(FENCE)
            parts.append("")
        if self.h1:
            parts.append(f"# {self.h1}")
            parts.append("")
        if self.preamble:
            parts.append(self.preamble)
            parts.append("")

        names = list(section_order) if section_order else []
        for name in self.sections:
            if name not in names:
                names.append(name)
        for name in names:
            if name not in self.sections:
                continue
            parts.append(f"## {name}")
            parts.append("")
            value = self.sections[name]
            if value:
                parts.append(value)
                parts.append("")

        text = "\n".join(parts).rstrip("\n")
        return text + "\n"

    def write(self, key_order=None, section_order=None, path=None):
        target = path or self.path
        if target is None:
            raise DhError("cannot write a document with no path")
        text = self.render(key_order=key_order, section_order=section_order)
        atomic_write(target, text)
        return text


class _IndentedDumper(yaml.SafeDumper):
    """Indent block sequences under their key, matching the style already in the corpus.

    PyYAML writes `key:\\n- item`; every file here writes `key:\\n  - item`. Without this the
    migration would rewrite every list line in the repository for no reason.
    """

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def dump_front_matter(mapping, key_order=None):
    """Serialize front matter deterministically: declared order first, block style throughout."""
    ordered = {}
    for key in key_order or []:
        if key in mapping:
            ordered[key] = mapping[key]
    for key, value in mapping.items():
        if key not in ordered:
            ordered[key] = value
    text = yaml.dump(
        ordered,
        Dumper=_IndentedDumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=100,
    )
    return text.rstrip("\n")


def atomic_write(path, text):
    """Write via a temp file in the same directory, then rename, so a crash cannot truncate."""
    directory = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(directory, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=directory, delete=False, suffix=".tmp"
    )
    try:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
        handle.close()
        os.replace(handle.name, path)
    except BaseException:
        handle.close()
        if os.path.exists(handle.name):
            os.unlink(handle.name)
        raise
