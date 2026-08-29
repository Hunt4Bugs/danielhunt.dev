---
id: content.publications.readme
kind: note
domain: content
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-28
facets:
  - channels
  - analytics
related:
  - ../concepts.md
  - ../_patterns/publication.md
  - ../blueprints/README.md
  - ../../10_brand/channels/README.md
  - ../../10_brand/analytics/measurements/README.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Publication records

You are in the instance directory for `content.publication`. Store one channel-specific expression
per record here.

- What a Publication *is* (definition, relationships, constraints, entity contract):
  [`concepts.md`](../concepts.md#publication).
- What a Publication document must *contain* (required sections): [`_patterns/publication.md`](../_patterns/publication.md).
- What *creates* a Publication: the [Develop Publication](../workflows/develop-publication.md)
  workflow for an Own Publication (durable publication facts are recorded only by
  [Publish Publication](../workflows/publish-publication.md)), or the
  [Capture Publication](../workflows/capture-publication.md) workflow for an Observed Publication
  (durable publication facts are recorded immediately at capture).
- Related instance directories: [Blueprints](../blueprints/README.md) (realized by a Publication),
  [Channels](../../10_brand/channels/README.md) (Channel registry), and
  [Measurements](../../10_brand/analytics/measurements/README.md) (attach to a published Publication).
