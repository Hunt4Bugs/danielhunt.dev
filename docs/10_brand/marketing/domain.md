---
id: marketing
kind: domain
domain: marketing
status: active
version: 1
class: "10"
collection: marketing
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - content
related:
  - README.md
  - concepts.md
  - ../../content/README.md
sources:
  - ../ONTOLOGY.md
---

# Marketing domain

## Purpose

Marketing owns the coordinated activity through which Brand strategy reaches audiences:
Content, Campaigns, Distribution, Growth, and Funnel. It exists as its own domain, distinct from
Content, because Content is one (fully modeled) area within Marketing's broader coordination
scope — most of that scope is deliberately unmodeled today.

## Scope

### Includes

- **Campaign** — optional, time-bounded coordination around a goal. Not used for ordinary
  recurring publishing.
- Distribution, Growth, and Funnel as named areas of Marketing's future scope (see V1 boundary
  below).

### Excludes

- Content itself (Knowledge, Topic, Blueprint, Publication, and the rest of the reusable editorial
  lifecycle) — modeled independently at [`docs/40_content/`](../../40_content/README.md), its own
  numbered class rather than nested inside this one.
- Identity, audience truth, and offer definitions — owned by
  [Identity](../identity/README.md), [Audience](../audience/README.md), and
  [Offers](../offers/README.md) respectively; Marketing applies them without owning them.
- Distribution destinations and Channel/Format compatibility — owned by
  [Channels](../channels/README.md); Marketing coordinates *how* Publications move through
  Channels, not the Channel registry itself.

## Model

- **Campaign** — optional, time-bounded coordination around a goal. Full definition in
  [`concepts.md`](concepts.md).

### V1 boundary

Distribution, Growth, and Funnel are named scope, not modeled Concepts. Distribution is how
Publications move through Channels and are repurposed — already covered by
`content.publication.derives_from` and the Channels domain; it does not need its own Concept
until recurring cross-Channel coordination work outgrows that. Growth (future experiments and
learning loops) and Funnel (future journey modeling) stay unmodeled and lightweight until
recurring experimentation or an actual funnel exists — do not infer a direct-response funnel from
the current credibility-moat strategy.

## Relationships

- `Campaign` **may group** `content.series` — Series membership under a Campaign is optional and
  many-to-many.
- `Marketing` **applies** Strategy, **uses** Assets, **publishes through** Channels, and **learns
  through** Analytics, without owning any of them.

## Constraints

- Do not use Campaign for ordinary recurring publishing — a Campaign exists only for genuinely
  time-bounded, goal-specific coordination.
- Marketing does not own identity, audience truth, or offer definitions; it applies them.
- Do not model Distribution, Growth, or Funnel as first-class Concepts until recurring work
  requires ownership, lifecycle, or analysis beyond a simple reference (mirrors
  [`ONTOLOGY.md`](../ONTOLOGY.md)'s V1 boundary principle).

## Related Domains

- **[Content](../../40_content/README.md)** (`docs/40_content/`) — the primary consumer:
  `content.series.campaign_refs` carries `ref(marketing.campaign)`.
- **[Strategy](../strategy/README.md)**, **[Assets](../assets/README.md)**,
  **[Channels](../channels/README.md)**, **[Analytics](../analytics/README.md)** — Marketing
  applies, uses, publishes through, and learns through these respectively, without owning them.

## Examples

- No Campaign instances exist yet (v1) — ordinary recurring publishing runs through Content's
  Series and Publication records without Campaign coordination.
