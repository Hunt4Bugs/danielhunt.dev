---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-27
updated: 2026-08-27
facets:
  - channels
related:
  - ../publications/README.md
  - ../../../identity/README.md
sources:
  - ../../../ONTOLOGY.md
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

- [Brand ontology v1](../../../ONTOLOGY.md): Publication, Format, Production Dependency State, and evidence conditions.
- [Channels](../../../channels/README.md): Channel registry and compatibility.
- [Identity](../../../identity/README.md), [Strategy](../../../strategy/README.md), and the Publication's Blueprint and Sources.

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
