---
id: content.workflow.validate-script
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
  subject_type: content.script
  entry_stage: Review
  exit_stage: Produce
  requires:
    - id: content.script
      state: completed
      optional: false
  inputs:
    - name: script
      type: ref(content.script)
      required: true
  creates: []
  updates:
    - type: content.work-item
  validation:
    - promise_payoff_checked
    - claims_sourced
    - hook_conditions_checked
    - dependencies_checked
    - documentary_restraint_checked
  next:
    - content.workflow.develop-publication
  failure_paths:
    - content.workflow.generate-short-form-script
    - content.workflow.capture-knowledge
---

# Validate Script

## Work Item contract

- **Primary subject:** one Script Asset.
- **Entry stage:** Review.
- **Successful exit stage:** Produce.
- **Creates:** no new domain entity.
- **Updates:** validation evidence and outcome on the Work Item; the Script only when applying an authorized revision.
- **Required predecessors:** a completed [Generate Short-Form Script](generate-short-form-script.md) Work Item or an equivalent existing Script.
- **Possible next workflows:** [Develop Publication](develop-publication.md) after a pass; Generate Short-Form Script after revision gaps; [Capture Knowledge](capture-knowledge.md) when evidence is insufficient.
- **Validation evidence:** Blueprint fidelity, intended Publication Format, evidence coverage, hook conditions, production dependencies, and editorial checks recorded in the Work Item.
- **Failure and return paths:** return to Draft for script revision or Capture for missing evidence. Channel-specific failures are outside this workflow.

## Required references

- [Brand ontology v1](../../10_brand/ONTOLOGY.md): Script relationship, Publication Format, hook taxonomies, and Hook usage conditions.
- [Identity](../../10_brand/identity/README.md): documentary restraint, observation over preaching, and scars-not-wounds rules.
- The Script's primary Blueprint, linked Sources, related Assets, and intended Publication Format.
- [Short-form Stop–Hook–Payoff Script Template](../../10_brand/assets/templates/scripts/short-form-stop-hook-payoff.md) when validating that format.

## Taxonomy contract

- **Reads:** the Blueprint and Script's Pattern, Purpose, Narrative Structure, Publication Format, and selected hook types.
- **Writes:** no taxonomy values. It writes only the validation outcome and specific revision gaps.
- **Restriction:** reject a Script that uses an undefined taxonomy value or bypasses a required evidence or editorial review condition.

## Input

One Script Asset, its primary Blueprint, linked Sources, and intended Publication Format. A Channel is not required.

## Checks

- The opening promise is explicit and the Payoff fulfills it.
- Facts, statistics, quotations, and outcomes have suitable Sources.
- Chosen hook types meet their evidence or editorial-review conditions.
- Every proposed visual or audio dependency is an Existing Asset, Planned Capture, or Obtainable External Asset; none remains Unresolved.
- The Script follows documentary restraint, observation over preaching, scars-not-wounds, and no unsupported performance claims.

## Output

Record a pass, revision-required result, or evidence-insufficient result on the Work Item. A pass makes the Script eligible for a Publication; it does not validate any Channel-specific expression.
