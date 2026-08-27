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
  - ../../../ONTOLOGY.md
---

# Generate Short-Form Script

## Work Item contract

- **Primary subject:** one script-ready short-form Blueprint.
- **Entry stage:** Draft.
- **Successful exit stage:** Review.
- **Creates:** one versioned Script Asset.
- **Updates:** none unless explicitly revising an existing Script from a failed validation Work Item.
- **Required predecessors:** a completed [Develop Blueprint](develop-blueprint.md) Work Item and, when used, [Generate Hook Options](generate-hook-options.md).
- **Possible next workflows:** [Validate Script](validate-script.md).
- **Validation evidence:** Blueprint fidelity, intended Publication Format, Source coverage, promise/payoff closure, production-dependency states, and Script link recorded in the Work Item.
- **Failure and return paths:** return to Develop Blueprint when the plan must change; return to Capture when evidence is insufficient.

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Script Asset relationship, Narrative Structure, hook usage conditions, and Publication Format.
- The approved Blueprint, including its selected Pattern, Purpose, Structure, hook types, proof, and constraints.
- [Short-form Stop–Hook–Payoff Script Template](../../../assets/templates/scripts/short-form-stop-hook-payoff.md).
- [Identity](../../../identity/README.md) and [Assets](../../../assets/README.md): editorial constraints and available Asset rules.

## Taxonomy contract

- **Reads:** Publication Format, Narrative Structure, Visual Hook Type, Verbal Hook Type, and the Blueprint's selected Pattern and Purpose.
- **Writes:** no new taxonomy values. The resulting Script repeats the Blueprint's selected values for traceability.
- **Restriction:** a Script may not change a Blueprint's Pattern, Structure, or hook types; return to Develop Blueprint when the plan itself must change.

## Input

One script-ready short-form Blueprint, the [Short-form Stop–Hook–Payoff Script Template](../../../assets/templates/scripts/short-form-stop-hook-payoff.md), linked Sources, and identified production dependencies.

## Procedure

1. Copy the Script Template into a versioned Script Asset record.
2. Fill the Scroll Stopper and Verbal Hook from the selected Blueprint values.
3. Build Development from real proof, observation, story beats, or examples.
4. Write a Payoff that directly fulfills the stated promise.
5. Link all factual statements to Sources. Assign every named visual or audio beat one Production Dependency State: Existing Asset, Planned Capture, Obtainable External Asset, or Unresolved.

## Output

A Script Asset with one primary Blueprint, intended Publication Format, production-dependency states, a link to its creating Work Item, and enough production detail for a later Publication.

## Prohibitions

Do not invent claims, evidence, footage, quotations, outcomes, personal experiences, or customer details. `Unresolved` dependencies may be recorded for revision but cannot pass validation.
