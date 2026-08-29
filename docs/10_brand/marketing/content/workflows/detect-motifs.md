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
  subject_type: content.review   # always anchor_review, one existing, completed candidate Review
                                   # — used uniformly for both execution modes, since a brand-new
                                   # Motif has no persisted instance to ref until this execution
                                   # produces one. `target_motif` (optional) separately names the
                                   # existing Motif being reinforced when that mode applies; it is
                                   # an input, not the subject_type, per the single-resolvable-ID
                                   # convention every other workflow in this domain follows. See
                                   # Work Item contract below.
  entry_stage: Review
  exit_stage: Learn
  requires:
    - id: content.review
      state: completed
      optional: false
    - id: content.motif
      state: completed
      optional: true   # only applies to a REINFORCE execution; absent when creating a new Motif
  inputs:
    - name: anchor_review
      type: ref(content.review)
      required: true
      cardinality: 1   # the primary subject, in both execution modes
    - name: candidate_reviews
      type: ref(content.review)
      required: true
      cardinality: 2..*   # the full corroborating set, including anchor_review
    - name: target_motif
      type: ref(content.motif)
      required: false
      cardinality: 0..1   # set only for a REINFORCE execution — the existing Motif being reinforced
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
    - target_motif_matches_shared_observation   # when set: target_motif is the correct existing
                                                  # Motif for this observation, not an arbitrary one
  next:
    - content.workflow.capture-knowledge
  failure_paths:
    - content.workflow.review-publication
---

# Detect Motifs

## Work Item contract

- **Primary subject:** `anchor_review` — one existing, completed candidate Review — in both
  execution modes. `subject_type` is a single resolvable concept ID, `content.review`, matching
  every other workflow in this domain; a brand-new Motif has no persisted instance to anchor on
  until this execution produces one, so the Motif is never the subject, even when reinforcing an
  existing one. `target_motif` is a separate, optional input that names the existing Motif being
  reinforced — it identifies what gets updated, not what the Work Item is filed against.
- **Entry stage:** Review.
- **Successful exit stage:** Learn.
- **Creates:** one Motif record naming the repeated observation (CREATE mode: no `target_motif`).
- **Updates:** an existing Motif when a new Review reinforces an observation already recorded,
  rather than creating a duplicate Motif (REINFORCE mode: `target_motif` set).
- **Required predecessors:** at least two completed [Review Publication](review-publication.md)
  executions (`content.review`, `state: completed` in the frontmatter `requires`) whose
  observations genuinely overlap. A REINFORCE execution additionally requires the `target_motif`
  it reinforces to already exist (`content.motif`, `state: completed`, optional in the frontmatter
  `requires` since it does not apply to CREATE).
- **Possible next workflows:** [Capture Knowledge](capture-knowledge.md), when the resulting Motif
  is well-evidenced enough to seed new, reusable Knowledge.
- **Validation evidence:** at least two corroborating Reviews linked, one Motif Category selected,
  the shared observation shown to be evidence-based rather than coincidental restatement, and —
  when reinforcing — `target_motif` confirmed to be the correct existing Motif for that
  observation rather than an arbitrary one, all recorded in the Work Item.
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

Two or more candidate Reviews suspected of sharing a corroborating observation, one of them named
as `anchor_review` (the Work Item's subject, in every execution), the Motif Category that
observation belongs to, a short, specific name for the Motif, and — only when reinforcing an
existing Motif — `target_motif`, naming that Motif.

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
5. Check the existing Motif registry for a matching Motif.
   - If one exists, this is a REINFORCE execution: set `target_motif` to it and add the new
     corroborating Review to its `supporting_reviews` rather than creating a duplicate. The Work
     Item's primary subject remains `anchor_review`; `target_motif` names what gets updated.
   - If none exists, this is a CREATE execution: leave `target_motif` unset and create a new Motif
     with `supporting_reviews` set to the corroborating Reviews found — the Motif has no instance
     to anchor on yet, which is exactly why the subject is `anchor_review` and not the Motif.
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
