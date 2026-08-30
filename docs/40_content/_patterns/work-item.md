---
id: content.pattern.work-item
kind: pattern
domain: content
pattern_for: content.work-item
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - operations
related:
  - ../work-items/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Work Item

What a `content.work-item` instance document (stored under `work-items/`) must contain. See
[`concepts.md`](../concepts.md#work-item) for the Work Item entity contract this pattern
instantiates.

## Identifier

`WI-YYYYMMDD-workflow-subject`, kebab-case, concise. Append `-02`, `-03`, and so on on collision.
Never rename an identifier after creation.

## Required frontmatter

```yaml
id: WI-YYYYMMDD-workflow-subject
type: work-item
status: active
owner: Daniel Hunt
created: YYYY-MM-DD
updated: YYYY-MM-DD
workflow: ../workflows/example.md
primary_subject: ../topics/example.md
work_state: In Progress
current_stage: Plan
related: []
sources: []
```

Repository `status` tracks record maintenance (`active` while queued or in progress, `blocked`
while blocked, `archived` after completion or cancellation). `work_state` carries the canonical
Work Item State — the two fields have different jobs and are never conflated.

## Required body sections

1. **Inputs** — what the execution started from.
2. **Decisions and assumptions** — choices made during execution and why.
3. **Outputs** — every domain record this execution created or updated, linked back to this Work
   Item.
4. **Validation** — the evidence proving the exit condition was met; a blocked item states the
   missing evidence, approval, or dependency instead.
5. **Predecessors** — links to Work Items this one required as preconditions.
6. **Possible next workflows** — which Workflows can validly follow this execution.

## Notes

Record verified evidence separately from interpretation and assumptions throughout. Work Items are
never moved or deleted after completion — only their metadata changes.
