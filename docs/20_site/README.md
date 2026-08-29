---
id: site.readme
kind: note
domain: site
class: "20"
collection: implementation
type: domain-reference
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - domain.md
  - concepts.md
  - ARCHITECTURE.md
sources:
  - ../../CLAUDE.md
---

# site

`site` is the domain for `danielhunt.dev`'s deployable static surface. [`domain.md`](domain.md)
states this domain's boundary and [`concepts.md`](concepts.md) is its concept registry (Page,
Component), per the [Domain Documentation Protocol](../00_system/010_governance/DOMAIN_PROTOCOL.md).

## Records

- [`ARCHITECTURE.md`](ARCHITECTURE.md): verified evidence about the deployable `site/` tree —
  routes, shared styling/behavior, and canonical constraints. The detailed operational source;
  `domain.md` does not re-derive it.

There is no local `_patterns/` or `workflows/` directory: Page and Component instances are the
actual files under the repository-root `site/` directory, not documents under `docs/`, and no
repeatable multi-step operation on this domain has recurred enough yet to justify a Workflow — see
[`domain.md`](domain.md)'s note on instance storage.
