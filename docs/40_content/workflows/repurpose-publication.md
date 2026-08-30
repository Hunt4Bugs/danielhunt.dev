---
id: content.workflow.repurpose-publication
kind: workflow
domain: content
type: workflow
status: active
version: 1
class: "40"
collection: content
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-28
facets:
  - distribution
related:
  - ../publications/README.md
  - ../../10_brand/analytics/insights/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Reuse / Repurpose
  exit_stage: Draft   # dual-path workflow; exits to Plan instead when upstream Blueprint intent must change (see Procedure)
  requires:
    - id: content.publication
      state: completed
      optional: false
    - id: content.workflow.derive-insight
      state: completed
      optional: true
  inputs:
    - name: target_channel
      type: ref(channels.channel)
      required: true
    - name: target_format
      type: taxonomy(Publication Format)
      required: true
    - name: reuse_rationale
      type: text
      required: true
  creates:
    - type: content.publication
      via_pattern: ../_patterns/publication.md
  updates:
    - type: content.publication
  validation:
    - source_publication_linked
    - reuse_rationale_recorded
    - promise_angle_structure_compared
    - path_selected
    - derivation_link_recorded
    - output_recorded
  next:
    - content.workflow.validate-publication
    - content.workflow.develop-blueprint
  failure_paths: []
---

# Repurpose Publication

## Work Item contract

- **Primary subject:** one existing Publication.
- **Entry stage:** Reuse / Repurpose.
- **Successful exit stage:** Draft when the existing Blueprint remains valid; Plan when upstream intent must change.
- **Creates:** one derived Publication in the Draft path; no new Publication in the Plan path.
- **Updates:** derivation links on the source and derived Publications when a derived Publication is created.
- **Required predecessors:** an existing Publication; a completed [Derive Insight](derive-insight.md) Work Item when analytics motivates the reuse.
- **Possible next workflows:** [Validate Publication](validate-publication.md) from Draft; [Develop Blueprint](develop-blueprint.md) from Plan.
- **Validation evidence:** source Publication, reuse rationale, promise/angle/structure comparison, selected path, derivation link, and output recorded in the Work Item.
- **Failure and return paths:** end without output when the reuse lacks Brand fit, evidence, or a distinct channel purpose.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Publication derivation and Blueprint relationships.
- The source Publication, Blueprint, Assets, Measurements, and relevant Insights.
- [Channels](../../10_brand/channels/README.md): target Channel and compatible Formats.

## Procedure

1. State the target Channel, Format, and reason for reuse.
2. Compare the intended promise, angle, proof, and structure with the source Blueprint.
3. When those upstream decisions remain valid, create a separate Publication linked through `derives from` and adapt only channel-specific content.
4. When any upstream decision materially changes, create no Publication; route the subject to Develop Blueprint at Plan.
5. Preserve Source, Asset, and derivation provenance in either path.

## Output

Either one derived Publication ready for Review after its Draft work, or a documented Plan-stage handoff to Develop Blueprint.
