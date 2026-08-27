---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - analytics
related:
  - ../../../analytics/insights/README.md
  - ../knowledge/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Derive Insight

## Work Item contract

- **Primary subject:** one Publication with one or more Measurement records.
- **Entry stage:** Learn.
- **Successful exit stage:** Reuse / Repurpose.
- **Creates:** one Insight and, when warranted, one new Knowledge record.
- **Updates:** existing Knowledge only when the new evidence materially revises it.
- **Required predecessors:** completed [Record Measurements](record-measurements.md) with sufficient verified observations.
- **Possible next workflows:** [Repurpose Publication](repurpose-publication.md), Develop Topic, or no further work.
- **Validation evidence:** linked Measurements, evidence/inference separation, limitations, competing explanations, Knowledge effect, and output links recorded in the Work Item.
- **Failure and return paths:** remain at Learn when evidence is insufficient; record no Insight rather than forcing a conclusion.

## Required references

- [Insight records](../../../analytics/insights/README.md) and [Analytics](../../../analytics/README.md).
- The Publication, its Blueprint, Measurements, and related Knowledge.
- [Strategy](../../../strategy/README.md): analytics does not automatically replace strategic constraints.

## Procedure

1. Compare Measurements within compatible windows and units.
2. State the observed evidence separately from interpretation.
3. Record limitations and plausible competing explanations.
4. Identify whether the interpretation creates Knowledge, revises Knowledge, or warrants no Knowledge change.
5. Record recommendations separately from decisions.

## Output

One Insight linked to its Measurements and creating Work Item, plus explicit Knowledge effects when supported. Do not silently change Strategy or taxonomy.
