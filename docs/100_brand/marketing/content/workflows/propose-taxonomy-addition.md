---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - governance
related:
  - README.md
  - ../work-items/README.md
sources:
  - ../../../ONTOLOGY.md
---

# Propose Taxonomy Addition

## Work Item contract

- **Primary subject:** one proposed controlled value.
- **Entry stage:** Validate.
- **Successful exit stage:** Validate; this governance operation does not advance the subject's Content lifecycle.
- **Creates:** a local proposal in the Work Item.
- **Updates:** the owning canonical context only after explicit approval.
- **Required predecessors:** a workflow encounter demonstrating that existing values do not fit.
- **Possible next workflows:** resume the originating workflow after approval; otherwise use an existing value or end the originating execution.
- **Validation evidence:** owning context, duplicate and synonym check, definition, provenance, usage conditions, approval, and canonical update link recorded in the Work Item.
- **Failure and return paths:** retain rejection or missing approval in the Work Item; never make the candidate selectable.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): existing Content vocabularies, entity attachment points, and vocabulary ownership rule.
- [Strategy](../../../strategy/README.md), [Audience](../../../audience/README.md), and [Channels](../../../channels/README.md): owner-specific registries when the candidate is a Theme, Audience Segment, or Channel.
- [Source records](../sources/README.md): provenance requirement.
- [Identity](../../../identity/README.md) and [Strategy](../../../strategy/README.md): brand-fit and editorial constraints.

## Taxonomy contract

- **Reads:** the full canonical taxonomy list for the proposed entity.
- **Writes:** nothing until explicit approval. After approval, the owning canonical context receives the new value, definition, usage conditions, and provenance link.
- **Restriction:** a workflow or skill may create a proposal record, but may not treat a proposed value as selectable.

## Input

A candidate Content Pattern, Purpose, Narrative Structure, Hook Type, Format, or other controlled value that is not already defined in [Brand ontology v1](../../../ONTOLOGY.md).

## Procedure

1. Record the proposed name, definition, intended entity, and why existing values do not fit.
2. Link at least one Source or verified internal example.
3. Define usage conditions, including evidence and editorial-review requirements where relevant.
4. Obtain explicit approval before adding the value to its owning canonical context.

## Output

An approved update to the owning canonical context or a rejected proposal retained in the Work Item. Skills must not silently add canonical values.
