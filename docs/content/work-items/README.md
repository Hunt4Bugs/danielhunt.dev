---
id: content.work-items.readme
kind: note
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-28
facets:
  - operations
related:
  - ../concepts.md
  - ../_patterns/work-item.md
  - ../workflows/README.md
  - ../../10_brand/ONTOLOGY.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Work Item records

You are in the instance directory for `content.work-item`. Store one persistent Markdown record
here for each execution of one Content Workflow against one primary subject. Work Items remain in
this directory after completion; change metadata rather than moving or deleting them.

- What a Work Item *is* (definition, relationships, constraints, entity contract):
  [`concepts.md`](../concepts.md#work-item).
- Identifier scheme, required frontmatter, and required body sections:
  [`_patterns/work-item.md`](../_patterns/work-item.md).
- What *executes* a Work Item: any [Workflow](../workflows/README.md).
