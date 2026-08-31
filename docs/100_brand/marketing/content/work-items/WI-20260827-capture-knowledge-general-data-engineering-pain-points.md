---
id: WI-20260827-capture-knowledge-general-data-engineering-pain-points
class: "100"
collection: content
type: work-item
status: archived
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
workflow: ../workflows/capture-knowledge.md
primary_subject: "Web research: burnout, hiring, and architecture pain points in general 2026 data engineering discourse"
work_state: Completed
current_stage: Validate
related:
  - ../sources/2026-general-data-engineering-pain-points-research.md
  - ../knowledge/general-data-engineering-pain-points-2026.md
sources:
  - ../sources/2026-general-data-engineering-pain-points-research.md
---

# Capture Knowledge: general data engineering pain points research

## Inputs

A second batch of public web searches (2026-08-27), run after feedback that the first batch of Topics leaned too heavily pharma-specific and more general data-engineering Topics were wanted: burnout/on-call, hiring/interview breakdown, and architecture/tool-fatigue clusters.

## Decisions and assumptions

- Kept this as a separate Source and Knowledge record rather than extending the first batch's records, since it is a distinct capture event with distinct provenance (a second, later search session).
- Treated all statistics (burnout rate, hiring-drop percentage, budget-overrun figure) as attributed industry claims, consistent with the evidence-boundary approach used in the first batch.
- Checked the existing Knowledge inventory — [2026 data engineering content landscape](../knowledge/2026-data-engineering-content-landscape.md) and [Pharma data-integration pain points (2026)](../knowledge/pharma-data-integration-pain-points-2026.md) — and confirmed this new material (burnout, interviews, mesh/lakehouse architecture) is not materially duplicative of either.

## Outputs

- Source: [General 2026 data engineering pain-point research](../sources/2026-general-data-engineering-pain-points-research.md)
- Knowledge: [General data engineering pain points (2026)](../knowledge/general-data-engineering-pain-points-2026.md)

## Validation

Provenance, access conditions, scope, and verification limits are recorded on the Source. The Knowledge record carries one Knowledge Kind (Research), links back to the Source, states a reusable synthesis, and records a Brand-constraints evidence boundary.

## Predecessors

None.

## Possible next workflows

[Develop Topic](../workflows/develop-topic.md) — executed six times against this Knowledge; see the `WI-20260827-develop-topic-*` Work Items in this directory.
