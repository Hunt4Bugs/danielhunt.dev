---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
updated: 2026-08-26
---

# Propose Taxonomy Addition

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): existing controlled vocabularies and entity attachment points.
- [Source records](../sources/README.md): provenance requirement.
- [Identity](../../../identity/README.md) and [Strategy](../../../strategy/README.md): brand-fit and editorial constraints.

## Taxonomy contract

- **Reads:** the full canonical taxonomy list for the proposed entity.
- **Writes:** nothing until explicit approval. After approval, the canonical ontology receives the new value, definition, usage conditions, and provenance link.
- **Restriction:** a workflow or skill may create a proposal record, but may not treat a proposed value as selectable.

## Input

A candidate Content Pattern, Purpose, Narrative Structure, Hook Type, Format, or other controlled value that is not already defined in [Brand ontology v1](../../../ONTOLOGY.md).

## Procedure

1. Record the proposed name, definition, intended entity, and why existing values do not fit.
2. Link at least one Source or verified internal example.
3. Define usage conditions, including evidence and editorial-review requirements where relevant.
4. Obtain explicit approval before adding the value to the canonical ontology.

## Output

An approved ontology update or a rejected proposal retained only as local working context. Skills must not silently add canonical taxonomy values.
