---
id: protocol.domain
rdf:type: owl:Class
rdfs:label: Domain
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
title_field: rdfs:label
persistence:
  mode: registry
  path: domain.md
  scope: all-domains
properties:
  - id: rdfs:label
    rdf:type: owl:DatatypeProperty
    rdfs:label: Label
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: root
    rdf:type: owl:DatatypeProperty
    rdfs:label: Root
    rdfs:comment: The domain's directory, relative to docs/.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: stage_vocabulary
    rdf:type: owl:DatatypeProperty
    rdfs:label: Stage vocabulary
    rdfs:comment: >-
      The taxonomy id whose values this domain's workflow entry_stage and exit_stage are drawn
      from. Absent when the domain defines no staged workflows.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: purpose
    rdf:type: owl:DatatypeProperty
    rdfs:label: Purpose
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Purpose
    format: prose
  - id: scope
    rdf:type: owl:DatatypeProperty
    rdfs:label: Scope
    rdfs:comment: What belongs to this domain and what does not.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Scope
    format: prose
  - id: model
    rdf:type: owl:DatatypeProperty
    rdfs:label: Model
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Model
    format: prose
  - id: relationships
    rdf:type: owl:DatatypeProperty
    rdfs:label: Relationships
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Relationships
    format: prose
  - id: constraints
    rdf:type: owl:DatatypeProperty
    rdfs:label: Constraints
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Constraints
    format: prose
  - id: related_domains
    rdf:type: owl:DatatypeProperty
    rdfs:label: Related Domains
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Related Domains
    format: prose
  - id: examples
    rdf:type: owl:DatatypeProperty
    rdfs:label: Examples
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Examples
    format: prose
related:
  - concept.md
  - ../domain.md
sources: []
---

# Domain

## Definition

A bounded context: an area of meaning with its own concepts, vocabularies, and operations. A
Domain is declared by a `domain.md` at the root of its directory, and that file's existence is
what makes the domain real — the filesystem is the registry, so no central list has to be
edited when one is added.

## Constraints

- A domain directory contains `README.md`, `domain.md`, and a non-empty `concepts/`.
  `taxonomies/` and `workflows/` are present only when the domain owns vocabularies or defines
  operations; an absent directory is correct, an empty one is not.
- `id` is the bare domain slug and equals the `domain` key of every file in the directory.
- Only `protocol`'s own `domain.md` carries `prefixes`, `base_iri`, `vocab_iri` and
  `record_properties`.

## Notes

A domain's namespace IRI is computed as `{base_iri}{id}#` and is never written down.
