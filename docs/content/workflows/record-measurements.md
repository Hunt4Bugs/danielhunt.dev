---
id: content.workflow.record-measurements
kind: workflow
domain: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-28
facets:
  - analytics
related:
  - ../../10_brand/analytics/measurements/README.md
  - ../publications/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Measure
  exit_stage: Learn
  requires:
    - id: content.publication
      state: completed
      optional: false
  inputs:
    - name: observation_window
      type: text
      required: true
    - name: metric_name
      type: taxonomy(Metric Name)
      required: true
  creates:
    - type: analytics.measurement
      via_pattern: ../../10_brand/analytics/_patterns/measurement.md
  updates:
    - type: content.publication
  validation:
    - observation_source_recorded
    - time_window_recorded
    - units_recorded
    - verification_limits_recorded
    - records_linked_to_publication
  next:
    - content.workflow.derive-insight
    - content.workflow.record-measurements
  failure_paths:
    - content.workflow.record-measurements
---

# Record Measurements

## Work Item contract

- **Primary subject:** one verified published Publication.
- **Entry stage:** Measure.
- **Successful exit stage:** Learn.
- **Creates:** one Measurement record per observed metric.
- **Updates:** the Publication's Measurement links.
- **Required predecessors:** completed [Publish Publication](publish-publication.md) or verified durable publication facts for an existing Publication.
- **Possible next workflows:** [Derive Insight](derive-insight.md) when sufficient observations exist; this workflow again for a later window.
- **Validation evidence:** observation source, time window, units, verification limits, created records, and Publication link recorded in the Work Item.
- **Failure and return paths:** remain at Measure when the observation cannot be verified or the measurement window is not yet complete.

## Required references

- [Measurement records](../../10_brand/analytics/measurements/README.md): record contract.
- [Measurement pattern](../../10_brand/analytics/_patterns/measurement.md): the required document
  shape this workflow's `creates` block produces.
- [Analytics](../../10_brand/analytics/README.md): interpretation boundary and evaluation windows.
- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Metric Name taxonomy.

## Procedure

1. Select the observation window defined by Analytics.
2. Record one Measurement for each observed metric using an existing Metric Name.
3. Preserve the reported unit, collection method, observation time, period start, period end, and limitations.
4. Link each Measurement to the Publication and creating Work Item.

## Output

One or more verified Measurement records. Do not add interpretation or strategic direction to a Measurement.
