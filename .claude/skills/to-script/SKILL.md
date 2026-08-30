---
name: to-script
description: Use when the user wants to turn an approved short-form Blueprint (with its selected hooks) into a full Script Asset: shotlist, voiceover, and production cues. Also trigger on "write the script," "draft the shotlist," or "turn this blueprint into a script." Writes Script Assets under docs/10_brand/assets/scripts/.
---

# To Script

## Overview

This skill produces one Script Asset from one approved Blueprint (including its selected hooks, whether finalized directly by `to-blueprint` or via `to-hooks`), that Blueprint's linked Sources, and identified production dependencies, following `docs/40_content/workflows/generate-short-form-script.md`.

## Required references

Before acting, read:

- `docs/40_content/workflows/generate-short-form-script.md` (this skill's Procedure, Input, Output, Taxonomy contract, and Prohibitions)
- `docs/40_content/workflows/README.md#skill-execution-contract` (taxonomy validation, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/10_brand/assets/templates/scripts/short-form-stop-hook-payoff.md` (the only Script template that currently exists; see Output below)
- `docs/10_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- `docs/10_brand/assets/README.md` (what an Asset and a Script Template are, how a Script relates to its primary Blueprint, and the "Production dependencies" section's criteria for choosing among the four Production Dependency State values)
- `docs/40_content/work-items/README.md` and `docs/40_content/_patterns/work-item.md` (the Work Item identifier format and its required frontmatter and body now live in the pattern file; the README is a short pointer to it)
- `.claude/skills/to-blueprint/SKILL.md` (defines the Final / Candidate / Ready-for-hook-development convention this skill's Input relies on to tell a settled Blueprint from an unsettled one)

## Input

One approved short-form Blueprint (path), with its Pattern, Purpose, Structure, and hook types already selected, specifically its `## Opening choices` section in the Final state, per `to-blueprint`'s Final / Candidate / Ready-for-hook-development convention. That Final state may have been reached either directly from `to-blueprint` (when the pairing was clear-cut enough to settle outright) or via `to-hooks` (when it needed further development); either path is acceptable Input here, so long as the section is actually Final. A Blueprint whose Opening choices is still Candidate or Ready for hook development is not acceptable Input; it needs `to-hooks` first. A Final and a Candidate Blueprint look nearly identical; distinguish them mechanically, the same way `to-hooks`' own Validation section does: confirm the Verbal Hook Type field carries no ` (candidate, pending to-hooks review)` suffix and no Opening choices field is still the bracket placeholder `[...]`. If either check fails, this is not acceptable Input; ask for a different Blueprint or route the user back to `to-hooks` (Candidate) or `to-blueprint` (still bracket placeholders) to finalize it. This skill's Input also includes that Blueprint's linked Sources and identified production dependencies, per `generate-short-form-script.md`'s Input; it does not need a Channel, since the Script template carries a fixed Intended Publication Format instead (see Output below).

Prefer an explicit Blueprint path when the user supplies one; otherwise identify the target Blueprint from the current conversation. If no approved Blueprint with a Final `## Opening choices` section can be identified from either source, ask for it rather than guessing; do not proceed on an assumed, still-provisional, or merely Candidate Blueprint.

## Procedure

Follow `generate-short-form-script.md`'s Procedure exactly, applying the Skill execution contract at each new-record decision point. Its step 2 (fill the Scroll Stopper and Verbal Hook from the selected Blueprint values) pulls directly from the Blueprint's now-final `## Opening choices` fields; it does not regenerate or re-select a hook. Its step 5 (link all factual statements to Sources, and assign every named visual or audio beat one Production Dependency State: Existing Asset, Planned Capture, Obtainable External Asset, or Unresolved) is a hard requirement for every row of the Development table, not an optional polish pass; do not leave a beat or a claim unlinked, or a beat without an assigned state, and move on. Per `docs/10_brand/ONTOLOGY.md`'s "Content and delivery taxonomies" table, Production Dependency State is scoped to "Script beat or Publication asset requirement," so this is the correct place in the pipeline for this taxonomy to apply, unlike at the Blueprint stage. Choose among the four values per `docs/10_brand/assets/README.md`'s "Production dependencies" section: an Existing Asset beat links to that Asset's own record; a Planned Capture beat states the required capture; an Obtainable External Asset beat records the intended source and its licensing or access constraint; and Unresolved is reserved for a beat whose supply is genuinely undecided (see Stop conditions below on why an Unresolved beat can never be presented as production-ready).

Per the Taxonomy contract, this skill writes no new taxonomy values: it reads Publication Format, Narrative Structure, Visual Hook Type, and Verbal Hook Type, and the Script repeats the Blueprint's already-selected values verbatim for traceability. The Blueprint's selected Pattern and Purpose also inform how the Development and Payoff sections are drafted, even though neither is restated in the Script's Header. A Script may not change a Blueprint's Pattern, Structure, or hook types. If, at any point while drafting, the Blueprint's selected plan turns out not to actually support a workable script (the Purpose the Development beats can't fulfill, a Structure the available proof can't carry, or a hook that no longer fits once the beats are drafted), stop drafting immediately. Do not edit the Blueprint's Pattern, Structure, or hook type fields to make the script fit, and do not quietly draft around the mismatch. Route back to `to-blueprint` instead, per Stop conditions below.

## Output

Write to `docs/10_brand/assets/scripts/<slug>.md`, using `docs/10_brand/assets/templates/scripts/short-form-stop-hook-payoff.md`. Derive `<slug>` by lowercasing the Script's title and hyphenating, matching the naming pattern already used at `docs/10_brand/assets/scripts/the-bet.md`. Every run of this skill produces a new Script file; it does not edit an existing Script or the source Blueprint.

The template's **Intended Publication Format** field is a fixed constant for this template, `Short-form Video`, not a value asked of the user or copied from the Blueprint (the Blueprint carries no Channel field, and this template has no Channel field either, fixed or otherwise). Write it verbatim; do not ask for a Channel and do not invent one.

Also create one Work Item record under `docs/40_content/work-items/`, per the Skill execution contract's point 7, `generate-short-form-script.md`'s own Work Item contract, and `docs/40_content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the source Blueprint's own path (`docs/40_content/blueprints/<slug>.md`), matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description.

Required predecessors follow a two-tier lookup, mirroring the mechanic `to-hooks` uses against the same Blueprint's Header field:

1. Read the source Blueprint's own "Creating Work Item" Header field (set by `to-blueprint` when it created the Blueprint, and never overwritten by `to-hooks`) to find the completed Develop Blueprint Work Item. This predecessor is always required. If the field is still the unfilled `[link]` placeholder, record "existing Blueprint, no Work Item on file" as that predecessor instead of a broken link, and stop this lookup here: with no Develop Blueprint Work Item on file, tier 2 has nothing to read either, so record plainly in the new Work Item's Predecessors section that predecessor lineage for any Generate Hook Options run is unrecoverable via this lookup path. Do not conclude that hook selection was finalized directly; that would be an unverified claim, not an established fact.
2. Otherwise, read that Develop Blueprint Work Item's own `related` field for any Generate Hook Options Work Item entries. Per `to-hooks`' Output, `to-hooks` adds its own new Work Item's path to that `related` field only when it finds an existing Develop Blueprint Work Item to link against in the first place; when the Blueprint's "Creating Work Item" field was still the unfilled placeholder at the time `to-hooks` ran, `to-hooks` instead notes that in its own new Work Item's body, not in any `related` field, so no entry lands here for that case even though `to-hooks` did run. If one or more entries are present, list them as additional required predecessors, since the Opening choices this run relies on were finalized there. If none are present, this Blueprint's Opening choices reached Final directly via `to-blueprint` without `to-hooks`; note plainly in the new Work Item's Predecessors section that hook selection was finalized directly, with no separate Generate Hook Options Work Item to cite.

This skill only ever creates a new Script, per the Work Item contract's "Updates: none unless explicitly revising an existing Script from a failed validation Work Item," a revision case that `to-validate` routes, not one this skill initiates itself. So the standard create pattern applies directly, no asymmetric-link complexity: fill the new Script record's "Creating Work Item" field with this Work Item's path.

Create the Work Item at `current_stage: Draft` (the entry stage), then, once the Script record is written and confirmed, update it to `current_stage: Review` (the successful exit stage). Do not write `current_stage: Review` directly on creation; the field must reflect the actual Draft-then-Review transition on every successful run, so two otherwise-identical successful runs do not diverge on this required field.

Confirm before writing, per the Skill execution contract: present the target file path, the Header fields (Script title, newly authored for this Script, not copied from the Blueprint; Primary Blueprint and Topic, linked from the Blueprint; Intended Publication Format, the fixed `Short-form Video` value; and primary visual and verbal hook types, repeated verbatim from the Blueprint per the Taxonomy contract), and a section-by-section summary of the planned Scroll Stopper + Verbal Hook, Development beats with their Source links and assigned Production Dependency States, with the Asset record linked for any Existing Asset beat, and Payoff, and wait for explicit approval. Include the Work Item's planned content, including the two-tier predecessor lookup result, in this same presentation, as one approval rather than a second round, matching the Skill execution contract's own wording.

## Stop conditions

Do not invent claims, evidence, footage, quotations, outcomes, personal experiences, or customer details (`generate-short-form-script.md`'s Prohibitions section). When real proof for a claim, beat, or outcome is missing, stop and route back to `to-knowledge`, which would need the additional or corrected raw material as Input.

A beat may be recorded with a Production Dependency State of `Unresolved` when its supply is genuinely undecided; this is not itself a Stop condition, since `generate-short-form-script.md`'s Procedure allows recording it for revision. But per that same doc's Prohibitions section, `Unresolved` dependencies cannot pass validation, so do not present an `Unresolved` beat as production-ready in the confirm-before-writing summary, and do not round an `Unresolved` state up to Existing Asset, Planned Capture, or Obtainable External Asset to make the Script look more finished than it is. `to-validate`, at the Validate Script step, is where this rule is actually enforced.

Stop and route back to `to-blueprint` when the Blueprint's selected Pattern, Structure, or hook types do not actually support a workable script once drafting is underway; per the Taxonomy contract this skill may not change those values itself. `to-blueprint` would need the specific mismatch (which field, and why the current selection doesn't hold) as Input to replan.

## Next step

`to-validate`, before this Script is treated as production-ready. `to-validate` would need the resulting Script Asset record as Input.

## Validation

```
rg -n '^---$|^## Header|^## Scroll Stopper|^## Development|^## Payoff|^## Script checks' docs/10_brand/assets/scripts/<slug>.md
```

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/40_content/work-items/README.md`'s spec instead.
