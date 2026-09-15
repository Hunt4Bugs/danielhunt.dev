---
id: protocol
rdf:type: protocol.domain
rdfs:label: Protocol
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
root: _protocol
base_iri: https://danielhunt.dev/ns/
vocab_iri: https://danielhunt.dev/ns/protocol#
prefixes:
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  owl: http://www.w3.org/2002/07/owl#
  skos: http://www.w3.org/2004/02/skos/core#
  sh: http://www.w3.org/ns/shacl#
  xsd: http://www.w3.org/2001/XMLSchema#
record_properties:
  - id: status
    rdf:type: owl:ObjectProperty
    rdfs:label: Status
    rdfs:range: skos:Concept
    skos:inScheme: protocol.taxonomy.status
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: version
    rdf:type: owl:DatatypeProperty
    rdfs:label: Version
    rdfs:range: xsd:integer
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: owner
    rdf:type: owl:DatatypeProperty
    rdfs:label: Owner
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: created
    rdf:type: owl:DatatypeProperty
    rdfs:label: Created
    rdfs:range: xsd:date
    sh:maxCount: 1
    store: frontmatter
  - id: updated
    rdf:type: owl:DatatypeProperty
    rdfs:label: Updated
    rdfs:range: xsd:date
    sh:maxCount: 1
    store: frontmatter
  - id: facets
    rdf:type: owl:DatatypeProperty
    rdfs:label: Facets
    rdfs:range: xsd:string
    store: frontmatter
  - id: related
    rdf:type: owl:DatatypeProperty
    rdfs:label: Related
    rdfs:range: xsd:anyURI
    store: frontmatter
  - id: sources
    rdf:type: owl:DatatypeProperty
    rdfs:label: Sources
    rdfs:range: xsd:anyURI
    store: frontmatter
  - id: previous_id
    rdf:type: owl:DatatypeProperty
    rdfs:label: Previous id
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
related:
  - README.md
  - PROTOCOL.md
  - ../ROUTER.md
sources: []
---

# Protocol

## Purpose

The meta-model every other domain conforms to. `protocol` owns the shapes — Concept, Domain,
Taxonomy, Workflow, Router, Note, Skill — that the `content`, `ops`, `site` and `delivery`
domains are written in, and it owns the vocabulary those shapes are expressed with.

This domain is self-hosting: `concepts/concept.md` is an instance of itself, and
`uv run dh lint` validates the protocol against its own contract.

## Scope

### Includes

- The meta-concepts every domain instantiates.
- The controlled vocabularies the protocol itself uses: document status, property storage,
  body format, persistence mode, and the vocabulary-term registry.
- Prefix binding, base IRI, and the record properties every file in the repository carries.
- The workflows that govern changes to the model itself.

### Excludes

- Any domain's own concepts, taxonomies, or instances.
- Physical file placement, which [`LIBRARY_MAP.md`](../00_system/010_governance/LIBRARY_MAP.md)
  routes.
- The engine's implementation. `src/dh/` is infrastructure, not a modelled domain.

## Model

A Domain declares a root and (for `protocol` alone) the prefix binding. A Concept declares
properties, each of which says what it ranges over and where its value is stored. A Taxonomy
declares a `skos:ConceptScheme` whose values are a table. A Workflow declares a contract. Every
other file is a Note.

## Relationships

Every file in the repository is an instance of exactly one `protocol` concept, named by its
`rdf:type`.

## Constraints

- `prefixes`, `base_iri`, `vocab_iri` and `record_properties` are declared here and nowhere else.
  Per-domain namespaces are computed as `{base_iri}{domain}#`; they are never listed.
- `record_properties` are properties of being a file in this repository, not of being any
  particular concept. They are why the model needs no class hierarchy.
- The protocol adopts OWL/RDFS/SKOS **vocabulary** and SHACL **semantics**. See
  [`PROTOCOL.md`](PROTOCOL.md) for why the two must never be traded for one another.

## Related Domains

- [`content`](../40_content/README.md), [`ops`](../00_system/README.md),
  [`site`](../20_site/README.md), [`delivery`](../30_delivery/README.md) — every one of them an
  instantiation of this model.

## Examples

`docs/40_content/concepts/creator.md` is an instance of `protocol.concept`.
`docs/40_content/taxonomies/creator-relationship.md` is an instance of `protocol.taxonomy`.
This file is an instance of `protocol.domain`.
