---
id: relationships
kind: domain
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
  - concepts.md
  - ../../content/domain.md
sources:
  - ../ONTOLOGY.md
---

# Relationships domain

## Purpose

Relationships is a reserved Brand context for people, organizations, roles, and interactions that
later need reusable operational records — collaborators, design partners, customers, sources, and
peers. It exists as its own domain boundary now, with `status: draft`, specifically so
[Content](../../40_content/README.md)'s narrower Creator/Creator Channel exception (see Relationships
below) has an explicit home to be promoted into rather than silently expanding.

## Scope

### Includes

- Nothing is modeled yet. This domain reserves the boundary for Person, Organization, and
  Relationship once recurring coordination, consent, provenance, or analysis requires them.

### Excludes

- Content's **Creator** and **Creator Channel** (`content.creator`, `content.creator-channel`) —
  a deliberate, narrow exception for content-intelligence (competitor and inspiration monitoring),
  owned by [Content](../../40_content/README.md). Creator does not extend, generalize, or substitute
  for this domain, and this domain does not absorb Creator.
- General people, organizations, and CRM relationships — explicitly out of v1 scope per
  [`ONTOLOGY.md`](../ONTOLOGY.md)'s V1 boundary, until promoted here.

## Model

No Concepts are modeled yet. See [`concepts.md`](concepts.md) for the explicit promotion
criteria.

## Relationships

- None yet. `content.creator` and `content.creator-channel` remain content-owned and do not
  reference this domain.

## Constraints

- Do not create a Relationship, Person, or Organization record in v1. References to
  collaborators, design partners, customers, sources, and peers remain contextual links or
  attributed `content.source` records instead.
- Promote Person, Organization, or Relationship only when recurring coordination, consent,
  provenance, or analysis genuinely requires an independently identified record — not merely
  because a name is mentioned more than once.

## Related Domains

- **[Content](../../40_content/README.md)** (`docs/40_content/`) — owns the narrow Creator /
  Creator Channel exception this domain does not absorb.

## Examples

None yet — this domain has no instances by design.
