---
id: content
kind: domain
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
  - concepts.md
  - ../00_system/010_governance/ONTOLOGY.md
sources:
  - ../00_system/010_governance/ONTOLOGY.md
---

# Content domain

## Purpose

Content is the whole personal-brand corpus: reusable editorial material and its lifecycle, plus
the positioning, audience, offers, assets, and measurement material that used to live in separate
domains under `docs/10_brand/`. It owns a distinct lifecycle (Capture → Validate → Plan → Draft →
Review → Produce → Publish → Measure → Learn → Reuse/Repurpose) and a distinct set of concepts
(Knowledge, Source, Topic, Blueprint, Publication, Series, Script, Script Template, Work Item)
that recur across every piece of brand communication, independent of which Theme, Audience
Segment, or Channel a given instance uses. Strategy, Audience, Offers, Analytics, and Assets were
retired as standalone domains (2026-09-07): their real content — the Theme and Audience Segment
registries, the credibility bank, the public service-offer descriptions, the measurement plan, and
the design/visual/script/template material — was folded in here rather than deleted, following the
same pattern Channels and Identity used earlier.

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
- Channel: a distribution destination and its compatible Publication Formats ([`channels.md`](channels.md)).
- Creator and Creator Channel: identity-bearing entities Daniel records and relates to — himself,
  external creators monitored for competitor, inspiration, peer, or reference intelligence, or a
  general person or organization worth tracking — and the specific platform accounts they hold.
  Daniel Hunt's own narrative identity (Brand Statement, Persona, voice/evidence/privacy
  boundaries) is held as the `Self` Creator record; every Content workflow applies it.
- Review: structured analysis of an Observed Publication, kept separate from the Publication so
  observations can evolve without mutating the source record.
- Motif: a reusable observation promoted from two or more corroborating Reviews, which may inform
  or seed Knowledge. Named "Motif" rather than "Pattern" to avoid colliding with this protocol's
  own `Pattern` primitive and the existing Content Pattern taxonomy.
- Theme: the single durable strategic lens a Topic aligns to ([`themes.md`](themes.md)).
- Audience Segment: who Content addresses, speaks with, or speaks about ([`audience.md`](audience.md)),
  plus the Painful Problems, Ideation Table, Credibility Bank, Interest Bank, Differentiation
  Breakdown, and Desired Associations that operationalize each Segment.
- Service Offer and Product Offer: the products or services the Brand can credibly introduce or
  support ([`offers.md`](offers.md)).
- Asset and Template: general reusable media, design, brand, and knowledge resources, plus
  fill-in-the-blank Template scaffolding — including the reusable visual and implementation
  contract ([`design.md`](design.md)) and visual direction ([`visual.md`](visual.md)).
- Measurement and Insight: dated observed metrics and their interpretations, plus the observation
  windows, operating success criteria, and interpretation rules that govern them
  ([`measurement-plan.md`](measurement-plan.md)).
- The Content-owned controlled vocabularies: Content Pattern, Content Purpose, Narrative
  Structure, Visual Hook Type, Verbal Hook Type, Knowledge Kind, Topic Mode, Publication Format,
  Workflow Stage, Work Item State, Production Dependency State, Creator Type, Creator
  Relationship, Review Type, Review Confidence, Motif Category, Theme, Audience Segment, Asset
  Type, Media Type, Metric Name.

**Excludes**

- Nothing Brand-shaped remains outside Content. `docs/00_system/` (governance, including the
  Brand-root [`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md)), `docs/20_site/` (the
  deployable site implementation), and `docs/30_delivery/` (how the site reaches production) are
  the only other classes, and none of them originate brand meaning, positioning, or content.

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
- **Channel** — a distribution destination (platform type) and its compatible Publication Formats.
- **Creator** — an identity-bearing entity: Daniel Hunt himself, an external creator (person,
  company, brand, or organization) monitored for competitor, inspiration, peer, or reference
  intelligence, or a general person or organization worth recording.
- **Creator Channel** — one specific account a Creator holds on a Channel platform type; named
  separately from Channel to avoid colliding with that platform-type registry.
- **Review** — structured analysis of an Observed Publication (visual, format, hook, topic,
  narrative, or technical), kept separate from the Publication so observations can evolve
  independently.
- **Motif** — a reusable observation promoted from two or more corroborating Reviews; may inform
  or seed a new Knowledge record. Named "Motif" rather than the source material's "Pattern" to
  avoid colliding with this protocol's own `Pattern` primitive and the existing Content Pattern
  taxonomy.
- **Theme** — the single durable strategic lens a Topic aligns to.
- **Audience Segment** — a named group the brand addresses, speaks with, or speaks about, carrying
  a stable code and an Audience Relationship.
- **Service Offer** — a public-facing service the commercial Services page can credibly present.
- **Product Offer** — a Brand-adjacent product direction, recorded at its actual maturity.
- **Asset** — a reusable media, design, brand, or knowledge resource.
- **Template** — reusable fill-in-the-blank scaffolding that is not itself a content record.
- **Measurement** — a dated observed metric for one Publication on one Channel.
- **Insight** — an interpretation of one or more Measurements.

Full definitions, relationships, and entity contracts live in [`concepts.md`](concepts.md), which
is this domain's scoped instantiation of the cross-context model in
[`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md).

## Relationships

- `Source` **supports** `Knowledge`
- `Knowledge` **informs** `Topic`
- `Topic` **aligned to** `Theme`; `Topic` **addressed by** `Audience Segment`
- `Blueprint` **communicates** `Topic`; `Blueprint` **addressed by** `Audience Segment`
- `Script` **produced by** `Blueprint`
- `ScriptTemplate` **instantiates** `Script`
- `Publication` **realizes** `Blueprint` (Own Publications only)
- `Publication` **observed from** `Creator`; `Publication` **captured via** `CreatorChannel`
  (Observed Publications only)
- `Publication` **belongs to** `content.channel`
- `Publication` **uses** `Script` and other Assets
- `Publication` **derives from** `Publication` (repurposed expressions)
- `Series` **groups** `Topic` and `Publication`
- `Measurement` **received by** `Publication`
- `Insight` **informed by** `Measurement`; `Insight` **creates or updates** `Knowledge`
- `Workflow` **defines** `WorkItem`; `WorkItem` **has one primary subject**
- `Creator` **controls** `CreatorChannel`
- `CreatorChannel` **takes form** `content.channel`
- `Review` **reviews** `Publication`
- `Motif` **derived from** `Review` (2 or more); `Motif` **may inform** `Knowledge`
- `Service Offer` **is classified by** the internal service taxonomy (Sales Systems, Marketing
  Systems, Operations Systems, Custom Software); **presented to** `Audience Segment` (`SERVICES`).

## Constraints

- A Topic must reference at least one supporting Knowledge.
- A Blueprint communicates exactly one primary Topic; a Topic may have zero or many Blueprints.
- A Topic and a Blueprint must each reference exactly one Theme and one Audience Segment.
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
  approval and an update to the owning registry — this domain owns all of them now (see
  [`concepts.md`](concepts.md) for each concept's specific registry file).
- Creator covers Daniel Hunt himself (`Self`), external creators monitored for competitor,
  inspiration, peer, or reference intelligence, and general people or organizations worth
  recording. It is not a full CRM system — do not model releases, claims, deal pipelines, or
  interaction logs on it.
- A Creator must carry at least one Creator Relationship classification; Creator Type (what it is)
  and Creator Relationship (our stance toward it) must never be conflated into one field.
- A Review does not mutate its source Publication; a Publication may carry multiple Reviews across
  different Review Types (or repeated over time), each evolving independently.
- A Motif must not be created from a single Review — `supporting_reviews` requires at least two
  corroborating Reviews before promotion.
- Public language for a Service Offer uses the concrete public name, never the internal
  service-taxonomy category name.
- A Product Offer and a Service Offer are not interchangeable; the personal brand is not a
  Product Offer's sales motion and describes a Product Offer only at its actual maturity.
- A Measurement is evidence, not an explanation or strategic instruction; simulated values are
  permitted only in explicitly illustrative examples, never in the Measurement record collection.
- An Insight must separate observed Measurement values from explanations, and must record
  limitations and plausible competing explanations.
- Do not infer causation from one Publication, and do not compare unlike Formats, Channels, or
  observation windows as though equivalent.
- An overperforming subject does not override Daniel Hunt's identity, Themes, or strategic
  priorities without an explicit decision recorded in [`themes.md`](themes.md).

## Related Domains

- **[`00_system`](../00_system/README.md)** — hosts the Brand-root [`ONTOLOGY.md`](../00_system/010_governance/ONTOLOGY.md)
  and dated evidence in `090_records/`; Content instantiates that model but does not own the
  protocol itself.
- **[`20_site`](../20_site/README.md)** — the deployable static surface; it implements, and must
  not originate, the voice, visual direction, and design tokens Content and Daniel Hunt's Creator
  record own.

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
  relationship and the Creator Channel's reference to an existing `content.channel` value — it is
  a simulation used to validate contracts, not asserted evidence of a real Creator or Creator
  Channel.
- `Systems and Observation` (Theme, active): the default primary Theme for technical instruction.
- `Primary Editorial Audience` (Audience Segment, code `B2`, Addressed, active): working data and
  software engineers across industries — the segment the brand talks *to*.
- `Workflow automation` (Service Offer, active): the broadest entry point among the five public
  offers.
