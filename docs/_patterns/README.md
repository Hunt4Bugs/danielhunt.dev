---
id: protocol.patterns
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
related:
  - ../README.md
  - ../_conventions/README.md
  - domain.md
  - concept.md
  - workflow.md
  - pattern.md
  - decision.md
  - ../00_system/010_governance/DOMAIN_PROTOCOL.md
---

# Meta-patterns

These are **meta**-patterns: they describe what each *kind* of protocol document must contain,
per [DOMAIN_PROTOCOL.md](../00_system/010_governance/DOMAIN_PROTOCOL.md) §9–§11. They apply across
every domain. Do not confuse this with a domain's own `_patterns/` directory (e.g.
`content/_patterns/`), which describes the representation convention for one
domain's own Concepts (what a Topic document looks like, what a Blueprint document looks like) —
that is domain-scoped content, not protocol infrastructure.

| File | Governs |
| --- | --- |
| [domain.md](domain.md) | Any domain's `domain.md` boundary document (§9.2). |
| [concept.md](concept.md) | Any domain's `concepts.md` registry and its per-concept entity contracts (§9.3, §10). |
| [workflow.md](workflow.md) | Any domain's `workflows/*.md` files (§9.5, §11). |
| [pattern.md](pattern.md) | Any domain's own `_patterns/*.md` files (§9.4). |
| [decision.md](decision.md) | A Decision record — an ordinary Concept with a Pattern, not a structural primitive (§3.7). |

A workflow (e.g. the `ops` domain's `create-domain` workflow, implementing DOMAIN_PROTOCOL.md §15)
reads these meta-patterns to generate a new domain's scaffold, rather than inventing structure.
