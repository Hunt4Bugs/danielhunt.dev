"""Loading the whole model from the filesystem.

The only literal paths here are `docs/`, the five structural names the protocol defines, and one
bootstrap axiom: `docs/_protocol/concepts/concept.md`. To read a concept you need the contract for
`protocol.concept`, and that contract is itself a concept file — so the bootstrap reads that one
path directly, builds the contract, and then re-validates the file against it. Everything after
that, including every domain's concepts, loads through the general path.

No domain name appears anywhere in this module. That is enforced by a test.
"""

from __future__ import annotations

import glob
import os

from . import types
from .contract import Contract, PropertySpec
from .doc import Document
from .errors import ModelError, NotFound

DOCS_DIR = "docs"

# Structural names the protocol defines (§8). Not domain names.
DOMAIN_FILE = "domain.md"
README_FILE = "README.md"
CONCEPTS_DIR = "concepts"
TAXONOMIES_DIR = "taxonomies"
WORKFLOWS_DIR = "workflows"

BOOTSTRAP_CONCEPT = os.path.join("_protocol", CONCEPTS_DIR, "concept.md")
BOOTSTRAP_DOMAIN = os.path.join("_protocol", DOMAIN_FILE)

# The meta-concept a domain declaration is typed with.
DOMAIN_CONCEPT = "protocol.domain"

# Default header -> SKOS term for taxonomy value tables. A header outside this map needs an
# explicit `columns` entry; lint fails rather than dropping the column.
DEFAULT_COLUMNS = {
    "definition": "skos:definition",
    "meaning": "skos:definition",
    "use": "skos:definition",
    "description": "skos:definition",
    "stable code": "skos:notation",
    "code": "skos:notation",
    "notation": "skos:notation",
    "broader": "skos:broader",
    "parent": "skos:broader",
    "note": "skos:scopeNote",
    "notes": "skos:scopeNote",
    "example": "skos:example",
    "alias": "skos:altLabel",
    "aliases": "skos:altLabel",
    "also known as": "skos:altLabel",
}


class Domain:
    def __init__(self, identifier, root, document):
        self.id = identifier
        self.root = root  # absolute
        self.document = document

    @property
    def label(self):
        return self.document.front_matter.get("rdfs:label", self.id)


class Concept:
    def __init__(self, identifier, document, contract, domain_id):
        self.id = identifier
        self.document = document
        self.contract = contract
        self.domain_id = domain_id

    @property
    def persistence(self):
        return self.document.front_matter.get("persistence") or {}

    @property
    def mode(self):
        return self.persistence.get("mode")

    @property
    def path(self):
        return self.persistence.get("path")

    @property
    def scope(self):
        return self.persistence.get("scope", "own")

    @property
    def title_field(self):
        return self.document.front_matter.get("title_field")

    @property
    def instance_rdf_type(self):
        """The `rdf:type` value this concept's instances carry.

        Usually the concept's own id. The meta-concepts are the exception: a concept file is an
        instance of `protocol.concept` and simultaneously *is* an `owl:Class`, so it declares the
        standard term as its marker. RDF permits both assertions; the file writes the one that
        says what the thing is.
        """
        return self.document.front_matter.get("instance_rdf_type", self.id)

    @property
    def label(self):
        return self.document.front_matter.get("rdfs:label", self.id)


class Taxonomy:
    def __init__(self, identifier, name, document, values, columns, domain_id):
        self.id = identifier
        self.name = name
        self.document = document
        self.values = values  # list of dicts, always carrying skos:prefLabel
        self.columns = columns  # header -> term or mapping
        self.domain_id = domain_id

    @property
    def labels(self):
        return [row["skos:prefLabel"] for row in self.values]


class Instance:
    def __init__(self, identifier, concept_id, document, domain_id):
        self.id = identifier
        self.concept_id = concept_id
        self.document = document
        self.domain_id = domain_id


class Model:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.docs = os.path.join(self.root, DOCS_DIR)
        self.base_iri = ""
        self.vocab_iri = ""
        self.prefixes = {}
        self.record_properties = []
        self.domains = {}
        self.concepts = {}
        self.taxonomies = {}  # by id
        self.taxonomies_by_name = {}
        self.instances = {}
        self.load_errors = []

    # -- entry point -----------------------------------------------------------

    @classmethod
    def load(cls, root=None):
        model = cls(root or find_root())
        model._load_bootstrap()
        model._load_domains()
        model._load_concepts()
        model._load_taxonomies()
        model._load_instances()
        return model

    def rel(self, path):
        return os.path.relpath(path, self.root)

    # -- bootstrap -------------------------------------------------------------

    def _load_bootstrap(self):
        """Read the prefix binding, then the one concept file that defines concept files."""
        domain_path = os.path.join(self.docs, BOOTSTRAP_DOMAIN)
        if not os.path.exists(domain_path):
            raise ModelError(
                f"missing {self.rel(domain_path)}",
                hint="the protocol domain declares the prefix binding and record properties",
            )
        domain_doc = Document.read(domain_path)
        front = domain_doc.front_matter
        self.base_iri = front.get("base_iri", "")
        self.vocab_iri = front.get("vocab_iri", "")
        self.prefixes = front.get("prefixes") or {}
        self.record_properties = [
            PropertySpec(raw, concept_id="protocol.record")
            for raw in front.get("record_properties") or []
        ]

        concept_path = os.path.join(self.docs, BOOTSTRAP_CONCEPT)
        if not os.path.exists(concept_path):
            raise ModelError(
                f"missing bootstrap axiom {self.rel(concept_path)}",
                hint="this file is an instance of itself; the engine cannot start without it",
            )
        doc = Document.read(concept_path)
        self._concept_contract = self._contract_from(doc)
        # Re-validate the axiom against the contract it just defined.
        problems = self._concept_contract.structural_errors()
        if problems:
            raise ModelError(
                "the bootstrap concept does not satisfy its own contract: " + "; ".join(problems)
            )

    def _contract_from(self, document):
        identifier = document.front_matter.get("id")
        raws = document.front_matter.get("properties") or []
        specs = [PropertySpec(raw, concept_id=identifier) for raw in raws]
        return Contract(
            identifier,
            specs,
            record_properties=self.record_properties,
            title_field=document.front_matter.get("title_field"),
        )

    # -- domains, concepts, taxonomies ----------------------------------------

    def _load_domains(self):
        for path in sorted(glob.glob(os.path.join(self.docs, "*", DOMAIN_FILE))):
            doc = Document.read(path)
            # A domain is declared by its type, not by its filename. Files that merely happen to
            # be called domain.md (a pattern, a template) are not domains.
            if doc.front_matter.get("rdf:type") != DOMAIN_CONCEPT:
                continue
            identifier = doc.front_matter.get("id")
            if not identifier:
                self.load_errors.append(f"{self.rel(path)}: missing `id`")
                continue
            self.domains[identifier] = Domain(identifier, os.path.dirname(path), doc)

    def _load_concepts(self):
        for domain in self.domains.values():
            pattern = os.path.join(domain.root, CONCEPTS_DIR, "*.md")
            for path in sorted(glob.glob(pattern)):
                if os.path.basename(path) == README_FILE:
                    continue
                doc = Document.read(path)
                identifier = doc.front_matter.get("id")
                if not identifier:
                    self.load_errors.append(f"{self.rel(path)}: missing `id`")
                    continue
                contract = self._contract_from(doc)
                self.concepts[identifier] = Concept(identifier, doc, contract, domain.id)

    def _load_taxonomies(self):
        for domain in self.domains.values():
            pattern = os.path.join(domain.root, TAXONOMIES_DIR, "*.md")
            for path in sorted(glob.glob(pattern)):
                if os.path.basename(path) == README_FILE:
                    continue
                doc = Document.read(path)
                identifier = doc.front_matter.get("id")
                name = doc.front_matter.get("skos:prefLabel")
                if not identifier or not name:
                    self.load_errors.append(
                        f"{self.rel(path)}: a taxonomy needs `id` and `skos:prefLabel`"
                    )
                    continue
                columns = doc.front_matter.get("columns") or {}
                values, problems = parse_values_table(doc.get_section("Values"), columns)
                for problem in problems:
                    self.load_errors.append(f"{self.rel(path)}: {problem}")
                taxonomy = Taxonomy(identifier, name, doc, values, columns, domain.id)
                self.taxonomies[identifier] = taxonomy
                if name in self.taxonomies_by_name:
                    other = self.rel(self.taxonomies_by_name[name].document.path)
                    self.load_errors.append(
                        f"{self.rel(path)}: vocabulary '{name}' is already owned by {other}"
                    )
                else:
                    self.taxonomies_by_name[name] = taxonomy

    # -- instances -------------------------------------------------------------

    def instance_dirs(self, concept):
        """Every directory holding this concept's instances, per its persistence declaration."""
        if concept.mode != "directory" or not concept.path:
            return []
        if concept.scope == "all-domains":
            return [
                os.path.join(domain.root, concept.path) for domain in self.domains.values()
            ]
        domain = self.domains.get(concept.domain_id)
        return [os.path.join(domain.root, concept.path)] if domain else []

    def _load_instances(self):
        for concept in self.concepts.values():
            for directory in self.instance_dirs(concept):
                for path in sorted(glob.glob(os.path.join(directory, "*.md"))):
                    if os.path.basename(path) == README_FILE:
                        continue
                    doc = Document.read(path)
                    identifier = doc.front_matter.get("id")
                    declared = doc.front_matter.get("rdf:type")
                    if not identifier:
                        continue
                    # A directory holds instances of one concept, but a file that has not been
                    # migrated yet may carry no rdf:type at all; skip rather than mistype it.
                    if declared != concept.instance_rdf_type:
                        continue
                    if identifier in self.instances:
                        continue
                    self.instances[identifier] = Instance(
                        identifier, concept.id, doc, concept.domain_id
                    )

    # -- lookup ----------------------------------------------------------------

    def concept(self, concept_id):
        found = self.concepts.get(concept_id)
        if not found:
            raise NotFound(f"no concept `{concept_id}`", hint="try `dh concepts`")
        return found

    def instance(self, instance_id):
        found = self.instances.get(instance_id)
        if not found:
            raise NotFound(f"no instance `{instance_id}`")
        return found

    def taxonomy(self, name):
        found = self.taxonomies_by_name.get(name) or self.taxonomies.get(name)
        if not found:
            raise NotFound(f"no vocabulary `{name}`", hint="try `dh taxonomy list`")
        return found

    def instances_of(self, concept_id):
        return [item for item in self.instances.values() if item.concept_id == concept_id]

    def contract_for(self, instance):
        concept = self.concepts.get(instance.concept_id)
        return concept.contract if concept else None


def parse_values_table(raw, columns=None):
    """Parse a row-per-value markdown table. Column 1 is always skos:prefLabel."""
    if not raw:
        return [], ["the `Values` section is empty"]
    columns = columns or {}
    problems = []
    rows = []
    header = None

    for line in raw.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = split_row(stripped)
        if header is None:
            header = cells
            continue
        if all(set(cell) <= {"-", ":"} and cell for cell in cells):
            continue
        rows.append(cells)

    if header is None:
        return [], ["the `Values` section has no table"]

    terms = []
    for index, name in enumerate(header):
        if index == 0:
            terms.append("skos:prefLabel")
            continue
        mapped = columns.get(name)
        if mapped is None:
            mapped = DEFAULT_COLUMNS.get(name.lower())
        if mapped is None:
            problems.append(
                f"column '{name}' maps to no term; add a `columns` entry so it is not dropped"
            )
            terms.append(None)
        else:
            terms.append(mapped)

    values = []
    seen_slugs = {}
    for cells in rows:
        row = {}
        for index, cell in enumerate(cells):
            if index >= len(terms) or terms[index] is None or not cell:
                continue
            term = terms[index] if isinstance(terms[index], str) else None
            if term:
                row[term] = cell
        label = row.get("skos:prefLabel")
        if not label:
            continue
        value_slug = types.slug(label)
        if value_slug in seen_slugs:
            problems.append(
                f"'{label}' and '{seen_slugs[value_slug]}' both slug to '{value_slug}'"
            )
        seen_slugs[value_slug] = label
        row["slug"] = value_slug
        values.append(row)

    return values, problems


def split_row(line):
    """Split a markdown table row, honouring `\\|` as an escaped literal pipe."""
    cells = []
    current = []
    index = 0
    while index < len(line):
        char = line[index]
        if char == "\\" and index + 1 < len(line) and line[index + 1] == "|":
            current.append("|")
            index += 2
            continue
        if char == "|":
            cells.append("".join(current).strip())
            current = []
            index += 1
            continue
        current.append(char)
        index += 1
    cells.append("".join(current).strip())
    # A well-formed row starts and ends with `|`, producing empty edge cells.
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def find_root(start=None):
    """Walk up until a directory containing docs/ is found."""
    current = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isdir(os.path.join(current, DOCS_DIR)):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise ModelError(
                "no docs/ directory found above the working directory",
                hint="run from inside the repository",
            )
        current = parent
