---
class: "200"
collection: implementation
type: architecture-reference
status: active
owner: Daniel Hunt
created: 2026-07-28
updated: 2026-07-28
facets: [brand, delivery]
related:
  - ../100_brand/IDENTITY.md
  - ../100_brand/VISUAL.md
  - ../300_delivery/README.md
sources:
  - ../../CLAUDE.md
  - ../../site/index.html
  - ../../site/css/site.css
  - ../../site/js/site.js
---

# Site architecture

## Verified evidence

- The deployable static site is the repository-root `site/` directory.
- `site/index.html` is the one-page public surface; `site/brand/index.html` is the public brand reference.
- `site/css/site.css` and `site/js/site.js` contain the shared styling and browser behavior. Shared navigation and footer are rendered by web components in `site/js/site.js`.
- GitHub Pages uploads `site/` directly through `.github/workflows/deploy.yml`.

## Canonical constraints

Brand-shaped site work must first follow `../100_brand/IDENTITY.md` and `../100_brand/VISUAL.md`. Keep all deployable implementation inside `site/`; this class holds its internal documentation only. There is no build step or configured test suite.

## Open question

The root README describes a retired Astro/Tailwind implementation. Its correction remains tracked as OPS-002 in `../000_system/030_operations/TRACKER.md`.
