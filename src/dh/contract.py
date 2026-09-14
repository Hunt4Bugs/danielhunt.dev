"""Property contracts: what a concept declares, and how to read or write a value for it.

A PropertySpec is one entry of a concept's `properties` list. A Contract is the whole list plus
the record properties every file carries. Declaration order is serialization order.
"""

from __future__ import annotations

from . import types
from .errors import ModelError

STORE_FRONTMATTER = "frontmatter"
STORE_BODY = "body"

FORMAT_PROSE = "prose"
FORMAT_LIST = "list"
FORMAT_TABLE = "table"


class PropertySpec:
    """One declared property: its range, its cardinality, and where its value lives."""

    def __init__(self, raw, concept_id=None):
        if not isinstance(raw, dict):
            raise ModelError(f"{concept_id}: each entry of `properties` must be a mapping")
        self.raw = raw
        self.concept_id = concept_id
        self.id = raw.get("id")
        if not self.id:
            raise ModelError(f"{concept_id}: a property entry is missing `id`")
        self.rdf_type = raw.get("rdf:type")
        self.label = raw.get("rdfs:label")
        self.comment = raw.get("rdfs:comment")
        self.range = raw.get("rdfs:range")
        self.in_scheme = raw.get("skos:inScheme")
        self.min_count = raw.get("sh:minCount")
        self.max_count = raw.get("sh:maxCount")
        self.pattern = raw.get("sh:pattern")
        self.store = raw.get("store")
        self.section = raw.get("section")
        self.format = raw.get("format")
        self.key = raw.get("key") or self.id
        self.derived = raw.get("derived")
        self.writable_after = raw.get("writable_after")

    # -- shape ---------------------------------------------------------------

    @property
    def is_derived(self):
        return bool(self.derived)

    @property
    def inverse_of(self):
        if not isinstance(self.derived, dict):
            return None
        return self.derived.get("owl:inverseOf") or self.derived.get("inverse_of")

    @property
    def index_of(self):
        if not isinstance(self.derived, dict):
            return None
        return self.derived.get("index_of")

    @property
    def is_object_property(self):
        return self.rdf_type == types.OBJECT_PROPERTY

    @property
    def is_controlled(self):
        return self.range == types.SKOS_CONCEPT

    @property
    def is_multivalued(self):
        return self.max_count is None or self.max_count > 1

    @property
    def required(self):
        return bool(self.min_count)

    def structural_errors(self):
        """Contract-level problems: a property that could never be read or written correctly."""
        problems = []
        where = f"{self.concept_id}.{self.id}"

        if self.rdf_type not in (types.OBJECT_PROPERTY, types.DATATYPE_PROPERTY):
            problems.append(
                f"{where}: rdf:type must be {types.OBJECT_PROPERTY} or {types.DATATYPE_PROPERTY}"
            )
        if not self.range:
            problems.append(f"{where}: rdfs:range is required")
        if self.store not in (STORE_FRONTMATTER, STORE_BODY):
            problems.append(f"{where}: store must be '{STORE_FRONTMATTER}' or '{STORE_BODY}'")

        if self.store == STORE_BODY:
            if not self.section:
                problems.append(f"{where}: store: body requires a verbatim `section`")
            if self.format not in (FORMAT_PROSE, FORMAT_LIST, FORMAT_TABLE):
                problems.append(f"{where}: store: body requires format prose, list or table")
            if self.format == FORMAT_PROSE and self.max_count not in (1, None):
                problems.append(f"{where}: format: prose requires sh:maxCount 1")
            if self.range in types.XSD_RANGES - {"xsd:string"}:
                problems.append(f"{where}: only xsd:string, refs and lists may be stored in body")
        elif self.store == STORE_FRONTMATTER and self.section:
            problems.append(f"{where}: `section` is meaningless with store: frontmatter")

        if self.is_controlled and not self.in_scheme:
            problems.append(f"{where}: a {types.SKOS_CONCEPT} range requires skos:inScheme")

        # A derived value is computed, so there is no authored value to constrain. A constraint
        # here would be vacuous or would fail on correct data.
        if self.is_derived and (self.min_count or self.max_count or self.pattern):
            problems.append(f"{where}: a derived property carries no sh: constraints")

        for term, why in types.FORBIDDEN_TERMS.items():
            if term in self.raw:
                problems.append(f"{where}: `{term}` is not part of this vocabulary — {why}")

        return problems

    # -- values --------------------------------------------------------------

    def read(self, document):
        """Return this property's value(s) from a document, normalized to the declared shape."""
        if self.store == STORE_FRONTMATTER:
            value = document.front_matter.get(self.key)
            return self._normalize(value)
        if self.format == FORMAT_LIST:
            return document.section_bullets(self.section)
        value = document.section_prose(self.section)
        return self._normalize(value)

    def _normalize(self, value):
        if value is None:
            return [] if self.is_multivalued else None
        if self.is_multivalued:
            return list(value) if isinstance(value, list) else [value]
        if isinstance(value, list):
            return value[0] if value else None
        return value

    def write(self, document, value):
        values = value if isinstance(value, list) else ([] if value is None else [value])
        if self.store == STORE_FRONTMATTER:
            if not values:
                document.front_matter.pop(self.key, None)
            elif self.is_multivalued:
                document.front_matter[self.key] = list(values)
            else:
                document.front_matter[self.key] = values[0]
            return
        if self.format == FORMAT_LIST:
            document.set_section(self.section, "\n".join(f"- {item}" for item in values))
        else:
            document.set_section(self.section, values[0] if values else "")


class Contract:
    """A concept's full property contract, including the universal record properties."""

    def __init__(self, concept_id, properties, record_properties=(), title_field=None):
        self.concept_id = concept_id
        self.properties = list(properties)
        self.record_properties = list(record_properties)
        self.title_field = title_field
        self._by_id = {spec.id: spec for spec in self.properties}
        self._by_id.update({spec.id: spec for spec in self.record_properties})

    def get(self, property_id):
        return self._by_id.get(property_id)

    @property
    def all_properties(self):
        return self.record_properties + self.properties

    @property
    def body_properties(self):
        return [spec for spec in self.properties if spec.store == STORE_BODY]

    @property
    def declared_sections(self):
        return [spec.section for spec in self.body_properties if spec.section]

    def key_order(self):
        """Canonical front-matter order: identity, record fields, contract fields, links last."""
        head = ["id", "rdf:type", "domain", "status", "version", "owner", "created", "updated"]
        contract_keys = [
            spec.key for spec in self.properties if spec.store == STORE_FRONTMATTER
        ]
        tail = ["facets", "related", "sources", "previous_id"]
        order = []
        for key in head + contract_keys + tail:
            if key not in order:
                order.append(key)
        return order

    def section_order(self):
        return self.declared_sections

    def read_all(self, document):
        return {spec.id: spec.read(document) for spec in self.properties}

    def structural_errors(self):
        problems = []
        seen = set()
        for spec in self.properties:
            if spec.id in seen:
                problems.append(f"{self.concept_id}: duplicate property `{spec.id}`")
            seen.add(spec.id)
            problems.extend(spec.structural_errors())

        sections = {}
        for spec in self.body_properties:
            if spec.section in sections:
                problems.append(
                    f"{self.concept_id}: `{spec.section}` is claimed by both "
                    f"`{sections[spec.section]}` and `{spec.id}`"
                )
            sections[spec.section] = spec.id

        if self.title_field and self.title_field not in self._by_id:
            problems.append(
                f"{self.concept_id}: title_field `{self.title_field}` is not a declared property"
            )
        return problems
