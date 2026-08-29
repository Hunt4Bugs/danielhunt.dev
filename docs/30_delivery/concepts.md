---
id: delivery.concepts
kind: concept-registry
domain: delivery
status: active
version: 1
class: "30"
collection: delivery
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../../.github/workflows/deploy.yml
---

# Delivery concepts

Canonical concept registry for the `delivery` domain (see [`domain.md`](domain.md)).

## Pipeline
**ID:** `delivery.pipeline`

An automated build-and-publish process triggered by a repository event.

### Relationships
- publishes `site.page` instances

### Constraints
- A Pipeline's canonical configuration is its GitHub Actions workflow file, not a duplicated
  description in `docs/`.
- Modifying a Pipeline is a CI/CD configuration change and requires explicit user authorization
  per [`AUTONOMY.md`](../00_system/020_agents/AUTONOMY.md); this registry documents what exists,
  it does not authorize changing it.

### Persistence

A Pipeline instance is persisted as its GitHub Actions workflow file under `.github/workflows/`,
not as a document under `docs/` (§14 — instance storage is domain-defined). No entity contract or
`_patterns/` directory is defined: there is currently exactly one Pipeline, and its shape is a
GitHub Actions workflow file, not a repeatable documentation template.

### Current instances

`deploy.yml` — publishes the root `site/` directory to GitHub Pages on every push to `main`.
