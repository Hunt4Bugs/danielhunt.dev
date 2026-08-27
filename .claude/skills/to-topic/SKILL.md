---
name: to-topic
description: Use when the user wants to develop a reusable Topic (subject or idea) from one or more existing Knowledge records. Also trigger on "turn this knowledge into a topic," "develop a topic," or "what should I plan content around." Writes Topic records under docs/100_brand/marketing/content/topics/.
---

# To Topic

## Overview

This skill produces one Topic record from one or more related Knowledge records with their supporting Sources and evidence boundaries, following `docs/100_brand/marketing/content/workflows/develop-topic.md`.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/develop-topic.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/100_brand/marketing/content/topics/README.md` (what a Topic record is for and what it must not be)
- `docs/100_brand/strategy/README.md` (primary Themes, positioning, and editorial constraints)
- `docs/100_brand/audience/README.md` (Audience Segments, needs, problems, and credibility boundaries)
- `docs/100_brand/identity/README.md` (voice, privacy, scars-not-wounds, and observation-over-preaching boundaries)

## Input

One or more Knowledge records, plus a primary Theme candidate, a Topic Mode candidate, and the relevant Audience Segment.

Prefer explicit links when the user supplies them; otherwise identify the Knowledge records, Theme, Topic Mode, and Audience Segment from the current conversation. If no Knowledge record can be identified from either source, do not guess; a missing or zero Knowledge record is the degenerate case of the Stop condition below where "the linked Knowledge records do not establish enough evidence to support a credible premise," not a prompt to proceed on an unsupported premise.

## Procedure

Follow `docs/100_brand/marketing/content/workflows/develop-topic.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value or new-record decision point. Two SKILL-specific mechanics apply on top of that Procedure:

- Its step 2 (check the existing Topic inventory) is the dedup decision point the Skill execution contract governs: when it finds a materially duplicative Topic, this run extends that record rather than producing a new one, per Output below.
- Its steps 3 and 4 (select one primary Theme and Topic Mode, identify the Audience Segment) are the taxonomy-value decision points; validate Topic Mode against the ONTOLOGY.md taxonomy table per the Skill execution contract, validate Theme against the Themes list in `docs/100_brand/strategy/README.md`, and validate Audience Segment against the Audience tiers in `docs/100_brand/audience/README.md`.

## Output

Write to `docs/100_brand/marketing/content/topics/<slug>.md` using `docs/100_brand/assets/templates/topics/topic-record.md`. Derive `<slug>` by lowercasing the Topic record's title and hyphenating.

When the dedup check in Procedure step 2 finds an existing Topic that is materially duplicative of the proposed subject, edit that existing file instead of creating a new one. Append new supporting Knowledge links without removing existing ones. Retain existing open questions unless the new Knowledge specifically resolves them, per `develop-topic.md` step 6. Revise the premise, strategic fit, and credibility boundary text only to incorporate the new Knowledge; do not rewrite unrelated existing content. Only write a new file at the derived `<slug>` path when no existing Topic covers the subject.

Confirm before writing, per the Skill execution contract: present the target file path (new or existing), the chosen primary Theme, Topic Mode, and Audience Segment, and a section-by-section summary of the planned content or edit, and wait for explicit approval.

## Stop conditions

Stop and return to `to-knowledge` when the linked Knowledge records do not establish enough evidence to support a credible premise. `to-knowledge` would need the additional raw material as Input.

Stop without creating a Topic when:

- The subject is outside the Brand's strategic constraints.
- The subject depends on private or customer-sensitive material that cannot be safely generalized.
- The subject would publish a wound rather than a scar.

No skill resolves these three conditions; they are hard stops pending a different subject or better clearance, not a handoff to another skill.

## Next step

`to-blueprint`, once the Topic is ready (has a premise, strategic fit, and credibility boundary). `to-blueprint` would need the resulting Topic record as Input.

## Validation

```
rg -n '^---$|^type: topic$|^## Header|^## Premise|^## Strategic fit|^## Supporting Knowledge|^## Credibility boundary|^## Open questions|^## Validation' docs/100_brand/marketing/content/topics/<slug>.md
```
