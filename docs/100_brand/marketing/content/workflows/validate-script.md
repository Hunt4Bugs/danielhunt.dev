---
class: "100"
collection: content
type: workflow
status: active
owner: Daniel Hunt
updated: 2026-08-26
---

# Validate Script

## Required references

- [Brand ontology v1](../../../ONTOLOGY.md): Script relationship, Publication Format, hook taxonomies, and Hook usage conditions.
- [Identity](../../../identity/README.md): documentary restraint, observation over preaching, and scars-not-wounds rules.
- The Script's primary Blueprint, linked Sources, related Assets, and intended Channel.
- [Short-form Stop–Hook–Payoff Script Template](../../../assets/templates/scripts/short-form-stop-hook-payoff.md) when validating that format.

## Taxonomy contract

- **Reads:** the Blueprint and Script's Pattern, Purpose, Narrative Structure, Publication Format, and selected hook types.
- **Writes:** no taxonomy values. It writes only the validation outcome and specific revision gaps.
- **Restriction:** reject a Script that uses an undefined taxonomy value or bypasses a required evidence or editorial review condition.

## Input

One Script Asset, its primary Blueprint, linked Sources, and the intended Publication format and Channel.

## Checks

- The opening promise is explicit and the Payoff fulfills it.
- Facts, statistics, quotations, and outcomes have suitable Sources.
- Chosen hook types meet their evidence or editorial-review conditions.
- Every proposed visual or audio asset exists, is obtainable, or is explicitly marked as a planned capture.
- The Script follows documentary restraint, observation over preaching, scars-not-wounds, and no unsupported performance claims.

## Output

Mark the Script ready for production, return it for revision with specific gaps, or return it to Knowledge capture if evidence is insufficient.
