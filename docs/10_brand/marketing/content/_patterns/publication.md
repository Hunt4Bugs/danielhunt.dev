---
id: content.pattern.publication
kind: pattern
domain: content
pattern_for: content.publication
status: active
version: 1
class: "10"
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
  - ../../../ONTOLOGY.md
---

# Pattern: Publication

What a `content.publication` instance document (stored under `publications/`) must contain. See
[`concepts.md`](../concepts.md#publication) for the Publication entity contract this pattern
instantiates.

## Required body sections

1. **Primary Blueprint and Channel** — the one Blueprint realized and the one Channel this
   Publication belongs to, plus the Publication Format.
2. **Channel-specific content** — the actual copy, caption, or script-adjacent content for this
   Channel and Format.
3. **Primary Script** — link to the primary Script, when the Publication uses one, plus any other
   Assets used.
4. **Production dependencies** — every required visual, audio, or design dependency and its
   Production Dependency State.
5. **Derivation** — a `derives from` link when this Publication repurposes another Publication.
6. **Durable publication facts** — `published_at`, `canonical_url`, `platform_identifier`. Leave
   empty before an authorized publish; record only after one.
7. **Measurements** — links to Measurement records once observed (may be empty before Measure
   stage).
8. **Creating Work Item** — link to the Work Item that created this Publication.

## Notes

Execution progress (Draft, Review, Produce, Publish, Measure) belongs to the Publication's Work
Item, not to the Publication document itself. A materially different channel expression or
repurposed output is always a new Publication document linked by `derives from`, never an edit to
this one — see the Publication Constraints in `concepts.md`.
