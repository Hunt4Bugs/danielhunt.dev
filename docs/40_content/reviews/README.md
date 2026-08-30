---
id: content.reviews.readme
kind: note
domain: content
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - analytics
related:
  - ../concepts.md
  - ../_patterns/review.md
  - ../publications/README.md
sources:
  - ../../10_brand/ONTOLOGY.md
---

# Review records

You are in the instance directory for `content.review`. Store structured analysis of a Publication
here, kept separate from the Publication so observations can evolve without mutating the source
record.

- What a Review *is* (definition, relationships, constraints, entity contract):
  [`concepts.md`](../concepts.md#review).
- What a Review document must *contain* (required sections): [`_patterns/review.md`](../_patterns/review.md).
- What *creates* a Review: the [Review Publication](../workflows/review-publication.md) workflow.
- Related instance directories: [Publications](../publications/README.md) (the record a Review
  analyzes).

A Publication may carry more than one Review — different Review Types, or repeated review of the
same Review Type over time — without conflict; each Review is an independently evolving record.
