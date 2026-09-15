---
id: content.creator
rdf:type: owl:Class
rdfs:label: Creator
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-09-14
previous_id: content.creator
title_field: name
persistence:
  mode: directory
  path: creators
  scope: own
properties:
  - id: name
    rdf:type: owl:DatatypeProperty
    rdfs:label: Name
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: creator_type
    rdf:type: owl:ObjectProperty
    rdfs:label: Creator Type
    rdfs:comment: What kind of entity this Creator is.
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.creator-type
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: creator_relationships
    rdf:type: owl:ObjectProperty
    rdfs:label: Creator Relationships
    rdfs:comment: Our stance toward this Creator; more than one may hold at once.
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.creator-relationship
    sh:minCount: 1
    store: frontmatter
  - id: creating_work_item
    rdf:type: owl:ObjectProperty
    rdfs:label: Creating Work Item
    rdfs:range: content.work-item
    sh:maxCount: 1
    store: frontmatter
  - id: niches
    rdf:type: owl:DatatypeProperty
    rdfs:label: Niches
    rdfs:comment: Free text, not controlled vocabulary.
    rdfs:range: xsd:string
    store: body
    section: Niches
    format: list
  - id: notes
    rdf:type: owl:DatatypeProperty
    rdfs:label: Notes
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Notes
    format: prose
  - id: creator_channels
    rdf:type: owl:ObjectProperty
    rdfs:label: Creator Channels
    rdfs:comment: The Creator Channels this Creator controls.
    rdfs:range: content.creator-channel
    derived:
      owl:inverseOf: content.creator-channel.creator
    store: body
    section: Creator Channels
    format: list
  - id: registration_provenance
    rdf:type: owl:DatatypeProperty
    rdfs:label: Registration Provenance
    rdfs:comment: >-
      The Work Item that created this record, or the manual addition date and its source
      evidence when no creation workflow exists.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Registration Provenance
    format: prose
  - id: identity
    rdf:type: owl:DatatypeProperty
    rdfs:label: Identity
    rdfs:comment: >-
      Present only when creator_relationships includes Self, or when another record genuinely
      warrants a fuller narrative. Absent entirely for an ordinary monitored Creator.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Identity
    format: prose
related:
  - README.md
  - creator-channel.md
  - ../creators/README.md
  - ../taxonomies/creator-type.md
  - ../taxonomies/creator-relationship.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Creator

## Definition

An identity-bearing entity — a person, company, brand, or organization. Covers Daniel Hunt
himself (`creator_relationships` includes `Self`), an external creator monitored for competitor,
inspiration, peer, or reference intelligence, or a general person or organization worth
recording.

## Constraints

- `creator_type` (what the Creator is) and `creator_relationships` (our stance toward it) are
  separate classifications and must never be conflated into one field.
- Niches and notes are free text, not controlled vocabulary.
- `Identity` is present only on a record whose `creator_relationships` includes `Self`, or one
  that genuinely warrants a fuller narrative. Do not add an empty Identity section to an ordinary
  monitored Creator. This is a judgement about whether a narrative is warranted, not a shape, so
  lint deliberately does not enforce it.
- Direct manual registry additions are permitted. `registration_provenance` must then state the
  addition date and the source evidence explicitly, rather than inventing a `creating_work_item`
  reference.

## Notes

`creator_channels` is derived: it is materialized from every `content.creator-channel` whose
`creator` points here. Do not hand-write it.

The property is named `creator_relationships`, not `relationships`, so that it cannot be misread
as the RDF sense of the word — and so that it matches its vocabulary's name exactly, the way
`creator_type` matches Creator Type. Its previous name was `relationships`; property names are
not identifiers, so the immutability rule does not apply to the rename.
