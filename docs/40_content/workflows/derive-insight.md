---
id: content.workflow.derive-insight
kind: workflow
domain: content
type: workflow
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-28
facets:
  - analytics
related:
  - ../../10_brand/analytics/insights/README.md
  - ../knowledge/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Learn
  exit_stage: Reuse / Repurpose
  requires:
    - id: content.publication
      state: completed
      optional: false
    - id: analytics.measurement
      state: completed
      optional: false
  inputs:
    - name: measurements
      type: ref(analytics.measurement)
      required: true
  creates:
    - type: analytics.insight
      via_pattern: ../../10_brand/analytics/_patterns/insight.md
    - type: content.knowledge
      via_pattern: ../_patterns/knowledge.md
  updates:
    - type: content.knowledge
  validation:
    - measurements_linked
    - evidence_interpretation_separated
    - limitations_recorded
    - competing_explanations_considered
    - knowledge_effect_stated
    - output_links_recorded
  next:
    - content.workflow.repurpose-publication
    - content.workflow.develop-topic
  failure_paths: []
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

- [Insight records](../../10_brand/analytics/insights/README.md) and [Analytics](../../10_brand/analytics/README.md).
- [Insight pattern](../../10_brand/analytics/_patterns/insight.md): the required document shape
  this workflow's `creates` block produces.
- The Publication, its Blueprint, Measurements, and related Knowledge.
- [Strategy](../../10_brand/strategy/README.md): analytics does not automatically replace strategic constraints.

## Procedure

1. Compare Measurements within compatible windows and units.
2. State the observed evidence separately from interpretation.
3. Record limitations and plausible competing explanations.
4. Identify whether the interpretation creates Knowledge, revises Knowledge, or warrants no Knowledge change.
5. Record recommendations separately from decisions.

## Output

One Insight linked to its Measurements and creating Work Item, plus explicit Knowledge effects when supported. Do not silently change Strategy or taxonomy.
