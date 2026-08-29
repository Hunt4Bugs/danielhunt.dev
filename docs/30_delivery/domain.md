---
id: delivery
kind: domain
domain: delivery
status: active
version: 1
class: "30"
collection: delivery
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - site
related:
  - README.md
  - concepts.md
  - ../20_site/domain.md
sources:
  - ../../.github/workflows/deploy.yml
---

# Delivery domain

## Purpose

`delivery` is the domain for how the Site domain's Page instances reach production. It exists as
its own domain, distinct from `site`, because it owns the publish mechanism (trigger, target,
gate) rather than the pages and components being published.

## Scope

### Includes

- **Pipeline** — an automated build-and-publish process triggered by repository events, currently
  the single GitHub Pages deploy pipeline defined in `.github/workflows/deploy.yml`.

### Excludes

- The pages and components being published — owned by [Site](../20_site/README.md); Delivery
  publishes them without owning their content or implementation.
- Deployment or configuration authorization — this domain is an internal pointer; it does not
  itself authorize a deploy or a workflow-configuration change.

## Model

- **Pipeline** — an automated build-and-publish process.

Full definition lives in [`concepts.md`](concepts.md).

## Relationships

- `Pipeline` **publishes** `site.page` instances by uploading the `site/` directory directly (no
  build step).
- `Pipeline` **is triggered by** a push to `main`.

## Constraints

- This domain's documentation is an internal pointer; it does not authorize deployment or
  configuration changes on its own — those require explicit user authorization per
  [`AUTONOMY.md`](../00_system/020_agents/AUTONOMY.md).
- The canonical Pipeline configuration lives in `.github/workflows/deploy.yml`, not duplicated
  here; this domain documents what the pipeline does, not a competing definition of it.

## Related Domains

- **[Site](../20_site/README.md)** (`docs/20_site/`) — the domain whose Page instances this
  domain's Pipeline publishes.

## Examples

- `deploy.yml` (Pipeline, active): publishes the root `site/` directory to GitHub Pages on every
  push to `main`, with no build step.
