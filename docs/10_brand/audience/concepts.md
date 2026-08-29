---
id: audience.concepts
kind: concept-registry
domain: audience
status: active
version: 1
class: "10"
collection: audience
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../specs/2026-06-01-personal-brand-workbook.md
---

# Audience concepts

Canonical concept registry for the `audience` domain (see [`domain.md`](domain.md)).

## Audience Segment
**ID:** `audience.segment`

A named group the brand addresses, speaks with as a peer, or speaks about with empathy, carrying a
stable code so it can be referenced unambiguously from Content records.

### Relationships
- addressed by `content.topic`
- addressed by `content.blueprint`
- classified by `taxonomy(Audience Relationship)`

### Constraints
- Each Segment carries exactly one stable code (e.g. `B2`) and exactly one Audience Relationship
  value (Addressed, Spoken-with, Spoken-about).
- Adding a Segment is a governed operation (§13.3) — a workflow or skill may propose one but may
  not select it before an explicit update to the registry below.
- Use the Segment name and stable code together when ambiguity is possible.

### Persistence

Audience Segment instances are persisted as rows in the Audience Segment registry table in
[`README.md`](README.md#audience-segment-registry), not as individual documents — a controlled
vocabulary, not a document-per-instance record (§14). No entity contract is defined per §10; the
registry table's four columns (Segment, Stable code, Audience Relationship, Use) are
self-describing.

## Owned vocabularies

`audience` owns two controlled vocabularies (§13.3 — extend only by governed edit here, never
silently from a workflow or skill):

- **Audience Segment** — the four canonical v1 values: Primary Editorial Audience (`B2`), Life
  Sciences Founder Peers (`B1`), Lab Operations and Scientists (`A`), Commercial Services Audience
  (`SERVICES`).
- **Audience Relationship** ([`ONTOLOGY.md`](../ONTOLOGY.md) Supporting taxonomy, applied to
  Audience Segment) — Addressed, Spoken-with, Spoken-about.


## No _patterns/ or workflows/

Audience Segment instances are registry rows, not individual documents, so no local `_patterns/`
is warranted (§14.1). No repeatable multi-step operation on Audience Segment itself has recurred
enough yet to justify a Workflow; it is read as an input by `content.workflow.develop-topic` and
`content.workflow.develop-blueprint` instead.
