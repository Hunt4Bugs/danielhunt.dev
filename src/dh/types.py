"""Identifiers, slugs, IRIs, and the OWL/SKOS term constants the model writes.

The id grammar is what makes lint check 2 decidable: an instance id is derivable from its
`domain` and its `rdf:type`, so a well-formed id is a checkable fact rather than a convention.
"""

from __future__ import annotations

import re
import unicodedata

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NON_SLUG_RE = re.compile(r"[^a-z0-9]+")

# Terms written as the value of rdf:type.
CLASS = "owl:Class"
OBJECT_PROPERTY = "owl:ObjectProperty"
DATATYPE_PROPERTY = "owl:DatatypeProperty"
CONCEPT_SCHEME = "skos:ConceptScheme"
SKOS_CONCEPT = "skos:Concept"

XSD_RANGES = {"xsd:string", "xsd:integer", "xsd:date", "xsd:anyURI", "xsd:boolean", "xsd:decimal"}

# Bound prefixes. The authoritative binding lives in docs/_protocol/domain.md; this set exists so
# the bootstrap can reject an unbound prefix before that file has been parsed.
PREFIXES = {"rdf", "rdfs", "owl", "skos", "sh", "xsd"}

# Constraint terms that carry open-world semantics and would silently disable a check.
FORBIDDEN_TERMS = {
    "rdfs:domain": "a property's domain is stated by containment in its concept's `properties`",
    "rdfs:subClassOf": "subtyping is modelled as a taxonomy value, not a class hierarchy",
    "owl:Restriction": "use sh:minCount / sh:maxCount",
    "owl:minCardinality": "use sh:minCount — an OWL cardinality infers rather than rejects",
    "owl:maxCardinality": "use sh:maxCount — an OWL cardinality infers rather than rejects",
    "owl:cardinality": "use sh:minCount and sh:maxCount",
    "owl:someValuesFrom": "use sh:minCount with rdfs:range",
    "owl:allValuesFrom": "use rdfs:range",
    "owl:FunctionalProperty": "use sh:maxCount: 1",
    "owl:disjointWith": "not part of this vocabulary",
    "owl:equivalentClass": "not part of this vocabulary",
}


def slug(value):
    """NFKC, lowercase, every run outside [a-z0-9] to a single hyphen, stripped.

    Total by construction, so `Hook -> Journey -> Payoff` and `Novel / Unusual Visual` both land
    on a legal slug. The original string is always kept elsewhere (skos:prefLabel), so the
    flattening loses nothing.
    """
    text = unicodedata.normalize("NFKC", str(value)).lower()
    text = NON_SLUG_RE.sub("-", text)
    return text.strip("-")


def is_slug(value):
    return bool(SLUG_RE.match(value or ""))


def split_id(identifier):
    return (identifier or "").split(".")


def concept_slug(concept_id):
    """`<domain>.<name>` -> `<name>`. The last segment of a concept id."""
    parts = split_id(concept_id)
    return parts[-1] if parts else ""


def expected_instance_id(domain, concept_id, name):
    return f"{domain}.{concept_slug(concept_id)}.{name}"


def is_prefixed(value):
    """True for a `prefix:local` term, false for a dotted repo id or bare text."""
    if not isinstance(value, str) or ":" not in value:
        return False
    head = value.split(":", 1)[0]
    return bool(head) and " " not in head and "/" not in head


def prefix_of(value):
    return value.split(":", 1)[0] if is_prefixed(value) else None


def is_repo_id(value):
    """True for a dotted identifier defined in this repository."""
    return isinstance(value, str) and "." in value and not is_prefixed(value)


# -- IRI minting -------------------------------------------------------------------
# Terms live in a hash namespace, resources in a slash path. The split is what keeps
# a class IRI distinct from an instance IRI that would otherwise collide with it.


def domain_iri(base, domain):
    return f"{base}{domain}"


def domain_namespace(base, domain):
    return f"{base}{domain}#"


def concept_iri(base, concept_id):
    parts = split_id(concept_id)
    domain = parts[0]
    rest = ".".join(parts[1:]) or domain
    return f"{base}{domain}#{rest}"


def property_iri(base, concept_id, property_id):
    """Properties are concept-scoped: `name` on Creator and on Creator Channel are distinct."""
    parts = split_id(concept_id)
    domain = parts[0]
    local = ".".join(parts[1:]) or domain
    return f"{base}{domain}#{local}.{property_id}"


def resource_iri(base, identifier):
    return base + "/".join(split_id(identifier))


def value_iri(base, scheme_id, pref_label):
    return f"{resource_iri(base, scheme_id)}/{slug(pref_label)}"
