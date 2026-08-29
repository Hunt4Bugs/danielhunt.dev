---
id: site
kind: domain
domain: site
status: active
version: 1
class: "20"
collection: implementation
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - brand
  - delivery
related:
  - README.md
  - concepts.md
  - ARCHITECTURE.md
  - ../30_delivery/domain.md
sources:
  - ../../CLAUDE.md
  - ../../site/index.html
---

# Site domain

## Purpose

`site` is the domain for `danielhunt.dev`'s deployable static surface: the routed pages that
carry the brand's credibility and contact path, and the shared web components those pages reuse.
It exists as its own domain, distinct from `delivery`, because it owns *what the site is and
contains* (pages, shared chrome, brand-implementation constraints), while `delivery` owns *how it
reaches production*.

## Scope

### Includes

- **Page** — a routed, deployable HTML surface with its own metadata and canonical URL
  (`index.html`, `services/index.html`, `brand/index.html`, `contact-card/index.html`).
- **Component** — a shared HTML web component reused across auxiliary pages (`site-nav`,
  `site-footer`, defined in `site/js/site.js`).
- Verified implementation facts about the deployable `site/` tree — kept in
  [`ARCHITECTURE.md`](ARCHITECTURE.md), which this domain.md does not re-derive.

### Excludes

- Brand meaning, voice, and visual direction — owned by [Identity](../10_brand/identity/README.md)
  and its [`visual.md`](../10_brand/identity/visual.md); Site work must follow those before any
  brand-shaped implementation decision.
- The reusable design-token and component contract — owned by
  [`assets/design.md`](../10_brand/assets/design.md); `site/css/site.css` is that contract's
  implementation, not a competing definition.
- How the site reaches production (build, deploy trigger, hosting) — owned by
  [Delivery](../30_delivery/README.md).

## Model

- **Page** — a routed, deployable HTML surface.
- **Component** — a shared web component reused across pages.

Full definitions and relationships live in [`concepts.md`](concepts.md).

## Relationships

- `Page` **uses** `Component` for shared chrome on auxiliary (non-home) pages.
- `Page` **implements** the tokens and components defined in
  [`assets/design.md`](../10_brand/assets/design.md).
- `Page` **is published by** `delivery.pipeline` — the deploy workflow uploads the `site/`
  directory that these Page instances live in.

## Constraints

- All deployable implementation stays inside the repository-root `site/` directory; this domain's
  documentation is internal reference only and never itself deployed.
- Brand-shaped Site work must first follow [Identity](../10_brand/identity/README.md) and its
  [`visual.md`](../10_brand/identity/visual.md) — this domain does not originate brand decisions.
- Head metadata (OG, Twitter, JSON-LD) is statically duplicated per Page because crawlers do not
  run JS — a Page's canonical metadata is not centrally templated.
- There is no build step and no configured test suite for `site/`.

## Related Domains

- **[Delivery](../30_delivery/README.md)** (`docs/30_delivery/`) — publishes this domain's Page
  instances to production; Site does not own the publish mechanism.
- **[Identity](../10_brand/identity/README.md)** and **[Assets](../10_brand/assets/README.md)** —
  Site implements, and must not originate, their voice, visual direction, and design tokens.

## Examples

- `index.html` (Page, active): the spatial profile surface — the primary in-page About/Contact
  entry point.
- `services/index.html` (Page, active): the indexed commercial-services route, static and
  crawlable without interaction.
