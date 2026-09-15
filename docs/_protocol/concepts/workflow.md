---
id: protocol.workflow
rdf:type: owl:Class
rdfs:label: Workflow
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
title_field: rdfs:label
persistence:
  mode: directory
  path: workflows
  scope: all-domains
properties:
  - id: rdfs:label
    rdf:type: owl:DatatypeProperty
    rdfs:label: Label
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: contract
    rdf:type: owl:DatatypeProperty
    rdfs:label: Contract
    rdfs:comment: >-
      The machine contract — subject_type, entry_stage, exit_stage, requires, inputs, creates,
      updates, validation, next, failure_paths. Its keys are protocol-local; its values are
      ontology-typed and resolved by lint.
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: skill
    rdf:type: owl:DatatypeProperty
    rdfs:label: Skill
    rdfs:comment: >-
      Name and description for the dispatcher skill generated from this workflow. Absent when the
      workflow is not agent-invocable.
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
  - id: procedure
    rdf:type: owl:DatatypeProperty
    rdfs:label: Procedure
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Procedure
    format: prose
  - id: exceptions
    rdf:type: owl:DatatypeProperty
    rdfs:label: Exceptions
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Exceptions
    format: prose
related:
  - concept.md
  - skill.md
sources: []
---

# Workflow

## Definition

A reusable operation on a domain's model: what it acts on, what must already exist, what it
takes in, what it produces, and where it can go next. The prose body stays human-readable; the
`contract` block is what the engine and lint read.

## Constraints

- `entry_stage` and `exit_stage` draw on the vocabulary the domain names in `stage_vocabulary`.
- Every id in `next` and `failure_paths` resolves to a workflow.
- Every `creates` entry names a concept that exists.
- `inputs` entries use the same property vocabulary as a concept's `properties` — one type
  system, one validator, two hosts.

## Notes

The contract's keys stay protocol-local because a workflow is a process, and OWL, RDFS and SKOS
have no process vocabulary. The candidates — PROV-O, schema.org Action, SPIN — are each out of
scope and would each add a prefix for one file kind. Minting a local term dressed as a standard
one would be worse than a plain key, so the keys are plain. Their *values* are still typed.
