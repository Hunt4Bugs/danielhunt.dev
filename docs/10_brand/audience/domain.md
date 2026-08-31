---
id: audience
kind: domain
domain: audience
status: active
version: 1
class: "10"
collection: audience
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - content
related:
  - README.md
  - concepts.md
  - ../identity/README.md
  - ../strategy/README.md
sources:
  - ../specs/2026-06-01-personal-brand-workbook.md
---

# Audience domain

## Purpose

Audience defines who the brand is for: who it addresses, who it speaks with as peers, who it
speaks about with empathy, what they are stuck with, and what credibility justifies speaking on
it. It exists as its own domain, distinct from Identity, because it owns audience *truth*
(segments, painful problems, credibility) rather than the brand's own voice and meaning.

## Scope

### Includes

- The **Audience Segment** registry — the canonical set of audience segments Content addresses,
  speaks with, or speaks about.
- Painful Problems, the Ideation Table, the Credibility Bank, and the Interest Bank that
  operationalize each Segment into a content backlog.
- The Differentiation Breakdown and Desired Associations that keep the brand's audience-facing
  positions legible over time.

### Excludes

- The Brand Statement, contrarians, and bridge sentence the audience material writes downstream
  from — owned by [Identity](../identity/README.md).
- Themes and strategic weighting — owned by [Strategy](../strategy/README.md).
- Topic, Blueprint, and Publication content itself — owned by
  [Content](../../40_content/README.md), which reads Audience Segment as an input but does not
  redefine it.

## Model

- **Audience Segment** — a named group the brand addresses, speaks with, or speaks about, carrying
  a stable code and an Audience Relationship. Full definition in [`concepts.md`](concepts.md).

## Relationships

- `Audience Segment` **is addressed by / referenced by** `content.topic` and `content.blueprint` —
  every Topic and Blueprint states which Segment it targets.
- `Audience Segment` **is classified by** `taxonomy(Audience Relationship)` (Addressed,
  Spoken-with, Spoken-about) — owned by this domain.

## Constraints

- A Topic and a Blueprint must each reference exactly one Audience Segment (enforced on the
  `content.topic` and `content.blueprint` entity contracts in
  [`content/concepts.md`](../../40_content/concepts.md); this domain owns the Segment values
  themselves).
- A proposed Segment requires the governed taxonomy-addition workflow and approval before use.
- The commercial services audience (Services page) is a distinct acquisition route from the
  primary Life Sciences editorial audience and must not be conflated with it.

## Related Domains

- **[Identity](../identity/README.md)** — the Brand Statement and contrarians Audience material
  writes downstream from.
- **[Strategy](../strategy/README.md)** — Themes and weighting are set with these Segments in
  mind, but do not redefine them.
- **[Content](../../40_content/README.md)** (`docs/40_content/`) — the primary consumer:
  `content.topic` and `content.blueprint` carry `ref(audience.segment)`.

## Examples

- `Primary Editorial Audience` (Audience Segment, code `B2`, Addressed, active): software
  engineers and SaaS/AI founders looking for a meaningful frontier — the segment the brand talks
  *to*.
- `Lab Operations and Scientists` (Audience Segment, code `A`, Spoken-about, active): the end
  users content describes with empathy but does not address directly.
