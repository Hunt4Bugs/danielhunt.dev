---
name: to-script
description: Use when the user wants to turn an approved short-form Blueprint (with its selected hooks) into a full Script Asset: shotlist, voiceover, and production cues. Also trigger on "write the script," "draft the shotlist," or "turn this blueprint into a script." Writes Script Assets under docs/100_brand/assets/scripts/.
---

# To Script

## Overview

This skill produces one Script Asset from one approved Blueprint (including its selected hooks from `to-hooks`), that Blueprint's linked Sources, and available Assets, following `docs/100_brand/marketing/content/workflows/generate-short-form-script.md`.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/generate-short-form-script.md` (this skill's Procedure, Input, Output, Taxonomy contract, and Prohibitions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/100_brand/assets/templates/scripts/short-form-stop-hook-payoff.md` (the only Script template that currently exists; see Output below)
- `docs/100_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- `docs/100_brand/assets/README.md` (what an Asset and a Script Template are, and how a Script relates to its primary Blueprint)

## Input

One approved short-form Blueprint (path), with its Pattern, Purpose, Structure, and hook types already selected, specifically its `## Opening choices` section finalized by `to-hooks`, plus that Blueprint's linked Sources and available Assets, per `generate-short-form-script.md`'s Input.

Prefer an explicit Blueprint path when the user supplies one; otherwise identify the target Blueprint from the current conversation. If no approved Blueprint with a finalized `## Opening choices` section can be identified from either source, ask for it rather than guessing; do not proceed on an assumed or still-provisional Blueprint.

## Procedure

Follow `generate-short-form-script.md`'s Procedure exactly, applying the Skill execution contract at each new-record decision point. Its step 2 (fill the Scroll Stopper and Verbal Hook from the selected Blueprint values) pulls directly from the Blueprint's now-final `## Opening choices` fields; it does not regenerate or re-select a hook. Its step 5 (link all factual statements to Sources and every named visual/audio beat to available Assets) is a hard requirement for every row of the Development table, not an optional polish pass; do not leave a beat or a claim unlinked and move on.

Per the Taxonomy contract, this skill writes no new taxonomy values: it reads Publication Format, Narrative Structure, Visual Hook Type, and Verbal Hook Type, and the Script repeats the Blueprint's already-selected values verbatim for traceability. The Blueprint's selected Pattern and Purpose also inform how the Development and Payoff sections are drafted, even though neither is restated in the Script's Header. A Script may not change a Blueprint's Pattern, Structure, or hook types. If, at any point while drafting, the Blueprint's selected plan turns out not to actually support a workable script (the Purpose the Development beats can't fulfill, a Structure the available proof can't carry, or a hook that no longer fits once the beats are drafted), stop drafting immediately. Do not edit the Blueprint's Pattern, Structure, or hook type fields to make the script fit, and do not quietly draft around the mismatch. Route back to `to-blueprint` instead, per Stop conditions below.

## Output

Write to `docs/100_brand/assets/scripts/<slug>.md`, using `docs/100_brand/assets/templates/scripts/short-form-stop-hook-payoff.md`. Derive `<slug>` by lowercasing the Script's title and hyphenating, matching the naming pattern already used at `docs/100_brand/assets/scripts/the-bet.md`. Every run of this skill produces a new Script file; it does not edit an existing Script or the source Blueprint.

Confirm before writing, per the Skill execution contract: present the target file path, the Header fields (Script title, newly authored for this Script, not copied from the Blueprint; Primary Blueprint and Topic, linked from the Blueprint; Target Channel (the Blueprint carries no Channel field, so ask the user for the intended Channel if not already given, do not invent one); and primary visual and verbal hook types, repeated verbatim from the Blueprint per the Taxonomy contract), and a section-by-section summary of the planned Scroll Stopper + Verbal Hook, Development beats with their Source and Asset links, and Payoff, and wait for explicit approval.

## Stop conditions

Do not invent claims, evidence, footage, quotations, outcomes, personal experiences, or customer details (`generate-short-form-script.md`'s Prohibitions section). When real proof for a claim, beat, or outcome is missing, stop and route back to `to-knowledge`, which would need the additional or corrected raw material as Input.

Stop and route back to `to-blueprint` when the Blueprint's selected Pattern, Structure, or hook types do not actually support a workable script once drafting is underway; per the Taxonomy contract this skill may not change those values itself. `to-blueprint` would need the specific mismatch (which field, and why the current selection doesn't hold) as Input to replan.

## Next step

`to-validate`, before this Script is treated as production-ready. `to-validate` would need the resulting Script Asset record as Input.

## Validation

```
rg -n '^---$|^## Header|^## Scroll Stopper|^## Development|^## Payoff|^## Script checks' docs/100_brand/assets/scripts/<slug>.md
```
