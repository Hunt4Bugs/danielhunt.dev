---
id: strategy.concepts
kind: concept-registry
domain: strategy
status: active
version: 1
class: "10"
collection: strategy
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../ONTOLOGY.md
---

# Strategy concepts

Canonical concept registry for the `strategy` domain (see [`domain.md`](domain.md)).

## Theme
**ID:** `strategy.theme`

The single durable strategic lens a Topic aligns to. Not a "Pillar" — this repository deliberately
uses one name for this idea (see [`ONTOLOGY.md`](../ONTOLOGY.md) §"Entities versus taxonomies").

### Relationships
- aligned to by `content.topic`

### Constraints
- A Theme is a controlled vocabulary value, owned exclusively by this domain; `content.topic`
  references it via `ref(strategy.theme)` rather than restating it.
- Adding a Theme is a governed operation (§13.3) — a workflow or skill may propose one but may not
  select it before an explicit update to the registry below.
- Every Topic must resolve to exactly one primary Theme (enforced on the `content.topic` entity
  contract in [`content/concepts.md`](../../content/concepts.md), not repeated here).

### Persistence

Theme instances are persisted as rows in the Theme registry table in
[`README.md`](README.md#theme-registry), not as individual documents — a controlled vocabulary,
not a document-per-instance record (§14). No entity contract is defined per §10; the registry
table's two columns (Theme, Meaning) are self-describing.

## Owned vocabularies

`strategy` owns one controlled vocabulary (§13.3 — extend only by governed edit to the
[Theme registry](README.md#theme-registry), never silently from a workflow or skill):

- **Theme** — the five canonical v1 values: Life Sciences Frontier, Serious Work Human Plot,
  Systems and Observation, Movement and Culture, Lived Build in Public.


## No _patterns/ or workflows/

Theme instances are registry rows, not individual documents, so no local `_patterns/` is
warranted (§14.1). No repeatable multi-step operation on Theme itself has recurred enough yet to
justify a Workflow; Theme is read as an input by `content.workflow.develop-topic` instead.
