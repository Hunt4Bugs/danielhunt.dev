---
class: "100"
collection: content
type: work-item-registry
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - operations
related:
  - ../workflows/README.md
  - ../../../ONTOLOGY.md
sources:
  - ../../../ONTOLOGY.md
---

# Work Item records

Store one persistent Markdown record here for each execution of one Content Workflow against one primary subject. Work Items remain in this directory after completion; change metadata rather than moving or deleting them.

## Identifier

Use `WI-YYYYMMDD-workflow-subject`. Keep the workflow and subject portions concise kebab-case. When the identifier already exists, append `-02`, `-03`, and so on. Never rename an identifier after creation.

## Required frontmatter

```yaml
id: WI-YYYYMMDD-workflow-subject
class: "100"
collection: content
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

Use repository metadata `status` for record maintenance: `active` while queued or in progress, `blocked` while blocked, and `archived` after completion or cancellation. Use `work_state` for the canonical Work Item State. The two fields have different jobs.

## Required body

Every Work Item contains `Inputs`, `Decisions and assumptions`, `Outputs`, `Validation`, `Predecessors`, and `Possible next workflows`. Link every domain record created by the execution back to this Work Item.

Record verified evidence separately from interpretation and assumptions. A completed Work Item names its actual output records and validation result; a blocked item states the missing evidence, approval, or dependency.
