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
  - ../../../analytics/measurements/README.md
  - ../publications/README.md
sources:
  - ../../../ONTOLOGY.md
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

- [Measurement records](../../../analytics/measurements/README.md): record contract.
- [Analytics](../../../analytics/README.md): interpretation boundary and evaluation windows.
- [Brand ontology v1](../../../ONTOLOGY.md): Metric Name taxonomy.

## Procedure

1. Select the observation window defined by Analytics.
2. Record one Measurement for each observed metric using an existing Metric Name.
3. Preserve the reported unit, collection method, observation time, period start, period end, and limitations.
4. Link each Measurement to the Publication and creating Work Item.

## Output

One or more verified Measurement records. Do not add interpretation or strategic direction to a Measurement.
