---
name: to-knowledge
description: Use when the user wants to capture raw material (an observation, experience, research finding, opinion, idea, question, lesson, process, framework, or evidence) from the current conversation or a supplied prompt into a reusable Knowledge record. Also trigger on "capture this as knowledge," "turn this into knowledge," or "add this to the brand's knowledge base." Writes Knowledge (and optionally Source) records under docs/100_brand/marketing/content/knowledge/.
---

# To Knowledge

## Overview

This skill produces one reusable Knowledge record, and optionally one or more Source records, from raw material plus its available context and provenance, following `docs/100_brand/marketing/content/workflows/capture-knowledge.md`.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/capture-knowledge.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- `docs/100_brand/marketing/content/knowledge/README.md` (what a Knowledge record is for and what it must link)
- `docs/100_brand/marketing/content/sources/README.md` (what a Source record is for and what it must not do)
- `docs/100_brand/identity/README.md` (truthfulness, evidence, privacy, and scars-not-wounds boundaries)

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

Follow `docs/100_brand/marketing/content/workflows/capture-knowledge.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value or new-record decision point. Two SKILL-specific mechanics apply on top of that Procedure:

- Where its step 2 (create or link a Source record) is warranted, see Output below for the file path and slug-derivation mechanics.
- Its step 4 (select one Knowledge Kind) and step 6 (dedup check) are the taxonomy-value and new-record decision points the Skill execution contract governs. Validate the chosen Kind and the duplication check against that contract, not against judgment alone.

## Output

Write to `docs/100_brand/marketing/content/knowledge/<slug>.md` using `docs/100_brand/assets/templates/knowledge/knowledge-record.md`. Derive `<slug>` by lowercasing the Knowledge record's title and hyphenating.

When step 2 above warrants a Source record, write it first to `docs/100_brand/marketing/content/sources/<source-slug>.md` using `docs/100_brand/assets/templates/sources/source-record.md`, then link it from the Knowledge record's Source field. `<source-slug>` is a separate slug: derive it by lowercasing and hyphenating the Source record's own Title field (per the Source template's Header section), which typically names the origin or attribution, not the Knowledge subject. It commonly differs from `<slug>` above, as in the existing pair `docs/100_brand/marketing/content/knowledge/short-form-anatomy.md` (Knowledge) and `docs/100_brand/marketing/content/sources/colin-and-samir-short-form-anatomy.md` (Source).

Confirm before writing, per the Skill execution contract: present the target file path(s), the chosen Knowledge Kind, and a section-by-section summary of the planned content, and wait for explicit approval.

## Stop conditions

Stop without creating Knowledge when:

- The origin cannot be represented honestly.
- The material is only an unsupported claim.
- Privacy or confidentiality constraints prevent safe internal capture.

Preserve material as an explicitly labeled unknown when it may become usable after verification later. No upstream skill resolves any of these conditions; this is a hard stop pending better material, origin, or clearance, not a handoff to another skill.

## Next step

`to-topic`, once one or more related Knowledge records exist to support a Topic premise. `to-topic` would need the resulting Knowledge record(s) as Input.

## Validation

```
rg -n '^---$|^type: knowledge$|^## Header|^## Reusable synthesis|^## Provenance|^## Evidence boundary|^## Validation' docs/100_brand/marketing/content/knowledge/<slug>.md
```

When a Source record was also created, additionally check it against the Source template's own structure:

```
rg -n '^---$|^type: source$|^## Header|^## Origin|^## Access conditions|^## Verification limits|^## Scope|^## Validation' docs/100_brand/marketing/content/sources/<source-slug>.md
```
