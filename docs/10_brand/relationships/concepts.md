---
id: relationships.concepts
kind: concept-registry
domain: relationships
status: draft
version: 1
class: "10"
collection: relationships
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../ONTOLOGY.md
---

# Relationships concepts

Canonical concept registry for the `relationships` domain (see [`domain.md`](domain.md)). This
registry is intentionally empty in v1 — no Concept is modeled here yet.

## Promotion criteria

Promote **Person**, **Organization**, or **Relationship** into a modeled Concept here, with its
own entity contract, only when a real recurring need appears:

- Recurring coordination with the same person or organization requires a durable record rather
  than a one-off contextual link.
- Consent or provenance must be tracked (for example, an interview subject's usage terms).
- Analysis needs an independent identity to reason over (for example, a design-partner
  relationship's history across multiple interactions).

Until then, references to collaborators, design partners, customers, sources, and peers remain
contextual links or attributed `content.source` records. Do not invent a Concept here merely
because a name is mentioned more than once — see DOMAIN_PROTOCOL.md §15 ("Start minimal; do not
invent dozens of concepts") and §18's V1-boundary discipline.

`content.creator` and `content.creator-channel` are a separate, already-modeled exception owned by
[Content](../../40_content/README.md) for content-intelligence monitoring; they do not extend into
this domain and this domain's eventual Person/Organization concepts will not retroactively absorb
them.
