"""Conform Creator and Creator Channel records to protocol v1.0.

A one-off, dated sweep. It is committed rather than thrown away because a 48-file mechanical diff
is unreviewable without the rule that produced it, and because it may need to run again on
another branch. `dh` never imports from this package.

The sweep moves values between storage locations and renames keys. It does not invent, drop, or
reword any value — that property is what the round-trip check in the test suite asserts.

    uv run python -m dh.migrate.m2026_09_14_creator_slice          # diff only
    uv run python -m dh.migrate.m2026_09_14_creator_slice --write
"""

from __future__ import annotations

import argparse
import difflib
import os
import sys

from ..doc import Document
from ..model import Model, find_root

# Body headings whose values move into front matter, per the new contract.
CREATOR_TO_FRONTMATTER = {
    "Creator Type": "creator_type",
    "Relationships": "creator_relationships",
}
CHANNEL_TO_FRONTMATTER = {
    "Creator": "creator",
    "Channel": "channel",
    "Handle": "handle",
    "URL": "url",
}

# Keys the v1.0 front matter no longer carries.
DROPPED_KEYS = ("kind", "class", "collection", "type")

MULTI_VALUE = {"creator_relationships"}


def split_values(text):
    """Read a body value that may be bullets, a comma list, or a single line."""
    if not text:
        return []
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    bullets = [line[2:].strip() for line in lines if line.startswith("- ")]
    if bullets:
        return bullets
    joined = " ".join(lines)
    if "," in joined:
        return [part.strip().rstrip(".") for part in joined.split(",") if part.strip()]
    return [joined.rstrip(".")]


def link_target(text):
    """`[label](../x.md)` -> `../x.md`; a bare path is returned unchanged."""
    if "](" in text:
        return text.split("](", 1)[1].rstrip(")")
    return text.strip()


def link_label(text):
    """`[YouTube](../channels.md)` -> `YouTube`.

    Channel used to be a reference to a registry file and is now a controlled value, so the label
    is the datum and the link is incidental.
    """
    if "](" in text and text.lstrip().startswith("["):
        return text.split("](", 1)[0].lstrip().lstrip("[")
    return text.strip()


def migrate_creator(document, concept_id="content.creator"):
    front = document.front_matter
    front["rdf:type"] = concept_id
    for key in DROPPED_KEYS:
        front.pop(key, None)

    # The H1 is the name. It stays as the H1, but the value it renders now has a home.
    if document.h1 and "name" not in front:
        front["name"] = document.h1.strip()

    for heading, key in CREATOR_TO_FRONTMATTER.items():
        if heading not in document.sections:
            continue
        values = split_values(document.sections.pop(heading))
        if not values:
            continue
        front[key] = values if key in MULTI_VALUE else values[0]

    # `Niches` was bullets in some records and a comma-separated sentence in others. The contract
    # says list, so both are normalized to bullets; no niche is added or removed.
    if "Niches" in document.sections:
        niches = split_values(document.sections["Niches"])
        document.set_section("Niches", "\n".join(f"- {n}" for n in niches))

    return document


def migrate_channel(document, concept_id="content.creator-channel"):
    front = document.front_matter
    front["rdf:type"] = concept_id
    for key in DROPPED_KEYS:
        front.pop(key, None)

    if document.h1 and "name" not in front:
        front["name"] = document.h1.strip()

    for heading, key in CHANNEL_TO_FRONTMATTER.items():
        if heading not in document.sections:
            continue
        values = split_values(document.sections.pop(heading))
        if not values:
            continue
        front[key] = values[0]

    # `creator` stays a reference, so it keeps the path. `channel` became a controlled value, so
    # the label is the datum. Normalize whether the value came from the body just now or from an
    # earlier pass that already moved it.
    if isinstance(front.get("creator"), str):
        front["creator"] = link_target(front["creator"])
    if isinstance(front.get("channel"), str):
        front["channel"] = link_label(front["channel"])

    return document


PLANS = (
    ("creators", "content.creator", migrate_creator),
    ("creator-channels", "content.creator-channel", migrate_channel),
)


def run(root, write=False):
    model = Model.load(root)
    domain = model.domains.get("content")
    base = domain.root if domain else os.path.join(root, "docs", "40_content")
    changed = []

    for directory, concept_id, migrate in PLANS:
        concept = model.concepts.get(concept_id)
        if not concept:
            print(f"skip {directory}: no {concept_id} concept", file=sys.stderr)
            continue
        target = os.path.join(base, directory)
        if not os.path.isdir(target):
            continue
        for name in sorted(os.listdir(target)):
            if not name.endswith(".md") or name == "README.md":
                continue
            path = os.path.join(target, name)
            before = open(path, encoding="utf-8").read()
            document = migrate(Document.parse(before, path=path), concept_id)
            after = document.render(
                key_order=concept.contract.key_order(),
                section_order=concept.contract.section_order(),
            )
            if after == before:
                continue
            changed.append(path)
            if write:
                document.write(
                    key_order=concept.contract.key_order(),
                    section_order=concept.contract.section_order(),
                )
            else:
                sys.stdout.writelines(
                    difflib.unified_diff(
                        before.splitlines(keepends=True),
                        after.splitlines(keepends=True),
                        fromfile=os.path.relpath(path, root),
                        tofile=os.path.relpath(path, root),
                    )
                )
    verb = "migrated" if write else "would migrate"
    print(f"{verb} {len(changed)} files", file=sys.stderr)
    return changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    run(args.root or find_root(), write=args.write)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
