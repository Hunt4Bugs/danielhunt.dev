---
class: "100"
collection: content
type: record-contract
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - channels
  - analytics
related:
  - ../blueprints/README.md
  - ../../../channels/README.md
  - ../../../analytics/measurements/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Publication records

Store one channel-specific expression per record here. Each Publication records one primary Blueprint, one Channel, one Publication Format, channel-specific content, an optional primary Script, related Assets, production dependencies, any `derives from` relationship, Measurements, and the creating Work Item.

Before real publication, leave `published_at`, `canonical_url`, and `platform_identifier` empty. After an authorized publish, record those durable facts on the Publication. Execution progress belongs to its Work Item. Git history supplies revisions in v1; a materially different channel expression or repurposed output is a separate Publication.
