---
id: identity
kind: domain
domain: identity
status: active
version: 1
class: "10"
collection: identity
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - strategy
  - audience
  - content
related:
  - README.md
  - concepts.md
  - visual.md
  - ../strategy/README.md
  - ../audience/README.md
sources:
  - ../specs/2026-05-28-brand-refinement-design.md
  - ../specs/2026-06-01-personal-brand-workbook.md
---

# Identity domain

## Purpose

Identity owns enduring meaning, voice, principles, and public language: who the brand permanently
is, independent of any given period's positioning or operating plan. It exists as its own domain
because it is the one thing every other Brand context reads from and none of them may redefine —
Strategy, Channels, and Marketing own positioning, goals, and operating decisions, but not the
brand's own meaning.

## Scope

### Includes

- The Brand Statement, Thesis, contrarians, bridge sentence, and public referral sentences.
- The Persona set (Maker-Mover, Walking-In Scout) and the Toggle (Build half / Offline half) as
  the brand's structural spine.
- Signature phrases and the References the brand's design borrows from (internal-only; never
  named in public copy).
- Guiding principles, what the brand is and is not, and the aesthetic tie-break.

### Excludes

- Positioning, goals, Themes, and strategic weighting — owned by
  [Strategy](../strategy/README.md), which Identity supplies enduring meaning to but does not
  operate.
- Audience segments, painful problems, and credibility — owned by
  [Audience](../audience/README.md), which the audience-facing parts of Identity (Brand
  Statement, contrarians) write toward.
- Topic, Blueprint, and Publication content itself — owned by
  [Content](../../40_content/README.md), which reads Identity's voice and principles as an input but
  does not redefine them.
- Implementation tokens, typography, geometry, and components — owned by
  [`assets/design.md`](../assets/design.md); Identity's [`visual.md`](visual.md) owns the
  photography and editorial art direction those tokens implement.

## Model

- **Contrarian** — a layered position the brand argues from, recurring as a frame across content.
- **Persona** — an internal-only design reference that informs tone and structure.
- **Signature Phrase** — a repeated public phrase that appears across captions, carousels, and
  the site.
- **Reference** — an internal-only influence the brand's design borrows craft or structure from,
  with an explicit boundary on what is left behind.

Full definitions and relationships live in [`concepts.md`](concepts.md).

## Relationships

- `Contrarian`, `Signature Phrase`, and `Public Referral Sentence` **inform** `content.blueprint`
  and `content.publication` voice without being persisted as Content records themselves.
- `Reference` and `Persona` **inform** [`visual.md`](visual.md) and
  [`assets/design.md`](../assets/design.md) without being named in public copy.
- `Identity` **is read by** every other Brand context; no other context may redefine its meaning
  or voice.

## Constraints

- Internal-only design references (Personas, References, the internal service taxonomy names)
  never appear in public copy — only Public Taglines and Public Referral Sentences do.
- The aesthetic tie-break is absolute when choices conflict: human/lived/curious wins over
  polished/aspirational.
- The Brand Statement must pass the dread test — it must still be true regardless of how long the
  brand has been running.

## Related Domains

- **[Strategy](../strategy/README.md)** — operates within the meaning Identity supplies; does not
  redefine it.
- **[Audience](../audience/README.md)** — the Brand Statement and contrarians write downstream to
  this domain's segments.
- **[Content](../../40_content/README.md)** (`docs/40_content/`) — reads Identity's voice and
  principles when producing Topics and Blueprints.
- **[Assets](../assets/README.md)** — `design.md` implements the tokens Identity's
  [`visual.md`](visual.md) directs.

## Examples

- `Bridge` (Contrarian, active): "You can't build for scientists if you've forgotten how to be a
  person." — justifies Offline-half content existing inside this brand.
- `Walking-In Scout` (Persona, internal-only): the orientation discipline behind Build-half
  content being forward-looking rather than an exit story.
