---
class: "000"
collection: records
type: setup
status: active
owner: Daniel Hunt
created: 2026-07-28
updated: 2026-07-28
facets: [brand, site, delivery]
related:
  - ../010_governance/LIBRARY_MAP.md
  - ../030_operations/TRACKER.md
  - ../../100_brand/IDENTITY.md
  - ../../100_brand/VISUAL.md
sources:
  - ../../../CLAUDE.md
  - ../../../.github/workflows/deploy.yml
  - ../../100_brand/OPERATING.md
---

# Project OS bootstrap

## Verified evidence

- The site is a static HTML/CSS/vanilla-JS surface in `site/`; GitHub Pages deploys it directly through `.github/workflows/deploy.yml`.
- `CLAUDE.md` identifies `docs/100_brand/IDENTITY.md` and `docs/100_brand/VISUAL.md` as the authoritative sources for brand-shaped work.
- The existing brand corpus was organized under the unnumbered `docs/brand/` path and had no preceding Project OS class map or metadata standard.
- `README.md` describes a retired Astro/Tailwind implementation and conflicts with `CLAUDE.md` and the repository tree.

## Interpretation

The smallest safe operating system is a class-000 layer that maps the current corpus without moving or rewriting it. The repository does not currently need a connected tracker, installed plugin, or external workflow.

## Assumptions

- Daniel Hunt owns the internal records because repository guidance identifies the site as his personal brand surface.
- Existing brand documents remain canonical in their current paths until they are materially revised.

## Decisions

- Created class 000 under `docs/000_system/` with governance, agent guidance, operations, and records collections.
- Kept the existing brand corpus mapped as class 100 and the deployable site and automation as implementation/delivery classes.
- Added an internal Markdown tracker and triage policy; no external tracker, plugin, global configuration, or repository setting was changed.

## Risks and open questions

- The README conflict can mislead a future contributor; it is tracked as OPS-002 and remains unmodified in this bootstrap.
- The class numbers beyond 000 and 100 are local organizational labels, not a claim about a wider canonical taxonomy.

## Next actions

1. Use the tracker and triage flow for the next repository task; refine only if practical friction appears.
2. Authorize a focused documentation-maintenance task if the README should be reconciled with the current static-site architecture.

## Documentation update — 2026-07-28

The brand corpus is now placed in `docs/100_brand/`. Site and delivery references are now mapped to `docs/200_site/` and `docs/300_delivery/` respectively, while deployable source and GitHub configuration remain in `site/` and `.github/`.

## Learning update

The root `AGENTS.md` now directs future work to the library map and preserves the existing brand sources as authoritative.
