---
id: content.work-item
rdf:type: owl:Class
rdfs:label: Work Item
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-09-14
previous_id: content.work-item
title_field: name
persistence:
  mode: directory
  path: work-items
  scope: own
properties:
  - id: name
    rdf:type: owl:DatatypeProperty
    rdfs:label: Name
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: workflow
    rdf:type: owl:ObjectProperty
    rdfs:label: Workflow
    rdfs:comment: The workflow this execution runs.
    rdfs:range: protocol.workflow
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: primary_subject
    rdf:type: owl:DatatypeProperty
    rdfs:label: Primary subject
    rdfs:comment: The record this execution acts on, as a repository-relative path.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: work_state
    rdf:type: owl:ObjectProperty
    rdfs:label: Work state
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.work-item-state
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: current_stage
    rdf:type: owl:ObjectProperty
    rdfs:label: Current stage
    rdfs:range: skos:Concept
    skos:inScheme: content.taxonomy.workflow-stage
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: decisions_and_assumptions
    rdf:type: owl:DatatypeProperty
    rdfs:label: Decisions and assumptions
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Decisions and assumptions
    format: prose
  - id: outputs
    rdf:type: owl:DatatypeProperty
    rdfs:label: Outputs
    rdfs:range: xsd:string
    store: body
    section: Outputs
    format: list
  - id: predecessors
    rdf:type: owl:DatatypeProperty
    rdfs:label: Predecessors
    rdfs:range: xsd:string
    store: body
    section: Predecessors
    format: list
related:
  - README.md
  - creator.md
  - ../work-items/README.md
sources:
  - ../../00_system/010_governance/ONTOLOGY.md
---

# Work Item

## Definition

One execution of one workflow: what was run, on what, how far it got, and what it produced. A
Work Item is the provenance record that lets any other record name what created it.

## Constraints

- `work_state` (execution) and `current_stage` (lifecycle position) are separate axes and must
  never be conflated. A Work Item may be `Blocked` at any stage.
- A Work Item is created at its workflow's `entry_stage` and moves to its `exit_stage` on
  success. `uv run dh workflow start` and `finish` perform that transition; it is not written by
  hand, and an attempt to finish from the wrong stage is refused.
- A blocked run still leaves a Work Item. Recording that an attempt was made and why it stopped
  is the point of the record.

## Notes

Work Item ids use a dated name — `content.work-item.20260827-develop-topic-alex-xu` — so they are
unique and never renamed. The `WI-YYYYMMDD-` prefix scheme that v0.2 specified is retired; it was
never used, because no Work Item instance was ever written under it.
