---
name: to-knowledge
description: Use when the user wants to capture raw material (an observation, experience, research finding, opinion, idea, question, lesson, process, framework, or evidence) from the current conversation or a supplied prompt into a reusable Knowledge record. Also trigger on "capture this as knowledge," "turn this into knowledge," or "add this to the brand's knowledge base." Writes Knowledge (and optionally Source) records under docs/40_content/knowledge/.
---

# To Knowledge

## Overview

This skill produces one reusable Knowledge record, and optionally one or more Source records, from raw material plus its available context and provenance, following `docs/40_content/workflows/capture-knowledge.md`.

## Required references

Before acting, read:

- `docs/40_content/workflows/capture-knowledge.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/40_content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/40_content/knowledge/README.md` (what a Knowledge record is for and what it must link)
- `docs/40_content/sources/README.md` (what a Source record is for and what it must not do)
- `docs/40_content/work-items/README.md` and `docs/40_content/_patterns/work-item.md` (the Work Item identifier format and its required frontmatter and body now live in the pattern file; the README is a short pointer to it)
- `docs/10_brand/identity/README.md` (truthfulness, evidence, privacy, and scars-not-wounds boundaries)

## Input

Raw material with its available context and provenance. The material may be an observation, experience, research finding, opinion, idea, question, lesson, process, framework, or evidence.

Prefer an explicit argument when the user supplies one; otherwise infer the raw material from the current conversation. Gather, from whichever source applies:

- The material itself.
- Its origin (where it came from).
- Its date or timeframe, if known.
- Any access conditions (confidentiality, embargo, or attribution limits).
- Relevant surrounding context, including whether it is firsthand and, if so, the verification limits on that firsthand account.

If the origin cannot be identified at all after checking both the explicit argument and the conversation, do not guess. Treat this as a Stop condition (see below), not a prompt to ask a clarifying question and continue.

## Procedure

Follow `docs/40_content/workflows/capture-knowledge.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value or new-record decision point. Two SKILL-specific mechanics apply on top of that Procedure:

- Where its step 2 (create or link a Source record) is warranted, see Output below for the file path and slug-derivation mechanics.
- Its step 4 (select one Knowledge Kind) and step 6 (dedup check) are the taxonomy-value and new-record decision points the Skill execution contract governs. Validate the chosen Kind and the duplication check against that contract, not against judgment alone.

## Output

Write to `docs/40_content/knowledge/<slug>.md` using `docs/10_brand/assets/templates/knowledge/knowledge-record.md`. Derive `<slug>` by lowercasing the Knowledge record's title and hyphenating.

When step 2 above warrants a Source record, write it first to `docs/40_content/sources/<source-slug>.md` using `docs/10_brand/assets/templates/sources/source-record.md`, then link it from the Knowledge record's Source field. `<source-slug>` is a separate slug: derive it by lowercasing and hyphenating the Source record's own Title field (per the Source template's Header section), which typically names the origin or attribution, not the Knowledge subject. It commonly differs from `<slug>` above, as in the existing pair `docs/40_content/knowledge/short-form-anatomy.md` (Knowledge) and `docs/40_content/sources/colin-and-samir-short-form-anatomy.md` (Source).

Also create, or on a dedup-extend update, one Work Item record under `docs/40_content/work-items/`, per the Skill execution contract's point 7, `capture-knowledge.md`'s own Work Item contract, and `docs/40_content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the target (or, on dedup-extend, the existing) Knowledge record's path (`docs/40_content/knowledge/<slug>.md`), matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description. No required predecessors.

- **Creating a new Knowledge record:** create the Work Item at entry stage Capture, and fill the Knowledge record's (and the Source record's, if one is written) "Creating Work Item" field with this Work Item's path.
- **Dedup-extending an existing Knowledge record:** create the Work Item at entry stage Capture, and add this Work Item's path to the *new* Work Item's own `related` field, pointing at the existing Knowledge record (and Source record, if any). Leave the existing Knowledge record's (and Source record's) "Creating Work Item" field untouched. It must keep naming whichever Work Item originally created it, not the one that merely extended it.

In both cases, create the Work Item at `current_stage: Capture`, then, once the Knowledge record is written and confirmed, update it to `current_stage: Validate` (the successful exit stage). Do not write `current_stage: Validate` directly on creation; the field must reflect the actual Capture-then-Validate transition on every successful run, so two otherwise-identical successful runs do not diverge on this required field.

Confirm before writing, per the Skill execution contract: present the target file path(s), the chosen Knowledge Kind, and a section-by-section summary of the planned content, and wait for explicit approval. Include the Work Item's planned content in this same presentation, as one approval rather than a second round, matching the Skill execution contract's own wording.

## Stop conditions

Stop without creating Knowledge when:

- The origin cannot be represented honestly.
- The material is only an unsupported claim.
- Privacy or confidentiality constraints prevent safe internal capture.

Preserve material as an explicitly labeled unknown when it may become usable after verification later. No upstream skill resolves any of these conditions; this is a hard stop pending better material, origin, or clearance, not a handoff to another skill.

Even when this skill stops without creating Knowledge, it still creates, or leaves, a Work Item recording the block rather than producing nothing with no record of the attempt: set `work_state: Blocked` (the matching Work Item State value in `docs/10_brand/ONTOLOGY.md`) and repository `status: blocked`, and record the actual missing evidence, approval, or dependency in the Work Item's own prose fields (see `docs/40_content/work-items/README.md`).

## Next step

`to-topic`, once one or more related Knowledge records exist to support a Topic premise. `to-topic` would need the resulting Knowledge record(s) as Input.

## Validation

```
rg -n '^---$|^type: knowledge$|^## Header|^## Reusable synthesis|^## Provenance|^## Evidence boundary|^## Validation' docs/40_content/knowledge/<slug>.md
```

When a Source record was also created, additionally check it against the Source template's own structure:

```
rg -n '^---$|^type: source$|^## Header|^## Origin|^## Access conditions|^## Verification limits|^## Scope|^## Validation' docs/40_content/sources/<source-slug>.md
```

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/40_content/work-items/README.md`'s spec instead.
