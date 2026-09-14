---
id: example.gadget
rdf:type: owl:Class
rdfs:label: Gadget
domain: example
status: active
version: 1
owner: Test
created: 2026-09-14
updated: 2026-09-14
title_field: name
persistence:
  mode: directory
  path: gadgets
  scope: own
properties:
  - id: name
    rdf:type: owl:DatatypeProperty
    rdfs:label: Name
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: grade
    rdf:type: owl:ObjectProperty
    rdfs:label: Grade
    rdfs:range: skos:Concept
    skos:inScheme: example.taxonomy.gadget-grade
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: tags
    rdf:type: owl:DatatypeProperty
    rdfs:label: Tags
    rdfs:range: xsd:string
    store: body
    section: Tags
    format: list
  - id: summary
    rdf:type: owl:DatatypeProperty
    rdfs:label: Summary
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Summary
    format: prose
related:
  - ../taxonomies/gadget-grade.md
sources: []
---

# Gadget

## Definition

A synthetic concept exercising every storage location and both property types.

## Constraints

- A Gadget carries exactly one grade.
