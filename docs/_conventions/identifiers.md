---
id: protocol.conventions.identifiers
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - README.md
  - documentation.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Identifiers

Restates [DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) §5 as a standalone
reference.

## Type and instance identifiers

```text
<domain>.<kind>.<name>
```

At the type level (a Concept or a Workflow definition):

```text
content.topic
content.workflow.develop-topic
ops.tracker-item
```

At the instance level (one particular record):

```text
content.topic.repository-context
```

`content.topic` is the concept/type identifier; `content.topic.repository-context` is one instance
of it. `id` is immutable once assigned — never rename an identifier after creation, even if the
subject it describes is later renamed or superseded.

## Executed instances (Work Items)

Work Items use a dated scheme so they stay unique and are never renamed:

```text
WI-YYYYMMDD-<workflow>-<subject>
```

Example: `WI-20260827-develop-topic-ai-repository-guidance`. Keep the workflow and subject portions
concise kebab-case. If an identifier would collide, append `-02`, `-03`, and so on — never reuse or
rename an existing one.

## Where `id` is required

Every document following the [documentation frontmatter contract](documentation.md) carries an
`id`. A routing `README.md` may use a short note-style `id` (e.g. `content.readme`) since it isn't
itself a modeled Concept, Pattern, or Workflow.
