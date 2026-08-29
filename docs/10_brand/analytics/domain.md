---
id: analytics
kind: domain
domain: analytics
status: active
version: 1
class: "10"
collection: analytics
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
facets:
  - content
related:
  - README.md
  - concepts.md
  - measurement-plan.md
  - ../../content/README.md
sources:
  - ../ONTOLOGY.md
---

# Analytics domain

## Purpose

Analytics turns observed results into learning without letting short-term engagement replace
strategy. It exists as its own domain because Measurement and Insight have their own lifecycle,
evidence standard, and interpretation rules distinct from the Publication they observe.

## Scope

### Includes

- **Measurement** — a dated observed metric for a Publication on a Channel.
- **Insight** — an interpretation of one or more Measurements that creates or revises Knowledge.
- Observation windows, operating success criteria, and interpretation rules — owned by the
  [measurement plan](measurement-plan.md).

### Excludes

- The Publication being measured — owned by [Content](../../content/README.md); Analytics
  attaches Measurements to a Publication without redefining it.
- Knowledge itself — owned by Content (`content.knowledge`); an Insight may create or revise it,
  but does not own its record.
- Strategy, positioning, Theme, and content weighting — owned by
  [Strategy](../strategy/README.md); an Insight may recommend a strategic review, but only an
  explicit Strategy decision changes those.

## Model

- **Measurement** — a dated observed metric for one Publication on one Channel.
- **Insight** — an interpretation of one or more Measurements.

Full definitions, relationships, and entity contracts live in [`concepts.md`](concepts.md).

## Relationships

- `Publication` (`content.publication`) **has many** `Measurement`.
- `Measurement` **informs** `Insight`.
- `Insight` **creates or revises** `Knowledge` (`content.knowledge`).
- `Insight` **may recommend** a `Strategy` review, but never changes Strategy directly.

## Constraints

- A Measurement is evidence, not an explanation or strategic instruction; simulated values are
  permitted only in explicitly illustrative examples, never in the Measurement record collection.
- An Insight must separate observed Measurement values from explanations, and must record
  limitations and plausible competing explanations.
- Do not infer causation from one Publication, and do not compare unlike Formats, Channels, or
  observation windows as though equivalent.
- An overperforming subject does not override the Build/Offline toggle, Theme registry, or
  strategic weighting without an explicit Strategy decision.

## Related Domains

- **[Content](../../content/README.md)** (`docs/content/`) — the primary producer and consumer:
  `content.publication.measurements` carries `ref(analytics.measurement)`, and
  `content.knowledge.related_insights` carries `ref(analytics.insight)`. Content's
  `content.workflow.record-measurements` and `content.workflow.derive-insight` create instances of
  this domain's concepts.
- **[Strategy](../strategy/README.md)** — the only domain an Insight's recommendation can act
  through; Analytics never edits Strategy directly.

## Examples

- A Measurement (`active`) recording Views and Completion Rate for one Publication at the 7-day
  observation window.
- An Insight (`active`) interpreting three Measurements across a Series and recommending a
  Strategy review of the Theme weighting — the review itself is a separate Strategy decision.
