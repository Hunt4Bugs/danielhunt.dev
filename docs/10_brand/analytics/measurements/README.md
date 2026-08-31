---
class: "10"
collection: analytics
type: record-contract
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - content
related:
  - ../README.md
  - ../concepts.md
  - ../_patterns/measurement.md
  - ../insights/README.md
  - ../../../40_content/publications/README.md
sources:
  - ../../ONTOLOGY.md
---

# Measurement records

Store one dated observed metric per record, per [`_patterns/measurement.md`](../_patterns/measurement.md) and the [`analytics.measurement`](../concepts.md#measurement) entity contract. Each Measurement identifies one Publication, its Channel, one ontology-defined Metric Name, value, unit, observation time, period start, period end, collection method, verification limits, and creating Work Item.

A Measurement is evidence, not an explanation or strategic instruction. Simulated values are permitted only in explicitly illustrative examples and never in this record collection.
