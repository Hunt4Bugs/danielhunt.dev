---
id: content.pattern.publication
kind: pattern
domain: content
pattern_for: content.publication
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - channels
  - analytics
related:
  - ../publications/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Publication

What a `content.publication` instance document (stored under `publications/`) must contain. See
[`concepts.md`](../concepts.md#publication) for the Publication entity contract this pattern
instantiates. A Publication is either **Own** (Daniel authored it, `creator` absent) or
**Observed** (captured from a tracked Creator, `creator` present) — never both. Sections below are
marked where the two branches diverge.

## Required body sections

1. **Channel and Format** — the one Channel this Publication belongs to and its Publication
   Format, in both branches.
   - **Own:** also the one Blueprint realized.
   - **Observed:** also the Creator and Creator Channel it was captured from, via `creator` and
     `creator_channel` — no Blueprint.
2. **Channel-specific content** — the actual copy, caption, or script-adjacent content for this
   Channel and Format.
3. **Primary Script** — link to the primary Script, when the Publication uses one, plus any other
   Assets used. Own only — an Observed Publication has no Script.
4. **Production dependencies** — every required visual, audio, or design dependency and its
   Production Dependency State. Own only.
5. **Derivation** — a `derives from` link when this Publication repurposes another Publication.
6. **Durable publication facts** — `published_at`, `canonical_url`, `platform_identifier`.
   - **Own:** leave empty before an authorized publish; record only after one, via Publish
     Publication.
   - **Observed:** record immediately at capture time, via Capture Publication — the post is
     already live when captured.
7. **Measurements** — links to Measurement records once observed (may be empty before Measure
   stage). Own only in this pass.
8. **Creating Work Item** — link to the Work Item that created this Publication.

## Notes

Execution progress (Draft, Review, Produce, Publish, Measure) belongs to an Own Publication's Work
Item, not to the Publication document itself; an Observed Publication is captured already-published
and does not pass through that lifecycle. A materially different channel expression or repurposed
output is always a new Publication document linked by `derives from`, never an edit to this one —
see the Publication Constraints in `concepts.md`.
