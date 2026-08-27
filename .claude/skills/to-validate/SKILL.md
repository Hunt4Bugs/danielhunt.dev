---
name: to-validate
description: Use when the user wants to check whether a drafted Script is ready for production: promise/payoff fit, source coverage for every claim, hook usage conditions, production dependency resolution, and brand voice rules. Also trigger on "validate this script," "is this ready to shoot," or "check this against brand rules." Produces a pass/revise/return verdict on an existing Script Asset.
---

# To Validate

## Overview

This skill checks one Script Asset against its primary Blueprint, linked Sources, related Assets, and intended Publication Format, following `docs/100_brand/marketing/content/workflows/validate-script.md`. It produces one of three verdicts: (a) ready for production, (b) returned for revision, or (c) returned to knowledge capture. Per that workflow's Work Item contract, this skill now creates its own execution Work Item on every run, to record the verdict and Check-by-Check evidence; it does not otherwise create or edit a domain record, and it edits the Script itself only in the narrow case of applying an authorized revision (see Output and Next step below).

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/validate-script.md` (this skill's Work Item contract, Required references, Taxonomy contract, Input, Checks, and Output)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation and stop-condition routing that apply to every check below; step 4, "confirm before writing," now does apply, to the Work Item this skill creates on every run, even though it does not apply to the Script or Blueprint themselves outside the narrow authorized-revision case)
- `docs/100_brand/marketing/content/work-items/README.md` (the Work Item identifier format and its required frontmatter and body)
- `docs/100_brand/ONTOLOGY.md` (the Script relationship in "Core entities" and the class diagram; the "Content and delivery taxonomies" table for Publication Format and Production Dependency State; the "Blueprint taxonomies" table for Visual Hook Type and Verbal Hook Type; the separate "Hook usage conditions" table for evidence-required, editorial-review-required, and always-required rows)
- `docs/100_brand/identity/README.md` (documentary restraint, observation-over-preaching, scars-not-wounds, and no-unsupported-performance-claims boundaries)
- `docs/100_brand/assets/templates/scripts/short-form-stop-hook-payoff.md` (the Script template shape, used to confirm the Script under review actually has an opening promise, Development, and Payoff to check, and to locate the Script's own "Creating Work Item" Header field for predecessor lookup)

## Input

One Script Asset (path), its primary Blueprint, linked Sources, related Assets, and its intended Publication Format, per `validate-script.md`'s Input. A Channel is not required.

Prefer an explicit Script path when the user supplies one; otherwise identify the target Script from the current conversation. If no Script can be identified from either source, or its primary Blueprint or linked Sources cannot be located, ask for them rather than guessing; do not validate against an assumed or partially-resolved set of references.

## Procedure

Run all 5 Checks from `docs/100_brand/marketing/content/workflows/validate-script.md`'s Checks section exactly, applying the Skill execution contract's taxonomy-validation step (step 2) wherever a Check touches a taxonomy value. Report the outcome of every Check individually; do not summarize them into a single pass/fail line. The 5 Checks are:

1. **Promise and Payoff.** The opening promise (Scroll Stopper + Verbal Hook) is explicit, and the Payoff fulfills it.
2. **Source coverage.** Every fact, statistic, quotation, and outcome in the Script has a suitable linked Source.
3. **Hook usage conditions.** The Script's chosen Visual Hook Type and Verbal Hook Type meet their evidence-required or editorial-review-required conditions from the "Hook usage conditions" table in `docs/100_brand/ONTOLOGY.md`.
4. **Production dependency resolution.** Every proposed visual or audio dependency carries one of the Production Dependency State taxonomy's values (`docs/100_brand/ONTOLOGY.md`'s "Content and delivery taxonomies" table): Existing Asset, Planned Capture, or Obtainable External Asset; none remains Unresolved.
5. **Voice and restraint.** The Script follows documentary restraint, observation over preaching, and scars-not-wounds, and makes no unsupported performance claims.

Per the Taxonomy contract, this skill writes no taxonomy values; it only reads the Blueprint and Script's Pattern, Purpose, Narrative Structure, Publication Format, and selected hook types. Reject outright, as part of Check 3 or Check 5, any Script that uses an undefined taxonomy value (one not present verbatim in the matching `docs/100_brand/ONTOLOGY.md` table) or that bypasses a required evidence or editorial-review condition; do not pass a Script with a known taxonomy or evidence gap on the assumption it will be caught later.

## Output

State one of three verdicts plainly, and record that verdict, with the Check-by-Check evidence backing it, in this run's Work Item (see below), not only in conversation. Never default silently to "ready" when a Check is inconclusive; an inconclusive Check counts as a failure of that Check.

**(a) Ready for production.** All 5 Checks pass. State this plainly and list which Check confirmed what (for example, which Sources cover which claims).

**(b) Returned for revision.** One or more Checks fail for reasons a script edit can fix (a claim missing its Source link, a weak Payoff, a hook missing its required editorial review, an asset not yet marked as a planned capture, a preachy or unsupported line). Name the specific gap per failed Check; do not report a bare "revise" without saying what to change.

**(c) Returned to knowledge capture.** One or more Checks fail because the underlying evidence itself is insufficient or does not exist (Check 2's Source coverage cannot be satisfied because no Source actually supports the claim, or Check 3's evidence-required hook condition cannot be met because the underlying fact or statistic was never substantiated). Name the specific claim and the missing evidence. The Script Asset file itself is left unchanged at its current path; this skill does not edit the Script or Blueprint domain records on this verdict, but the Work Item created below records the specific evidence gap, so tracking that it is pending re-evidence is anchored to that Work Item until `to-knowledge` and a subsequent `to-validate` re-run resolve it.

### Work Item

Also create one Work Item record under `docs/100_brand/marketing/content/work-items/`, on every run regardless of verdict, per the Skill execution contract's point 7, `validate-script.md`'s own Work Item contract, and `docs/100_brand/marketing/content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the Script Asset's own path, matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description.

Required predecessors follow the same single-tier lookup, mirroring `to-blueprint`'s single-tier lookup against its own upstream "Creating Work Item" field (this skill needs only the one Generate Short-Form Script predecessor, unlike `to-script`'s own two-tier Blueprint lookup): read the Script's own "Creating Work Item" Header field (set by `to-script` when it created the Script, and never overwritten by this skill) to find the completed Generate Short-Form Script Work Item. This predecessor is always required. If the field is still the unfilled `[link]` placeholder, record "existing Script, no Work Item on file" as that predecessor instead of a broken link, per `validate-script.md`'s own "a completed Generate Short-Form Script Work Item or an equivalent existing Script."

On a re-validation run, after a verdict-(b) revision-and-rerun cycle, always create a new Work Item under a fresh `-02`-suffixed identifier per the identifier spec's dedup rule; never update the prior Validate Script Work Item in place. List that prior (superseded) Validate Script Work Item for this same Script as an additional predecessor alongside the Generate Short-Form Script Work Item, so the revision loop stays traceable end to end through to the eventual pass.

Create the Work Item at `current_stage: Review` (the entry stage). Then, depending on verdict:

- **Verdict (a), pass:** once all 5 Checks are complete and confirmed, update it to `current_stage: Produce` (the successful exit stage). Do not write `current_stage: Produce` directly on creation; the field must reflect the actual Review-then-Produce transition on every successful run. Set `work_state: Completed` and `status: archived`: this Work Item's own job, running the 5 Checks and recording a verdict, is finished, so per `docs/100_brand/marketing/content/workflows/README.md` point 7 and `work-items/README.md`'s `status: archived` definition ("after completion"), it moves out of `status: active` immediately rather than being left to look still in progress.
- **Verdict (b), revision required:** leave `current_stage: Review`; this Work Item never reaches Produce, since the Script did not pass. Set `work_state: Completed`, not `Blocked`, and `status: archived`. Reasoning: this Work Item's own execution still finished exactly what it set out to do, it ran all 5 Checks to completion and produced a full, actionable verdict; the Checks did their job even though the Script did not pass them. A revision-required outcome is a routine, expected part of the editorial loop, not a stalled or incomplete execution, so it does not fit the same `Blocked` pattern `to-knowledge`, `to-topic`, `to-blueprint`, and `to-hooks` use when their own execution could not produce a result at all. The `status: archived` follows the same completion rule as verdict (a): this Work Item's own run is done, even though the Script itself still needs revision and a fresh `to-validate` run of its own.
- **Verdict (c), evidence insufficient:** leave `current_stage: Review`. Set `work_state: Blocked` (the matching Work Item State value in `docs/100_brand/ONTOLOGY.md`) and repository `status: blocked`, matching the pattern those same sibling skills use when the underlying evidence, approval, or dependency genuinely does not exist yet. Reasoning: unlike verdict (b), this outcome is not something a script edit alone can resolve; evidence that was never captured cannot be revised into existence, so production readiness stays genuinely blocked pending a `to-knowledge` capture this Work Item cannot itself perform, distinguishing "sent back for revision" (b) from "genuinely blocked" (c).

Confirm before writing, per the Skill execution contract: present the target Work Item path, the verdict, and the Check-by-Check evidence behind it, and wait for explicit approval before creating the Work Item. When verdict (b) is applied through an authorized in-place Script revision (see Next step), present that Script edit alongside the Work Item's planned content as one approval, matching the Skill execution contract's own wording; otherwise present the Work Item's planned content on its own, since no Script or Blueprint edit occurs on this run.

## Next step

- **Verdict (a):** per `validate-script.md`'s Work Item contract, the next workflow is Develop Publication. No skill for Develop Publication exists yet, so a human currently takes over there; note it as context only rather than inventing a skill invocation, the same pattern `to-blueprint` uses for the same not-yet-built workflow.
- **Verdict (b):** the existing Script file is revised in place, at its current path, directly, not by re-invoking `to-script`. This matches `validate-script.md`'s Work Item contract, which updates "the Script only when applying an authorized revision," not by creating a new domain record.
  - Not `to-script`: its own Output section states plainly that "every run of this skill produces a new Script file; it does not edit an existing Script or the source Blueprint," so re-running `to-script` against the same target would create a new, differently-slugged file rather than fix the one under review.
  - What "revise in place" means: a human, or this session working directly on the file, edits the existing Script Asset's content using this verdict's named gaps as the punch list, without going through `to-script`'s create-only mechanism again.
  - After such edits: reuse `to-script`'s Validation command (below) against the revised file to confirm its section structure is still intact, then re-run `to-validate`'s 5 Checks against the revised file before treating it as production-ready.
- **Verdict (c):** `to-knowledge`, to capture or correct the missing raw material. `to-knowledge` would need the specific claim and the nature of the missing evidence, as named in the verdict, as Input. This run's Work Item records the block (see Output), so the gap is not lost between now and that follow-on capture.

## Validation

This skill writes a Work Item on every run, but no domain record outside the narrow verdict-(b) authorized-revision case, so there is no fixed Script or Blueprint path to validate against by default. The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/100_brand/marketing/content/work-items/README.md`'s spec instead.

If the Script itself is edited during a verdict-(b) revision, reuse `to-script`'s validation command against it:

```
rg -n '^---$|^## Header|^## Scroll Stopper|^## Development|^## Payoff|^## Script checks' docs/100_brand/assets/scripts/<slug>.md
```
