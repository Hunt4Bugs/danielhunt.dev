---
id: content.workflow.capture-publication
kind: workflow
domain: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-28
updated: 2026-08-28
facets:
  - operations
  - channels
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
  - ../creator-channels/README.md
  - ../publications/README.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.creator-channel   # the Creator Channel being observed; the Publication is what this workflow creates
  entry_stage: Capture
  exit_stage: Capture
  requires: []
  inputs:
    - name: creator_channel
      type: ref(content.creator-channel)
      required: true
    - name: url
      type: url
      required: true
    - name: observed_format
      type: taxonomy(Publication Format)
      required: true
    - name: published_at
      type: date
      required: true   # already known at capture time, unlike an authored Publication
  creates:
    - type: content.publication
      via_pattern: ../_patterns/publication.md
  updates: []
  validation:
    - creator_channel_resolved
    - url_recorded
    - no_duplicate_publication
    - publication_format_valid
  next:
    - content.workflow.review-publication
  failure_paths:
    - content.workflow.capture-publication
---

# Capture Publication

## Work Item contract

- **Primary subject:** the Creator Channel being observed.
- **Entry stage:** Capture.
- **Successful exit stage:** Capture.
- **Creates:** one Observed Publication record (`creator` and `creator_channel` set, no Blueprint).
- **Updates:** no existing domain entity.
- **Required predecessors:** none — the referenced Creator Channel must already exist in the
  registry, but this workflow carries no `requires` precondition of its own.
- **Possible next workflows:** [Review Publication](review-publication.md) once the captured
  Publication is ready for analysis; this workflow again when the capture is incomplete or
  duplicate.
- **Validation evidence:** Creator Channel resolved, URL recorded, duplicate check performed, and
  Publication Format valid, all recorded in the Work Item.
- **Failure and return paths:** remain at Capture when the URL, format, or publish date cannot be
  confirmed, or when the observation duplicates an existing captured Publication.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Publication, Creator, Creator Channel, Publication
  Format, and their relationships.
- [Creator Channel records](../creator-channels/README.md): the subject this workflow observes.
- [Publication records](../publications/README.md): the Observed Publication this workflow
  produces.
- [Identity](../../10_brand/identity/README.md): truthfulness and evidence boundaries — an Observed
  Publication records what a Creator published, not Daniel's own claim.

## Taxonomy contract

- **Reads:** Publication Format and the existing Creator Channel registry.
- **Writes:** one existing Publication Format value on the resulting Publication's `format` field
  (`observed_format` at input becomes `format` on the record — Content does not maintain a second,
  observation-only format vocabulary).
- **Restriction:** use only ontology-defined values. Route a missing value through [Propose
  Taxonomy Addition](propose-taxonomy-addition.md).

## Input

A Creator Channel already present in the registry, the URL of the specific external publication
being observed, its channel-neutral Publication Format, and its known `published_at` date. Unlike
an authored Publication, an Observed Publication's durable publication facts are already known at
capture time — nothing here waits on an internal publish step.

## Procedure

1. Resolve the input `creator_channel` against the Creator Channel registry; stop if it does not
   resolve to exactly one existing record.
2. Record the `url`, `observed_format`, and `published_at` as given — these become the Publication's
   `canonical_url`, `format`, and `published_at`.
3. Check existing captured Publications for this Creator Channel and this `url` before creating a
   new record; extend or link the existing Publication instead of duplicating it when one is
   already captured.
4. Create the Publication with `creator` set to the Creator Channel's owning Creator,
   `creator_channel` set to the input Creator Channel, and no `blueprint`.
5. Record a `platform_identifier` when the platform exposes a stable native identifier distinct
   from the URL; leave it empty otherwise.
6. Summarize the observed content in the Publication's `content` field without asserting it as
   Daniel's own claim.

## Output

One Observed Publication record with `creator`, `creator_channel`, `channel`, `format`, `content`,
`published_at`, `canonical_url`, and a link to the creating Work Item. `blueprint` is absent by
design.

## Stop conditions

Stop without creating a Publication when the Creator Channel does not resolve, the URL cannot be
confirmed as belonging to that Creator Channel, or the observation duplicates an existing captured
Publication for the same Creator Channel and URL.
