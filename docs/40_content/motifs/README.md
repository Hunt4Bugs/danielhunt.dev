---
id: content.motifs.readme
kind: note
domain: content
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - analytics
related:
  - ../concepts.md
  - ../_patterns/motif.md
  - ../reviews/README.md
  - ../knowledge/README.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Motif records

You are in the instance directory for `content.motif`. Store reusable observations promoted from
two or more corroborating Reviews here — a specific, repeated characteristic worth naming and
reusing, not a one-off impression from a single occurrence.

- What a Motif *is* (definition, relationships, constraints, entity contract):
  [`concepts.md`](../concepts.md#motif).
- What a Motif document must *contain* (required sections): [`_patterns/motif.md`](../_patterns/motif.md).
- What *creates* a Motif: the [Detect Motifs](../workflows/detect-motifs.md) workflow.
- Related instance directories: [Reviews](../reviews/README.md) (the corroborating evidence a
  Motif is derived from), [Knowledge](../knowledge/README.md) (what a well-evidenced Motif may
  inform or seed).

A Motif must draw on at least two corroborating Reviews — `supporting_reviews` carries cardinality
`2..*`, so this is enforced structurally rather than left to prose. A new corroborating Review for
an existing Motif updates that record; it never creates a duplicate.
