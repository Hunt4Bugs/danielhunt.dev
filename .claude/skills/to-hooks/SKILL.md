---
name: to-hooks
description: Use when the user wants to generate and select Visual Hook Type / Verbal Hook Type opening pairings for an approved short-form Blueprint, using the Quilt Method. Also trigger on "give me hook options," "what's the opening for this," or "pick a hook." Edits the Opening choices section of an existing Blueprint record.
---

# To Hooks

## Overview

This skill produces one selected opening pair, plus discarded options and rejection reasons recorded in this run's own Work Item, on a Blueprint that is ready for hook development, following `docs/content/workflows/generate-hook-options.md`.

This is the one skill in this pipeline that edits an existing record rather than creating a new one: it does not write a new file at a new `<slug>.md` path. It locates the target Blueprint from Input and edits that file's `## Opening choices` section in place.

`to-blueprint` step 4 leaves the Blueprint's `## Opening choices` section in one of three states, using its own Final / Candidate / Ready for hook development convention:

- **Final**: all six fields filled with real values, no marker. A settled decision, not expecting revision, though a user can still invoke `to-hooks` manually to reconsider even a Final pairing if they want to.
- **Candidate**: all six fields filled with real values, plus the literal suffix ` (candidate, pending to-hooks review)` appended directly after the Verbal Hook Type field's value.
- **Ready for hook development**: all six fields left exactly as the template's own bracket placeholders (`[...]`), completely unfilled.

Treat a Final or Candidate pairing as one candidate among the at least three this skill generates: for Candidate, strip the ` (candidate, pending to-hooks review)` suffix before treating the remaining value as a plain hook-type value, since that suffix is internal bookkeeping on how the pairing arrived, not part of the hook-type value itself. For Ready for hook development (still bracket placeholders), there is nothing to seed from: generate the full set of at least three candidates from scratch, with nothing pre-seeded. The default assumption when a Blueprint arrives here is Candidate or Ready for hook development, since a genuinely Final pairing usually means `to-blueprint` already routed the user to `to-script` directly instead of here. Once a final pairing is confirmed, this skill overwrites the section's six fields with that selection; it does not append the new pairing alongside the old one or leave both sitting in the file.

## Required references

Before acting, read:

- `docs/content/workflows/generate-hook-options.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/content/workflows/README.md#skill-execution-contract` (taxonomy validation, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/content/work-items/README.md` and `docs/content/_patterns/work-item.md` (the Work Item identifier format and its required frontmatter and body now live in the pattern file; the README is a short pointer to it)
- `docs/10_brand/ONTOLOGY.md` (the "Blueprint taxonomies" table for Visual Hook Type and Verbal Hook Type; the separate "Hook usage conditions" table for evidence-required, editorial-review-required, and always-required rows)
- `docs/content/sources/colin-and-samir-short-form-anatomy.md` (attributed origin of the hook catalog and Quilt Method)
- `docs/content/knowledge/short-form-anatomy.md` (reusable method and timing boundary)
- `docs/10_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- `docs/10_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)

## Input

One Blueprint ready for hook development (path), its Topic, audience promise, evidence boundary, production dependencies, and any hook-type restrictions already on the Blueprint, per `generate-hook-options.md`'s Input. Production dependencies here means informal context about what's feasible to produce, drawn from the Blueprint's own Constraints field, not a formally assigned Production Dependency State, which is only assigned later, at the Script beat level, by `to-script`.

Prefer an explicit Blueprint path when the user supplies one; otherwise identify the target Blueprint from the current conversation. If no Blueprint can be identified from either source, ask for it rather than guessing; do not proceed on an assumed Blueprint. Read the target Blueprint's existing `## Opening choices` section as part of gathering Input, to determine which of the three states described above it is currently in (Final, Candidate, or Ready for hook development), since that determines what, if anything, seeds the candidate set below.

## Procedure

Follow `generate-hook-options.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value decision point. Its step 1 requires generating at least three Visual Hook Type and Verbal Hook Type pairings, including the Blueprint's existing pairing (Final taken as-is, or Candidate with its suffix stripped, per Overview above) as one candidate if it is still viable, before narrowing to the single strongest pairing in step 5; do not stop at the first workable option or treat the existing pairing as already final. When the Blueprint arrived Ready for hook development, there is no existing pairing to include; generate all candidates fresh. Its step 2 requires writing a first-frame description and a concise open-loop line for EACH of those generated pairings, not only for the eventual winner; do this per-pairing detail work before narrowing to one in step 5. Validate every candidate's Visual Hook Type and Verbal Hook Type against the "Blueprint taxonomies" table in `docs/10_brand/ONTOLOGY.md`, and apply the separate "Hook usage conditions" table there (evidence-required, editorial-review-required, always-required) before final selection, per step 4.

## Output

Edit the target Blueprint's `## Opening choices` section in place at its existing path (for example `docs/content/blueprints/<slug>.md`); do not create a new file. Overwrite the section's six fields with the selected pairing: Visual Hook Type, Scroll Stopper / first frame, Visual intent, Verbal Hook Type, Open loop, and Spoken or on-screen hook, per the shape in `docs/10_brand/assets/templates/blueprints/short-form-video.md`. Write the selected pairing in as Final (real values, no marker): a confirmed `to-hooks` selection is the settled decision this skill exists to produce. Replace the prior content of the section entirely rather than appending the new pairing beside it. The Blueprint template still has no field for rejected alternatives, so they are not persisted in the Blueprint file itself; instead, record every discarded option and its concise rejection reason in this run's own Work Item (see below), in that Work Item's `Decisions and assumptions` or `Outputs` body section per `docs/content/work-items/README.md`'s required body. They are no longer surfaced only in conversation and lost.

Also create one Work Item record under `docs/content/work-items/`, per the Skill execution contract's point 7, `generate-hook-options.md`'s own Work Item contract, and `docs/content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the target Blueprint's own path (`docs/content/blueprints/<slug>.md`), matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description. Required predecessors are a Develop Blueprint Work Item that established the promise, angle, proof, and constraints. Read the target Blueprint's own "Creating Work Item" Header field to find that predecessor's path, the same lookup mechanic `to-blueprint` uses against a Topic record's "Creating Work Item" field. If the Blueprint's "Creating Work Item" field is still the unfilled `[link]` placeholder, record "existing Blueprint, no Work Item on file" as the predecessor in the new Work Item's Predecessors section instead of a broken link.

This skill updates the Blueprint; it does not create a new domain record, so there is no "Creating Work Item" field to fill on the Blueprint itself, and the field it already has must stay untouched, since it must keep naming whichever Work Item originally created the Blueprint. Instead, once the predecessor Work Item named in the Blueprint's "Creating Work Item" field is located (same lookup and fallback as above), add this new Work Item's own path to *that existing Work Item's* `related` field. That predecessor Work Item is expected to already be at `current_stage: Draft`, since a Blueprint file can't exist on disk until `to-blueprint`'s own successful run already moved it Plan-then-Draft; this run only adds the `related` link and does not need to update its stage. This mirrors the sibling skills' "don't overwrite Creating Work Item, link via `related` instead" pattern, adapted to the fact that this run already has a forward link to the Blueprint (`primary_subject`); the backward link that pattern would normally place on the domain record's own "Creating Work Item" field instead lands on the Blueprint's existing Work Item's `related` field. When the Blueprint's "Creating Work Item" field is still the unfilled placeholder, there is no existing Work Item record to add this link to; note that in the new Work Item's own body instead of leaving a broken link.

Create the Work Item at `current_stage: Plan`, then, once the selected pairing is written and confirmed, update it to `current_stage: Draft` (the successful exit stage). Do not write `current_stage: Draft` directly on creation; the field must reflect the actual Plan-then-Draft transition on every successful run, so two otherwise-identical successful runs do not diverge on this required field.

Confirm before writing, per the Skill execution contract: present the target file path, a before/after of the six `## Opening choices` fields (the current values about to be replaced alongside the proposed new values, not the proposed values alone), and a short note on the rejected alternatives (including why the prior Final, Candidate, or Ready-for-hook-development state was kept or dropped) and where they will be recorded in the Work Item, and wait for explicit approval. Include the Work Item's planned content in this same presentation, as one approval rather than a second round, matching the Skill execution contract's own wording.

## Stop conditions

Reject any option that requires invented footage, unsupported facts, customer outcomes, celebrity likeness, or off-brand trend participation (`generate-hook-options.md` Procedure step 3). Apply the ontology's Hook usage conditions (evidence-required, editorial-review-required) before final selection; when a candidate fails one of these and no viable alternative remains among the generated set, generate additional pairings rather than selecting a non-compliant option.

Stop and return to `to-blueprint` when, after generating and exhausting reasonable candidates, no truthful and feasible pairing preserves the intended promise or structure. `to-blueprint` is the skill that set the promise, angle, proof, and constraints that no candidate could satisfy, so it is the one positioned to resolve this, whether by revising those or by routing the Topic elsewhere.

Even when this skill stops without a resolved pairing, it still creates, or leaves, a Work Item recording the block rather than producing nothing with no record of the attempt. This skill has no domain record write of its own to block (it only ever edits the existing Blueprint file, and leaves that file untouched when it stops here), but its own execution Work Item should still record `work_state: Blocked` (the matching Work Item State value in `docs/10_brand/ONTOLOGY.md`) and repository `status: blocked`, with the actual missing evidence, approval, or dependency recorded in the Work Item's own prose fields (see `docs/content/work-items/README.md`).

## Next step

`to-script`, to draft the full Script Asset from this Blueprint's now-selected opening. `to-script` would need the resulting Blueprint record, with its `## Opening choices` section now final, as Input.

## Validation

```
rg -n '^## Opening choices' -A 8 docs/content/blueprints/<slug>.md
```

Confirm the six bracketed fields (Visual Hook Type, Scroll Stopper / first frame, Visual intent, Verbal Hook Type, Open loop, Spoken or on-screen hook) are filled with the selected pairing, not still `[...]`, and carry no leftover ` (candidate, pending to-hooks review)` suffix.

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/content/work-items/README.md`'s spec instead.
