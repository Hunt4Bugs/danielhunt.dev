"""protocol-lint: closed-world validation of the model as written.

Every check here is a SHACL-shaped constraint or a protocol-structural one. None of them is an
OWL axiom, and that distinction is load-bearing: `sh:minCount: 1` fails when a value is missing,
while `owl:minCardinality 1` would infer the missing value into existence and could never fail.
See PROTOCOL.md §17.

Severity is scoped by status. A missing required value is an error on an `active` record and a
warning on a draft, blocked, superseded or archived one, because those statuses are already
honest labels for incompleteness.
"""

from __future__ import annotations

import os
import re

from . import types
from .contract import STORE_BODY
from .model import DOMAIN_CONCEPT, README_FILE

ERROR = "error"
WARN = "warn"
ADVISORY = "advisory"

STRICT_STATUS = "active"

# Distinguishes "the path exists but carries no readable type" from "nothing is there".
UNTYPED = object()

# Markdown links in a body, excluding images and absolute/external targets.
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
# Inline code spans and fenced blocks. Link syntax inside them is not a link, so stripping them
# first is what stops an illustrative `- [Label](path.md)` from being reported as a dead target.
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
CODE_BLOCK_RE = re.compile(r"^(```|~~~).*?^(```|~~~)", re.MULTILINE | re.DOTALL)


def strip_code(text):
    return CODE_SPAN_RE.sub(" ", CODE_BLOCK_RE.sub(" ", text or ""))


class Finding:
    def __init__(self, check, severity, message, file=None, line=None, hint=None):
        self.check = check
        self.severity = severity
        self.message = message
        self.file = file
        self.line = line
        self.hint = hint

    def as_dict(self):
        out = {"check": self.check, "severity": self.severity, "message": self.message}
        if self.file:
            out["file"] = self.file
        if self.line:
            out["line"] = self.line
        if self.hint:
            out["hint"] = self.hint
        return out

    def as_text(self):
        location = self.file or "<model>"
        if self.line:
            location = f"{location}:{self.line}"
        return f"{location}  {self.severity}  {self.check}  {self.message}"


class Linter:
    def __init__(self, model):
        self.model = model
        self.findings = []

    def report(self, check, severity, message, file=None, hint=None):
        self.findings.append(Finding(check, severity, message, file=file, hint=hint))

    def severity_for(self, document):
        """Errors are only errors on an active record; elsewhere they are warnings."""
        status = document.front_matter.get("status")
        return ERROR if status == STRICT_STATUS else WARN

    # -- entry point -----------------------------------------------------------

    def run(self, paths=None):
        for message in self.model.load_errors:
            self.report("model-load", ERROR, message)

        self.check_structure()
        self.check_contracts()
        self.check_ids()
        self.check_required_keys()
        self.check_status()
        self.check_links()
        self.check_ranges()
        self.check_taxonomy_values()
        self.check_body_sections()
        self.check_closed()
        self.check_sources_advisory()

        if paths:
            wanted = {os.path.abspath(p) for p in paths}

            def keeps(finding):
                if not finding.file:
                    return False
                absolute = os.path.join(self.model.root, finding.file)
                return any(
                    absolute == w or absolute.startswith(w.rstrip("/") + os.sep) for w in wanted
                )

            self.findings = [f for f in self.findings if keeps(f)]
        return self.findings

    # -- 1. structure ----------------------------------------------------------

    def check_structure(self):
        for domain in self.model.domains.values():
            for required in (README_FILE, "domain.md"):
                if not os.path.exists(os.path.join(domain.root, required)):
                    self.report(
                        "structure",
                        ERROR,
                        f"domain `{domain.id}` has no {required}",
                        file=self.model.rel(domain.root),
                    )
            concepts = [c for c in self.model.concepts.values() if c.domain_id == domain.id]
            if not concepts:
                self.report(
                    "structure",
                    ERROR,
                    f"domain `{domain.id}` declares no concepts",
                    file=self.model.rel(domain.root),
                    hint="a domain with nothing modelled is not yet a domain",
                )
            if domain.document.front_matter.get("rdf:type") != DOMAIN_CONCEPT:
                self.report(
                    "structure",
                    ERROR,
                    f"`{domain.id}` domain.md is not typed {DOMAIN_CONCEPT}",
                    file=self.model.rel(domain.document.path),
                )

        # An instance directory holds that concept's instances and its README, nothing else.
        for concept in self.model.concepts.values():
            for directory in self.model.instance_dirs(concept):
                if not os.path.isdir(directory):
                    continue
                for name in sorted(os.listdir(directory)):
                    if not name.endswith(".md") or name == README_FILE:
                        continue
                    path = os.path.join(directory, name)
                    instance = next(
                        (i for i in self.model.instances.values() if i.document.path == path),
                        None,
                    )
                    if instance is None:
                        self.report(
                            "structure",
                            ERROR,
                            f"not an instance of `{concept.id}`",
                            file=self.model.rel(path),
                            hint=f"this directory holds `{concept.id}` instances and README.md",
                        )

    # -- contracts -------------------------------------------------------------

    def check_contracts(self):
        for concept in self.model.concepts.values():
            for message in concept.contract.structural_errors():
                self.report(
                    "contract", ERROR, message, file=self.model.rel(concept.document.path)
                )
            if concept.mode == "directory" and not concept.title_field:
                self.report(
                    "contract",
                    ERROR,
                    f"`{concept.id}` persists as a directory but declares no title_field",
                    file=self.model.rel(concept.document.path),
                )

    # -- 2. ids ----------------------------------------------------------------

    def check_ids(self):
        seen = {}
        for document, _ in self._all_documents():
            identifier = document.front_matter.get("id")
            path = self.model.rel(document.path)
            if not identifier:
                continue
            if identifier in seen and seen[identifier] != path:
                self.report(
                    "ids", ERROR, f"id `{identifier}` is also used by {seen[identifier]}", file=path
                )
            seen[identifier] = path

        for instance in self.model.instances.values():
            path = self.model.rel(instance.document.path)
            parts = types.split_id(instance.id)
            expected_domain = instance.document.front_matter.get("domain")
            concept = self.model.concepts.get(instance.concept_id)

            # A class's id IS its class name: `<domain>.<slug>`, two segments, with no concept
            # slug to bind against. Every other instance is a resource and takes the full
            # `<domain>.<concept>.<name>` form that makes this check decidable.
            if concept and concept.instance_rdf_type == types.CLASS:
                if len(parts) != 2:
                    self.report(
                        "ids", ERROR, f"a class id must be <domain>.<name>, got `{instance.id}`",
                        file=path,
                    )
                elif parts[0] != expected_domain:
                    self.report(
                        "ids",
                        ERROR,
                        f"`{instance.id}` starts with `{parts[0]}` but domain is "
                        f"`{expected_domain}`",
                        file=path,
                    )
                elif not types.is_slug(parts[1]):
                    self.report("ids", ERROR, f"`{parts[1]}` is not a slug", file=path)
                continue

            if len(parts) < 3:
                self.report(
                    "ids",
                    ERROR,
                    f"`{instance.id}` is not <domain>.<concept>.<name>",
                    file=path,
                )
                continue
            if parts[0] != expected_domain:
                self.report(
                    "ids",
                    ERROR,
                    f"`{instance.id}` starts with `{parts[0]}` but domain is `{expected_domain}`",
                    file=path,
                )
            expected_concept = types.concept_slug(instance.concept_id)
            if parts[1] != expected_concept:
                self.report(
                    "ids",
                    ERROR,
                    f"`{instance.id}` says `{parts[1]}` but rdf:type is `{instance.concept_id}`",
                    file=path,
                    hint=f"expected {expected_domain}.{expected_concept}.<name>",
                )
            name = ".".join(parts[2:])
            if not types.is_slug(name):
                self.report("ids", ERROR, f"`{name}` is not a well-formed slug", file=path)

    # -- 3. required keys ------------------------------------------------------

    REQUIRED_KEYS = ("id", "rdf:type", "domain", "status", "version")

    def check_required_keys(self):
        for document, _ in self._all_documents():
            path = self.model.rel(document.path)
            for key in self.REQUIRED_KEYS:
                if key not in document.front_matter:
                    self.report("required-keys", ERROR, f"missing `{key}`", file=path)

    # -- 4. status -------------------------------------------------------------

    def check_status(self):
        scheme = self.model.taxonomies_by_name.get("Status")
        if not scheme:
            self.report("status", ERROR, "no `Status` vocabulary is declared")
            return
        allowed = set(scheme.labels)
        for document, _ in self._all_documents():
            status = document.front_matter.get("status")
            if status is None:
                continue
            if status not in allowed:
                self.report(
                    "status",
                    ERROR,
                    f"`{status}` is not a Status value",
                    file=self.model.rel(document.path),
                    hint=f"one of: {', '.join(sorted(allowed))}",
                )

    # -- 5. links --------------------------------------------------------------

    def check_links(self):
        for document, _ in self._all_documents():
            path = self.model.rel(document.path)
            directory = os.path.dirname(document.path)
            targets = []
            for key in ("related", "sources"):
                value = document.front_matter.get(key) or []
                if isinstance(value, str):
                    value = [value]
                targets.extend((key, item) for item in value)
            for section_text in document.sections.values():
                for match in LINK_RE.finditer(strip_code(section_text)):
                    targets.append(("body", match.group(1)))

            for origin, target in targets:
                if not isinstance(target, str) or not target:
                    continue
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                file_part = target.split("#", 1)[0]
                if not file_part:
                    continue
                resolved = os.path.normpath(os.path.join(directory, file_part))
                if not os.path.exists(resolved):
                    self.report(
                        "links",
                        ERROR,
                        f"{origin} link `{target}` does not resolve",
                        file=path,
                    )

    # -- 6. ranges -------------------------------------------------------------

    def check_ranges(self):
        for concept in self.model.concepts.values():
            path = self.model.rel(concept.document.path)
            for spec in concept.contract.properties:
                target = spec.range
                if not isinstance(target, str):
                    continue
                # Checked for every range, prefixed or not. A controlled property whose scheme
                # does not exist would otherwise accept any value at all: the membership check
                # silently has nothing to check against.
                if spec.is_controlled and spec.in_scheme not in self.model.taxonomies:
                    self.report(
                        "ranges",
                        ERROR,
                        f"`{spec.id}` is in scheme `{spec.in_scheme}`, which does not exist",
                        file=path,
                        hint="its values cannot be validated until the scheme is declared",
                    )

                if types.is_prefixed(target):
                    prefix = types.prefix_of(target)
                    if prefix not in self.model.prefixes:
                        self.report(
                            "ranges", ERROR, f"`{target}` uses an unbound prefix", file=path
                        )
                    continue
                if target not in self.model.concepts:
                    self.report(
                        "ranges",
                        ERROR,
                        f"`{spec.id}` ranges over `{target}`, which is not a concept",
                        file=path,
                    )

        # Instance-level: a reference must resolve, AND what it resolves to must be an instance
        # of the declared range. Existence alone is not type-checking -- without the second half,
        # a property ranging over one concept happily points at a file of another.
        for instance in self.model.instances.values():
            contract = self.model.contract_for(instance)
            if not contract:
                continue
            path = self.model.rel(instance.document.path)
            for spec in contract.properties:
                if not spec.is_object_property or spec.is_controlled or spec.is_derived:
                    continue
                for value in spec.read_authored(instance.document):
                    if not value:
                        continue
                    match = LINK_RE.search(str(value))
                    target = match.group(1) if match else str(value)
                    self._check_reference(instance, spec, target, path)


    def _check_reference(self, instance, spec, target, path):
        """Resolve one reference value and verify its type against the property's range."""
        found = self.resolve_reference(instance, target)
        if found is None:
            self.report(
                "ranges",
                self.severity_for(instance.document),
                f"`{spec.id}` references `{target}`, which does not resolve",
                file=path,
            )
            return
        if found is UNTYPED:
            # The path exists but carries no type we can read -- a file not yet conformed.
            # Reportable, but not the same defect as pointing at the wrong kind of thing.
            self.report(
                "ranges",
                self.severity_for(instance.document),
                f"`{spec.id}` references `{target}`, which is not a typed record",
                file=path,
                hint="it cannot be checked against the declared range until it is conformed",
            )
            return
        if found.concept_id != spec.range:
            self.report(
                "ranges",
                ERROR,
                f"`{spec.id}` ranges over `{spec.range}` but `{target}` is a "
                f"`{found.concept_id}`",
                file=path,
            )

    def resolve_reference(self, instance, target):
        """An instance id or a relative path -> the Instance it names.

        Returns None when nothing is there, and UNTYPED when a file exists but is not a loaded
        instance. The two are different findings, so they stay distinguishable here.
        """
        if target in self.model.instances:
            return self.model.instances[target]
        directory = os.path.dirname(instance.document.path)
        resolved = os.path.normpath(os.path.join(directory, target.split("#", 1)[0]))
        if not os.path.exists(resolved):
            return None
        for candidate in self.model.instances.values():
            if os.path.abspath(candidate.document.path) == os.path.abspath(resolved):
                return candidate
        return UNTYPED

    # -- 7. taxonomy values ----------------------------------------------------

    def check_taxonomy_values(self):
        for instance in self.model.instances.values():
            contract = self.model.contract_for(instance)
            if not contract:
                continue
            path = self.model.rel(instance.document.path)
            for spec in contract.properties:
                if not spec.is_controlled or spec.is_derived:
                    continue
                scheme = self.model.taxonomies.get(spec.in_scheme)
                if not scheme:
                    # The missing scheme is reported once, against the concept that declares it
                    # (check_ranges). Repeating it per instance would bury that one finding.
                    continue
                allowed = set(scheme.labels)
                for value in spec.read_authored(instance.document):
                    if value not in allowed:
                        self.report(
                            "taxonomy-values",
                            self.severity_for(instance.document),
                            f"`{spec.id}` = '{value}' is not in {scheme.name}",
                            file=path,
                            hint=(
                                f"owner: {self.model.rel(scheme.document.path)}; "
                                "propose through govern-taxonomy, never inline"
                            ),
                        )

    # -- body sections + cardinality -------------------------------------------

    def check_body_sections(self):
        for instance in self.model.instances.values():
            contract = self.model.contract_for(instance)
            if not contract:
                continue
            document = instance.document
            path = self.model.rel(document.path)
            severity = self.severity_for(document)
            declared = set(contract.declared_sections)

            if declared:
                for heading in document.sections:
                    if heading not in declared:
                        self.report(
                            "body-sections",
                            ERROR,
                            f"`## {heading}` is not a declared section",
                            file=path,
                            hint=f"declare it on {instance.concept_id} or remove it",
                        )

            for spec in contract.properties:
                # Count what the file authored, not what read() projects to. A single-valued
                # property projects a two-element list down to a scalar, so counting the
                # projection would report 1 and hide the very violation being checked.
                count = len(spec.read_authored(document))
                if spec.min_count and count < spec.min_count:
                    self.report(
                        "cardinality",
                        severity,
                        f"`{spec.id}` needs at least {spec.min_count} value(s), found {count}",
                        file=path,
                    )
                if spec.max_count is not None and count > spec.max_count:
                    self.report(
                        "cardinality",
                        ERROR,
                        f"`{spec.id}` allows at most {spec.max_count}, found {count}",
                        file=path,
                    )

            # The H1 is derived presentation: it renders title_field and is never read as data.
            concept = self.model.concepts.get(instance.concept_id)
            if concept and concept.title_field:
                spec = contract.get(concept.title_field)
                if spec:
                    expected = spec.read(document)
                    if isinstance(expected, list):
                        expected = expected[0] if expected else None
                    if expected and document.h1 and document.h1.strip() != str(expected).strip():
                        self.report(
                            "title",
                            severity,
                            f"H1 '{document.h1}' does not match {concept.title_field}"
                            f" '{expected}'",
                            file=path,
                        )

    # -- closed shape ----------------------------------------------------------

    def check_closed(self):
        allowed_always = {
            "id",
            "rdf:type",
            "domain",
            "previous_id",
            "supersedes",
            "superseded_by",
            "owl:deprecated",
            "legacy_frontmatter",
        }
        record_keys = {spec.key for spec in self.model.record_properties}
        for instance in self.model.instances.values():
            contract = self.model.contract_for(instance)
            if not contract:
                continue
            permitted = set(allowed_always) | record_keys | {
                spec.key for spec in contract.properties if spec.store != STORE_BODY
            }
            path = self.model.rel(instance.document.path)
            for key in instance.document.front_matter:
                if key in permitted:
                    continue
                hint = None
                if key in types.FORBIDDEN_TERMS:
                    hint = types.FORBIDDEN_TERMS[key]
                elif types.is_prefixed(key) and types.prefix_of(key) not in self.model.prefixes:
                    hint = "unbound prefix"
                self.report(
                    "closed",
                    ERROR,
                    f"`{key}` is not declared by {instance.concept_id}",
                    file=path,
                    hint=hint,
                )

    # -- 10. sources (advisory only) -------------------------------------------

    PLACEHOLDERS = ("TBD", "TODO", "XXX", "???")

    def check_sources_advisory(self):
        for document, _ in self._all_documents():
            path = self.model.rel(document.path)
            status = document.front_matter.get("status")
            # `draft` IS the explicit unknown label check 10 asks for. Flagging it would punish
            # the honest state, so draft records produce no finding at all.
            if status != STRICT_STATUS:
                continue
            body = "\n".join(document.sections.values())
            sources = document.front_matter.get("sources") or []
            if not sources and len(body) > 200:
                self.report(
                    "sources",
                    ADVISORY,
                    "active record with substantial prose and no `sources`",
                    file=path,
                    hint="not machine-checkable; set status: draft or add sources",
                )
            for marker in self.PLACEHOLDERS:
                if marker in body:
                    self.report(
                        "sources",
                        WARN,
                        f"active record contains an unfilled `{marker}`",
                        file=path,
                    )
                    break

    # -- helpers ---------------------------------------------------------------

    def _all_documents(self):
        """Every document exactly once.

        Concepts and taxonomies are also instances of their meta-concepts, so a naive walk would
        report each of them twice.
        """
        seen = set()
        groups = (
            (self.model.domains.values(), "domain"),
            (self.model.concepts.values(), "concept"),
            (self.model.taxonomies.values(), "taxonomy"),
            (self.model.instances.values(), "instance"),
        )
        for items, role in groups:
            for item in items:
                path = item.document.path
                if path in seen:
                    continue
                seen.add(path)
                yield item.document, role


def counts(findings):
    out = {ERROR: 0, WARN: 0, ADVISORY: 0}
    for finding in findings:
        out[finding.severity] = out.get(finding.severity, 0) + 1
    return out
