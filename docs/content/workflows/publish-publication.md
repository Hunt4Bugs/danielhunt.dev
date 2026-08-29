---
id: content.workflow.publish-publication
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
  subject_type: content.publication
  entry_stage: Publish
  exit_stage: Measure
  requires:
    - id: content.publication
      state: completed
      optional: false
  inputs:
    - name: authorization
      type: text
      required: true
  creates: []
  updates:
    - type: content.publication
  validation:
    - authorization_confirmed
    - final_preflight_passed
    - publication_location_verified
    - timestamp_recorded
    - platform_identifier_recorded
    - publication_link_updated
  next:
    - content.workflow.record-measurements
  failure_paths:
    - content.workflow.produce-publication
---

# Publish Publication

## Work Item contract

- **Primary subject:** one production-complete Publication.
- **Entry stage:** Publish.
- **Successful exit stage:** Measure.
- **Creates:** no new domain entity.
- **Updates:** durable publication facts on the Publication after verified publication.
- **Required predecessors:** completed [Produce Publication](produce-publication.md) and explicit authorization for the external publish action.
- **Possible next workflows:** [Record Measurements](record-measurements.md).
- **Validation evidence:** approval, final preflight, verified publication location, timestamp, platform identifier, and updated Publication link recorded in the Work Item.
- **Failure and return paths:** stop at Publish without authorization; return to Produce when final preflight fails; remain at Publish when external state cannot be verified.

## Required references

- The production-complete Publication and its final Assets.
- [Channels](../../10_brand/channels/README.md): selected Channel and constraints.
- Repository [autonomy boundaries](../../00_system/020_agents/AUTONOMY.md).

## Procedure

1. Confirm the final content and Assets match the production-complete Publication.
2. Obtain explicit authorization for the external action.
3. Publish through the selected Channel only within that authorization.
4. Verify the published result.
5. Record `published_at`, `canonical_url`, `platform_identifier`, and final Asset links on the Publication.

## Output

One verified published Publication with durable publication facts. A dry run records the approval boundary and stops without changing external state.
