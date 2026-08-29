---
id: content.workflow.develop-publication
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
  - ../../10_brand/channels/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.blueprint
  entry_stage: Draft
  exit_stage: Review
  requires:
    - id: content.blueprint
      state: completed
      optional: false
    - id: content.script
      state: validated
      optional: true
  inputs:
    - name: channel
      type: ref(channels.channel)
      required: true
    - name: format
      type: taxonomy(Publication Format)
      required: true
    - name: content
      type: text
      required: true
  creates:
    - type: content.publication
      via_pattern: ../_patterns/publication.md
  updates:
    - type: content.publication
  validation:
    - blueprint_linked
    - channel_format_compatible
    - content_recorded
    - asset_links_recorded
    - production_dependencies_assigned
    - derivation_recorded_if_applicable
    - output_link_recorded
  next:
    - content.workflow.validate-publication
  failure_paths:
    - content.workflow.develop-blueprint
    - content.workflow.generate-short-form-script
---

# Develop Publication

## Work Item contract

- **Primary subject:** one Blueprint.
- **Entry stage:** Draft.
- **Successful exit stage:** Review.
- **Creates:** one channel-specific Publication.
- **Updates:** an existing unpublished Publication only when its Blueprint, Channel, and Format remain unchanged.
- **Required predecessors:** a completed Blueprint Work Item; a passed [Validate Script](validate-script.md) Work Item when the Publication uses a primary Script.
- **Possible next workflows:** [Validate Publication](validate-publication.md).
- **Validation evidence:** Blueprint, exact Channel and Format, compatibility check, content, Asset links, production dependencies, derivation, and output link recorded in the Work Item.
- **Failure and return paths:** return to Develop Blueprint when promise, angle, or structure must change; return to script revision when a required Script has not passed validation.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Publication, Publication Format, derivation, and Asset relationships.
- [Publication records](../publications/README.md): record contract.
- [Channels](../../10_brand/channels/README.md): Channel registry and compatible Formats.
- The primary Blueprint, supporting Sources, related Assets, and any validated primary Script.

## Taxonomy contract

- **Reads:** Publication Format, Production Dependency State, Channel, Blueprint taxonomies, and existing Publication inventory.
- **Writes:** one existing Publication Format, one existing Channel, and dependency states on the Publication.
- **Restriction:** do not add a value or use an incompatible Channel and Format pair.

## Procedure

1. Select one Channel and compatible Publication Format.
2. Adapt the Blueprint into channel-specific content without changing its promise, angle, proof, or structure.
3. Link the primary Script when applicable and all required Assets.
4. Assign every production requirement a Production Dependency State.
5. Link a source Publication through `derives from` when this is a repurposed expression.
6. Leave publication time, canonical URL, and platform identifier empty.

## Output

One Publication record linked to its creating Work Item and ready for review.

## Stop conditions

Stop when Channel and Format are incompatible, a required Script has not passed validation, evidence cannot support the adapted copy, or the adaptation requires changing upstream Blueprint intent.
