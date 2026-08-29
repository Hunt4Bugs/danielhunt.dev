---
id: content.workflow.monitor-creators
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
  - channels
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
  - ../creators/README.md
  - ../creator-channels/README.md
  - ../publications/README.md
  - ../examples/creator-monitoring-trace.md
sources:
  - ../../../ONTOLOGY.md
contract:
  subject_type: content.creator
  entry_stage: Capture
  exit_stage: Capture
  requires: []
  inputs:
    - name: creator
      type: ref(content.creator)
      required: true
    - name: relationship_filter
      type: taxonomy(Creator Relationship)
      required: false
  creates: []
  updates: []
  validation:
    - creator_channels_resolved
    - unseen_publications_identified
  next:
    - content.workflow.capture-publication
  failure_paths: []
---

# Monitor Creators

## Work Item contract

- **Primary subject:** the Creator being monitored.
- **Entry stage:** Capture.
- **Successful exit stage:** Capture — this workflow never itself advances past Capture; it hands
  unseen Publications off to [Capture Publication](capture-publication.md), whose own executions
  advance from there.
- **Creates:** no domain entity — a pure orchestration/resolution step.
- **Updates:** no existing domain entity.
- **Required predecessors:** none — the referenced Creator, and any Creator Channels it controls,
  must already exist in the registry, but this workflow carries no `requires` precondition of its
  own.
- **Possible next workflows:** [Capture Publication](capture-publication.md), once per unseen
  Publication this execution identifies.
- **Validation evidence:** the Creator's Creator Channels resolved and its unseen Publications
  identified, both recorded in the Work Item.
- **Failure and return paths:** none — a Creator that fails to resolve, or that controls no Creator
  Channels, simply yields no hand-offs; there is no dedicated failure workflow to route back to.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Creator, Creator Channel, Publication, Creator
  Relationship, and their relationships.
- [Creator records](../creators/README.md): the registry this workflow selects from.
- [Creator Channel records](../creator-channels/README.md): resolved per selected Creator.
- [Publication records](../publications/README.md): checked to identify what is already captured.
- [Capture Publication](capture-publication.md): the workflow this one hands unseen Publications
  off to.
- [Identity](../../../identity/README.md): truthfulness and evidence boundaries — this workflow
  only identifies what a Creator has published; it does not itself characterize or judge it.

## Taxonomy contract

- **Reads:** Creator Relationship, used only as an optional filter over the Creator registry, plus
  the existing Creator, Creator Channel, and Publication registries.
- **Writes:** none — this workflow does not create or update any record, so it writes no taxonomy
  value anywhere.
- **Restriction:** use only ontology-defined Creator Relationship values when filtering. Route a
  missing value through [Propose Taxonomy Addition](propose-taxonomy-addition.md).

## Input

One Creator already present in the registry. At the level that decides which Creators to run this
workflow against — a human working through the registry, an agent, or a future scheduled process —
the full Creator registry may be loaded and optionally narrowed by a Creator Relationship
`relationship_filter` (for example, running against only Competitors) before selecting each Creator
this workflow is executed for.

## Procedure

1. Load the Creator registry, optionally narrowed to Creators carrying a given Creator Relationship
   value (`relationship_filter`), and select each Creator to run this workflow against in turn. Per
   the [Work Item](../../../../00_system/010_governance/DOMAIN_PROTOCOL.md#12-execution-model) model,
   one execution of this workflow always targets exactly one resolved `creator`; the registry scan
   is the orchestration step that decides which Creators get an execution, not a change to this
   workflow's subject cardinality.
2. Resolve the selected Creator's Creator Channels. A Creator that controls no Creator Channels
   produces no further work for this execution.
3. For each resolved Creator Channel, identify Publications not yet captured: compare it against
   the existing Publication registry, and treat any externally observed item at that Creator
   Channel as unseen when no existing `content.publication` record references both that Creator
   Channel and a matching `url` or `platform_identifier`.
4. Hand off each unseen Publication to [Capture Publication](capture-publication.md), supplying the
   resolved Creator Channel and the observed `url`, `observed_format`, and `published_at` as that
   workflow's inputs.
5. Leave Publications already represented by an existing record untouched — this workflow never
   creates, updates, or re-captures them.

This contract is deliberately implementation-agnostic: nothing above names a particular scraper,
platform API, or scheduling runtime. Whatever executes it — a person working through a Creator's
Creator Channels by hand, an agent, or a future scheduled process running daily or weekly — resolves
the same registry, applies the same identify-unseen check, and hands off the same way to Capture
Publication. Only the thing that eventually executes this contract is runtime-specific; the contract
itself is not.

### Illustrative walkthrough

Running this workflow against the illustrative Creator `content.creator.acme-fictional-fitness-co`
from the creator-monitoring worked example
([`examples/creator-monitoring-trace.md`](../examples/creator-monitoring-trace.md); simulation only,
not a real Creator) resolves its one Creator Channel,
`content.creator-channel.acme-fictional-fitness-co-instagram`. Checking that Creator Channel against
the Publication registry finds the existing
`content.publication.acme-fictional-fitness-co-instagram-home-gym-carousel` record, whose
`creator_channel` and `canonical_url` match exactly — so this workflow correctly treats it as
already captured and does not hand it off to Capture Publication again. A hypothetical new post
observed at that same Creator Channel but at a different `canonical_url`, with no matching
Publication record, would have no existing `content.publication` referencing that Creator Channel
plus that url — so this workflow would correctly identify it as unseen and hand it off to Capture
Publication.

## Output

No domain entity. A successful execution's output is the set of hand-offs — one per unseen
Publication — to [Capture Publication](capture-publication.md) executions, plus the Work Item's own
record of which Creator Channels were resolved and which Publications were judged unseen versus
already captured.

## Stop conditions

Produce no hand-offs when the Creator does not resolve to exactly one existing registry record,
when it controls no Creator Channels, or when every Publication found at its Creator Channels is
already represented by an existing `content.publication` record.
