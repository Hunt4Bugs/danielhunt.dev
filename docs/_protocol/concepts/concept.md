---
id: protocol.concept
rdf:type: owl:Class
rdfs:label: Concept
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
title_field: rdfs:label
instance_rdf_type: owl:Class
persistence:
  mode: directory
  path: concepts
  scope: all-domains
properties:
  - id: rdfs:label
    rdf:type: owl:DatatypeProperty
    rdfs:label: Label
    rdfs:comment: The concept's human-readable name.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: title_field
    rdf:type: owl:DatatypeProperty
    rdfs:label: Title field
    rdfs:comment: >-
      The property whose value the H1 of an instance renders. Required when persistence.mode is
      directory. The H1 is derived presentation and is never read as data.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: instance_rdf_type
    rdf:type: owl:DatatypeProperty
    rdfs:label: Instance rdf:type
    rdfs:comment: >-
      The rdf:type value this concept's instances carry. Defaults to the concept's own id. The
      meta-concepts are the exception: a concept file is an instance of protocol.concept and
      simultaneously is an owl:Class, so it declares the standard term as its marker.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: persistence
    rdf:type: owl:DatatypeProperty
    rdfs:label: Persistence
    rdfs:comment: >-
      How instances are stored — mode (directory, registry, external, none), path, and scope
      (own, all-domains). A concept with no persistence block is modelled but not stored.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: frontmatter
  - id: properties
    rdf:type: owl:DatatypeProperty
    rdfs:label: Properties
    rdfs:comment: >-
      The property contract. Declaration order is serialization order, for both front-matter keys
      and body sections.
    rdfs:range: xsd:string
    store: frontmatter
  - id: definition
    rdf:type: owl:DatatypeProperty
    rdfs:label: Definition
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Definition
    format: prose
  - id: constraints
    rdf:type: owl:DatatypeProperty
    rdfs:label: Constraints
    rdfs:comment: >-
      Anything expressible as sh:minCount, sh:maxCount or skos:inScheme must be expressed there
      and must not be restated here.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Constraints
    format: prose
  - id: notes
    rdf:type: owl:DatatypeProperty
    rdfs:label: Notes
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Notes
    format: prose
related:
  - domain.md
  - taxonomy.md
  - note.md
  - ../PROTOCOL.md
sources: []
---

# Concept

## Definition

A class of thing a domain models, together with the contract its instances must satisfy. A
Concept declares one `owl:Class` and, by the same identity, one `sh:NodeShape` whose target is
that class: the class is the vocabulary, the shape is the validator, and this file writes both
at once.

Every file under `docs/` is an instance of exactly one Concept, named by its `rdf:type`.

This file is an instance of itself. It is the engine's single bootstrap axiom: to load
`protocol.concept` you already need `protocol.concept`, so the engine reads this one path
literally with a minimal parser, builds the contract, and then re-validates this file against it.

## Constraints

- `rdfs:domain` is never written. A property declared inside a concept file has that concept as
  its domain by construction. `rdfs:domain` is an inference axiom — it would mean *anything
  carrying this property is thereby an instance of this class*, manufacturing type assertions
  rather than rejecting misplaced ones — and containment already states the closed-world fact
  that is actually wanted.
- `store` is explicit on every property and is never derived from the range.
- A property with `store: body` declares `section` verbatim and `format`. A heading is never
  derived from a property name.
- A property carrying `derived` has no `sh:` constraints: there is no authored value to
  constrain, so a constraint there would be vacuous or would fail on correct data.
- `title_field` is required when `persistence.mode` is `directory`.
- Property declaration order is serialization order.

## Notes

A Concept's own prose lives in its body because this file declares `definition`, `constraints`
and `notes` as `store: body`. The self-hosting is not a trick — it is the same contract
mechanism every other concept uses, applied to the concept that defines it.

`persistence.scope: all-domains` on this concept is what makes `concepts/` resolve in every
domain directory rather than only in `_protocol/`. It is the one place the model says "this
path, in every domain", and it names no domain.
