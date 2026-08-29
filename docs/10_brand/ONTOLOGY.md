---
class: "10"
collection: brand
type: ontology
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - content
  - assets
  - analytics
related:
  - README.md
sources:
  - marketing/content/sources/colin-and-samir-short-form-anatomy.md
---

# Brand ontology v1

## Purpose

This is a lightweight, domain-driven model for planning, creating, reusing, distributing, and learning from personal-brand content. It is documentation, not a database schema, RDF/OWL model, API, or implementation contract.

This is the Brand-root model: it owns entity definitions, relationships, and taxonomy ownership across every Brand context. [`marketing/content/domain.md`](marketing/content/README.md) and [`marketing/content/concepts.md`](marketing/content/concepts.md) are Content's domain-scoped instantiation of it under the [Domain Documentation Protocol](../00_system/010_governance/DOMAIN_PROTOCOL.md) — they cross-reference the definitions, relationships, and constraints below rather than re-authoring them, and add the field-level entity contracts (§10) each Content concept's persisted instances require. Content is the first Brand context fully modeled under that protocol; other contexts remain lighter-weight reference material here until they receive the same treatment.

## Bounded contexts

`Brand` is the root domain. Its primary contexts are Identity, Strategy, Audience, Marketing, Offers, Assets, Channels, Relationships, and Analytics. Marketing contains Content, Campaigns, Distribution, Growth, and Funnel. Content contains Knowledge, Source, Topic, Blueprint, Publication, Series, Creator, Creator Channel, Review, Motif, Workflow, Work Item, and Taxonomy. Script and Script Template are Content Asset subtypes.

## Source migration map

| Former active reference | Canonical v1 location | Notes |
| --- | --- | --- |
| `IDENTITY.md` | [Identity](identity/README.md), [Strategy](strategy/README.md), [Offers](offers/README.md), [Channels](channels/README.md) | Identity remains the detailed narrative source; cross-context ownership is explicit. |
| `AUDIENCE.md` | [Audience](audience/README.md) | Moved intact with repaired links. |
| `OPERATING.md` | [Marketing / Content](marketing/content/README.md), [Channels](channels/README.md), [Analytics](analytics/README.md) | Content Operations remains the detailed operational source. |
| `VISUAL.md` | [Identity / visual](identity/visual.md) | Visual direction remains a supporting Identity reference. |
| `DESIGN.md` | [Assets / design](assets/design.md) | The reusable design-system contract is an Asset reference. |

The former paths are compatibility pointers for historical links. Plans, specifications, and the changelog remain in place as dated evidence.

## Core entities

| Entity | Definition |
| --- | --- |
| Knowledge | Reusable, attributable material: an insight, observation, experience, research finding, question, lesson, process, or framework. |
| Source | The origin that supports Knowledge, such as a document, dataset, recording, interview, or firsthand context. |
| Topic | A reusable subject or idea being communicated. It is not a post. |
| Blueprint | A Topic-specific communication plan: objective, audience, angle, pattern, structure, hook, CTA, proof, and constraints. |
| Publication | One channel-specific expression of a Topic through a Blueprint. It owns channel-specific content and durable publication facts. |
| Series | A recurring editorial grouping of related Topics and/or Publications. |
| Workflow | A reusable operation with defined entry and exit stages. |
| Work Item | One execution of one Workflow against one primary subject. It records execution state, current stage, inputs, decisions, outputs, and validation. |
| Asset | A reusable media, design, brand, knowledge, script, or template resource. A Script is a versioned, publication-oriented authored asset for audio or video; a Script Template is reusable fill-in-the-blank scaffolding that generates Scripts. |
| Measurement | A dated observed metric for a Publication on a Channel. |
| Insight | An interpretation of Measurements that creates or revises Knowledge. |
| Creator | A content-producing entity — a person, company, brand, or organization — being monitored for competitor, inspiration, peer, or reference intelligence. Narrower than a general Person or Organization record. |
| Creator Channel | One specific account a Creator holds on a Channel platform type. Named separately from Channel because it is a different granularity: one Creator's specific account, not the platform type itself. |
| Review | Structured analysis of one Publication, kept separate from the Publication so observations can evolve without mutating the source record. |
| Motif | A reusable observation promoted from two or more corroborating Reviews. Named "Motif" rather than the source brief's "Pattern" — "Pattern" is already this protocol's own meta-model primitive (`_patterns/*.md`) and an existing Content taxonomy (Content Pattern), so a third meaning would be ambiguous; the semantics carry over unchanged under the new name. |

## Relationships

- Knowledge and Topic are many-to-many. Source and Knowledge are many-to-many.
- A Topic has zero or many Blueprints; each Blueprint communicates one primary Topic.
- A Blueprint has zero or many Publications; each Publication has one primary Blueprint and one Channel in v1. A Publication stores its channel-specific content and, after publishing, durable facts such as publication time, canonical URL, and platform identifier.
- A Blueprint has zero or many Script Assets; each Script has one primary Blueprint. A Publication may use one primary Script plus other Assets.
- Publications and Assets are many-to-many. Repurposed outputs are separate Publications linked by `derives from`.
- Series can group zero or many Topics and Publications. Campaign membership is optional and many-to-many.
- A Publication has many Measurements. Measurements inform Insights; Insights create or revise Knowledge.
- Workflow defines many Work Items. A Work Item executes one Workflow, has one primary subject, one Work Item State, and one current Workflow Stage.
- Workflow Stage describes where one Work Item execution is in the Content lifecycle. It is not a mutable lifecycle field on the Work Item's primary subject. Work Item State describes whether that execution is queued, in progress, blocked, completed, or cancelled.
- `Draft` is a Workflow Stage, not an entity. Git history provides record revision history in v1. Promote a revision concept only when recurring work requires independent identity, provenance, relationships, or analysis.
- A Script may identify an intended Publication Format, but Channel remains a Publication concern. A Script may support more than one Publication.
- A Creator controls zero or many Creator Channels; each Creator Channel belongs to exactly one Creator and takes form through exactly one `channels.channel` value. A Creator must carry at least one Creator Relationship classification, and may carry more than one at once (for example, both Competitor and Inspiration).
- A Publication has zero or many Reviews; each Review reviews exactly one Publication. A Publication is not required to have a Review, and a Review does not mutate the Publication it reviews.
- A Motif is derived from two or more corroborating Reviews (never one); a well-evidenced Motif may inform or seed Knowledge, mirroring how Measurements inform Insights which create or revise Knowledge. Reinforcing an existing Motif with a new corroborating Review updates that Motif rather than creating a duplicate.

## Entities versus taxonomies

Use an entity when it has a reusable identity, independent lifecycle, provenance, or relationships. Use a taxonomy when a shared controlled label classifies an entity but does not require its own lifecycle. `Theme` is the single durable strategic lens. Do not introduce both Theme and Pillar in v1. A Blueprint is not a Template: Templates are Asset subtypes.

Controlled vocabularies remain with the context that owns their meaning. This ontology owns Content taxonomies. [Strategy](strategy/README.md) owns Theme, [Audience](audience/README.md) owns Audience Segment, and [Channels](channels/README.md) owns Channel. A governed addition updates its authoritative owner and is not selectable before approval.

## Taxonomies

These are the canonical v1 starter vocabularies. They are deliberately extensible, but additions should be made here before use so that planning and analysis retain a shared language.

### Blueprint taxonomies

| Taxonomy | Applied to | Values | Definition |
| --- | --- | --- | --- |
| Content Pattern | Blueprint | Story, Educational, List, Tutorial, Framework, Case Study, Breakdown, Comparison, Myth vs Fact, Opinion, Challenge, Journey, Experiment, Prediction, Reaction, Review, Behind the Scenes | The repeatable editorial shape. Use `Story` for storytelling and `Educational` for explanatory teaching. |
| Content Purpose | Blueprint | Educate, Inform, Entertain, Inspire, Persuade, Build Trust, Engage, Convert | The intended audience effect. A Blueprint may identify one primary purpose and supporting purposes. |
| Narrative Structure | Blueprint | Hook → Journey → Payoff; Problem → Solution; Before → After; Setup → Conflict → Resolution; Question → Answer; Claim → Evidence; Hook → Problem → Framework → Example → Payoff; Scroll Stopper + Verbal Hook → Development → Payoff | The ordered rhetorical or story sequence inside the expression. |
| Visual Hook Type | Blueprint | Potential Energy, Kinetic Energy, General Motion, Trend Hook, God View, Novel / Unusual Visual, Emotionally Charged Imagery, Close-Up Shot, Rapid Scene Change, Bold Colors / High Contrast, Visual Symmetry / Balance, Celebrity / Face Equity, Satisfying, Cute Hook, Text Hook | The visual mechanism used to stop the scroll. |
| Verbal Hook Type | Blueprint | Question, Personal Story, Statistic, Quotation, Fact, Shocking / Exaggeration, Description, Cliffhanger / Suspense, Humor, Dialogue, Emotion, Prediction, Motivational, Opinion, Definition | The spoken or on-screen language mechanism that establishes the audience promise or open loop. |

Content Pattern answers **what kind of editorial treatment is this?** Content Purpose answers **what should it do for the audience?** Narrative Structure answers **in what order is it communicated?** These are separate classifications and may be combined freely when they make sense.

For the short-form structure, the Scroll Stopper and Verbal Hook begin together; Development carries the proof, observation, story, or example; Payoff fulfills the promise. The source's 60-second timing is guidance for that template only: Scroll Stopper 0–3 seconds, Verbal Hook 0–5 seconds, Payoff in the final 5–10 seconds.

### Hook usage conditions

| Condition | Hook types |
| --- | --- |
| Evidence required | Statistic, Fact, Quotation |
| Editorial review required | Trend Hook, Celebrity / Face Equity, Cute Hook, Shocking / Exaggeration, Motivational |
| Always required | Truthfulness, documentary restraint, observation over preaching, and no unsupported performance claims. |

### Content and delivery taxonomies

| Taxonomy | Applied to | Values | Definition |
| --- | --- | --- | --- |
| Knowledge Kind | Knowledge | Insight, Observation, Experience, Research, Opinion, Idea, Question, Lesson, Process, Framework, Evidence | The nature of reusable source material. `Source` remains a separate entity because it is provenance, not a kind of Knowledge. |
| Topic Mode | Topic | Build, Offline, Bridge | The Brand toggle lens. `Bridge` connects the two modes; it is not a third brand identity. |
| Publication Format | Publication; intended by Script and Script Template | Text Post, Thread, Carousel, Short-form Video, Long-form Video, Article, Newsletter | The channel-neutral form of a Publication. A Script or Script Template may declare the Format it is intended to support. The Channel identifies where a Publication appears. |
| Workflow Stage | Work Item | Capture, Validate, Plan, Draft, Review, Produce, Publish, Measure, Learn, Reuse / Repurpose | The current lifecycle stage of a particular work execution. |
| Work Item State | Work Item | Queued, In Progress, Blocked, Completed, Cancelled | The execution state of a Work Item, independent of its Content lifecycle stage. |
| Production Dependency State | Script beat or Publication asset requirement | Existing Asset, Planned Capture, Obtainable External Asset, Unresolved | How a required visual, audio, design, or other production dependency will be supplied. `Unresolved` cannot pass validation. |

### Creator-monitoring, review, and motif taxonomies

| Taxonomy | Applied to | Values | Definition |
| --- | --- | --- | --- |
| Creator Type | Creator | Person, Company, Brand, Organization, Other | What kind of entity the Creator is. |
| Creator Relationship | Creator | Competitor, Inspiration, Peer, Reference | Our stance toward the Creator. Multi-valued — a Creator may hold more than one Creator Relationship simultaneously (for example, both Competitor and Inspiration). |
| Review Type | Review | Visual, Format, Hook, Topic, Narrative, Technical | The dimension of a Publication a Review analyzes. |
| Review Confidence | Review | Low, Medium, High | How confident the Review's observations are. |
| Motif Category | Motif | Format, Visual, Hook, Narrative, Topic, Distribution | The dimension of the repeated, corroborated characteristic a Motif names. |

Creator Type answers **what is this entity?** Creator Relationship answers **what is our stance
toward it?** These are separate classifications and must never be conflated into one field. Review
Type answers **what dimension of the Publication is being analyzed?** Review Confidence answers
**how sure are we in that analysis?** — likewise two separate classifications on the same Review,
never conflated. Motif Category answers **what dimension of the repeated observation is this?** —
it closely mirrors Review Type's dimensions (Visual, Format, Hook, Topic, Narrative), since a
Motif is promoted from Reviews along one of those same dimensions, but replaces Technical with
Distribution to name repeated posting-and-reach characteristics that Review Type does not
otherwise classify.

### Supporting taxonomies

| Taxonomy | Applied to | Values |
| --- | --- | --- |
| Audience Relationship | Audience Segment | Addressed, Spoken-with, Spoken-about |
| Asset Type | Asset | Media, Design, Brand, Knowledge Asset, Script, Template, Script Template |
| Media Type | Media Asset | Image, Video, Audio, Screenshot, Recording, B-roll |
| Metric Name | Measurement | Impressions, Views, Watch Time, Completion Rate, Likes, Comments, Saves, Shares, Clicks |

## Content flow

```mermaid
classDiagram
    class Knowledge
    class Source
    class Topic
    class Blueprint
    class Publication
    class Channel
    class Asset
    class Measurement
    class Insight
    class Series
    class Script {
        <<asset subtype>>
    }
    class ScriptTemplate {
        <<asset subtype>>
    }
    class KnowledgeKind {
        <<enumeration>>
    }
    class TopicMode {
        <<enumeration>>
    }
    class ContentPattern {
        <<enumeration>>
    }
    class ContentPurpose {
        <<enumeration>>
    }
    class NarrativeStructure {
        <<enumeration>>
    }
    class VisualHookType {
        <<enumeration>>
    }
    class VerbalHookType {
        <<enumeration>>
    }
    class PublicationFormat {
        <<enumeration>>
    }
    class WorkflowStage {
        <<enumeration>>
    }
    class WorkItemState {
        <<enumeration>>
    }
    class ProductionDependencyState {
        <<enumeration>>
    }
    class Workflow
    class WorkItem

    Source "*" --> "*" Knowledge : supports
    Knowledge "*" --> "*" Topic : informs
    Knowledge ..> KnowledgeKind : classified by
    Topic ..> TopicMode : classified by
    Topic "1" <-- "0..*" Blueprint : communicates
    Blueprint ..> ContentPattern : uses
    Blueprint ..> ContentPurpose : intends
    Blueprint ..> NarrativeStructure : follows
    Blueprint ..> VisualHookType : selects
    Blueprint ..> VerbalHookType : selects
    Blueprint "1" <-- "0..*" Script : produces
    Script --|> Asset
    ScriptTemplate --|> Asset
    ScriptTemplate "1" <-- "0..*" Script : instantiates
    ScriptTemplate ..> ContentPattern : supports
    ScriptTemplate ..> NarrativeStructure : follows
    ScriptTemplate ..> PublicationFormat : targets
    Script ..> PublicationFormat : intends
    Blueprint "1" <-- "0..*" Publication : realizes
    Publication "*" --> "1" Channel : belongs to
    Publication ..> PublicationFormat : takes form
    Script "0..1" <-- "0..*" Publication : primary script
    Publication "*" --> "*" Asset : uses
    Workflow "1" --> "*" WorkItem : defines
    WorkItem ..> WorkflowStage : current stage
    WorkItem ..> WorkItemState : execution state
    Script ..> ProductionDependencyState : resolves beats through
    Publication ..> ProductionDependencyState : resolves requirements through
    Publication "1" --> "*" Measurement : receives
    Measurement "*" --> "*" Insight : informs
    Insight "*" --> "*" Knowledge : creates or updates
    Series "*" --> "*" Topic : groups
    Series "*" --> "*" Publication : groups
```

## V1 boundary

Do not model releases, claims, experiments, projects, or general CRM relationships as first-class records yet. Promote them only when recurring work requires ownership, lifecycle, or analysis beyond a simple reference.

Content's Creator and Creator Channel are a deliberate, narrow exception to the earlier
platform-account and people/organization prohibition, introduced specifically for
content-intelligence: competitor and inspiration monitoring. General people, organizations, and
CRM relationships remain out of scope and reserved for the still-empty
[Relationships](relationships/README.md) context; Creator does not extend, generalize, or
substitute for it.
