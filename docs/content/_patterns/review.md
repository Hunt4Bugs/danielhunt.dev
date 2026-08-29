---
id: content.pattern.review
kind: pattern
domain: content
pattern_for: content.review
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - analytics
related:
  - ../reviews/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Pattern: Review

What a `content.review` instance document (stored under `reviews/`) must contain. See
[`concepts.md`](../concepts.md#review) for the Review entity contract this pattern instantiates.

## Required body sections

1. **Publication** — link to the one `content.publication` this Review analyzes.
2. **Review Type** — the one classification of what dimension is being analyzed (Visual, Format,
   Hook, Topic, Narrative, or Technical).
3. **Observations** — one or more specific, evidence-based observations. Each observation must
   describe something actually present in the Publication, not a vague judgment or bare verdict.
4. **Confidence** — the one Review Confidence value (Low, Medium, High) for this Review.
5. **Reviewed at** — the date this Review was performed.
6. **Creating Work Item** — link to the Work Item that created this record.

## Notes

A Review does not mutate its source Publication — it is a separate, independently evolving record.
A Publication may carry more than one Review, whether different Review Types or repeated review of
the same Review Type over time. Observations recorded here are the raw material a later Motif may
draw on across multiple Reviews; keep them concrete enough to compare across records rather than
restating a single overall impression.
