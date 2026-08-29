---
id: channels.concepts
kind: concept-registry
domain: channels
status: active
version: 1
class: "10"
collection: channels
owner: Daniel Hunt
created: 2026-08-29
updated: 2026-08-29
related:
  - README.md
  - domain.md
sources:
  - ../ONTOLOGY.md
---

# Channels concepts

Canonical concept registry for the `channels` domain (see [`domain.md`](domain.md)).

## Channel
**ID:** `channels.channel`

A distribution destination — not a Publication. Named separately from `content.creator-channel`,
which is one Creator's specific account on a Channel platform type, a different granularity.

### Relationships
- used by `content.publication` (exactly one per Publication in v1)
- taken form through `content.creator-channel`
- constrains `taxonomy(Publication Format)`

### Constraints
- Each Channel carries exactly one status (Active, Planned, Future) and one or more compatible
  Publication Formats.
- A workflow must reject a Channel/Format pair that is not listed as compatible.
- Adding a Channel or changing its compatible Formats is a governed operation (§13.3) — a workflow
  or skill may propose one but may not select it before an explicit update to the registry below.

### Persistence

Channel instances are persisted as rows in the Channel registry table in
[`README.md`](README.md), not as individual documents — a controlled vocabulary, not a
document-per-instance record (§14). No entity contract is defined per §10; the registry table's
four columns (Channel, Status, Compatible Publication Formats, Role) are self-describing.

## Owned vocabularies

`channels` owns one controlled vocabulary (§13.3 — extend only by governed edit to the
[Channel registry](README.md), never silently from a workflow or skill):

- **Channel** — the five canonical v1 values: X, Instagram, LinkedIn, YouTube, Newsletter, each
  with a status and its currently compatible Publication Formats.


## No _patterns/ or workflows/

Channel instances are registry rows, not individual documents, so no local `_patterns/` is
warranted (§14.1). No repeatable multi-step operation on the Channel registry itself has recurred
enough yet to justify a Workflow; Channel is read as an input by
`content.workflow.develop-publication` and `content.workflow.publish-publication` instead.
