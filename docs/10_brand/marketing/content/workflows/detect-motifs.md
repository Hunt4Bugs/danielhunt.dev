---
id: content.workflow.detect-motifs
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
  - analytics
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
  - ../reviews/README.md
  - ../motifs/README.md
  - ../knowledge/README.md
sources:
  - ../../../ONTOLOGY.md
contract:
  subject_type: content.motif   # judgment call, matching Capture Knowledge: the Motif has no
                                 # persisted identity until this execution creates or reinforces
                                 # it, so it is modeled as the Motif-in-formation. A Work Item has
                                 # exactly one primary subject; the corroborating Reviews are
                                 # evidence, carried as a typed input, not the subject.
  entry_stage: Review
  exit_stage: Learn
  requires:
    - id: content.review
      state: completed
      optional: false
  inputs:
    - name: candidate_reviews
      type: ref(content.review)
      required: true
      cardinality: 2..*
    - name: motif_category
      type: taxonomy(Motif Category)
      required: true
    - name: name
      type: text
      required: true
  creates:
    - type: content.motif
      via_pattern: ../_patterns/motif.md
  updates:
    - type: content.motif   # reinforcing an existing Motif with a new corroborating Review
  validation:
    - minimum_corroborating_reviews
    - motif_category_selected
    - evidence_linked
  next:
    - content.workflow.capture-knowledge
  failure_paths:
    - content.workflow.review-publication
---

# Detect Motifs

## Work Item contract

- **Primary subject:** the Motif being detected or reinforced — a new Motif in formation, or an
  existing Motif gaining another corroborating Review. This is the same judgment call Capture
  Knowledge makes for material with no persisted concept of its own until the execution creates
  it: a Work Item has exactly one primary subject, so the corroborating Reviews are carried as a
  typed input (`candidate_reviews`), not as the subject itself.
- **Entry stage:** Review.
- **Successful exit stage:** Learn.
- **Creates:** one Motif record naming the repeated observation.
- **Updates:** an existing Motif when a new Review reinforces an observation already recorded,
  rather than creating a duplicate Motif.
- **Required predecessors:** at least two completed [Review Publication](review-publication.md)
  executions (`content.review`, `state: completed` in the frontmatter `requires`) whose
  observations genuinely overlap.
- **Possible next workflows:** [Capture Knowledge](capture-knowledge.md), when the resulting Motif
  is well-evidenced enough to seed new, reusable Knowledge.
- **Validation evidence:** at least two corroborating Reviews linked, one Motif Category selected,
  and the shared observation shown to be evidence-based rather than coincidental restatement, all
  recorded in the Work Item.
- **Failure and return paths:** [Review Publication](review-publication.md) when fewer than two
  Reviews corroborate the same observation — go get more evidence rather than promoting a single
  occurrence.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Motif, Review, Motif Category, and their
  relationships.
- [Review records](../reviews/README.md): the corroborating evidence this workflow draws on.
- [Motif records](../motifs/README.md): the record this workflow produces or reinforces.
- [Knowledge records](../knowledge/README.md): the possible downstream effect of a well-evidenced
  Motif.
- [Identity](../../../identity/README.md): truthfulness and evidence boundaries — a Motif names
  something genuinely repeated and independently observed, not a pattern imposed on unrelated
  observations.

## Taxonomy contract

- **Reads:** Motif Category, and the existing Review and Motif registries.
- **Writes:** one existing Motif Category value on the resulting Motif's `motif_category` field.
- **Restriction:** use only ontology-defined values. Route a missing value through [Propose
  Taxonomy Addition](propose-taxonomy-addition.md).

## Input

Two or more candidate Reviews suspected of sharing a corroborating observation, the Motif Category
that observation belongs to, and a short, specific name for the Motif.

## Procedure

1. Compare observations across the candidate Reviews; look for a repeated, specific characteristic
   recorded independently in more than one Review, not a restatement of one Review's language
   copied into another.
2. Identify the exact shared observation and state it precisely enough to recognize again in
   future Reviews.
3. Check that at least two corroborating Reviews genuinely support it; stop if only one Review
   contains the observation.
4. Assign one Motif Category describing the dimension the repeated observation belongs to (Format,
   Visual, Hook, Narrative, Topic, or Distribution).
5. Check the existing Motif registry: if a matching Motif already exists, update it by adding the
   new corroborating Review to `supporting_reviews` rather than creating a duplicate; otherwise
   create a new Motif with `supporting_reviews` set to the corroborating Reviews found.
6. When the Motif is well-evidenced enough to seed reusable material beyond this one observation,
   hand off to [Capture Knowledge](capture-knowledge.md) and link the resulting Knowledge back via
   `related_knowledge`; otherwise leave `related_knowledge` empty rather than filling it
   speculatively.

## Output

One Motif record with `name`, `motif_category`, `description`, `supporting_reviews` (2..*), and a
link to the creating Work Item — or an existing Motif updated with a new corroborating Review.
`related_knowledge` is populated only when this execution also seeded or informed a Knowledge
record.

## Stop conditions

Stop without creating or updating a Motif when fewer than two Reviews corroborate the same
specific observation, or when the apparently shared language across Reviews looks like a
restatement of one Review rather than an independently observed repetition.
