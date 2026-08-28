---
class: "100"
collection: content
type: workflow-registry
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - operations
related:
  - ../work-items/README.md
  - ../../../ONTOLOGY.md
sources:
  - ../../../ONTOLOGY.md
---

# Workflows

Store reusable Content operations here. Store executions separately as persistent [Work Items](../work-items/README.md). The default lifecycle is Capture, Validate, Plan, Draft, Review, Produce, Publish, Measure, Learn, and Reuse / Repurpose.

These workflow references define the minimum behavior for future content-generation skills. They are not executable skills themselves.

Every Workflow defines its primary subject, entry and successful exit stages, records created or updated, required predecessors, possible next workflows, validation evidence, and failure or return paths. A workflow consumes canonical definitions and may not redefine entities or silently extend controlled vocabulary.

Entry and exit stages locate that Work Item execution, not a lifecycle field on the primary subject. Separate Work Items may operate at different stages against related records; predecessor and output links preserve their actual order.

- [Capture Knowledge](capture-knowledge.md)
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
