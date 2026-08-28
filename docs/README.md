---
id: docs
kind: note
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
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

Everything else lives under a numbered class directory, per
[`00_system/010_governance/LIBRARY_MAP.md`](00_system/010_governance/LIBRARY_MAP.md):

| Class | Path | Holds |
| --- | --- | --- |
| 00 | [`00_system/`](00_system/010_governance/LIBRARY_MAP.md) | This repository's own project-operations domain (`ops`): governance, agent guidance, tracker, triage, dated records — and hosts the protocol document itself. |
| 10 | [`10_brand/`](10_brand/README.md) | The personal-brand corpus. `10_brand/marketing/content/` is the first domain fully modeled under this protocol (`content`); the other Brand contexts (Identity, Strategy, Audience, Offers, Assets, Channels, Analytics, Relationships) are lighter-weight reference material today. |
| 20 | [`20_site/`](20_site/ARCHITECTURE.md) | Documentation for the deployable site in `site/`. Not modeled as a protocol domain — no recurring concept instances justify it yet. |
| 30 | [`30_delivery/`](30_delivery/README.md) | Internal delivery/automation documentation. Not modeled as a protocol domain for the same reason. |

Numeric class prefixes are the physical placement scheme (where a file lives); Domains are the
protocol's modeling scheme (what a file means). A class directory may contain zero, one, or more
Domains. Resolve *where something goes* through `LIBRARY_MAP.md`; resolve *what something is*
through the relevant domain's `domain.md` and `concepts.md`.
