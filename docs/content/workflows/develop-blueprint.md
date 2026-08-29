---
id: content.workflow.develop-blueprint
kind: workflow
domain: content
type: workflow
status: active
version: 1
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-28
facets:
  - operations
related:
  - README.md
  - ../work-items/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.topic
  entry_stage: Plan
  exit_stage: Draft
  requires:
    - id: content.topic
      state: completed
      optional: false
  inputs:
    - name: topic
      type: ref(content.topic)
      required: true
    - name: audience_segment
      type: ref(audience.segment)
      required: true
    - name: asset_constraints
      type: text
      required: false
  creates:
    - type: content.blueprint
      via_pattern: ../_patterns/blueprint.md
  updates:
    - type: content.blueprint
  validation:
    - taxonomy_values_canonical
    - proof_linked
    - promise_payoff_fit
    - constraints_stated
    - output_link_recorded
  next:
    - content.workflow.generate-hook-options
    - content.workflow.generate-short-form-script
    - content.workflow.develop-publication
  failure_paths:
    - content.workflow.capture-knowledge
---

# Develop Blueprint

## Work Item contract

- **Primary subject:** one Topic.
- **Entry stage:** Plan.
- **Successful exit stage:** Draft.
- **Creates:** one Topic-specific Blueprint.
- **Updates:** an existing Blueprint only when its Topic, promise, angle, and structural intent remain unchanged.
- **Required predecessors:** a completed [Develop Topic](develop-topic.md) Work Item or an existing validated Topic.
- **Possible next workflows:** [Generate Hook Options](generate-hook-options.md) when specialized short-form hook development is required; otherwise [Generate Short-Form Script](generate-short-form-script.md) or [Develop Publication](develop-publication.md).
- **Validation evidence:** canonical taxonomy values, linked proof, promise/payoff fit, constraints, and output link recorded in the Work Item.
- **Failure and return paths:** return to Capture when proof is missing or complete without a Blueprint when the Topic is outside strategic constraints.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Content Pattern, Content Purpose, Narrative Structure, Topic Mode, and hook taxonomies.
- [Strategy](../../10_brand/strategy/README.md): Themes, positioning, and editorial constraints.
- [Audience](../../10_brand/audience/README.md): primary Audience Segment and relevant needs or problems.
- [Identity](../../10_brand/identity/README.md): voice and evidence boundaries.
- For short-form video, the [Short-form video Blueprint Template](../../10_brand/assets/templates/blueprints/short-form-video.md).

## Taxonomy contract

- **Reads:** the Topic's Strategy-owned Theme and Audience-owned Audience Segment; Topic Mode, Content Pattern, Content Purpose, and Narrative Structure; Visual Hook Type and Verbal Hook Type for short-form video.
- **Writes:** one primary Topic Mode, Pattern, Purpose, and Structure; selected hook types when applicable.
- **Restriction:** use only values from the ontology or their owning Strategy and Audience registries. Route a missing value through [Propose Taxonomy Addition](propose-taxonomy-addition.md).

## Input

One Topic, its supporting Knowledge and Sources, a primary Audience Segment, and any relevant Asset constraints.

## Procedure

1. Read the required references and select the primary Theme and Topic Mode.
2. Select one Content Pattern, one primary Content Purpose, and one Narrative Structure.
3. State an audience promise, angle, proof, and constraints.
4. For short-form video, either select the final Visual Hook Type and Verbal Hook Type or mark them ready for [Generate Hook Options](generate-hook-options.md). A short-form Blueprint is not script-ready until the required hook selection is complete.
5. Link Sources for every factual claim, statistic, quotation, or outcome.

## Output

A Topic-specific Blueprint record linked to its creating Work Item. It may produce several Scripts and Publications.

## Stop conditions

Stop and return to Knowledge capture when the proof is missing, the claim cannot be supported, or the Topic does not fit the Brand's strategic constraints.
