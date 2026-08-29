---
id: content.workflow.validate-publication
kind: workflow
domain: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-28
facets:
  - channels
related:
  - ../publications/README.md
  - ../../10_brand/identity/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Review
  exit_stage: Produce
  requires:
    - id: content.publication
      state: completed
      optional: false
    - id: content.script
      state: validated
      optional: true
  inputs:
    - name: publication
      type: ref(content.publication)
      required: true
  creates: []
  updates:
    - type: content.work-item
  validation:
    - channel_format_compatible
    - blueprint_fidelity_checked
    - claims_sourced
    - copy_checked
    - privacy_checked
    - asset_links_checked
    - dependencies_checked
    - derivation_checked
    - editorial_checked
  next:
    - content.workflow.produce-publication
  failure_paths:
    - content.workflow.develop-publication
    - content.workflow.capture-knowledge
---

# Validate Publication

## Work Item contract

- **Primary subject:** one unpublished Publication.
- **Entry stage:** Review.
- **Successful exit stage:** Produce.
- **Creates:** no new domain entity.
- **Updates:** validation evidence and outcome on the Work Item.
- **Required predecessors:** completed [Develop Publication](develop-publication.md); passed Validate Script when a primary Script is present.
- **Possible next workflows:** [Produce Publication](produce-publication.md) after a pass; Develop Publication after revision gaps; Capture Knowledge when evidence is insufficient.
- **Validation evidence:** Channel compatibility, Blueprint fidelity, claims, copy, privacy, Assets, dependencies, derivation, and editorial checks recorded in the Work Item.
- **Failure and return paths:** return to Draft with specific gaps or Capture when evidence is insufficient.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Publication, Format, Production Dependency State, and evidence conditions.
- [Channels](../../10_brand/channels/README.md): Channel registry and compatibility.
- [Identity](../../10_brand/identity/README.md), [Strategy](../../10_brand/strategy/README.md), and the Publication's Blueprint and Sources.

## Checks

- Channel and Publication Format are compatible.
- Channel-specific content preserves the Blueprint's promise, angle, structure, proof, and CTA constraints.
- Facts, statistics, quotations, and outcomes have suitable Sources.
- Privacy, scars-not-wounds, documentary restraint, and unsupported-claim restrictions are satisfied.
- The primary Script, when present, has a passed validation Work Item.
- Every production dependency has a defined state and none is Unresolved.
- Derivation is recorded when the Publication repurposes another Publication.

## Output

Record a pass, revision-required result, or evidence-insufficient result on the Work Item.
