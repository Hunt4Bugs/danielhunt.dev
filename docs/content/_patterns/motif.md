---
id: content.pattern.motif
kind: pattern
domain: content
pattern_for: content.motif
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - analytics
related:
  - ../motifs/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Motif

What a `content.motif` instance document (stored under `motifs/`) must contain. See
[`concepts.md`](../concepts.md#motif) for the Motif entity contract this pattern instantiates.

## Required body sections

1. **Name** — a short, specific label for the repeated observation.
2. **Motif Category** — the one classification of what dimension the repeated observation belongs
   to (Format, Visual, Hook, Narrative, Topic, or Distribution).
3. **Description** — the specific, repeated characteristic being named, stated precisely enough to
   recognize again across future Reviews.
4. **Supporting Reviews** — links to two or more `content.review` records whose observations
   corroborate this Motif. A single Review can never satisfy this field.
5. **Related Knowledge** — optional links to `content.knowledge` records this Motif has informed or
   seeded. Leave empty rather than filling it speculatively when no Knowledge effect exists yet.
6. **Creating Work Item** — link to the Work Item that created this record.

## Notes

A Motif is not itself an observation — it is what two or more independently recorded Review
observations have in common. A new corroborating Review for an already-named Motif updates that
Motif (extends `supporting_reviews`) rather than creating a duplicate. A well-evidenced Motif may
inform or seed a new Knowledge record, the same way `analytics.insight` already feeds
`content.knowledge`; when a Motif has not yet been used that way, `related_knowledge` stays empty.
