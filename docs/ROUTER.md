---
id: protocol.router.docs
rdf:type: protocol.router
domain: protocol
status: active
version: 1
owner: Daniel Hunt
created: 2026-09-14
updated: 2026-09-14
related:
  - _protocol/PROTOCOL.md
  - _protocol/README.md
  - 00_system/010_governance/LIBRARY_MAP.md
sources: []
---

# Domain router

## Purpose

The entry point for deciding which domain models a subject. Resolve *what something is* here,
then read that domain's `domain.md` and `concepts/`. Resolve *where a file physically lives*
through [`LIBRARY_MAP.md`](00_system/010_governance/LIBRARY_MAP.md) — class prefixes are
placement, not meaning, and the two are independent by design.

## Domains

<!-- generated: derived from docs/**/domain.md. Do not edit by hand. Run `uv run dh index router --write`. -->

| Domain | Root | Ask it about |
| --- | --- | --- |
| `protocol` | [`_protocol/`](_protocol/README.md) | The meta-model every other domain conforms to. |
| `content` | [`40_content/`](40_content/README.md) | Knowledge, Topics, Blueprints, Publications, Creators, Scripts, Work Items. |
| `ops` | [`00_system/`](00_system/README.md) | Tracker, triage, agent guidance, dated records. |
| `site` | [`20_site/`](20_site/README.md) | Pages and shared components in `site/`. |
| `delivery` | [`30_delivery/`](30_delivery/README.md) | How the site reaches production. |

## Routing rules

1. Identify the subject. If it is something the repository produces or records, it belongs to a
   domain above.
2. Read that domain's `concepts/` and pick the concept whose `## Definition` fits.
3. Read that concept file for its contract, constraints, and persistence.
4. Operate through `uv run dh`, never by hand-editing a modelled record.
5. If no concept fits, the subject is either out of scope — check the domain's
   `## Scope` — or it needs modelling. Extend that domain's `concepts/`.

## Adding a domain

Create `docs/<path>/domain.md` with `id`, `root` and a purpose, add at least one concept under
`concepts/`, then run `uv run dh index router --write`. This table regenerates. No engine change,
and no manual edit to this file, is required — the filesystem is the registry, so nothing
central has to learn the new name.
