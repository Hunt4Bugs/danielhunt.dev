---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
created: 2026-08-26
updated: 2026-08-27
facets:
  - operations
related:
  - README.md
  - ../work-items/README.md
sources:
  - ../sources/colin-and-samir-short-form-anatomy.md
---

# Generate Hook Options

Apply the source-derived Quilt Method to a short-form Blueprint that is ready for hook development.

## Work Item contract

- **Primary subject:** one short-form Blueprint.
- **Entry stage:** Plan.
- **Successful exit stage:** Draft.
- **Creates:** no new domain entity.
- **Updates:** candidate and final hook selections on the Blueprint.
- **Required predecessors:** a [Develop Blueprint](develop-blueprint.md) Work Item that established the promise, angle, proof, and constraints.
- **Possible next workflows:** [Generate Short-Form Script](generate-short-form-script.md) or [Develop Publication](develop-publication.md).
- **Validation evidence:** considered pairs, rejection reasons, hook-condition checks, production feasibility, selected pair, and updated Blueprint link recorded in the Work Item.
- **Failure and return paths:** return to Develop Blueprint when no truthful and feasible pair preserves the intended promise or structure.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Visual Hook Type, Verbal Hook Type, and Hook usage conditions.
- [Short-form anatomy Source](../sources/colin-and-samir-short-form-anatomy.md): attributed origin of the hook catalog and Quilt Method.
- [Short-form anatomy Knowledge](../knowledge/short-form-anatomy.md): reusable method and timing boundary.
- [Identity](../../../identity/README.md) and [Strategy](../../../strategy/README.md): documentary and editorial constraints.

## Taxonomy contract

- **Reads:** the Blueprint's Content Pattern, Content Purpose, Narrative Structure, and any selected or restricted hook values.
- **Writes:** candidate and selected Visual Hook Type / Verbal Hook Type pairs on the Blueprint.
- **Restriction:** apply evidence-required and editorial-review-required conditions before selection; do not add or rename hook types.

## Input

One Blueprint ready for hook development with a Topic, audience promise, evidence boundary, production dependencies, and any hook-type restrictions.

## Procedure

1. Generate at least three Visual Hook Type and Verbal Hook Type pairings.
2. Write one first-frame description and one concise open-loop line for each pairing.
3. Reject options that require invented footage, unsupported facts, customer outcomes, celebrity likeness, or off-brand trend participation.
4. Apply the hook usage conditions in [Brand ontology v1](../../../ONTOLOGY.md).
5. Select the strongest remaining pairing based on truthfulness, Brand fit, and production feasibility.

## Output

One selected opening pair recorded in the Blueprint, plus discarded options and concise rejection reasons in the Work Item. The updated Blueprint becomes script-ready when all other validation requirements are met.
