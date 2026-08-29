---
name: to-topic
description: Use when the user wants to develop a reusable Topic (subject or idea) from one or more existing Knowledge records. Also trigger on "turn this knowledge into a topic," "develop a topic," or "what should I plan content around." Writes Topic records under docs/content/topics/.
---

# To Topic

## Overview

This skill produces one Topic record from one or more related Knowledge records with their supporting Sources and evidence boundaries, following `docs/content/workflows/develop-topic.md`.

## Required references

Before acting, read:

- `docs/content/workflows/develop-topic.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/content/topics/README.md` (what a Topic record is for and what it must not be)
- `docs/content/work-items/README.md` and `docs/content/_patterns/work-item.md` (the Work Item identifier format and its required frontmatter and body now live in the pattern file; the README is a short pointer to it)
- `docs/10_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)
- `docs/10_brand/audience/README.md` (Audience Segments, needs, problems, and credibility boundaries)
- `docs/10_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)

## Input

One or more Knowledge records, plus a primary Theme candidate, a Topic Mode candidate, and the relevant Audience Segment.

Prefer explicit links when the user supplies them; otherwise identify the Knowledge records, Theme, Topic Mode, and Audience Segment from the current conversation. If no Knowledge record can be identified from either source, do not guess; a missing or zero Knowledge record is the degenerate case of the Stop condition below where "the linked Knowledge records do not establish enough evidence to support a credible premise," not a prompt to proceed on an unsupported premise.

## Procedure

Follow `docs/content/workflows/develop-topic.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value or new-record decision point. Two SKILL-specific mechanics apply on top of that Procedure:

- Its step 2 (check the existing Topic inventory) is the dedup decision point the Skill execution contract governs: when it finds a materially duplicative Topic, this run extends that record rather than producing a new one, per Output below.
- Its steps 3 and 4 (select one primary Theme and Topic Mode, identify the Audience Segment) are the taxonomy-value decision points; validate Topic Mode against the ONTOLOGY.md taxonomy table per the Skill execution contract, validate Theme against the Theme registry table in `docs/10_brand/strategy/README.md`, and validate Audience Segment against the Audience Segment registry table in `docs/10_brand/audience/README.md`, recording the Segment's name and stable code together (for example "Primary Editorial Audience (B2)").

## Output

Write to `docs/content/topics/<slug>.md` using `docs/10_brand/assets/templates/topics/topic-record.md`. Derive `<slug>` by lowercasing the Topic record's title and hyphenating.

When the dedup check in Procedure step 2 finds an existing Topic that is materially duplicative of the proposed subject, edit that existing file instead of creating a new one. Append new supporting Knowledge links without removing existing ones. Retain existing open questions unless the new Knowledge specifically resolves them, per `develop-topic.md` step 6. Revise the premise, strategic fit, and credibility boundary text only to incorporate the new Knowledge; do not rewrite unrelated existing content. Only write a new file at the derived `<slug>` path when no existing Topic covers the subject.

Also create, or on a dedup-extend update, one Work Item record under `docs/content/work-items/`, per the Skill execution contract's point 7, `develop-topic.md`'s own Work Item contract, and `docs/content/work-items/README.md`'s required frontmatter and body: `primary_subject` is the principal Knowledge record's path (`docs/content/knowledge/<slug>.md`) from which the Topic is developed, matching the `../topics/example.md`-style file-path format `work-items/README.md` specifies, not a prose description. Required predecessors are the completed Capture Knowledge Work Items for the supporting Knowledge records linked in Procedure step 6. For each supporting Knowledge record, read that record's own "Creating Work Item" Header field (set by `to-knowledge` when it created or last extended the record) to find its creating Work Item's path. List every one of them in the new Work Item's `Predecessors` body section, deduplicated: when two or more supporting Knowledge records share the same creating Work Item, list that Work Item's path once, not once per record.

- **Creating a new Topic record:** create the Work Item at entry stage Validate, and fill the Topic record's "Creating Work Item" field with this Work Item's path.
- **Dedup-extending an existing Topic record:** create the Work Item at entry stage Validate, and add this Work Item's path to the *new* Work Item's own `related` field, pointing at the existing Topic record. Leave the existing Topic record's "Creating Work Item" field untouched. It must keep naming whichever Work Item originally created it, not the one that merely extended it.

In both cases, create the Work Item at `current_stage: Validate`, then, once the Topic record is written and confirmed, update it to `current_stage: Plan` (the successful exit stage). Do not write `current_stage: Plan` directly on creation; the field must reflect the actual Validate-then-Plan transition on every successful run, so two otherwise-identical successful runs do not diverge on this required field.

Confirm before writing, per the Skill execution contract: present the target file path (new or existing), the chosen primary Theme, Topic Mode, and Audience Segment (name and stable code together, for example "Primary Editorial Audience (B2)"), and a section-by-section summary of the planned content or edit, and wait for explicit approval. Include the Work Item's planned content in this same presentation, as one approval rather than a second round, matching the Skill execution contract's own wording.

## Stop conditions

Stop and return to `to-knowledge` when the linked Knowledge records do not establish enough evidence to support a credible premise. `to-knowledge` would need the additional raw material as Input.

Stop without creating a Topic when:

- The subject is outside the Brand's strategic constraints.
- The subject depends on private or customer-sensitive material that cannot be safely generalized.
- The subject would publish a wound rather than a scar.

No skill resolves these three conditions; they are hard stops pending a different subject or better clearance, not a handoff to another skill.

Even when this skill stops, whether returning to `to-knowledge` or stopping without creating a Topic, it still creates, or leaves, a Work Item recording the block rather than producing nothing with no record of the attempt: set `work_state: Blocked` (the matching Work Item State value in `docs/10_brand/ONTOLOGY.md`) and repository `status: blocked`, and record the actual missing evidence, approval, or dependency in the Work Item's own prose fields (see `docs/content/work-items/README.md`).

## Next step

`to-blueprint`, once the Topic is ready (has a premise, strategic fit, and credibility boundary). `to-blueprint` would need the resulting Topic record as Input.

## Validation

```
rg -n '^---$|^type: topic$|^## Header|^## Premise|^## Strategic fit|^## Supporting Knowledge|^## Credibility boundary|^## Open questions|^## Validation' docs/content/topics/<slug>.md
```

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/content/work-items/README.md`'s spec instead.
