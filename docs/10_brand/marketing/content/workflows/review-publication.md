---
id: content.workflow.review-publication
kind: workflow
domain: content
class: "10"
collection: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - operations
  - analytics
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
  - ../publications/README.md
  - ../reviews/README.md
sources:
  - ../../../ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Capture
  exit_stage: Review
  requires:
    - id: content.publication
      state: completed
      optional: false
  inputs:
    - name: publication
      type: ref(content.publication)
      required: true
    - name: review_type
      type: taxonomy(Review Type)
      required: true
    - name: observations
      type: list of text
      required: true
    - name: confidence
      type: taxonomy(Review Confidence)
      required: true
    - name: reviewed_at
      type: date
      required: true
  creates:
    - type: content.review
      via_pattern: ../_patterns/review.md
  updates: []
  validation:
    - observations_evidence_based
    - review_type_selected
    - confidence_assigned
    - reviewed_at_recorded
    - publication_linked
  next:
    - content.workflow.detect-motifs
  failure_paths:
    - content.workflow.review-publication
---

# Review Publication

## Work Item contract

- **Primary subject:** the Publication being reviewed.
- **Entry stage:** Capture.
- **Successful exit stage:** Review.
- **Creates:** one Review record analyzing the Publication.
- **Updates:** no existing domain entity — a Review never mutates its source Publication.
- **Required predecessors:** the referenced Publication must already exist with a completed
  creating Work Item (`content.publication`, `state: completed` in the frontmatter `requires`).
- **Possible next workflows:** [Detect Motifs](detect-motifs.md) once enough corroborating Reviews
  exist; this workflow again to add another Review of the same or a different Review Type.
- **Validation evidence:** the Publication resolved and linked, one Review Type selected, every
  observation shown to be specific and evidence-based rather than a bare verdict, a Review
  Confidence value assigned, and `reviewed_at` recorded, all recorded in the Work Item.
- **Failure and return paths:** remain at Capture when the Publication cannot be resolved or when
  observations cannot be stated as specific, evidence-based claims.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Review, Publication, Review Type, Review Confidence,
  and their relationships.
- [Publication records](../publications/README.md): the subject this workflow reviews.
- [Review records](../reviews/README.md): the Review this workflow produces.
- [Identity](../../../identity/README.md): truthfulness and evidence boundaries — a Review records
  what is actually present in a Publication, not a vague impression of it.

## Taxonomy contract

- **Reads:** Review Type, Review Confidence, and the existing Publication registry.
- **Writes:** one existing Review Type value on the resulting Review's `review_type` field and one
  existing Review Confidence value on its `confidence` field.
- **Restriction:** use only ontology-defined values. Route a missing value through [Propose
  Taxonomy Addition](propose-taxonomy-addition.md).

## Input

An existing Publication, the Review Type being applied to it, one or more specific,
evidence-based observations about that Publication along the chosen dimension, a Review
Confidence value, and the review date.

## Procedure

1. Resolve the input `publication` against the Publication registry; stop if it does not resolve
   to exactly one existing record with a completed creating Work Item.
2. Select one Review Type describing the dimension under analysis (Visual, Format, Hook, Topic,
   Narrative, or Technical).
3. Record one or more observations. Each observation must describe something specifically present
   in the Publication — a visible pattern, a structural choice, a line of copy — never a bare
   verdict or an unsupported vague judgment.
4. Assign one Review Confidence value (Low, Medium, High) reflecting how confident the
   observations are, independent of Review Type.
5. Record the `reviewed_at` date.
6. Create the Review with `publication` set to the resolved Publication. Do not modify the
   Publication record itself.
7. Check existing Reviews of this Publication before creating a new one; a repeated Review of the
   same Review Type is valid and additive, never a replacement of the earlier Review.

## Output

One Review record with `publication`, `review_type`, `observations`, `confidence`, `reviewed_at`,
and a link to the creating Work Item. The source Publication is unchanged.

## Stop conditions

Stop without creating a Review when the Publication does not resolve to exactly one existing,
completed record, or when the observations cannot be stated as specific, evidence-based claims
rather than a vague judgment or bare verdict.
