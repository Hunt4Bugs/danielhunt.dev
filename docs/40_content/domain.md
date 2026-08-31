---
id: content
kind: domain
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
  - concepts.md
  - ../10_brand/ONTOLOGY.md
sources:
  - ../10_brand/ONTOLOGY.md
---

# Content domain

## Purpose

Content is the Marketing context for reusable editorial material and its lifecycle: capturing
reusable Knowledge, developing it into communicable Topics, planning channel-agnostic Blueprints,
and expressing those Blueprints as channel-specific Publications, then measuring and learning from
what was published. It exists as its own domain — rather than folding into Strategy, Audience, or
Channels — because it owns a distinct lifecycle (Capture → Validate → Plan → Draft → Review →
Produce → Publish → Measure → Learn → Reuse/Repurpose) and a distinct set of concepts (Knowledge,
Source, Topic, Blueprint, Publication, Series, Script, Script Template, Work Item) that recur
across every piece of brand communication, independent of which Theme, Audience Segment, or
Channel a given instance uses.

## Scope

**Includes**

- The Content lifecycle stages and the Workflows that move a Work Item through them.
- Knowledge and Source: reusable, attributable synthesis and its provenance.
- Topic and Blueprint: reusable subjects and their Topic-specific communication plans.
- Publication: one channel-specific expression of content, either Own (authored through a
  Blueprint) or Observed (captured from a tracked Creator), including its durable publication
  facts.
- Series: recurring editorial groupings of Topics and/or Publications.
- Script and Script Template as Content Asset subtypes (a Script is a versioned,
  publication-oriented authored asset; a Script Template is reusable fill-in-the-blank scaffolding
  that generates Scripts).
- Work Item: the persistent record of one execution of one Content Workflow against one subject.
- Creator and Creator Channel: content-producing entities monitored for competitor, inspiration,
  peer, or reference intelligence, and the specific platform accounts they hold.
- Review: structured analysis of an Observed Publication, kept separate from the Publication so
  observations can evolve without mutating the source record.
- Motif: a reusable observation promoted from two or more corroborating Reviews, which may inform
  or seed Knowledge. Named "Motif" rather than "Pattern" to avoid colliding with this protocol's
  own `Pattern` primitive and the existing Content Pattern taxonomy.
- The Content-owned controlled vocabularies: Content Pattern, Content Purpose, Narrative
  Structure, Visual Hook Type, Verbal Hook Type, Knowledge Kind, Topic Mode, Publication Format,
  Workflow Stage, Work Item State, Production Dependency State, Creator Type, Creator
  Relationship, Review Type, Review Confidence, Motif Category.

**Excludes**

- Theme, the strategic lens a Topic aligns to — owned by [Strategy](../10_brand/strategy/README.md).
- Audience Segment, who a Topic or Publication addresses — owned by [Audience](../10_brand/audience/README.md).
- Channel and channel-Format compatibility — owned by [Channels](../10_brand/channels/README.md).
- General (non-Script/Script-Template) reusable resources — owned by [Assets](../10_brand/assets/README.md).
- Measurement and Insight record contracts and interpretation rules, and the observation-window
  policy — owned by [Analytics](../10_brand/analytics/README.md); Content only produces the Publication
  that Measurements attach to and consumes Insights as an input to Knowledge.
- Voice, evidence, and privacy boundaries as brand-wide rules — owned by [Identity](../10_brand/identity/README.md);
  Content applies them but does not redefine them.

## Model

- **Knowledge** — reusable, attributable synthesis: an insight, observation, experience, research
  finding, question, lesson, process, or framework.
- **Source** — the origin that supports Knowledge (a document, dataset, recording, interview, or
  firsthand context).
- **Topic** — a reusable subject or idea being communicated; not a post.
- **Blueprint** — a Topic-specific communication plan: objective, audience, angle, pattern,
  structure, hook, CTA, proof, and constraints.
- **Publication** — one channel-specific expression of content: Own (a Topic expressed through a
  Blueprint) or Observed (captured from a tracked Creator's Creator Channel, no Blueprint); owns
  channel-specific content and durable publication facts.
- **Series** — a recurring editorial grouping of related Topics and/or Publications.
- **Script** — a versioned, publication-oriented authored asset for audio or video (Asset subtype).
- **Script Template** — reusable fill-in-the-blank scaffolding that generates Scripts (Asset
  subtype).
- **Work Item** — one execution of one Content Workflow against one primary subject, recording
  execution state, current stage, inputs, decisions, outputs, and validation.
- **Creator** — a content-producing entity (person, company, brand, or organization) monitored
  for competitor, inspiration, peer, or reference intelligence; narrower than a general Person or
  Organization record.
- **Creator Channel** — one specific account a Creator holds on a Channel platform type; named
  separately from Channel to avoid colliding with that platform-type registry.
- **Review** — structured analysis of an Observed Publication (visual, format, hook, topic,
  narrative, or technical), kept separate from the Publication so observations can evolve
  independently.
- **Motif** — a reusable observation promoted from two or more corroborating Reviews; may inform
  or seed a new Knowledge record. Named "Motif" rather than the source material's "Pattern" to
  avoid colliding with this protocol's own `Pattern` primitive and the existing Content Pattern
  taxonomy.

Full definitions, relationships, and entity contracts live in [`concepts.md`](concepts.md), which
is this domain's scoped instantiation of the cross-context model in
[`10_brand/ONTOLOGY.md`](../10_brand/ONTOLOGY.md).

## Relationships

- `Source` **supports** `Knowledge`
- `Knowledge` **informs** `Topic`
- `Blueprint` **communicates** `Topic`
- `Script` **produced by** `Blueprint`
- `ScriptTemplate` **instantiates** `Script`
- `Publication` **realizes** `Blueprint` (Own Publications only)
- `Publication` **observed from** `Creator`; `Publication` **captured via** `CreatorChannel`
  (Observed Publications only)
- `Publication` **belongs to** `channels.channel`
- `Publication` **uses** `Script` and other Assets
- `Publication` **derives from** `Publication` (repurposed expressions)
- `Series` **groups** `Topic` and `Publication`
- `Measurement` **received by** `Publication` (record contract owned by Analytics)
- `Insight` **informed by** `Measurement`; `Insight` **creates or updates** `Knowledge`
- `Workflow` **defines** `WorkItem`; `WorkItem` **has one primary subject**
- `Creator` **controls** `CreatorChannel`
- `CreatorChannel` **takes form** `channels.channel`
- `Review` **reviews** `Publication`
- `Motif` **derived from** `Review` (2 or more); `Motif` **may inform** `Knowledge`

## Constraints

- A Topic must reference at least one supporting Knowledge.
- A Blueprint communicates exactly one primary Topic; a Topic may have zero or many Blueprints.
- A Publication is either Own (authored through exactly one primary Blueprint) or Observed
  (captured from a Creator via a Creator Channel, no Blueprint) — never both; either way it has
  exactly one Channel. A Blueprint may have zero or many Own Publications.
- A Publication may use at most one primary Script, plus zero or more other Assets.
- A repurposed expression is a separate Publication linked by `derives from`, never a mutation of
  the source Publication.
- Workflow Stage describes where a Work Item execution is in the Content lifecycle; it is not a
  mutable lifecycle field on the Work Item's primary subject.
- `Draft` is a Workflow Stage, not an entity — git history provides record revision history until
  recurring work requires an independent revision concept.
- A Script may identify an intended Publication Format, but Channel remains a Publication concern.
- A workflow or skill may propose a new controlled-vocabulary value but may not use it before
  approval and an update to the owning canonical context (Content itself for Content-owned
  vocabularies; Strategy, Audience, or Channels for theirs).
- Creator is scoped to content-producing entities monitored for competitor, inspiration, peer, or
  reference intelligence; it does not model general people, organizations, or CRM relationships,
  which remain reserved for the Relationships context.
- A Creator must carry at least one Creator Relationship classification; Creator Type (what it is)
  and Creator Relationship (our stance toward it) must never be conflated into one field.
- A Review does not mutate its source Publication; a Publication may carry multiple Reviews across
  different Review Types (or repeated over time), each evolving independently.
- A Motif must not be created from a single Review — `supporting_reviews` requires at least two
  corroborating Reviews before promotion.

## Related Domains

- [Strategy](../10_brand/strategy/README.md) — owns Theme; Content reads Theme when planning Topics and
  Blueprints but never defines or extends it.
- [Audience](../10_brand/audience/README.md) — owns Audience Segment; Content reads it for Topic and
  Blueprint targeting.
- [Channels](../10_brand/channels/README.md) — owns Channel and Channel/Format compatibility; Content
  reads it when developing and validating Publications.
- [Assets](../10_brand/assets/README.md) — owns general reusable resources; Content owns the Script and
  Script Template subtypes specifically (`10_brand/assets/scripts/`,
  `10_brand/assets/templates/`).
- [Analytics](../10_brand/analytics/README.md) — owns Measurement and Insight record contracts and
  interpretation rules; Content's Publications are the subject Measurements attach to, and
  Insights feed back into Content's Knowledge.
- [Identity](../10_brand/identity/README.md) — owns brand-wide voice, evidence, and privacy boundaries
  that every Content workflow applies.
- [Relationships](../10_brand/relationships/README.md) — remains reserved for general Person,
  Organization, and CRM records; Content's Creator and Creator Channel are a narrower,
  content-producing-entity-only exception scoped to competitor and inspiration monitoring, and do
  not extend or duplicate this context.

## Examples

- The [full lifecycle trace](examples/full-lifecycle-trace.md) walks one illustrative subject
  through every Content Workflow from Capture Knowledge through Repurpose Publication, showing
  each Work Item's stage transition and output — it is a simulation used to validate contracts, not
  asserted evidence of a real Topic, Blueprint, Script, or Publication.
- The [short-form anatomy Knowledge record](knowledge/short-form-anatomy.md), sourced from
  [`colin-and-samir-short-form-anatomy.md`](sources/colin-and-samir-short-form-anatomy.md), is a
  real Knowledge instance: reusable synthesis (pair a visual Scroll Stopper with a verbal Hook,
  carry the promise through Development, fulfill it in the Payoff) with an explicit evidence
  boundary and Source link, demonstrating the Source → Knowledge relationship end to end.
- The [creator monitoring trace](examples/creator-monitoring-trace.md) is the seed of an
  illustrative Creator and Creator Channel record, showing the Creator → Creator Channel
  relationship and the Creator Channel's reference to an existing `channels.channel` value — it is
  a simulation used to validate contracts, not asserted evidence of a real Creator or Creator
  Channel.
