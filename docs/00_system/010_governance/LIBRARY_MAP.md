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

## Class 10 collections

Each is its own modeled protocol Domain (`README.md`, `domain.md`, `concepts.md`, per
[`DOMAIN_PROTOCOL.md`](DOMAIN_PROTOCOL.md) §8.1), physically nested under `docs/10_brand/` rather
than graduated to root — see [Root-level domains](#root-level-domains) below for the one Brand
context (`content`) that has graduated.

| Collection | Domain | Path | Holds |
| --- | --- | --- | --- |
| `brand` | — (root-level Brand corpus material, not itself a modeled Domain) | `docs/10_brand/` | `README.md`, `ONTOLOGY.md`, compatibility pointers, `specs/`, `plans/`, `CHANGELOG.md`. |
| `identity` | `identity` | `identity/` | Enduring meaning, voice, principles, public language. |
| `strategy` | `strategy` | `strategy/` | Positioning, goals, Theme registry, strategic weighting. |
| `audience` | `audience` | `audience/` | Audience Segment registry, painful problems, credibility. |
| `marketing` | `marketing` | `marketing/` | Campaign, and the unmodeled Distribution/Growth/Funnel scope. |
| `offers` | `offers` | `offers/` | Service Offer and Product Offer registries. |
| `assets` | `assets` | `assets/` | Asset and Template registries; hosts Content's Script instances. |
| `channels` | `channels` | `channels/` | Channel registry and Format compatibility. |
| `relationships` | `relationships` | `relationships/` | Reserved (`status: draft`); no Concepts modeled yet. |
| `analytics` | `analytics` | `analytics/` | Measurement and Insight registries, with `_patterns/`. |

## Class 20 collections

| Collection | Domain | Path | Holds |
| --- | --- | --- | --- |
| `implementation` | `site` | `docs/20_site/` | Page and Component registry, `ARCHITECTURE.md`. |

## Class 30 collections

| Collection | Domain | Path | Holds |
| --- | --- | --- | --- |
| `delivery` | `delivery` | `docs/30_delivery/` | Pipeline registry (the GitHub Pages deploy workflow). |

Resolve all Project OS paths through this map. Cross-domain relevance belongs in frontmatter `facets` and `related`, not by duplicating an artifact into another class.

Class directories use their numeric prefix as the stable documentation placement. The former unnumbered `docs/brand/` path is retired.

Class prefixes above are physical placement only — *where* a file lives. Class `00` (now `docs/00_system/`) is also the physical home of the `ops` Domain — *what* this class's own content means under the [Domain Documentation Protocol](DOMAIN_PROTOCOL.md) — modeled in [`../domain.md`](../domain.md) and [`../concepts.md`](../concepts.md).

## Root-level domains

A protocol Domain does not have to sit inside a numbered class. When one outgrows a single class
— enough instance directories, workflows, and cross-references that the numeric nesting only adds
indirection — it graduates to its own directory directly under `docs/`, as a peer of `00_system/`,
`10_brand/`, `20_site/`, and `30_delivery/` rather than nested inside one of them.

| Domain | Path | Migrated from |
| --- | --- | --- |
| `content` | `docs/content/` | `docs/10_brand/marketing/content/` (class `10`, collection `content`) |

A root-level domain has no `class` / `collection` — there is no numbered class to route through —
so those two frontmatter keys are omitted rather than carried forward stale (see
[`../../_conventions/documentation.md`](../../_conventions/documentation.md)). It still carries
`id` / `kind` / `domain` / `status` / `version` and conforms to the same §8.1 required structure
(`README.md`, `domain.md`, `concepts.md`, `_patterns/`, `workflows/`) as any other domain.

## Owned vocabularies

This file owns two controlled vocabularies (`ops` §13.3 — extend only by governed edit here, never
silently from a workflow or skill):

- **Library Map Class** — `00`, `10`, `20`, `30`, per the table above.
- **Library Map Collection** — the collection names listed in each class's collections table
  above (e.g. `governance`, `agent-guidance`, `operations`, `records` for class `00`; `brand`,
  `identity`, `strategy`, `audience`, `marketing`, `offers`, `assets`, `channels`,
  `relationships`, `analytics` for class `10`; `implementation` for class `20`; `delivery` for
  class `30`). A root-level domain (see above) has no collection — it isn't nested in a class.

`ops.workflow.create-domain` and `ops.workflow.maintain-record` read both as `taxonomy(...)`-typed
inputs; neither may extend either vocabulary without a governed edit to this file.
