---
name: to-hooks
description: Use when the user wants to generate and select Visual Hook Type / Verbal Hook Type opening pairings for an approved short-form Blueprint, using the Quilt Method. Also trigger on "give me hook options," "what's the opening for this," or "pick a hook." Edits the Opening choices section of an existing Blueprint record.
---

# To Hooks

## Overview

This skill produces one selected opening pair, plus discarded options and rejection reasons, recorded on an already-approved Blueprint, following `docs/100_brand/marketing/content/workflows/generate-hook-options.md`.

This is the one skill in this pipeline that edits an existing record rather than creating a new one: it does not write a new file at a new `<slug>.md` path. It locates the target Blueprint from Input and edits that file's `## Opening choices` section in place.

`to-blueprint` step 4 already writes a single, provisional Visual Hook Type / Verbal Hook Type pairing into that section to complete the Blueprint record. Treat whatever is already in `## Opening choices` as one candidate among the at least three this skill generates, not as an empty section to fill from scratch and not as a fixed constraint that limits what else can be proposed. Once a final pairing is confirmed, this skill overwrites the section's six fields with that selection; it does not append the new pairing alongside the old one or leave both sitting in the file.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/generate-hook-options.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/100_brand/ONTOLOGY.md` (the "Blueprint taxonomies" table for Visual Hook Type and Verbal Hook Type; the separate "Hook usage conditions" table for evidence-required, editorial-review-required, and always-required rows)
- `docs/100_brand/marketing/content/sources/colin-and-samir-short-form-anatomy.md` (attributed origin of the hook catalog and Quilt Method)
- `docs/100_brand/marketing/content/knowledge/short-form-anatomy.md` (reusable method and timing boundary)
- `docs/100_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- `docs/100_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)

## Input

One approved Blueprint record (path), its Topic, audience promise, evidence boundary, available Assets, and any hook-type restrictions already on the Blueprint, per `generate-hook-options.md`'s Input.

Prefer an explicit Blueprint path when the user supplies one; otherwise identify the target Blueprint from the current conversation. If no approved Blueprint can be identified from either source, ask for it rather than guessing; do not proceed on an assumed Blueprint. Read the target Blueprint's existing `## Opening choices` section as part of gathering Input, since its current pairing (whether provisional from `to-blueprint` or a prior `to-hooks` run) becomes one of the candidates considered below.

## Procedure

Follow `generate-hook-options.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value decision point. Its step 1 requires generating at least three Visual Hook Type and Verbal Hook Type pairings, including the Blueprint's existing pairing as one candidate if it is still viable, before narrowing to the single strongest pairing in step 5; do not stop at the first workable option or treat the existing pairing as already final. Its step 2 requires writing a first-frame description and a concise open-loop line for EACH of those generated pairings, not only for the eventual winner; do this per-pairing detail work before narrowing to one in step 5. Validate every candidate's Visual Hook Type and Verbal Hook Type against the "Blueprint taxonomies" table in `docs/100_brand/ONTOLOGY.md`, and apply the separate "Hook usage conditions" table there (evidence-required, editorial-review-required, always-required) before final selection, per step 4.

## Output

Edit the target Blueprint's `## Opening choices` section in place at its existing path (for example `docs/100_brand/marketing/content/blueprints/<slug>.md`); do not create a new file. Overwrite the section's six fields with the selected pairing: Visual Hook Type, Scroll Stopper / first frame, Visual intent, Verbal Hook Type, Open loop, and Spoken or on-screen hook, per the shape in `docs/100_brand/assets/templates/blueprints/short-form-video.md`. Replace the prior content of the section entirely rather than appending the new pairing beside it. Rejected alternatives are surfaced only in the confirmation step below; the Blueprint template has no field for them, so they are not persisted anywhere in the Blueprint file.

Confirm before writing, per the Skill execution contract: present the target file path, a before/after of the six `## Opening choices` fields (the current values about to be replaced alongside the proposed new values, not the proposed values alone), and a short note on the rejected alternatives (including why the prior provisional pairing was kept or dropped), and wait for explicit approval.

## Stop conditions

Reject any option that requires invented footage, unsupported facts, customer outcomes, celebrity likeness, or off-brand trend participation (`generate-hook-options.md` Procedure step 3). Apply the ontology's Hook usage conditions (evidence-required, editorial-review-required) before final selection; when a candidate fails one of these and no viable alternative remains among the generated set, generate additional pairings rather than selecting a non-compliant option.

## Next step

`to-script`, to draft the full Script Asset from this Blueprint's now-selected opening. `to-script` would need the resulting Blueprint record, with its `## Opening choices` section now final, as Input.

## Validation

```
rg -n '^## Opening choices' -A 8 docs/100_brand/marketing/content/blueprints/<slug>.md
```

Confirm the six bracketed fields (Visual Hook Type, Scroll Stopper / first frame, Visual intent, Verbal Hook Type, Open loop, Spoken or on-screen hook) are filled with the selected pairing, not still `[...]`.
