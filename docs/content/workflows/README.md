---
id: content.workflows.readme
kind: note
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-28
facets:
  - operations
related:
  - ../work-items/README.md
  - ../concepts.md
  - ../../10_brand/ONTOLOGY.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Workflows

Store reusable Content operations here. Store executions separately as persistent [Work Items](../work-items/README.md). The default lifecycle is Capture, Validate, Plan, Draft, Review, Produce, Publish, Measure, Learn, and Reuse / Repurpose.

These workflow references define the minimum behavior for future content-generation skills. They are not executable skills themselves.

Every Workflow carries its operational contract in two places: a human-readable prose body
(Purpose/Work Item contract/Required references/Taxonomy contract/Procedure/Output/exceptions) and
a structured `contract:` YAML block in its frontmatter (`subject_type`, `entry_stage`,
`exit_stage`, `requires`, `inputs`, `creates`, `updates`, `validation`, `next`, `failure_paths`)
per [DOMAIN_PROTOCOL.md §11](../../00_system/010_governance/DOMAIN_PROTOCOL.md#11-the-workflow-contract-centerpiece).
The two are kept consistent; the YAML block is what a future skill or lint checks mechanically. A
workflow consumes canonical definitions from [`concepts.md`](../concepts.md) and may not redefine
entities or silently extend controlled vocabulary.

Entry and exit stages locate that Work Item execution, not a lifecycle field on the primary subject. Separate Work Items may operate at different stages against related records; predecessor and output links preserve their actual order.

- [Capture Knowledge](capture-knowledge.md)
- [Monitor Creators](monitor-creators.md)
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

## Skill execution contract

This section defines the common execution contract for the Claude Code skills in `.claude/skills/` that run these workflows: `to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, and `to-validate`. `to-taxonomy` is the exception these route to when a controlled value is missing, not a follower of this contract. Each skill's own `SKILL.md` links here instead of restating the mechanics below.

1. **Resolve references.** Before acting, read every file listed in the target workflow doc's "Required references" section. Do not proceed from memory of a prior run; re-read on every invocation.
2. **Validate the taxonomy contract.** For every value the workflow doc's Taxonomy contract lists under "Writes," confirm it appears verbatim in its owning registry: the matching table of [Brand ontology v1](../../../ONTOLOGY.md) for Knowledge Kind, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook Type, or Publication Format; the Theme registry in [Strategy](../../../strategy/README.md) for Theme; the Audience Segment registry in [Audience](../../../audience/README.md) for Audience Segment; or the Channel registry in [Channels](../../../channels/README.md) for Channel. Read the owning registry at run time; never hardcode a copy of its values elsewhere, since `to-taxonomy` can extend the ones it governs. If a needed value is not in its owning registry, stop and name `to-taxonomy` as the next step. Never approximate, rename, or silently invent a value.
3. **Check for duplicates.** Before creating a new record, search the target collection directory (for example `rg -il '<keyword>' ../knowledge/` from within `workflows/`) for an existing record covering materially the same subject. When the workflow doc's Procedure calls for extending an existing record on duplication (currently specified in `capture-knowledge.md` step 6 and `develop-topic.md` step 2 only), extend that record instead of creating a near-duplicate.
4. **Confirm before writing.** Present the target file path, every chosen taxonomy value, and a section-by-section summary of the planned content. Wait for explicit approval before creating or editing the file. Silence or an unrelated reply is not approval.
5. **Honor stop conditions.** When a workflow doc's "Stop conditions" trigger, halt immediately. State which condition triggered and which workflow (and its skill, if one exists yet) resolves it. Never proceed past a stated stop condition.
6. **Suggest, do not chain.** On a successful Output, name the next applicable skill in the pipeline and what it would need as Input. Do not invoke that skill automatically.
7. **Track execution as a Work Item.** Create or update one persistent record under `docs/10_brand/marketing/content/work-items/`, per [Work Item records](../work-items/README.md): identifier `WI-YYYYMMDD-workflow-subject` (append `-02`, `-03`, and so on when that identifier already exists), the required frontmatter (`id`, `workflow`, `primary_subject`, `work_state`, `current_stage`, plus the standard metadata fields), and the required body sections (`Inputs`, `Decisions and assumptions`, `Outputs`, `Validation`, `Predecessors`, `Possible next workflows`). Link every domain record this run creates or updates back to this Work Item, and link the Work Item forward from that domain record's own "Creating Work Item" field when its template has one. A completed Work Item names its actual output records and validation result; a blocked or stopped one states the missing evidence, approval, or dependency, with `work_state` and `status` set accordingly. Present the Work Item's planned content alongside the domain record's in the confirm-before-writing step above; both are part of one approval, not a second round.
