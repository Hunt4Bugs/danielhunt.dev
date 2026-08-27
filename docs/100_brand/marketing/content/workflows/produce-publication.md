---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - assets
related:
  - ../publications/README.md
  - ../../../assets/README.md
sources:
  - ../../../ONTOLOGY.md
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
- [Assets](../../../assets/README.md): Asset types and production-dependency rules.
- [Identity](../../../identity/README.md) and [visual direction](../../../identity/visual.md).

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
