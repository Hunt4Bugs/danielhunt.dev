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

## Skill execution contract

This section defines the common execution contract for the Claude Code skills in `.claude/skills/` that run these workflows: `to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, and `to-validate`. `to-taxonomy` is the exception these route to when a controlled value is missing, not a follower of this contract. Each skill's own `SKILL.md` links here instead of restating the mechanics below.

1. **Resolve references.** Before acting, read every file listed in the target workflow doc's "Required references" section. Do not proceed from memory of a prior run; re-read on every invocation.
2. **Validate the taxonomy contract.** For every value the workflow doc's Taxonomy contract lists under "Writes," confirm it appears verbatim in the matching table of [Brand ontology v1](../../../ONTOLOGY.md): Knowledge Kind, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook Type, or Publication Format, as applicable. Read the table at run time; never hardcode a copy of its values elsewhere, since `to-taxonomy` can extend it. If a needed value is not in the table, stop and name `to-taxonomy` as the next step. Never approximate, rename, or silently invent a value.
3. **Check for duplicates.** Before creating a new record, search the target collection directory (for example `rg -il '<keyword>' ../knowledge/` from within `workflows/`) for an existing record covering materially the same subject. When the workflow doc's Procedure calls for extending an existing record on duplication (currently specified in `capture-knowledge.md` step 6 and `develop-topic.md` step 2 only), extend that record instead of creating a near-duplicate.
4. **Confirm before writing.** Present the target file path, every chosen taxonomy value, and a section-by-section summary of the planned content. Wait for explicit approval before creating or editing the file. Silence or an unrelated reply is not approval.
5. **Honor stop conditions.** When a workflow doc's "Stop conditions" trigger, halt immediately. State which condition triggered and which workflow (and its skill, if one exists yet) resolves it. Never proceed past a stated stop condition.
6. **Suggest, do not chain.** On a successful Output, name the next applicable skill in the pipeline and what it would need as Input. Do not invoke that skill automatically.
