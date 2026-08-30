---
id: assets
kind: domain
domain: assets
status: active
version: 1
class: "10"
collection: assets
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - content
related:
  - README.md
  - concepts.md
  - ../../content/README.md
sources:
  - ../ONTOLOGY.md
  - design.md
---

# Assets domain

## Purpose

Assets owns reusable media, design, brand, and knowledge resources, plus the reusable
fill-in-the-blank Templates that scaffold Content records. It exists as its own domain so Content
does not have to own general production resources it merely consumes — Content owns only the two
Asset subtypes tightly bound to its own Blueprint → Script pipeline (Script and Script Template),
which stay defined in [`content/concepts.md`](../../40_content/concepts.md) even though their
instances are physically hosted here.

## Scope

### Includes

- **Asset** — general reusable resources: Media, Design, Brand, and Knowledge Asset subtypes.
- **Template** — reusable fill-in-the-blank scaffolding for Blueprint, post, carousel, video, and
  prompt templates (Blueprint Template instances persist under `templates/blueprints/`).
- The Production Dependency State vocabulary as applied to how a required Asset is supplied
  (Existing Asset, Planned Capture, Obtainable External Asset, Unresolved).
- The reusable visual and implementation contract ([`design.md`](design.md)).

### Excludes

- **Script** (`content.script`) and **Script Template** (`content.script-template`) as *concepts*
  — defined and contracted by [Content](../../40_content/README.md) because they are tightly coupled
  to its Blueprint pipeline. Assets hosts their instances (`scripts/`, `templates/scripts/`) and
  owns the Asset Type / Template taxonomy values that name them, but does not redefine their
  entity contracts.
- Visual direction (photography, editorial art direction) — owned by
  [Identity / visual](../identity/visual.md); this domain owns only the implementation contract
  that direction compiles into.
- Publication Format as a taxonomy, and which Formats a Channel accepts — owned by
  [Content](../../40_content/README.md) and [Channels](../channels/README.md) respectively; a Script
  or Script Template may *intend* a Format without redefining it.

## Model

- **Asset** — a reusable media, design, brand, or knowledge resource.
- **Template** — reusable fill-in-the-blank scaffolding that is not itself a content record.

Full definitions, relationships, and entity contracts live in [`concepts.md`](concepts.md).

## Relationships

- `Asset` **is used by** `content.publication` (`related_assets`, `ref(assets.asset)`).
- `Template` **instantiates** persisted records in the domain it scaffolds — a Blueprint Template
  scaffolds a `content.blueprint`; a Script Template (content-owned, see Excludes) scaffolds a
  `content.script`.
- `Asset` and `Template` **resolve through** `taxonomy(Production Dependency State)` when named as
  a production requirement in a Script or Publication.

## Constraints

- A Template is an Asset subtype; a Blueprint itself is not a Template — it is a Topic-specific
  communication plan (owned by Content).
- Every named visual, audio, design, or other production requirement in a Script or Publication
  must carry exactly one Production Dependency State; `Unresolved` cannot pass validation or enter
  production.
- New brand components must consume [`design.md`](design.md)'s tokens rather than introduce raw
  colors, one-off radii, or arbitrary spacing.

## Related Domains

- **[Content](../../40_content/README.md)** (`docs/40_content/`) — the primary consumer:
  `content.publication.related_assets` carries `ref(assets.asset)`; Content owns Script and Script
  Template as concepts while Assets hosts their instances.
- **[Identity](../identity/README.md)** — owns visual direction and voice that
  [`design.md`](design.md) implements as reusable tokens and components.
- **[Channels](../channels/README.md)** — owns Publication Format compatibility per Channel; a
  Script or Script Template may intend a Format without owning it.

## Examples

- `short-form-video` (Blueprint Template, active): scaffolds a short-form video Blueprint's
  planning decisions, stored at `templates/blueprints/short-form-video.md`.
- `short-form-stop-hook-payoff` (Script Template, active, content-owned concept hosted here):
  generates versioned Scripts from an approved Blueprint, stored at
  `templates/scripts/short-form-stop-hook-payoff.md`.
