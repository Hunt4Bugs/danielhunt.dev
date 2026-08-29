---
id: content.readme
kind: note
domain: content
class: "10"
collection: content
type: domain-reference
status: active
version: 1
owner: Daniel Hunt
created: 2026-05-28
updated: 2026-08-28
facets:
  - marketing
  - assets
  - analytics
related:
  - ../../ONTOLOGY.md
  - domain.md
  - concepts.md
  - operating-plan.md
  - production.md
sources:
  - ../../specs/2026-05-28-brand-refinement-design.md
---

# Content

Content is the Marketing context for reusable editorial material and its lifecycle. The [Brand ontology](../../ONTOLOGY.md) owns the cross-context entity meanings, relationships, and Content taxonomies; [`domain.md`](domain.md) states this domain's boundary and [`concepts.md`](concepts.md) is its domain-scoped, entity-contract-bearing instantiation of that ontology (definitions, relationships, and constraints cross-referenced rather than re-authored, plus the field-level entity contracts DOMAIN_PROTOCOL.md §10 requires). [Strategy](../../strategy/README.md) owns Themes and strategic constraints, [Audience](../../audience/README.md) owns Audience Segments, [Channels](../../channels/README.md) owns distribution destinations and compatible Formats, [Assets](../../assets/README.md) owns reusable resources, and [Analytics](../../analytics/README.md) owns Measurements, Insights, and learning feedback.

## Lifecycle

The default lifecycle is Capture → Validate → Plan → Draft → Review → Produce → Publish → Measure → Learn → Reuse / Repurpose.

Workflow Stage describes where a Work Item is in this lifecycle. Workflow describes the operation being executed. The lifecycle is not a strict one-to-one pipeline: Knowledge and Topics are reusable, a Topic may produce several Blueprints, a Blueprint may produce several Scripts and Publications, and a repurposed expression is a separate Publication linked through `derives from`.

## Records

- [Sources](sources/README.md): provenance for external and firsthand material.
- [Knowledge](knowledge/README.md): reusable synthesis with evidence boundaries.
- [Topics](topics/README.md): reusable subjects, not posts.
- [Blueprints](blueprints/README.md): Topic-specific communication plans.
- [Publications](publications/README.md): channel-specific expressions and durable publication
  facts — Own (authored through a Blueprint) or Observed (captured from a tracked Creator).
- [Series](series/README.md): recurring editorial groupings.
- [Creators](creators/README.md) and [Creator Channels](creator-channels/README.md):
  content-producing entities monitored for competitor, inspiration, peer, or reference
  intelligence, and the specific platform accounts they hold.
- [Reviews](reviews/README.md): structured analysis of an Observed Publication, kept separate so
  observations can evolve without mutating the source record.
- [Work Items](work-items/README.md): persistent executions of one Workflow against one subject.
- [Measurements](../../analytics/measurements/README.md) and [Insights](../../analytics/insights/README.md): observed results and interpretations.
- [Script Assets](../../assets/scripts/README.md) and [Templates](../../assets/templates/README.md): authored audio/video material and reusable scaffolding.

Create records only when real working material exists. Illustrative material belongs under [Examples](examples/README.md) and must be labeled so it cannot be mistaken for actual evidence, publication, or performance.

Each record type's required document shape lives in [`_patterns/`](_patterns/) (`topic.md`, `blueprint.md`, `publication.md`, `work-item.md`, `knowledge.md`, `series.md`, `source.md`, `creator.md`, `creator-channel.md`, `review.md`) rather than in the record type's own `README.md`, which is a routing document only.

## Operations

- [Workflows](workflows/README.md) define reusable operations, contracts, transitions, and failure paths.
- [Content operating plan](operating-plan.md) owns cadence, phasing, launch gates, sustainability, editorial operating rules, and capture targets.
- [Content production](production.md) owns production practice, craft development, and production checklists.
- [Content measurement plan](../../analytics/measurement-plan.md) owns observation windows, success criteria, and interpretation rules.

Workflows consume canonical definitions rather than redefining them. A workflow or future skill may propose new controlled vocabulary, but it may not use that value before approval and an update to the owning canonical context.

## Approval boundary

Repository-local documentation, planning, validation, and illustrative dry runs are reversible internal work. Publishing, external writes, deployments, customer contact, and other external actions require explicit authorization. The Publish Publication workflow stops at that boundary when authorization is absent.
