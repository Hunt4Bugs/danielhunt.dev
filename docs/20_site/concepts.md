---
id: site.concepts
kind: concept-registry
domain: site
status: active
version: 1
class: "20"
collection: implementation
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
  - ARCHITECTURE.md
sources:
  - ../../CLAUDE.md
---

# Site concepts

Canonical concept registry for the `site` domain (see [`domain.md`](domain.md)). Instances are
persisted as the actual HTML/JS files under the repository-root `site/` directory, not as
documents under `docs/` — per DOMAIN_PROTOCOL.md §14 ("If Engineering Services are represented
primarily by source code, you may not need `services/` at all — the Concept still exists in the
model"). No `_patterns/` directory exists for the same reason: the pattern each Page and Component
follows is the existing code itself plus the constraints below, not a template document.

## Page
**ID:** `site.page`

A routed, deployable HTML surface with its own canonical URL and statically duplicated head
metadata.

### Relationships
- uses `site.component` for shared chrome (auxiliary pages only)
- implements tokens and components from `assets/design.md`
- published by `delivery.pipeline`

### Constraints
- Every Page carries its own OG, Twitter, and JSON-LD metadata inline — crawlers do not execute
  JS, so metadata cannot be centrally templated.
- The home page (`index.html`) owns the persistent header role, hover/focus wordmark, and
  in-page About/Contact states directly in static HTML; auxiliary pages render shared chrome
  through `site.component` web components instead of duplicating markup.
- A Page's brand-shaped copy and layout decisions must follow
  [Identity](../10_brand/identity/README.md) and [`visual.md`](../10_brand/identity/visual.md).

### Current instances

`site/index.html`, `site/services/index.html`, `site/brand/index.html`,
`site/contact-card/index.html` (this last one `noindex`, for in-person contact sharing).

## Component
**ID:** `site.component`

A shared HTML web component reused across auxiliary (non-home) pages for consistent chrome.

### Relationships
- used by `site.page` (auxiliary pages)

### Constraints
- A Component is defined once, in `site/js/site.js`, and consumed by reference — never
  copy-pasted markup duplicated per Page.
- Home-only interactive behavior (hover/focus wordmark, hash navigation, browser-history routing)
  stays guarded to the spatial index and is not generalized into a shared Component unless a
  second page genuinely needs it.

### Current instances

`<site-nav>`, `<site-footer>`.
