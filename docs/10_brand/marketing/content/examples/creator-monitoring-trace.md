---
class: "100"
collection: content
type: example
status: active
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - operations
related:
  - ../concepts.md
  - ../_patterns/creator.md
  - ../_patterns/creator-channel.md
  - ../_patterns/publication.md
  - ../_patterns/review.md
  - ../_patterns/motif.md
  - ../workflows/capture-publication.md
  - ../workflows/review-publication.md
  - ../workflows/detect-motifs.md
  - ../../../channels/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Illustrative creator monitoring trace

> **Simulation only.** This trace validates the Creator, Creator Channel, Observed Publication, Review, and Motif contracts. It does not assert a real Creator, Creator Channel, Publication, Review, or Motif. Nothing here may be promoted without the appropriate Workflow and evidence.

## Subject

An illustrative competitor-and-inspiration account being onboarded into Content's creator-monitoring model: a fictional Creator, "Acme Fictional Fitness Co.", and one Creator Channel it holds on Instagram. This is the seed of a worked example that later slices in this parent extend — capturing a Publication observed from this Creator Channel, then Reviews of that Publication, then a Motif drawn from repeated observation.

## Happy path

| Illustrative Work Item | Workflow | Stage transition | Output |
| --- | --- | --- | --- |
| `WI-20260828-add-creator-acme-fictional-fitness-co` | Add Creator | Capture → Validate | Illustrative Creator `content.creator.acme-fictional-fitness-co`: Creator Type `Brand`, Creator Relationships `Competitor` and `Inspiration`. |
| `WI-20260828-add-creator-channel-acme-fictional-fitness-co-instagram` | Add Creator Channel | Capture → Validate | Illustrative Creator Channel `content.creator-channel.acme-fictional-fitness-co-instagram` belonging to the Creator above, referencing the existing Instagram `channels.channel` value. |
| `WI-20260828-capture-publication-acme-fictional-fitness-co-instagram` | Capture Publication | Capture → Capture | Illustrative Observed Publication `content.publication.acme-fictional-fitness-co-instagram-home-gym-carousel`: Instagram Carousel captured from the Creator Channel above, with `published_at`, `canonical_url`, and `platform_identifier` populated immediately at capture and no Blueprint linked. |
| `WI-20260828-review-publication-acme-fictional-fitness-co-instagram-home-gym-carousel` (and `-02`) | Review Publication | Capture → Review | Two illustrative Reviews of the Publication above: `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-visual` (Visual) and `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-format` (Format), sharing one overlapping observation — the corroborating pair a later Motif can draw on. |
| `WI-20260828-detect-motifs-plain-background-product-isolation` | Detect Motifs | Review → Learn | Illustrative Motif `content.motif.plain-background-product-isolation` (Motif Category: Visual), promoted from the two Reviews' shared observation — the corroboration the `supporting_reviews` cardinality (2..*) requires. CREATE execution: primary subject is `anchor_review`, since the Motif has no instance to `ref` until this row produces it. |

"Add Creator" and "Add Creator Channel" above are illustrative labels for a manual registry addition, not named Workflow documents — Creator and Creator Channel instances are added directly to the registry rather than through a dedicated Workflow contract in this pass. Every later row in this table names a real `workflows/*.md` contract.

This table traces the full illustrative pipeline this parent PRD's slices built one row at a time:
Creator, Creator Channel, Observed Publication, two corroborating Reviews, and one Motif drawn
from them.

## Illustrative records

### Creator

- `id`: `content.creator.acme-fictional-fitness-co`
- `name`: Acme Fictional Fitness Co.
- `creator_type`: Brand
- `relationships`: Competitor, Inspiration — demonstrating that Creator Relationship is multi-valued
- `niches`: Home Gym Equipment, Beginner Strength Training
- `notes`: Illustrative only, invented for contract validation; not a real account or brand.
- `creating_work_item`: `WI-20260828-add-creator-acme-fictional-fitness-co`

### Creator Channel

- `id`: `content.creator-channel.acme-fictional-fitness-co-instagram`
- `creator`: `content.creator.acme-fictional-fitness-co`
- `channel`: Instagram (`channels.channel`, per [Channels](../../../channels/README.md))
- `handle`: @acmefictionalfitnessco
- `url`: https://instagram.com/acmefictionalfitnessco (illustrative, not a real destination)
- `creating_work_item`: `WI-20260828-add-creator-channel-acme-fictional-fitness-co-instagram`

### Publication

- `id`: `content.publication.acme-fictional-fitness-co-instagram-home-gym-carousel`
- `creator`: `content.creator.acme-fictional-fitness-co`
- `creator_channel`: `content.creator-channel.acme-fictional-fitness-co-instagram`
- `channel`: Instagram (`channels.channel`, per [Channels](../../../channels/README.md))
- `format`: Carousel (`taxonomy(Publication Format)`)
- `content`: Illustrative summary — a five-slide carousel positioning a compact home gym rack against small-space objections. Observed, not authored, so no Blueprint is linked.
- `published_at`: 2026-08-20 (illustrative — already known at capture time, not gated behind Publish Publication)
- `canonical_url`: https://instagram.com/p/acmefictionalfitnessco-home-gym-carousel (illustrative, not a real destination)
- `platform_identifier`: acmefictionalfitnessco-home-gym-carousel (illustrative Instagram media id)
- `creating_work_item`: `WI-20260828-capture-publication-acme-fictional-fitness-co-instagram`

### Review

Two illustrative Reviews of the Publication above, of different Review Types, sharing one
genuinely overlapping observation — the corroboration a later Motif slice draws on.

**Review 1 — Visual**

- `id`: `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-visual`
- `publication`: `content.publication.acme-fictional-fitness-co-instagram-home-gym-carousel`
- `review_type`: Visual
- `observations`:
  - "Product isolated against a plain, uncluttered background in every slide."
  - "Numbered callouts (1, 2, 3) mark each equipment feature on slide two."
- `confidence`: Medium
- `reviewed_at`: 2026-08-22
- `creating_work_item`: `WI-20260828-review-publication-acme-fictional-fitness-co-instagram-home-gym-carousel`

**Review 2 — Format**

- `id`: `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-format`
- `publication`: `content.publication.acme-fictional-fitness-co-instagram-home-gym-carousel`
- `review_type`: Format
- `observations`:
  - "Product isolated against a plain, uncluttered background in every slide."
  - "Five-slide carousel follows a consistent numbered-callout structure across slides two through
    four."
- `confidence`: High
- `reviewed_at`: 2026-08-23
- `creating_work_item`: `WI-20260828-review-publication-acme-fictional-fitness-co-instagram-home-gym-carousel-02`

The first observation in each Review is identical: "Product isolated against a plain, uncluttered
background in every slide." That corroboration — the same specific pattern independently observed
under two different Review Types — is what a later Motif may legitimately draw on; a single Review
alone cannot support a Motif.

### Motif

This is a CREATE execution — no matching Motif exists yet, so the Work Item's primary subject is
`anchor_review` (one of the two corroborating Reviews), not the Motif being created, which has no
persisted instance to `ref` until this execution produces it.

- `id`: `content.motif.plain-background-product-isolation`
- `name`: Plain-background product isolation
- `motif_category`: Visual
- `description`: The product is isolated against a plain, uncluttered background in every slide —
  independently observed in both the Visual and Format Reviews of the Publication above.
- `supporting_reviews`:
  - `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-visual`
  - `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-format`
- `anchor_review`: `content.review.acme-fictional-fitness-co-instagram-home-gym-carousel-visual`
  (the Work Item's primary subject for this CREATE execution)
- `related_knowledge`: none — this illustrative Motif has not yet been used to seed or inform a
  Knowledge record; `related_knowledge` stays empty rather than being filled speculatively, per
  [`_patterns/motif.md`](../_patterns/motif.md).
- `creating_work_item`: `WI-20260828-detect-motifs-plain-background-product-isolation`

This trace now demonstrates the full pipeline end to end: Creator → Creator Channel → Observed
Publication → two corroborating Reviews → one Motif. Every `ref()` above resolves to a record
defined earlier in this same trace, and every workflow's `creates`/`next` was followed in order —
[Review Publication](../workflows/review-publication.md)'s `next: content.workflow.detect-motifs`
resolves to the workflow used for the row above, and [Detect Motifs](../workflows/detect-motifs.md)'s
own `next: content.workflow.capture-knowledge` remains available for a future slice that exercises
the Motif → Knowledge handoff, mirroring [`full-lifecycle-trace.md`](full-lifecycle-trace.md)'s
verification style.

## Validation scenarios

- A Creator with no Creator Relationship value fails validation.
- A Creator Channel that restates a platform type instead of referencing `channels.channel` fails validation.
- Two Creator Relationship values on the same Creator (Competitor and Inspiration) are valid — Creator Relationship is multi-valued.
- A Creator Channel without a `creator` link, or with more than one, fails validation — cardinality is exactly 1.
- A Publication with a Creator but no Blueprint is valid (the Observed branch); a Publication with no Creator and no Blueprint fails validation.
- A Publication with both a Creator and a Blueprint is invalid — Own and Observed are mutually exclusive branches.
- A Publication may carry more than one Review — of the same or different Review Types — without conflict; each Review evolves independently and never mutates the Publication it reviews.
- A Review with a vague, non-specific observation ("this is good," "strong post") fails validation — every observation must describe something specifically present in the Publication.
- Two Reviews of the same Publication may share a genuinely overlapping observation (as in the illustrative Visual and Format Reviews above) without being merged into one record — corroboration across Reviews is what a later Motif draws on, not automatic deduplication.
- A Motif with only one supporting Review fails validation — `supporting_reviews`' `2..*` cardinality makes the corroboration requirement structural, not a discretionary editorial judgment.
- A new Review that repeats an existing Motif's observation updates that Motif's `supporting_reviews` rather than creating a second, duplicate Motif for the same repeated characteristic.
