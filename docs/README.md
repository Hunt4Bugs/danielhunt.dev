---
id: docs
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-29
related:
  - _conventions/README.md
  - _patterns/README.md
  - 00_system/010_governance/DOMAIN_PROTOCOL.md
  - 00_system/010_governance/LIBRARY_MAP.md
---

# docs/

This is the root of the repository's documentation. Everything here is governed by the
[Domain Documentation Protocol v0.2](00_system/010_governance/DOMAIN_PROTOCOL.md) (Domain →
Concept → Relationship → Constraint → Pattern → Workflow). Two things sit above any single domain:

- [`_conventions/`](_conventions/README.md) — the standing rules every document follows
  (identifiers, relationship notation, frontmatter shape).
- [`_patterns/`](_patterns/README.md) — the meta-patterns: what a `domain.md`, `concepts.md`,
  `workflow.md`, a `_patterns/*.md` entry, or a decision record must each contain. These describe
  the *kinds of documents the protocol defines*, not any one domain's concepts.

Most other material lives under a numbered class directory, per
[`00_system/010_governance/LIBRARY_MAP.md`](00_system/010_governance/LIBRARY_MAP.md):

| Class | Path | Holds |
| --- | --- | --- |
| 00 | [`00_system/`](00_system/README.md) | This repository's own project-operations domain (`ops`): governance, agent guidance, tracker, triage, dated records — and hosts the protocol document itself. |
| 20 | [`20_site/`](20_site/README.md) | The `site` domain: the deployable static surface in `site/`, modeled as Page and Component concepts. |
| 30 | [`30_delivery/`](30_delivery/README.md) | The `delivery` domain: how `site`'s pages reach production, modeled as a Pipeline concept. |
| 40 | [`40_content/`](40_content/README.md) | The `content` domain: the whole personal-brand corpus — reusable editorial material and its lifecycle, plus Themes, Audience, Offers, Assets (design/visual/scripts/templates), and Measurements/Insights, all folded in after `10_brand/`'s standalone domains were retired (2026-09-07). Modeled as Knowledge, Topic, Blueprint, Publication, Series, Source, Work Item, Channel, Creator, Creator Channel, Theme, Audience Segment, Service Offer, Product Offer, Asset, Template, Measurement, Insight, Motif, and Review concepts. Includes Daniel Hunt's own identity, held as a Creator record. |

Numeric class prefixes are the physical placement scheme (where a file lives); Domains are the
protocol's modeling scheme (what a file means). A class directory may contain zero, one, or more
Domains. Resolve *where something goes* through `LIBRARY_MAP.md`; resolve *what something is*
through the relevant domain's `domain.md` and `concepts.md`.

A Domain that fully outgrows a single class — enough instance directories, workflows, and
cross-references that nesting it under a numbered class only adds indirection — can instead live
directly at `docs/<domain>/`, as a peer of the numbered class directories rather than inside one.
No Domain currently uses this placement; `content` briefly did (as the first domain fully modeled
under this protocol) and has since been numbered as class 40 above, consistent with every other
Domain. A root-level domain still conforms to the same [§8.1 required
structure](00_system/010_governance/DOMAIN_PROTOCOL.md#8-domain-structure-contract) (`README.md`,
`domain.md`, `concepts.md`, `_patterns/`, `workflows/`) and the same frontmatter contract, minus
the `class` / `collection` fields, which are omitted rather than left stale when this placement is
used (see [`_conventions/documentation.md`](_conventions/documentation.md) and
[`LIBRARY_MAP.md`'s "Root-level domains" section](00_system/010_governance/LIBRARY_MAP.md#root-level-domains)).
