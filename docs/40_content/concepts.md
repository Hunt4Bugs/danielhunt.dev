---
id: content.concepts
kind: concept-registry
domain: content
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - marketing
  - assets
  - analytics
related:
  - README.md
  - domain.md
  - ../10_brand/ONTOLOGY.md
sources:
  - ../10_brand/ONTOLOGY.md
---

# Content concepts

This is Content's domain-scoped concept registry (DOMAIN_PROTOCOL.md §9.3). It does not re-derive
the model: [`10_brand/ONTOLOGY.md`](../10_brand/ONTOLOGY.md) is the authoritative, cross-context Brand
model — it owns each entity's definition, relationships, and the taxonomies Content uses. This
file adds the piece the brand-root ontology doesn't carry: a per-concept **entity contract**
(field list, type, cardinality — §10) so a workflow or future skill can validate instances
mechanically. Where ONTOLOGY.md's prose states a relationship or constraint, it is repeated here
only far enough to keep this registry self-contained; ONTOLOGY.md remains the source of truth if
the two ever disagree.

Cross-domain taxonomy ownership: `ref(strategy.theme)` and `ref(audience.segment)` and
`ref(channels.channel)` point at concepts owned by neighboring contexts (Strategy, Audience,
Channels respectively — see [`domain.md`](domain.md)'s Related Domains). `taxonomy(...)` values
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
- created or revised by `analytics.insight`
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
    type: ref(analytics.insight)
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
- aligned to `ref(strategy.theme)`
- addresses `ref(audience.segment)`
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
    type: ref(strategy.theme)
    required: true
    cardinality: 1
  - name: topic_mode
    type: taxonomy(Topic Mode)
    required: true
    cardinality: 1
  - name: audience_segment
    type: ref(audience.segment)
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
    type: ref(audience.segment)
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

## Publication
**ID:** `content.publication`

One channel-specific expression of a Topic through a Blueprint. It owns channel-specific content
and, after publishing, durable publication facts.

### Relationships
- realizes `content.blueprint`
- observed from `content.creator` (when externally captured)
- captured via `content.creator-channel`
- belongs to `ref(channels.channel)`
- takes form `taxonomy(Publication Format)`
- uses `content.script` (primary) and other Assets
- derives from `content.publication` (repurposed expressions)
- receives `analytics.measurement`
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
    type: ref(channels.channel)
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
    type: ref(assets.asset)
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
    type: ref(analytics.measurement)
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
- optionally grouped under a Campaign (Marketing / Campaigns context)

### Constraints
- A Series is not necessarily a Campaign and does not replace Topic or Publication identity.
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
  - name: campaign_refs
    type: ref(marketing.campaign)
    required: false
    cardinality: 0..*
  - name: creating_work_item
    type: ref(content.work-item)
    required: true
    cardinality: 1

## Script
**ID:** `content.script`

A versioned, publication-oriented authored Asset for audio or video (Asset subtype). Instances are
persisted under `10_brand/assets/scripts/`, outside this domain's own instance directories, so this
entry documents the concept and its contract without owning a `_patterns/` file in this pass.

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
persisted under `10_brand/assets/templates/`, outside this domain's own instance directories, so
this entry documents the concept and its contract without owning a `_patterns/` file in this pass.

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

A content-producing entity — a person, company, brand, or organization — being monitored for
competitor, inspiration, peer, or reference intelligence. A Creator is not a general Person or
Organization record; it exists only to support content-intelligence monitoring.

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
    required: true
    cardinality: 1

## Creator Channel
**ID:** `content.creator-channel`

One specific account a Creator holds on a Channel platform type. Named "Creator Channel" rather
than "Channel" specifically to avoid colliding with `channels.channel`, which means the platform
type (for example, Instagram) — a different granularity than one Creator's specific account on
that platform.

### Relationships
- belongs to `content.creator`
- takes form `ref(channels.channel)`

### Constraints
- A Creator Channel must reference exactly one Creator and one Channel.
- A Creator Channel must not duplicate the platform-type registry Channels already owns —
  reference `channels.channel`, never restate it.

### Entity contract
entity: content.creator-channel
fields:
  - name: creator
    type: ref(content.creator)
    required: true
    cardinality: 1
  - name: channel
    type: ref(channels.channel)
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
    required: true
    cardinality: 1

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
  `analytics.insight` already feeds `content.knowledge` — see [Knowledge](#knowledge). This
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

## Workflow
**ID:** `content.workflow`

A reusable operation with defined entry and exit stages (DOMAIN_PROTOCOL.md §3.6). Content reuses
the protocol's own structural primitive name for this concept — see
[`ONTOLOGY.md`](../10_brand/ONTOLOGY.md)'s Core entities table.

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
