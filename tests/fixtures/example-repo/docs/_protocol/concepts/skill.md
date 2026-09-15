---
id: protocol.skill
rdf:type: owl:Class
rdfs:label: Skill
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
title_field: rdfs:label
persistence:
  mode: registry
  path: skill.md
  scope: all-domains
properties:
  - id: rdfs:label
    rdf:type: owl:DatatypeProperty
    rdfs:label: Label
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: frontmatter
  - id: overview
    rdf:type: owl:DatatypeProperty
    rdfs:label: Overview
    rdfs:range: xsd:string
    sh:minCount: 1
    sh:maxCount: 1
    store: body
    section: Overview
    format: prose
  - id: voice
    rdf:type: owl:DatatypeProperty
    rdfs:label: Voice
    rdfs:comment: Domain-level instruction — tone, evidence boundaries, what this domain is for.
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Voice
    format: prose
  - id: stop_conditions
    rdf:type: owl:DatatypeProperty
    rdfs:label: Stop conditions
    rdfs:range: xsd:string
    sh:maxCount: 1
    store: body
    section: Stop conditions
    format: prose
related:
  - workflow.md
sources: []
---

# Skill

## Definition

A domain's instruction layer: what an agent operating in this domain needs to know that is not
already in the model. One per domain, at `docs/<domain>/skill.md`, read after routing.

## Constraints

- A Skill is pure instruction. It carries no logic, no derivation rules, and no path lists that
  the engine could resolve instead.
- Anything a Skill would explain about *which* fields exist, what they range over, or where they
  are stored belongs in the concept file, not here.

## Notes

This is distinct from the generated dispatchers under `.claude/skills/`. Those are produced by
`dh index skills` from each workflow's `skill` block and are never hand-edited; this is the
domain-level instruction a human writes once.
