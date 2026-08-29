---
id: channels
kind: domain
domain: channels
status: active
version: 1
class: "10"
collection: channels
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
---

# Channels domain

## Purpose

Channels owns distribution destinations — where a Publication appears — and which Publication
Formats each destination currently supports. It exists as its own domain because Channel identity
and Channel/Format compatibility are stable operating facts Content depends on, not something
Content should redefine per Publication.

## Scope

### Includes

- The **Channel** registry — the canonical set of distribution destinations (X, Instagram,
  LinkedIn, YouTube, Newsletter) and their status (Active, Planned, Future).
- Channel/Publication-Format compatibility — which `taxonomy(Publication Format)` values a given
  Channel currently accepts.
- Deferred destinations (podcasts, trade publications, conferences) and the rule that excluding
  them is a revisable Channels decision, not an inferred one.

### Excludes

- The Publication record itself, and Publication Format as a taxonomy — owned by
  [Content](../../content/README.md); Channels owns *which* Formats a Channel accepts, not the
  Format taxonomy's definition.
- Cadence, phasing, and launch gates — owned by the
  [Content operating plan](../../content/operating-plan.md).
- Creator Channel (one Creator's specific account on a Channel platform type) — owned by Content
  (`content.creator-channel`), which references `channels.channel` for the platform type rather
  than restating it.

## Model

- **Channel** — a distribution destination and its current Publication Format compatibility. Full
  definition in [`concepts.md`](concepts.md).

## Relationships

- `Channel` **is used by** `content.publication` — every Publication belongs to exactly one
  Channel in v1.
- `Channel` **takes form through** `content.creator-channel` — a Creator Channel is one specific
  account on exactly one Channel platform type.
- `Channel` **constrains** `taxonomy(Publication Format)` — a workflow must reject an incompatible
  Channel/Format pair.

## Constraints

- A Publication has exactly one Channel in v1, whether Own or Observed (enforced on the
  `content.publication` entity contract in [`content/concepts.md`](../../content/concepts.md);
  this domain owns the Channel values and their Format compatibility).
- A workflow must reject a Channel/Format pair that isn't listed as compatible in the registry.
- Adding a Channel, or changing its status or compatible Formats, is a governed, explicit Channels
  decision — never inferred from a one-off invitation or short-term opportunity.

## Related Domains

- **[Content](../../content/README.md)** (`docs/content/`) — the primary consumer:
  `content.publication` and `content.creator-channel` carry `ref(channels.channel)`.
- **[Marketing](../marketing/README.md)** — publishes through Channels without owning the
  registry.
- **[Assets](../assets/README.md)** — Script and Script Template may intend a Publication Format;
  Channel remains a Publication concern, not a Script concern.

## Examples

- `X` (Channel, Active): Text Post, Thread — build-journal fragments and shipping notes.
- `YouTube` (Channel, Planned): Short-form Video, Long-form Video — the hero cinematic vlog once
  launch readiness criteria are met.
