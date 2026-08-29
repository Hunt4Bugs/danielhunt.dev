---
id: ops.library-map
kind: note
domain: ops
version: 1
class: "00"
collection: governance
type: library-map
status: active
owner: Daniel Hunt
updated: 2026-07-28
---

# Library map

| Class | Purpose | Canonical path | Notes |
| --- | --- | --- | --- |
| 00 | Project operating system, governance, and records | `docs/00_system/` | Internal-only system of record. |
| 10 | Brand foundation and strategy | `docs/10_brand/` | Authoritative brand corpus; filenames are retained. |
| 20 | Site implementation | `docs/20_site/` | Canonical site documentation; deployable source remains in `site/`. |
| 30 | Delivery automation | `docs/30_delivery/` | Internal delivery documentation; configuration remains in `.github/`. |

## Class 00 collections

| Collection | Path | Holds |
| --- | --- | --- |
| Governance | `010_governance/` | Map, metadata rules, policies. |
| Agent guidance | `020_agents/` | Autonomy, workflows, validation, nested guidance. |
| Operations | `030_operations/` | Tracker and triage queue. |
| Records | `090_records/` | Dated decisions, audits, and setup outputs. |

Resolve all Project OS paths through this map. Cross-domain relevance belongs in frontmatter `facets` and `related`, not by duplicating an artifact into another class.

Class directories use their numeric prefix as the stable documentation placement. The former unnumbered `docs/brand/` path is retired.

Class prefixes above are physical placement only — *where* a file lives. Class `00` (now `docs/00_system/`) is also the physical home of the `ops` Domain — *what* this class's own content means under the [Domain Documentation Protocol](DOMAIN_PROTOCOL.md) — modeled in [`../domain.md`](../domain.md) and [`../concepts.md`](../concepts.md).

## Owned vocabularies

This file owns two controlled vocabularies (`ops` §13.3 — extend only by governed edit here, never
silently from a workflow or skill):

- **Library Map Class** — `00`, `10`, `20`, `30`, per the table above.
- **Library Map Collection** — the collection names listed for each class (e.g. `governance`,
  `agent-guidance`, `operations`, `records` for class `00`; `content` for class `10`'s Marketing/
  Content area).

`ops.workflow.create-domain` and `ops.workflow.maintain-record` read both as `taxonomy(...)`-typed
inputs; neither may extend either vocabulary without a governed edit to this file.
