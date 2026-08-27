---
name: to-blueprint
description: Use when the user wants to turn an approved Topic into a Topic-specific communication plan: objective, audience, angle, pattern, structure, hook, CTA, proof, and constraints. Also trigger on "plan this topic," "develop a blueprint," or "what's the angle for this." Writes Blueprint records under docs/100_brand/marketing/content/blueprints/.
---

# To Blueprint

## Overview

This skill produces one Blueprint record from one Topic, its supporting Knowledge and Sources, a primary Audience Segment, and any Asset constraints, following `docs/100_brand/marketing/content/workflows/develop-blueprint.md`.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/develop-blueprint.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/100_brand/marketing/content/blueprints/README.md` (what a Blueprint record is for and what it must not contain)
- `docs/100_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)
- `docs/100_brand/audience/README.md` (Audience Segments, needs, problems, and credibility boundaries)
- `docs/100_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- For short-form video specifically, `docs/100_brand/assets/templates/blueprints/short-form-video.md` (the only Blueprint template that currently exists; see Output below)

## Input

One Topic record, its supporting Knowledge and Sources, a primary Audience Segment, and any relevant Asset constraints, per `develop-blueprint.md`'s Input.

Prefer an explicit Topic link when the user supplies one; otherwise identify the Topic from the current conversation. Also gather a Theme candidate and Topic Mode candidate for step 1's selection, and, for short-form video, the intended Content Pattern for step 2's selection. If no Topic record can be identified from either source, ask for it rather than guessing; do not proceed on an assumed Topic.

## Procedure

Follow `develop-blueprint.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value decision point:

- Step 1 (select the primary Theme and Topic Mode) validates Theme against the Themes list in `docs/100_brand/strategy/README.md`, and Topic Mode against the "Content and delivery taxonomies" table in `docs/100_brand/ONTOLOGY.md`.
- Step 2 (select one Content Pattern, one primary Content Purpose, and one Narrative Structure) validates each against the "Blueprint taxonomies" table in `docs/100_brand/ONTOLOGY.md`.
- Step 4 (for short-form video, select Visual Hook Type and Verbal Hook Type) validates both against the same "Blueprint taxonomies" table in `docs/100_brand/ONTOLOGY.md`. This selection is a single, provisional working pairing made to complete the record, not a final decision: `to-hooks` (see Next step) later generates at least three pairings via the Quilt Method and may replace it after vetting the alternatives.

Unlike `to-topic`, this skill has no dedup-and-extend step: `develop-blueprint.md`'s Procedure has no step that checks an existing Blueprint inventory, and per `docs/100_brand/ONTOLOGY.md`'s relationships section, "A Topic has zero or many Blueprints." Every run of this skill produces a new Blueprint record, even when other Blueprints already exist for the same Topic.

## Output

Write to `docs/100_brand/marketing/content/blueprints/<slug>.md`, using `docs/100_brand/assets/templates/blueprints/short-form-video.md` when the target format is short-form video. Derive `<slug>` by lowercasing the Blueprint's title and hyphenating.

`docs/100_brand/assets/templates/blueprints/` currently contains only the short-form-video template. If the target format is not short-form video, stop before writing and tell the user that no Blueprint template exists yet for that format, rather than improvising a Blueprint shape from the short-form-video template or from scratch.

Confirm before writing, per the Skill execution contract: present the target file path, the chosen primary Theme, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, and (for short-form video) the provisional Visual Hook Type and Verbal Hook Type pairing (flagged as provisional, since `to-hooks` will revisit it), plus a section-by-section summary of the planned content, and wait for explicit approval.

## Stop conditions

Stop and return to `to-knowledge` when the proof is missing, the claim cannot be supported, or the Topic does not fit the Brand's strategic constraints. `to-knowledge` would need the additional or corrected raw material as Input.

## Next step

`to-hooks`, to select the opening Visual/Verbal Hook Type pairing for this Blueprint. `to-hooks` would need the resulting Blueprint record as Input, and treats step 4's pairing as a starting candidate only, generating and vetting at least three alternatives via the Quilt Method before confirming the final pairing.

## Validation

```
rg -n '^---$|^## Brief|^## Opening choices|^## Story plan|^## Validation' docs/100_brand/marketing/content/blueprints/<slug>.md
```
