---
id: content.workflow.produce-publication
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
  - assets
related:
  - ../publications/README.md
  - ../../10_brand/assets/README.md
  - ../concepts.md
sources:
  - ../../10_brand/ONTOLOGY.md
contract:
  subject_type: content.publication
  entry_stage: Produce
  exit_stage: Publish
  requires:
    - id: content.publication
      state: completed
      optional: false
  inputs:
    - name: production_dependencies
      type: taxonomy(Production Dependency State)
      required: true
  creates:
    - type: assets.asset
  updates:
    - type: content.publication
  validation:
    - final_asset_links_recorded
    - capture_completion_confirmed
    - license_restrictions_recorded
    - output_format_checked
    - final_blueprint_comparison_done
  next:
    - content.workflow.publish-publication
  failure_paths:
    - content.workflow.validate-publication
---

# Produce Publication

## Work Item contract

- **Primary subject:** one validated Publication.
- **Entry stage:** Produce.
- **Successful exit stage:** Publish.
- **Creates:** final media, design, audio, or other Assets when required.
- **Updates:** the Publication's Asset links and resolved production dependencies.
- **Required predecessors:** a passed [Validate Publication](validate-publication.md) Work Item.
- **Possible next workflows:** [Publish Publication](publish-publication.md).
- **Validation evidence:** final Asset links, capture completion, source or license restrictions, output-format checks, and final Blueprint comparison recorded in the Work Item.
- **Failure and return paths:** remain in Produce while planned captures or obtainable Assets are outstanding; return to Review when the final output changes approved content or intent.

## Required references

- The validated Publication and its validation Work Item.
- [Assets](../../10_brand/assets/README.md): Asset types and production-dependency rules.
- [Identity](../../10_brand/identity/README.md) and [visual direction](../../10_brand/identity/visual.md).

## Procedure

1. Resolve each Planned Capture and Obtainable External Asset.
2. Create or link final Assets and record source, access, and licensing restrictions.
3. Update dependency states to Existing Asset when the material is available locally.
4. Assemble the final channel-ready expression.
5. Compare the final output with the validated Publication and Blueprint.

## Output

One production-complete Publication with final Asset links and no unresolved dependency.

## Stop conditions

Stop before Publish when an Asset is missing, a usage right is unclear, the final output fails its Channel constraints, or production has changed approved intent.
