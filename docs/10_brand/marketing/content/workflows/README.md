---
id: content.workflows.readme
kind: note
domain: content
status: active
version: 1
class: "10"
collection: content
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-28
facets:
  - operations
related:
  - ../work-items/README.md
  - ../concepts.md
  - ../../../ONTOLOGY.md
sources:
  - ../../../ONTOLOGY.md
---

# Workflows

Store reusable Content operations here. Store executions separately as persistent [Work Items](../work-items/README.md). The default lifecycle is Capture, Validate, Plan, Draft, Review, Produce, Publish, Measure, Learn, and Reuse / Repurpose.

These workflow references define the minimum behavior for future content-generation skills. They are not executable skills themselves.

Every Workflow carries its operational contract in two places: a human-readable prose body
(Purpose/Work Item contract/Required references/Taxonomy contract/Procedure/Output/exceptions) and
a structured `contract:` YAML block in its frontmatter (`subject_type`, `entry_stage`,
`exit_stage`, `requires`, `inputs`, `creates`, `updates`, `validation`, `next`, `failure_paths`)
per [DOMAIN_PROTOCOL.md §11](../../../../00_system/010_governance/DOMAIN_PROTOCOL.md#11-the-workflow-contract-centerpiece).
The two are kept consistent; the YAML block is what a future skill or lint checks mechanically. A
workflow consumes canonical definitions from [`concepts.md`](../concepts.md) and may not redefine
entities or silently extend controlled vocabulary.

Entry and exit stages locate that Work Item execution, not a lifecycle field on the primary subject. Separate Work Items may operate at different stages against related records; predecessor and output links preserve their actual order.

- [Capture Knowledge](capture-knowledge.md)
- [Capture Publication](capture-publication.md)
- [Review Publication](review-publication.md)
- [Detect Motifs](detect-motifs.md)
- [Develop Topic](develop-topic.md)
- [Develop Blueprint](develop-blueprint.md)
- [Generate Hook Options](generate-hook-options.md)
- [Generate Short-Form Script](generate-short-form-script.md)
- [Validate Script](validate-script.md)
- [Develop Publication](develop-publication.md)
- [Validate Publication](validate-publication.md)
- [Produce Publication](produce-publication.md)
- [Publish Publication](publish-publication.md)
- [Record Measurements](record-measurements.md)
- [Derive Insight](derive-insight.md)
- [Repurpose Publication](repurpose-publication.md)
- [Propose Taxonomy Addition](propose-taxonomy-addition.md)
