---
name: to-validate
description: Use when the user wants to check whether a drafted Script is ready for production: promise/payoff fit, source coverage for every claim, hook usage conditions, asset availability, and brand voice rules. Also trigger on "validate this script," "is this ready to shoot," or "check this against brand rules." Produces a pass/revise/return verdict on an existing Script Asset.
---

# To Validate

## Overview

This skill checks one Script Asset against its primary Blueprint, linked Sources, related Assets, and intended Channel, following `docs/100_brand/marketing/content/workflows/validate-script.md`. Unlike the other skills in this pipeline, it does not create or edit a record. It produces one of three verdicts: (a) ready for production, (b) returned for revision, or (c) returned to knowledge capture.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/validate-script.md` (this skill's Required references, Taxonomy contract, Input, Checks, and Output)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation and stop-condition routing that apply to every check below; note step 4, "confirm before writing," does not apply here since this skill writes no record)
- `docs/100_brand/ONTOLOGY.md` (the Script relationship in "Core entities" and the class diagram; the "Content and delivery taxonomies" table for Publication Format; the "Blueprint taxonomies" table for Visual Hook Type and Verbal Hook Type; the separate "Hook usage conditions" table for evidence-required, editorial-review-required, and always-required rows)
- `docs/100_brand/identity/README.md` (documentary restraint, observation-over-preaching, scars-not-wounds, and no-unsupported-performance-claims boundaries)
- `docs/100_brand/assets/templates/scripts/short-form-stop-hook-payoff.md` (the Script template shape, used to confirm the Script under review actually has an opening promise, Development, and Payoff to check)

## Input

One Script Asset (path), its primary Blueprint, linked Sources, related Assets, and the intended Publication format and Channel, per `validate-script.md`'s Input.

Prefer an explicit Script path when the user supplies one; otherwise identify the target Script from the current conversation. If no Script can be identified from either source, or its primary Blueprint or linked Sources cannot be located, ask for them rather than guessing; do not validate against an assumed or partially-resolved set of references.

## Procedure

Run all 5 Checks from `docs/100_brand/marketing/content/workflows/validate-script.md`'s Checks section exactly, applying the Skill execution contract's taxonomy-validation step (step 2) wherever a Check touches a taxonomy value. Report the outcome of every Check individually; do not summarize them into a single pass/fail line. The 5 Checks are:

1. **Promise and Payoff.** The opening promise (Scroll Stopper + Verbal Hook) is explicit, and the Payoff fulfills it.
2. **Source coverage.** Every fact, statistic, quotation, and outcome in the Script has a suitable linked Source.
3. **Hook usage conditions.** The Script's chosen Visual Hook Type and Verbal Hook Type meet their evidence-required or editorial-review-required conditions from the "Hook usage conditions" table in `docs/100_brand/ONTOLOGY.md`.
4. **Asset availability.** Every proposed visual or audio asset exists, is obtainable, or is explicitly marked as a planned capture.
5. **Voice and restraint.** The Script follows documentary restraint, observation over preaching, and scars-not-wounds, and makes no unsupported performance claims.

Per the Taxonomy contract, this skill writes no taxonomy values; it only reads the Blueprint and Script's Pattern, Purpose, Narrative Structure, Publication Format, and selected hook types. Reject outright, as part of Check 3 or Check 5, any Script that uses an undefined taxonomy value (one not present verbatim in the matching `docs/100_brand/ONTOLOGY.md` table) or that bypasses a required evidence or editorial-review condition; do not pass a Script with a known taxonomy or evidence gap on the assumption it will be caught later.

## Output

State one of three verdicts plainly. Never default silently to "ready" when a Check is inconclusive; an inconclusive Check counts as a failure of that Check.

**(a) Ready for production.** All 5 Checks pass. State this plainly and list which Check confirmed what (for example, which Sources cover which claims).

**(b) Returned for revision.** One or more Checks fail for reasons a script edit can fix (a claim missing its Source link, a weak Payoff, a hook missing its required editorial review, an asset not yet marked as a planned capture, a preachy or unsupported line). Name the specific gap per failed Check; do not report a bare "revise" without saying what to change.

**(c) Returned to knowledge capture.** One or more Checks fail because the underlying evidence itself is insufficient or does not exist (Check 2's Source coverage cannot be satisfied because no Source actually supports the claim, or Check 3's evidence-required hook condition cannot be met because the underlying fact or statistic was never substantiated). Name the specific claim and the missing evidence. The Script Asset file itself is left unchanged at its current path; this skill writes nothing on any verdict, so tracking that it is pending re-evidence is the caller's responsibility until `to-knowledge` and a subsequent `to-validate` re-run resolve it.

## Next step

- **Verdict (a):** none. The Script is production-ready as written.
- **Verdict (b):** the existing Script file is revised in place, at its current path, directly, not by re-invoking `to-script`.
  - Not `to-script`: its own Output section states plainly that "every run of this skill produces a new Script file; it does not edit an existing Script or the source Blueprint," so re-running `to-script` against the same target would create a new, differently-slugged file rather than fix the one under review.
  - What "revise in place" means: a human, or this session working directly on the file, edits the existing Script Asset's content using this verdict's named gaps as the punch list, without going through `to-script`'s create-only mechanism again.
  - After such edits: reuse `to-script`'s Validation command (below) against the revised file to confirm its section structure is still intact, then re-run `to-validate`'s 5 Checks against the revised file before treating it as production-ready.
- **Verdict (c):** `to-knowledge`, to capture or correct the missing raw material. `to-knowledge` would need the specific claim and the nature of the missing evidence, as named in the verdict, as Input.

## Validation

None: this skill writes no file on any verdict, so there is nothing of its own to validate. If the Script itself is edited during a verdict-(b) revision, reuse `to-script`'s validation command against it:

```
rg -n '^---$|^## Header|^## Scroll Stopper|^## Development|^## Payoff|^## Script checks' docs/100_brand/assets/scripts/<slug>.md
```
