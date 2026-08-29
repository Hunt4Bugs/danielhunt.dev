---
name: to-blueprint
description: Use when the user wants to turn an approved Topic into a Topic-specific communication plan: objective, audience, angle, pattern, structure, hook, CTA, proof, and constraints. Also trigger on "plan this topic," "develop a blueprint," or "what's the angle for this." Writes Blueprint records under docs/content/blueprints/.
---

# To Blueprint

## Overview

This skill produces one Blueprint record from one Topic, its supporting Knowledge and Sources, a primary Audience Segment, and any Asset constraints, following `docs/content/workflows/develop-blueprint.md`.

## Required references

Before acting, read:

- `docs/content/workflows/develop-blueprint.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/content/blueprints/README.md` (what a Blueprint record is for and what it must not contain)
- `docs/content/work-items/README.md` and `docs/content/_patterns/work-item.md` (the Work Item identifier format and its required frontmatter and body now live in the pattern file; the README is a short pointer to it)
- `docs/10_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)
- `docs/10_brand/audience/README.md` (Audience Segments, needs, problems, and credibility boundaries)
- `docs/10_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)
- For short-form video specifically, `docs/10_brand/assets/templates/blueprints/short-form-video.md` (the only Blueprint template that currently exists; see Output below)

## Input

One Topic record, its supporting Knowledge and Sources, a primary Audience Segment, and any relevant Asset constraints, per `develop-blueprint.md`'s Input.

Prefer an explicit Topic link when the user supplies one; otherwise identify the Topic from the current conversation. Also gather a Theme candidate and Topic Mode candidate for step 1's selection, and, for short-form video, the intended Content Pattern for step 2's selection. If no Topic record can be identified from either source, ask for it rather than guessing; do not proceed on an assumed Topic. Prefer an explicit existing-Blueprint path when the user supplies one, treating that as the signal that this run continues or refines that Blueprint (subject to the Procedure's create-versus-update test below); absent an explicit existing-Blueprint path, treat this run as producing a new Blueprint.

## Procedure

Follow `develop-blueprint.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value decision point:

- Step 1 (select the primary Theme and Topic Mode) validates Theme against the "Theme registry" table in `docs/10_brand/strategy/README.md`, and Topic Mode against the "Content and delivery taxonomies" table in `docs/10_brand/ONTOLOGY.md`. The primary Audience Segment is read from the Topic record, not re-selected here: the Topic already validated it against the "Audience Segment registry" table in `docs/10_brand/audience/README.md` when `to-topic` created or extended it.
- Step 2 (select one Content Pattern, one primary Content Purpose, and one Narrative Structure) validates each against the "Blueprint taxonomies" table in `docs/10_brand/ONTOLOGY.md`.
- Step 4 (for short-form video, either select the final Visual Hook Type and Verbal Hook Type or mark them ready for Generate Hook Options) validates any selected hook types against the same "Blueprint taxonomies" table in `docs/10_brand/ONTOLOGY.md`. Three outcomes are possible here, and each must be written so it is distinguishable from the other two on disk, using this convention:
  - **Final**: the pairing is settled and no further hook development is expected. Fill the Visual Hook Type and Verbal Hook Type fields (and the rest of Opening choices) with real values, with no additional marker.
  - **Candidate**: the pairing is clear-cut enough to select now, but `to-hooks` (see Next step) is still welcome to revisit it, though not obligated to override it. Fill the fields with real values, and append the literal suffix ` (candidate, pending to-hooks review)` directly after the Verbal Hook Type field's value, so the state is greppable and cannot be mistaken for a Final pairing.
  - **Ready for hook development**: the pairing is not clear-cut. Leave all six Opening choices fields exactly as the template's own bracket placeholders, unfilled, rather than inventing a placeholder pairing. This state is trivially detectable later since the fields still contain literal `[` and `]` characters.

  Per `develop-blueprint.md`, a short-form Blueprint is not script-ready until this hook selection is actually complete: Final only, not Candidate or Ready for hook development.

Unlike `to-topic`, this skill has no keyword-search dedup check against the whole Blueprint collection: `develop-blueprint.md`'s Procedure has no step that scans the existing Blueprint inventory for a materially duplicative subject, and per `docs/10_brand/ONTOLOGY.md`'s relationships section, "A Topic has zero or many Blueprints"; several genuinely distinct Blueprints for the same Topic remain normal. Instead, `develop-blueprint.md`'s Work Item contract narrows the create-versus-update choice to a different question, one specific to a single record already in motion rather than a search across the collection: is this run continuing or refining a Blueprint already in progress, or starting a new communication plan? Create a new Blueprint file for any new or materially different communication plan, even when other Blueprints already exist for the same Topic. Update an existing Blueprint file in place only when this run is continuing or refining a Blueprint already in progress, and its Topic, promise, angle, and structural intent are unchanged from what is already on disk. Do not conflate this with `to-topic`'s dedup-and-extend check: that check asks whether an existing record already covers the same subject and triggers on discovering a pre-existing similar one; this check asks whether the current run is a resumption of one specific record it (or a prior run) already started, and triggers on continuing that same plan.

## Output

Write to `docs/content/blueprints/<slug>.md`, using `docs/10_brand/assets/templates/blueprints/short-form-video.md` when the target format is short-form video. Derive `<slug>` by lowercasing the Blueprint's title and hyphenating.

`docs/10_brand/assets/templates/blueprints/` currently contains only the short-form-video template. If the target format is not short-form video, stop before writing and tell the user that no Blueprint template exists yet for that format, rather than improvising a Blueprint shape from the short-form-video template or from scratch.

When the Procedure's create-versus-update distinction (above) resolves to continuing or refining a Blueprint already in progress, edit that existing file in place instead of creating a new one at the derived `<slug>` path.

Also create, or on an update-in-place, one Work Item record under `docs/content/work-items/`, per the Skill execution contract's point 7, `develop-blueprint.md`'s own Work Item contract, and `docs/content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the Topic's own path (`docs/content/topics/<slug>.md`), matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description and not the Blueprint's own path. Required predecessors are a completed Develop Topic Work Item or an existing validated Topic. Read the Topic record's own "Creating Work Item" Header field (set by `to-topic` when it created or last extended the record) to find that predecessor's path, the same lookup mechanic `to-topic` uses to find its own predecessors against the Knowledge records it links. If the Topic record's "Creating Work Item" field is still the unfilled `[link]` placeholder, record "existing validated Topic, no Work Item on file" as the predecessor in the new Work Item's Predecessors section instead of a broken link.

- **Creating a genuinely new Blueprint:** create the Work Item at entry stage Plan, and fill the new Blueprint record's "Creating Work Item" field with this Work Item's path.
- **Updating an existing in-progress Blueprint:** create the Work Item at entry stage Plan, and add this Work Item's path to the *new* Work Item's own `related` field, pointing at the existing Blueprint record. Leave the existing Blueprint record's "Creating Work Item" field untouched. It must keep naming whichever Work Item originally created it, not the one that merely continued or refined it.

In both cases, create the Work Item at `current_stage: Plan`, then, once the Blueprint record is written and confirmed, update it to `current_stage: Draft` (the successful exit stage). Do not write `current_stage: Draft` directly on creation; the field must reflect the actual Plan-then-Draft transition on every successful run, so two otherwise-identical successful runs do not diverge on this required field.

Confirm before writing, per the Skill execution contract: present the target file path (new or existing), the chosen primary Theme, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, and, for short-form video, the actual state of the Opening choices section this run produced, using step 4's Final / Candidate / Ready for hook development convention: either the selected Visual Hook Type and Verbal Hook Type pairing, marked as Final (a settled decision) or Candidate (presented honestly as one `to-hooks` may still revisit), or the section left unfilled and marked ready for hook development, whichever actually happened. Present this alongside a section-by-section summary of the planned content or edit, and wait for explicit approval. Include the Work Item's planned content in this same presentation, as one approval rather than a second round, matching the Skill execution contract's own wording.

## Stop conditions

Stop and return to `to-knowledge` when the proof is missing, the claim cannot be supported, or the Topic does not fit the Brand's strategic constraints. `to-knowledge` would need the additional or corrected raw material as Input.

Even when this skill stops and returns to `to-knowledge`, it still creates, or leaves, a Work Item recording the block rather than producing nothing with no record of the attempt: set `work_state: Blocked` (the matching Work Item State value in `docs/10_brand/ONTOLOGY.md`) and repository `status: blocked`, and record the actual missing evidence, approval, or dependency in the Work Item's own prose fields (see `docs/content/work-items/README.md`).

## Next step

When this run leaves the Opening choices section Ready for hook development (unfilled) or marked Candidate, short-form video still needs hook selection, so the next step is `to-hooks`, to select the opening Visual/Verbal Hook Type pairing for this Blueprint. `to-hooks` would need the resulting Blueprint record as Input, and treats whatever is already in Opening choices, whether empty, Ready for hook development, or a Candidate pairing, as a starting point only, generating and vetting at least three alternatives via the Quilt Method before confirming the Final pairing.

When this run selected a Final Visual Hook Type and Verbal Hook Type pairing outright and no further hook development is needed, the honest next step is `to-script` directly, skipping `to-hooks`. `to-script` would need the resulting Blueprint record, with its `## Opening choices` section already Final, as Input.

`develop-blueprint.md` also names Develop Publication as a further possible next workflow beyond Generate Short-Form Script, but no skill for that workflow exists yet; note it as context only rather than inventing one.

## Validation

```
rg -n '^---$|^## Brief|^## Opening choices|^## Story plan|^## Validation' docs/content/blueprints/<slug>.md
```

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/content/work-items/README.md`'s spec instead.
