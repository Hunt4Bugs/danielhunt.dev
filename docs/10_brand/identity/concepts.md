---
id: identity.concepts
kind: concept-registry
domain: identity
status: active
version: 1
class: "10"
collection: identity
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../specs/2026-05-28-brand-refinement-design.md
---

# Identity concepts

Canonical concept registry for the `identity` domain (see [`domain.md`](domain.md)). Singleton
facts (the Brand Statement, Thesis, Mission, the Toggle) are not registered here as Concepts — a
Concept is a *type* with recurring instances (DOMAIN_PROTOCOL.md §3.2); a one-of-a-kind fact
belongs in [`domain.md`](domain.md)'s Purpose and Model instead.

## Contrarian
**ID:** `identity.contrarian`

A layered position the brand argues from, recurring across content as a frame.

### Relationships
- informs `content.blueprint` and `content.publication` voice

### Constraints
- Exactly three canonical Contrarians exist in v1 (Brand-level, Product-level, Bridge); adding a
  fourth is a deliberate Identity decision, not a per-post variation.

### Persistence

Persisted as subsections in [`README.md`](README.md#contrarians), not as individual documents —
domain-defined persistence (§14). No entity contract is defined per §10.

## Persona
**ID:** `identity.persona`

An internal-only design reference that informs the brand's tone and structure. Never appears in
public copy.

### Relationships
- informs `identity.contrarian` framing and content voice

### Constraints
- A Persona is internal-only design scaffolding, not a public identity; public language uses
  Public Referral Sentences instead.

### Persistence

Persisted as subsections in [`README.md`](README.md#the-persona), not as individual documents
(§14). No entity contract is defined per §10.

## Signature Phrase
**ID:** `identity.signature-phrase`

A repeated public phrase the brand uses across captions, carousels, video lower-thirds, sign-offs,
and the site.

### Relationships
- appears in `content.publication` copy

### Constraints
- Four canonical Signature Phrases exist in v1; each is either a Public Tagline or an Editorial
  Discipline phrase, per the vocabulary-discipline layering in [`README.md`](README.md).

### Persistence

Persisted as a list in [`README.md`](README.md#signature-phrases), not as individual documents
(§14). No entity contract is defined per §10.

## Reference
**ID:** `identity.reference`

An internal-only influence the brand's design borrows craft, tone, or structure from, paired with
an explicit boundary on what is deliberately left behind. Never named in public copy.

### Relationships
- informs [`visual.md`](visual.md) and [`assets/design.md`](../assets/design.md)

### Constraints
- Each Reference states what is borrowed, what is left behind, and its Type (Tonal, Production
  craft, Structural, Methodological).
- References are internal-only; they explain design choices and are never named in public copy.

### Persistence

Persisted as rows in the References table in [`README.md`](README.md#references-we-borrow-from),
not as individual documents (§14). No entity contract is defined per §10; the table's four columns
(Reference, What we borrow, What we leave, Type) are self-describing.

## No _patterns/ or workflows/

Contrarian, Persona, Signature Phrase, and Reference instances are all subsections or table rows
in README.md, not individual documents, so no local `_patterns/` is warranted (§14.1). No
repeatable multi-step operation on Identity itself has recurred enough yet to justify a Workflow;
Identity is read as an input by Content's workflows instead.
