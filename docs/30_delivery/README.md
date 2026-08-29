---
id: delivery.readme
kind: note
domain: delivery
class: "30"
collection: delivery
type: delivery-reference
status: active
version: 1
owner: Daniel Hunt
created: 2026-07-28
updated: 2026-08-29
facets: [site]
related:
  - domain.md
  - concepts.md
  - ../20_site/ARCHITECTURE.md
sources:
  - ../../.github/workflows/deploy.yml
---

# delivery

GitHub Pages deployment configuration is maintained in `.github/workflows/deploy.yml`. The workflow publishes the root `site/` directory when changes are pushed to `main`. This document is an internal pointer; it does not authorize deployment or configuration changes. [`domain.md`](domain.md) states this domain's boundary and [`concepts.md`](concepts.md) is its concept registry (Pipeline), per the [Domain Documentation Protocol](../00_system/010_governance/DOMAIN_PROTOCOL.md).

There is no local `_patterns/` or `workflows/` directory: the single Pipeline instance is a
GitHub Actions workflow file, not a document under `docs/`, and no repeatable multi-step operation
on this domain has recurred enough yet to justify a Workflow.
