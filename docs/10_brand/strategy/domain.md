---
id: strategy
kind: domain
domain: strategy
status: active
version: 1
class: "10"
collection: strategy
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - content
related:
  - README.md
  - concepts.md
  - ../identity/README.md
  - ../../content/domain.md
sources:
  - ../ONTOLOGY.md
  - ../specs/2026-05-28-brand-refinement-design.md
---

# Strategy domain

## Purpose

Strategy sets direction and constraints for the Brand: positioning, goals, Themes, differentiation,
and the strategic weighting that governs what Content produces. It exists as its own domain,
distinct from Identity, because it owns operating decisions (what to prioritize now) rather than
enduring meaning and voice (who the brand permanently is).

## Scope

### Includes

- The positioning statement and goals.
- The **Theme** registry — the canonical set of durable strategic lenses a Topic aligns to.
- Strategic content weighting (the Life-Sciences-vs-general-operator-material guardrail) and the
  constraints that keep it a planning guardrail rather than a per-item quota.

### Excludes

- Enduring meaning, voice, persona, and public language — owned by [Identity](../identity/README.md).
- Audience truth (who the brand is for, painful problems, credibility) — owned by
  [Audience](../audience/README.md).
- Topic, Blueprint, and Publication content itself — owned by [Content](../../40_content/README.md),
  which reads Theme as an input but does not redefine it.
- Distribution mechanics and Channel/Format compatibility — owned by
  [Channels](../channels/README.md).

## Model

- **Theme** — the single durable strategic lens a Topic aligns to. Full definition in
  [`concepts.md`](concepts.md).

## Relationships

- `Theme` **is aligned to by** `content.topic` — every Topic states exactly one primary Theme.
- `Strategy` **constrains** Content's Topic creation without owning Topic itself.
- `analytics.insight` **may recommend** a Strategy review, but only an explicit Strategy decision
  changes Themes, positioning, or content weighting — Measurements and Insights inform, they do
  not automatically redirect strategy.

## Constraints

- A Topic must state exactly one primary Theme (constraint lives structurally on
  `content.topic` in [`content/concepts.md`](../../40_content/concepts.md); Strategy owns the Theme
  values themselves).
- Use `Theme`, not `Pillar` — do not introduce a second, competing strategic-lens concept.
- A proposed Theme requires the governed taxonomy-addition workflow and approval before use; a
  workflow or skill may propose one but may not select it before that approval.
- Strategic content weighting is a planning guardrail, not a quota enforced on every batch or
  period.

## Related Domains

- **[Identity](../identity/README.md)** — supplies the enduring meaning and voice Strategy
  operates within; Strategy does not redefine it.
- **[Audience](../audience/README.md)** — Strategy's Themes and weighting are set with Audience
  Segments in mind, but Audience owns segment truth.
- **[Content](../../40_content/README.md)** (`docs/40_content/`) — the primary consumer: `content.topic`
  carries `ref(strategy.theme)` and every Topic must resolve to exactly one Theme.
- **[Channels](../channels/README.md)** and **[Marketing](../marketing/README.md)** — apply
  Strategy's direction to distribution and coordinated activity without owning Theme.

## Examples

- `Life Sciences Frontier` (Theme, active): the primary Theme most Build-half Topics align to.
- `Movement and Culture` (Theme, active): the Theme Offline-half Topics typically align to.
