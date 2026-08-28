---
class: "000"
collection: governance
type: library-map
status: active
owner: Daniel Hunt
updated: 2026-07-28
---

# Library map

| Class | Purpose | Canonical path | Notes |
| --- | --- | --- | --- |
| 000 | Project operating system, governance, and records | `docs/00_system/` | Internal-only system of record. |
| 100 | Brand foundation and strategy | `docs/10_brand/` | Authoritative brand corpus; filenames are retained. |
| 200 | Site implementation | `docs/20_site/` | Canonical site documentation; deployable source remains in `site/`. |
| 300 | Delivery automation | `docs/30_delivery/` | Internal delivery documentation; configuration remains in `.github/`. |

## Class 000 collections

| Collection | Path | Holds |
| --- | --- | --- |
| Governance | `010_governance/` | Map, metadata rules, policies. |
| Agent guidance | `020_agents/` | Autonomy, workflows, validation, nested guidance. |
| Operations | `030_operations/` | Tracker and triage queue. |
| Records | `090_records/` | Dated decisions, audits, and setup outputs. |

Resolve all Project OS paths through this map. Cross-domain relevance belongs in frontmatter `facets` and `related`, not by duplicating an artifact into another class.

Class directories use their numeric prefix as the stable documentation placement. The former unnumbered `docs/brand/` path is retired.
