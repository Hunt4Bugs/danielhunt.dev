---
id: assets.readme
kind: note
domain: assets
class: "10"
collection: assets
type: asset-library
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-29
facets:
  - content
related:
  - domain.md
  - concepts.md
  - ../../content/README.md
  - scripts/README.md
sources:
  - ../ONTOLOGY.md
---

# Assets

Assets are reusable resources referenced by Content and other Brand contexts. Content does not own media, design, brand, knowledge, or template resources. [`domain.md`](domain.md) states this domain's boundary and [`concepts.md`](concepts.md) is its concept registry (Asset, Template), per the [Domain Documentation Protocol](../../00_system/010_governance/DOMAIN_PROTOCOL.md).

## Asset types

- Media: image, video, audio, screenshot, recording, B-roll.
- Design: graphic, diagram, chart, illustration.
- Brand: logo, typography, colors, and style references.
- Knowledge: transcript, notes, documents, datasets.
- Scripts: versioned, publication-oriented authored assets, primarily for video or audio.
- Templates: post, carousel, video, prompt, Blueprint, and Script templates.

A Template is an Asset subtype. A Blueprint is not a Template: it is a Topic-specific communication plan. A Script is an authored Asset produced from one primary Blueprint. A Script Template is a reusable fill-in-the-blank Asset for generating Scripts. The reusable visual and implementation contract lives in [design.md](design.md); visual direction lives in [Identity / visual](../identity/visual.md). Reusable scripts live in [scripts](scripts/) and templates live in [templates](templates/).

## Production dependencies

Every named visual, audio, design, or other production requirement in a Script or Publication uses one ontology-defined Production Dependency State: Existing Asset, Planned Capture, Obtainable External Asset, or Unresolved. Existing Assets link to their record. Planned captures state the required capture. Obtainable external Assets record the intended source and licensing or access constraint. Unresolved dependencies cannot pass validation or enter production.
