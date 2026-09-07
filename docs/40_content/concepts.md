---
id: content.concepts
kind: concept-registry
domain: content
status: active
version: 3
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-09-07
related:
  - README.md
  - domain.md
  - themes.md
  - audience.md
  - offers.md
  - ../00_system/010_governance/ONTOLOGY.md
sources:
  - ../00_system/010_governance/ONTOLOGY.md
---

# Content concepts

This is Content's domain-scoped concept registry (DOMAIN_PROTOCOL.md §9.3). It does not re-derive
the model: [`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md) is the authoritative, cross-context Brand
model — it owns each entity's definition, relationships, and the taxonomies Content uses. This
file adds the piece the brand-root ontology doesn't carry: a per-concept **entity contract**
(field list, type, cardinality — §10) so a workflow or future skill can validate instances
mechanically. Where ONTOLOGY.md's prose states a relationship or constraint, it is repeated here
only far enough to keep this registry self-contained; ONTOLOGY.md remains the source of truth if
the two ever disagree.

Theme (`content.theme`), Audience Segment (`content.audience-segment`), Channel
(`content.channel`), Measurement, Insight, Asset, Template, and Creator Relationship are all owned
by Content itself, alongside the entities above — see [`themes.md`](themes.md),
[`audience.md`](audience.md), and [`offers.md`](offers.md) for their registries. `taxonomy(...)` values
below are the sixteen Content-owned controlled vocabularies from ONTOLOGY.md's Taxonomies
section: Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook
Type, Knowledge Kind, Topic Mode, Publication Format, Workflow Stage, Work Item State, Production
Dependency State, Creator Type, Creator Relationship, Review Type, Review Confidence, Motif
Category.

## Knowledge
**ID:** `content.knowledge`

Reusable, attributable material: an insight, observation, experience, research finding, question,
lesson, process, or framework.

### Relationships
- supported by `content.source`
- informs `content.topic`
- created or revised by `content.insight`
- may be informed by `content.motif`
- created or revised by `content.work-item`

### Constraints
- A Knowledge record must identify one Knowledge Kind.
- A Knowledge record must distinguish verified evidence, firsthand account, interpretation, and
  unknowns, and must record an evidence boundary for anything that must not be stated as
  established fact.
- Raw assets are not stored in Knowledge; link to the Asset instead.

### Entity contract
entity: content.knowledge
fields:
  - name: knowledge_kind
    type: taxonomy(Knowledge Kind)
    required: true
    cardinality: 1
  - name: synthesis
    type: text
    required: true
    cardinality: 1
  - name: evidence_boundary
    type: text
    required: true
    cardinality: 1
  - name: supporting_sources
    type: ref(content.source)
    required: true
    cardinality: 1..*
  - name: related_topics
    type: ref(content.topic)
    required: false
    cardinality: 0..*
  - name: related_insights
    type: ref(content.insight)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Source
**ID:** `content.source`

The origin that supports Knowledge, such as a document, dataset, recording, interview, or
firsthand context.

### Relationships
- supports `content.knowledge`
- created by `content.work-item`

### Constraints
- A Source is not automatically an approved brand claim.
- A Source must preserve the distinction between accessible source material, attributed firsthand
  context, and an unsupported assertion.

### Entity contract
entity: content.source
fields:
  - name: title
    type: text
    required: true
    cardinality: 1
  - name: origin
    type: text
    required: true
    cardinality: 1
  - name: source_format
    type: text
    required: true
    cardinality: 1
  - name: date_or_timeframe
    type: date
    required: false
    cardinality: 0..1
  - name: access_conditions
    type: text
    required: true
    cardinality: 1
  - name: scope
    type: text
    required: true
    cardinality: 1
  - name: verification_limits
    type: text
    required: true
    cardinality: 1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Topic
**ID:** `content.topic`

A reusable subject or idea intended for communication. It is not a post.

### Relationships
- supported by `content.knowledge`
- classified by `taxonomy(Topic Mode)`
- aligned to `ref(content.theme)`
- addresses `ref(content.audience-segment)`
- communicated by `content.blueprint`
- grouped by `content.series`

### Constraints
- A Topic must reference at least one supporting Knowledge.
- A Topic must not carry Channel, hook, CTA, treatment, or publication copy — those belong to
  Blueprint or Publication.
- A Topic must state exactly one primary Theme and one Topic Mode.

### Entity contract
entity: content.topic
fields:
  - name: premise
    type: text
    required: true
    cardinality: 1
  - name: theme
    type: ref(content.theme)
    required: true
    cardinality: 1
  - name: topic_mode
    type: taxonomy(Topic Mode)
    required: true
    cardinality: 1
  - name: audience_segment
    type: ref(content.audience-segment)
    required: true
    cardinality: 1
  - name: strategic_fit
    type: text
    required: true
    cardinality: 1
  - name: supporting_knowledge
    type: ref(content.knowledge)
    required: true
    cardinality: 1..*
  - name: credibility_boundary
    type: text
    required: true
    cardinality: 1
  - name: open_questions
    type: list
    required: false
    cardinality: 0..*
  - name: related_blueprints
    type: ref(content.blueprint)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Blueprint
**ID:** `content.blueprint`

A Topic-specific communication plan: objective, audience, angle, pattern, structure, hook, CTA,
proof, and constraints.

### Relationships
- communicates `content.topic`
- uses `taxonomy(Content Pattern)`
- intends `taxonomy(Content Purpose)`
- follows `taxonomy(Narrative Structure)`
- selects `taxonomy(Visual Hook Type)` and `taxonomy(Verbal Hook Type)`
- produces `content.script`
- realized by `content.publication`

### Constraints
- A Blueprint communicates exactly one primary Topic; a Topic may have zero or many Blueprints.
- A short-form Blueprint is script-ready only after its required hook selection is complete.
- Every factual claim, statistic, quotation, or outcome in a Blueprint must link a supporting
  Source.
- A Blueprint is not a Template — reusable production scaffolds are Assets.

### Entity contract
entity: content.blueprint
fields:
  - name: topic
    type: ref(content.topic)
    required: true
    cardinality: 1
  - name: objective
    type: text
    required: true
    cardinality: 1
  - name: audience
    type: ref(content.audience-segment)
    required: true
    cardinality: 1
  - name: angle
    type: text
    required: true
    cardinality: 1
  - name: content_pattern
    type: taxonomy(Content Pattern)
    required: true
    cardinality: 1
  - name: primary_content_purpose
    type: taxonomy(Content Purpose)
    required: true
    cardinality: 1
  - name: supporting_content_purposes
    type: taxonomy(Content Purpose)
    required: false
    cardinality: 0..*
  - name: narrative_structure
    type: taxonomy(Narrative Structure)
    required: true
    cardinality: 1
  - name: visual_hook_type
    type: taxonomy(Visual Hook Type)
    required: false
    cardinality: 0..1
  - name: verbal_hook_type
    type: taxonomy(Verbal Hook Type)
    required: false
    cardinality: 0..1
  - name: audience_promise
    type: text
    required: true
    cardinality: 1
  - name: cta
    type: text
    required: true
    cardinality: 1
  - name: proof
    type: ref(content.source)
    required: true
    cardinality: 1..*
  - name: constraints
    type: text
    required: false
    cardinality: 0..1
  - name: related_scripts
    type: ref(content.script)
    required: false
    cardinality: 0..*
  - name: related_publications
    type: ref(content.publication)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Channel
**ID:** `content.channel`

A distribution destination — not a Publication. Named separately from `content.creator-channel`,
which is one Creator's specific account on a Channel platform type, a different granularity.

### Relationships
- used by `content.publication` (exactly one per Publication in v1)
- taken form through `content.creator-channel`
- constrains `taxonomy(Publication Format)`

### Constraints
- Each Channel carries exactly one status (Active, Planned, Future) and one or more compatible
  Publication Formats.
- A workflow must reject a Channel/Format pair that is not listed as compatible.
- Adding a Channel or changing its compatible Formats is a governed operation (§13.3) — a workflow
  or skill may propose one but may not select it before an explicit update to the registry.

### Persistence

Channel instances are persisted as rows in the Channel registry table in
[`channels.md`](channels.md), not as individual documents — a controlled vocabulary, not a
document-per-instance record (§14). No entity contract is defined per §10; the registry table's
four columns (Channel, Status, Compatible Publication Formats, Role) are self-describing.

### Owned vocabularies

Content owns one controlled vocabulary here (§13.3 — extend only by governed edit to the
[Channel registry](channels.md), never silently from a workflow or skill):

- **Channel** — the five canonical v1 values: X, Instagram, LinkedIn, YouTube, Newsletter, each
  with a status and its currently compatible Publication Formats.

## Publication
**ID:** `content.publication`

One channel-specific expression of a Topic through a Blueprint. It owns channel-specific content
and, after publishing, durable publication facts.

### Relationships
- realizes `content.blueprint`
- observed from `content.creator` (when externally captured)
- captured via `content.creator-channel`
- belongs to `ref(content.channel)`
- takes form `taxonomy(Publication Format)`
- uses `content.script` (primary) and other Assets
- derives from `content.publication` (repurposed expressions)
- receives `content.measurement`
- grouped by `content.series`

### Constraints
- A Publication has exactly one Channel in v1, in both branches below — Channel identifies the
  platform type whether the Publication is authored or observed.
- A Publication is either **Own** (Daniel authored it; `creator` absent) or **Observed** (captured
  from a tracked Creator; `creator` present). A Publication with neither a Blueprint nor a Creator
  fails validation, and a Publication carrying both is invalid — the branches are mutually
  exclusive.
- A materially different channel expression or repurposed output is a separate Publication, never
  an edit to the source Publication.

**Own** (no `creator`):
- Exactly one primary Blueprint.
- A Publication may use at most one primary Script.
- Before real publication, `published_at`, `canonical_url`, and `platform_identifier` must remain
  empty; they are recorded only after an authorized publish via Publish Publication.
- Every production dependency must carry a Production Dependency State; `Unresolved` cannot pass
  validation.

**Observed** (has `creator`):
- No Blueprint — an Observed Publication is captured from a Creator Channel, not planned through
  Content's own Blueprint pipeline.
- Must reference exactly one Creator Channel via `creator_channel`, and that Creator Channel must
  belong to the referenced Creator.
- `published_at`, `canonical_url`, and `platform_identifier` are populated immediately at capture
  time via Capture Publication, not gated behind Publish Publication.

### Entity contract
entity: content.publication
fields:
  - name: blueprint
    type: ref(content.blueprint)
    required: false   # required when `creator` is absent — see Constraints
    cardinality: 0..1
  - name: creator
    type: ref(content.creator)
    required: false
    cardinality: 0..1
  - name: creator_channel
    type: ref(content.creator-channel)
    required: false   # required when `creator` is present — see Constraints
    cardinality: 0..1
  - name: channel
    type: ref(content.channel)
    required: true
    cardinality: 1
  - name: format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1
  - name: content
    type: text
    required: true
    cardinality: 1
  - name: primary_script
    type: ref(content.script)
    required: false
    cardinality: 0..1
  - name: related_assets
    type: ref(content.asset)
    required: false
    cardinality: 0..*
  - name: production_dependencies
    type: taxonomy(Production Dependency State)
    required: true
    cardinality: 0..*
  - name: derives_from
    type: ref(content.publication)
    required: false
    cardinality: 0..1
  - name: measurements
    type: ref(content.measurement)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1
  - name: published_at
    type: date
    required: false
    cardinality: 0..1
    writable_after: content.workflow.publish-publication   # or content.workflow.capture-publication for an Observed Publication
  - name: canonical_url
    type: url
    required: false
    cardinality: 0..1
    writable_after: content.workflow.publish-publication   # or content.workflow.capture-publication for an Observed Publication
  - name: platform_identifier
    type: text
    required: false
    cardinality: 0..1
    writable_after: content.workflow.publish-publication   # or content.workflow.capture-publication for an Observed Publication

## Series
**ID:** `content.series`

A recurring editorial grouping of related Topics and/or Publications.

### Relationships
- groups `content.topic`
- groups `content.publication`

### Constraints
- A Series does not replace Topic or Publication identity.
- A Series must state its continuing premise and inclusion boundary so membership stays legible.

### Entity contract
entity: content.series
fields:
  - name: premise
    type: text
    required: true
    cardinality: 1
  - name: inclusion_boundary
    type: text
    required: true
    cardinality: 1
  - name: related_topics
    type: ref(content.topic)
    required: false
    cardinality: 0..*
  - name: related_publications
    type: ref(content.publication)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Script
**ID:** `content.script`

A versioned, publication-oriented authored Asset for audio or video (Asset subtype). Instances are
persisted under [`scripts/`](scripts/README.md), alongside this domain's other instance
directories; this entry documents the concept and its contract without owning a `_patterns/` file
in this pass.

### Relationships
- produced by `content.blueprint`
- instantiated from `content.script-template`
- intends `taxonomy(Publication Format)`
- used by `content.publication` (primary or supporting)
- resolves through `taxonomy(Production Dependency State)`

### Constraints
- A Script has exactly one primary Blueprint and may not change that Blueprint's Pattern,
  Narrative Structure, or hook types — a plan change routes back to Develop Blueprint.
- A Script does not own Channel; it may support more than one Publication.
- Every named visual or audio beat must carry one Production Dependency State; `Unresolved`
  cannot pass validation.

### Entity contract
entity: content.script
fields:
  - name: primary_blueprint
    type: ref(content.blueprint)
    required: true
    cardinality: 1
  - name: intended_format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1
  - name: source_links
    type: ref(content.source)
    required: false
    cardinality: 0..*
  - name: production_beats
    type: list
    required: true
    cardinality: 1..*
  - name: beat_dependency_states
    type: taxonomy(Production Dependency State)
    required: true
    cardinality: 1..*
  - name: validation_work_item
    type: ref(content.work-item)
    required: false
    cardinality: 0..1
  - name: related_publications
    type: ref(content.publication)
    required: false
    cardinality: 0..*

## Script Template
**ID:** `content.script-template`

Reusable fill-in-the-blank scaffolding that generates Scripts (Asset subtype). Instances are
persisted under [`templates/`](templates/README.md), alongside this domain's other instance
directories; this entry documents the concept and its contract without owning a `_patterns/` file
in this pass.

### Relationships
- instantiates `content.script`
- supports `taxonomy(Content Pattern)`
- follows `taxonomy(Narrative Structure)`
- targets `taxonomy(Publication Format)`

### Constraints
- A Script Template is scaffolding, not a content record, and is not a substitute for evidence or
  editorial judgment.
- A Script Template must name its supported Content Pattern, Narrative Structure, and Publication
  Format.

### Entity contract
entity: content.script-template
fields:
  - name: supported_content_pattern
    type: taxonomy(Content Pattern)
    required: true
    cardinality: 1..*
  - name: supported_narrative_structure
    type: taxonomy(Narrative Structure)
    required: true
    cardinality: 1..*
  - name: target_publication_format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1..*

## Creator
**ID:** `content.creator`

An identity-bearing entity — a person, company, brand, or organization. Covers Daniel Hunt himself
(`relationships` includes `Self`), an external creator monitored for competitor, inspiration,
peer, or reference intelligence, or a general person or organization worth recording.

### Relationships
- controls `content.creator-channel`
- classified by `taxonomy(Creator Type)`
- classified by `taxonomy(Creator Relationship)`

### Constraints
- A Creator must carry at least one Creator Relationship classification.
- `creator_type` (what the Creator is) and `relationships` (our stance toward it) must never be
  conflated into one field.
- Niches and notes are free text, not controlled vocabulary.

### Entity contract
entity: content.creator
fields:
  - name: name
    type: text
    required: true
    cardinality: 1
  - name: creator_type
    type: taxonomy(Creator Type)
    required: true
    cardinality: 1
  - name: relationships
    type: taxonomy(Creator Relationship)
    required: true
    cardinality: 1..*
  - name: niches
    type: list
    required: false
    cardinality: 0..*
  - name: notes
    type: text
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: false
    cardinality: 0..1

## Creator Channel
**ID:** `content.creator-channel`

One specific account a Creator holds on a Channel platform type. Named "Creator Channel" rather
than "Channel" specifically to avoid colliding with `content.channel`, which means the platform
type (for example, Instagram) — a different granularity than one Creator's specific account on
that platform.

### Relationships
- belongs to `content.creator`
- takes form `ref(content.channel)`

### Constraints
- A Creator Channel must reference exactly one Creator and one Channel.
- A Creator Channel must not duplicate the platform-type registry Content already owns —
  reference `content.channel`, never restate it.

### Entity contract
entity: content.creator-channel
fields:
  - name: creator
    type: ref(content.creator)
    required: true
    cardinality: 1
  - name: channel
    type: ref(content.channel)
    required: true
    cardinality: 1
  - name: handle
    type: text
    required: false
    cardinality: 0..1
  - name: url
    type: url
    required: true
    cardinality: 1
  - name: creating_work_item
    type: ref(content.work-item)
    required: false
    cardinality: 0..1

## Review
**ID:** `content.review`

Structured analysis of one Publication — observations about its visual, format, hook, topic,
narrative, or technical characteristics — kept separate from the Publication so those observations
can evolve without mutating the source record.

### Relationships
- reviews `content.publication`
- classified by `taxonomy(Review Type)`
- classified by `taxonomy(Review Confidence)`
- may inform `content.motif` — at least two corroborating Reviews are required before a Motif can
  draw on them (see [Motif](#motif))
- created by `content.work-item`

### Constraints
- A Publication may carry more than one Review — different Review Types, or repeated review of the
  same Review Type over time — without conflict.
- Observations must be specific and evidence-based, describing something actually present in the
  Publication; a vague judgment or bare verdict fails validation.
- A Review does not mutate its source Publication; it is an independently evolving record.

### Entity contract
entity: content.review
fields:
  - name: publication
    type: ref(content.publication)
    required: true
    cardinality: 1
  - name: review_type
    type: taxonomy(Review Type)
    required: true
    cardinality: 1
  - name: observations
    type: text
    required: true
    cardinality: 1..*
  - name: confidence
    type: taxonomy(Review Confidence)
    required: true
    cardinality: 1
  - name: reviewed_at
    type: date
    required: true
    cardinality: 1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Motif
**ID:** `content.motif`

A reusable observation promoted from two or more corroborating Reviews — a specific, repeated
characteristic worth naming and reusing, not a one-off impression from a single occurrence. Named
"Motif" rather than the source brief's "Pattern": the word "Pattern" is already the documentation
protocol's own meta-model primitive (`_patterns/*.md`, see DOMAIN_PROTOCOL.md §3.5) and an
existing Content-owned taxonomy (Content Pattern: Story, Educational, List, Tutorial, ...), so a
third meaning would be ambiguous; the underlying concept and its semantics are otherwise unchanged
from the source brief.

### Relationships
- derived from `content.review` (2..*)
- classified by `taxonomy(Motif Category)`
- may inform `content.knowledge`
- created or updated by `content.work-item`

### Constraints
- A Motif must not be created from a single Review occurrence — at least two corroborating Reviews
  are required. This is enforced structurally, not just in prose: `supporting_reviews` carries
  cardinality `2..*`.
- A Motif must identify exactly one Motif Category.
- A well-evidenced Motif may inform or seed a new Knowledge record, mirroring how
  `content.insight` already feeds `content.knowledge` — see [Knowledge](#knowledge). This
  Motif → Knowledge feed is an explicit design goal of the parent PRD, not an incidental
  similarity.
- A new corroborating Review for an already-named repeated observation updates the existing Motif
  (adds to `supporting_reviews`) rather than creating a duplicate Motif.

### Entity contract
entity: content.motif
fields:
  - name: name
    type: text
    required: true
    cardinality: 1
  - name: motif_category
    type: taxonomy(Motif Category)
    required: true
    cardinality: 1
  - name: description
    type: text
    required: true
    cardinality: 1
  - name: supporting_reviews
    type: ref(content.review)
    required: true
    cardinality: 2..*
  - name: related_knowledge
    type: ref(content.knowledge)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Theme
**ID:** `content.theme`

The single durable strategic lens a Topic aligns to. Not a "Pillar" — this repository deliberately
uses one name for this idea (see [`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md)
§"Entities versus taxonomies").

### Relationships
- aligned to by `content.topic`

### Constraints
- A Theme is a controlled vocabulary value; `content.topic` references it via `ref(content.theme)`
  rather than restating it.
- Adding a Theme is a governed operation (§13.3) — a workflow or skill may propose one but may not
  select it before an explicit update to the registry below.
- Every Topic must resolve to exactly one primary Theme (enforced on the `content.topic` entity
  contract above).

### Persistence

Theme instances are persisted as rows in the Theme registry table in
[`themes.md`](themes.md#theme-registry), not as individual documents — a controlled vocabulary,
not a document-per-instance record (§14). No entity contract is defined per §10; the registry
table's two columns (Theme, Meaning) are self-describing.

### Owned vocabulary

The five canonical v1 Theme values: Life Sciences Frontier, Serious Work Human Plot, Systems and
Observation, Movement and Culture, Lived Build in Public. Extend only by governed edit to the
[Theme registry](themes.md#theme-registry), never silently from a workflow or skill.

## Audience Segment
**ID:** `content.audience-segment`

A named group the brand addresses, speaks with as a peer, or speaks about with empathy, carrying a
stable code so it can be referenced unambiguously from Content records.

### Relationships
- addressed by `content.topic`
- addressed by `content.blueprint`
- classified by `taxonomy(Audience Relationship)`

### Constraints
- Each Segment carries exactly one stable code (e.g. `B2`) and exactly one Audience Relationship
  value (Addressed, Spoken-with, Spoken-about).
- Adding a Segment is a governed operation (§13.3) — a workflow or skill may propose one but may
  not select it before an explicit update to the registry below.
- Use the Segment name and stable code together when ambiguity is possible.

### Persistence

Audience Segment instances are persisted as rows in the Audience Segment registry table in
[`audience.md`](audience.md#audience-segment-registry), not as individual documents — a controlled
vocabulary, not a document-per-instance record (§14). No entity contract is defined per §10; the
registry table's four columns (Segment, Stable code, Audience Relationship, Use) are
self-describing.

### Owned vocabularies

- **Audience Segment** — the four canonical v1 values: Primary Editorial Audience (`B2`), Life
  Sciences Founder Peers (`B1`), Lab Operations and Scientists (`A`), Commercial Services Audience
  (`SERVICES`).
- **Audience Relationship** ([`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md) Supporting
  taxonomy, applied to Audience Segment) — Addressed, Spoken-with, Spoken-about.

## Service Offer
**ID:** `content.service-offer`

A public-facing service the commercial Services page can credibly present.

### Relationships
- classified by the internal service taxonomy (Sales Systems, Marketing Systems, Operations
  Systems, Custom Software)
- presented to `content.audience-segment` (`SERVICES`)

### Constraints
- Public copy uses the concrete public offer name, never the internal service-taxonomy category
  name.
- Each Service Offer uses one plain-language description of what is connected or produced.

### Persistence

Persisted as a list in [`offers.md`](offers.md#current-service-offers), not as individual
documents — domain-defined persistence (§14). No entity contract is defined per §10.

## Product Offer
**ID:** `content.product-offer`

A Brand-adjacent product direction, recorded at its actual maturity. The personal brand may
reference it but is not its go-to-market motion.

### Constraints
- Not interchangeable with a Service Offer.
- The personal brand is not a Product Offer's sales motion; registry inclusion does not imply
  commercial availability, customers, or revenue.

### Persistence

Persisted as prose in [`offers.md`](offers.md#product-offers) — currently one instance (Datavial).
No entity contract is defined per §10; a contract is added if a second Product Offer with distinct
tracked fields emerges.

## Asset
**ID:** `content.asset`

A reusable media, design, brand, or knowledge resource — the general (non-Script, non-Template)
Asset subtypes.

### Relationships
- used by `content.publication` (`related_assets`)
- resolves through `taxonomy(Production Dependency State)` when named as a production requirement

### Constraints
- Each Asset carries exactly one `asset_type` from the four general subtypes: Media, Design,
  Brand, Knowledge Asset.
- Raw asset files are not stored inside a Knowledge record; a Knowledge record links to the Asset
  instead (constraint mirrored from `content.knowledge`).

### Entity contract
```yaml
entity: content.asset
fields:
  - name: asset_type
    type: taxonomy(Asset Type)
    required: true
    cardinality: 1
  - name: title
    type: text
    required: true
    cardinality: 1
  - name: media_type
    type: taxonomy(Media Type)
    required: false   # applies when asset_type is Media
    cardinality: 0..1
  - name: source_or_location
    type: text
    required: true
    cardinality: 1
  - name: licensing_or_access_constraint
    type: text
    required: false
    cardinality: 0..1
```

## Template
**ID:** `content.template`

Reusable fill-in-the-blank scaffolding for Blueprint, post, carousel, video, and prompt templates
— not itself a content record and not a substitute for evidence or editorial judgment. Script
Template is a related but separately owned concept (`content.script-template`, see the
[Script Template](#script-template) section above).

### Relationships
- scaffolds the domain record it targets (e.g. a Blueprint Template scaffolds `content.blueprint`)
- supports `taxonomy(Content Pattern)`
- follows `taxonomy(Narrative Structure)`
- targets `taxonomy(Publication Format)`

### Constraints
- A Template must name its supported Content Pattern, Narrative Structure, and Publication
  Format.
- A Template does not contain publication-specific copy and does not replace the record it
  scaffolds.

### Entity contract
```yaml
entity: content.template
fields:
  - name: template_kind
    type: taxonomy(Asset Type)   # the Template-family values: Template (Blueprint, post,
                                  # carousel, video, prompt)
    required: true
    cardinality: 1
  - name: supported_content_pattern
    type: taxonomy(Content Pattern)
    required: true
    cardinality: 1..*
  - name: supported_narrative_structure
    type: taxonomy(Narrative Structure)
    required: true
    cardinality: 1..*
  - name: target_publication_format
    type: taxonomy(Publication Format)
    required: true
    cardinality: 1..*
```

### Owned vocabularies (Asset / Template)

- **Asset Type** ([`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md) Supporting taxonomy) —
  Media, Design, Brand, Knowledge Asset, Script, Template, Script Template. `content.asset` and
  `content.template` use the general values; Script and Script Template are Content-owned concepts
  hosted alongside them.
- **Media Type** ([`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md) Supporting taxonomy,
  applied to Media Asset) — Image, Video, Audio, Screenshot, Recording, B-roll.

## Measurement
**ID:** `content.measurement`

A dated observed metric for one Publication on one Channel.

### Relationships
- attached to `content.publication`
- informs `content.insight`
- created by `content.work-item`

### Constraints
- A Measurement is evidence, not an explanation or strategic instruction.
- Simulated values are permitted only in explicitly illustrative examples, never in this record
  collection.
- Compare Measurements only when Metric Name, unit, Format, Channel, and observation window are
  meaningfully compatible; missing platform data remains unknown rather than recorded as zero.
- Use cumulative observations at approximately 24 hours, 7 days, and 30 days after publication
  when the Channel exposes the metric, per [`measurement-plan.md`](measurement-plan.md).

### Entity contract
```yaml
entity: content.measurement
fields:
  - name: publication
    type: ref(content.publication)
    required: true
    cardinality: 1
  - name: channel
    type: ref(content.channel)
    required: true
    cardinality: 1
  - name: metric_name
    type: taxonomy(Metric Name)
    required: true
    cardinality: 1
  - name: value
    type: text
    required: true
    cardinality: 1
  - name: unit
    type: text
    required: true
    cardinality: 1
  - name: observation_time
    type: date
    required: true
    cardinality: 1
  - name: period_start
    type: date
    required: true
    cardinality: 1
  - name: period_end
    type: date
    required: true
    cardinality: 1
  - name: collection_method
    type: text
    required: true
    cardinality: 1
  - name: verification_limits
    type: text
    required: true
    cardinality: 1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1
```

## Insight
**ID:** `content.insight`

An interpretation of one or more Measurements that creates or revises Knowledge.

### Relationships
- interprets `content.measurement` (1..*)
- creates or revises `content.knowledge`
- may recommend a Themes review (never changes Themes directly)
- created by `content.work-item`

### Constraints
- Must separate observed Measurement values from explanations.
- Must record limitations and plausible competing explanations.
- Must not infer causation from one Publication, and must not compare unlike Formats, Channels, or
  observation windows as though equivalent.
- May recommend later work or a Themes review; may not silently change Theme, taxonomy, or
  the controlling editorial plan.

### Entity contract
```yaml
entity: content.insight
fields:
  - name: measurements
    type: ref(content.measurement)
    required: true
    cardinality: 1..*
  - name: interpretation
    type: text
    required: true
    cardinality: 1
  - name: limitations
    type: text
    required: true
    cardinality: 1
  - name: competing_explanations
    type: text
    required: false
    cardinality: 0..*
  - name: knowledge_created_or_revised
    type: ref(content.knowledge)
    required: false
    cardinality: 0..*
  - name: positioning_recommendation
    type: text
    required: false
    cardinality: 0..1
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1
```

### Owned vocabulary (Measurement)

**Metric Name** ([`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md) Supporting taxonomy,
applied to Measurement) — Impressions, Views, Watch Time, Completion Rate, Likes, Comments, Saves,
Shares, Clicks.

## Workflow
**ID:** `content.workflow`

A reusable operation with defined entry and exit stages (DOMAIN_PROTOCOL.md §3.6). Content reuses
the protocol's own structural primitive name for this concept — see
[`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md)'s Core entities table.

### Relationships
- defines `content.work-item` (1 Workflow → many Work Items)

### Constraints
- A Workflow declares its own machine contract (`subject_type`, `entry_stage`, `exit_stage`,
  `requires`, `inputs`, `creates`, `updates`, `validation`, `next`, `failure_paths`) per
  DOMAIN_PROTOCOL.md §11 — that contract lives in the Workflow document's own frontmatter, not
  duplicated as an entity contract here.

### Persistence

Workflow instances are persisted as individual documents under [`workflows/`](workflows/README.md)
(`content.workflow.<name>`). No local `_patterns/workflow.md` is defined: a Workflow document's
required shape is already specified once, at the protocol level, by DOMAIN_PROTOCOL.md §11 itself
— a domain-local pattern would only duplicate it.

## Work Item
**ID:** `content.work-item`

One execution of one Workflow against one primary subject. It records execution state, current
stage, inputs, decisions, outputs, and validation.

### Relationships
- executes `content.workflow.*`
- has one primary subject: `ref(content.knowledge | content.source | content.topic |
  content.blueprint | content.script | content.publication | content.series | content.creator |
  content.creator-channel | content.review)`
- creates or updates the records named in its Outputs

### Constraints
- A Work Item has exactly one primary subject, one Work Item State, and one current Workflow
  Stage.
- Work Item State (queued, in progress, blocked, completed, cancelled) is independent of the
  Content lifecycle stage the execution is at.
- A Work Item identifier (`WI-YYYYMMDD-workflow-subject`) is immutable — never renamed after
  creation; a collision appends `-02`, `-03`, and so on.
- Work Items remain in place after completion; change metadata rather than moving or deleting
  them.
- Every domain record the execution creates must link back to its creating Work Item.

### Entity contract
entity: content.work-item
fields:
  - name: workflow
    type: ref(content.workflow)
    required: true
    cardinality: 1
  - name: primary_subject
    type: ref(content.*)   # polymorphic — one of Knowledge, Source, Topic, Blueprint, Script, Publication, Series, Creator, Creator Channel, Review
    required: true
    cardinality: 1
  - name: work_state
    type: taxonomy(Work Item State)
    required: true
    cardinality: 1
  - name: current_stage
    type: taxonomy(Workflow Stage)
    required: true
    cardinality: 1
  - name: inputs
    type: text
    required: true
    cardinality: 1..*
  - name: decisions_and_assumptions
    type: text
    required: false
    cardinality: 0..*
  - name: outputs
    type: list
    required: false
    cardinality: 0..*
  - name: validation
    type: text
    required: true
    cardinality: 1
  - name: predecessors
    type: ref(content.work-item)
    required: false
    cardinality: 0..*
  - name: next_workflows
    type: ref(content.workflow)
    required: false
    cardinality: 0..*
