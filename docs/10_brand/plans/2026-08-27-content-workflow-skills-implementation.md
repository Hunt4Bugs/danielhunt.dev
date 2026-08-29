# Content Workflow Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Each task is one vertical slice. Pause for user review between tasks; do not chain.

**Goal:** Turn the seven `docs/100_brand/marketing/content/workflows/*.md` docs into seven executable, project-local Claude Code skills that gather Input, enforce each doc's Taxonomy contract and dedup check, confirm before writing, and suggest (never auto-run) the next pipeline stage.

**Architecture:** A shared "Skill execution contract" section added once to `workflows/README.md`, three new upstream record templates (Knowledge, Topic, Source) added under `assets/templates/` to close a gap the review surfaced, and seven thin `SKILL.md` files under `.claude/skills/` that each point at their one workflow doc plus the shared contract rather than restating either.

**Tech stack:** Markdown only. No code changes, no build step, no test suite (matches the rest of this repo: `docs/000_system/020_agents/VALIDATION.md` confirms there is none). Verification is `rg` checks for required structure plus a full-content review at the end of each task, same pattern as `docs/100_brand/plans/2026-06-01-workbook-docs-implementation.md`.

**Source spec:** `docs/100_brand/specs/2026-08-27-content-workflow-skills-design.md` (read in full before starting; every task below implements one of its eight locked decisions).

**Brand vocabulary discipline:** No em-rules anywhere in brand-shaped writing (`~/.claude/projects/-Users-danielhunt-projects-danielhunt-dev/memory/feedback_no_em_rules.md`). Use commas, periods, parens, mid-dots, asterisms, colons, or numbered sections.

---

## File Structure

| Path | Action | Purpose |
|---|---|---|
| `docs/100_brand/marketing/content/workflows/README.md` | Modify | Add the shared Skill execution contract every skill points to |
| `docs/100_brand/assets/templates/knowledge/README.md` | Create | Knowledge Templates index (mirrors `blueprints/README.md`) |
| `docs/100_brand/assets/templates/knowledge/knowledge-record.md` | Create | Generic Knowledge record template |
| `docs/100_brand/assets/templates/topics/README.md` | Create | Topic Templates index |
| `docs/100_brand/assets/templates/topics/topic-record.md` | Create | Generic Topic record template |
| `docs/100_brand/assets/templates/sources/README.md` | Create | Source Templates index |
| `docs/100_brand/assets/templates/sources/source-record.md` | Create | Generic Source record template |
| `docs/100_brand/assets/templates/README.md` | Modify | Link the three new template categories |
| `.claude/skills/to-knowledge/SKILL.md` | Create | Executes `capture-knowledge.md` |
| `.claude/skills/to-topic/SKILL.md` | Create | Executes `develop-topic.md` |
| `.claude/skills/to-blueprint/SKILL.md` | Create | Executes `develop-blueprint.md` |
| `.claude/skills/to-hooks/SKILL.md` | Create | Executes `generate-hook-options.md` |
| `.claude/skills/to-script/SKILL.md` | Create | Executes `generate-short-form-script.md` |
| `.claude/skills/to-validate/SKILL.md` | Create | Executes `validate-script.md` |
| `.claude/skills/to-taxonomy/SKILL.md` | Create | Executes `propose-taxonomy-addition.md` |
| `docs/100_brand/CHANGELOG.md` | Modify (append) | One entry summarizing this work |

No `.claude/skills/` directory exists yet; Task 6 creates it implicitly via the first `SKILL.md`.

---

## Task 1: Shared skill execution contract

**Type:** AFK. Foundation for every later task; nothing else should reference this section before it exists.

**Blocked by:** None. Start here.

**Files:**
- Modify: `docs/100_brand/marketing/content/workflows/README.md`

### What to build

Append a new `## Skill execution contract` section after the existing bullet list of workflow links. This is the one place the taxonomy-validation, dedup-check, confirm-before-write, stop-condition, and chaining mechanics live; every `SKILL.md` in Tasks 6 to 12 links here instead of restating it.

Content, in this order:

1. **Opening line** stating this section defines the common execution contract for the skills in `.claude/skills/` that run these workflows (`to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, `to-validate`); `to-taxonomy` is the exception these route to, not a follower of this contract.
2. **Resolve references.** Before acting, read every file in the target workflow doc's "Required references" section. Do not proceed from memory of a prior run.
3. **Validate the taxonomy contract.** For every value the workflow doc's Taxonomy contract lists under "Writes," confirm it appears verbatim in the matching table of `../../../ONTOLOGY.md` (Knowledge Kind, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook Type, or Publication Format, as applicable). Read the table at run time; never hardcode a copy of the values elsewhere, since `to-taxonomy` can extend them. If a needed value is not in the table, stop and name `to-taxonomy` as the next step; never approximate, rename, or silently invent a value.
4. **Check for duplicates.** Before creating a new record, search the target collection directory (for example `rg -il '<keyword>' ../knowledge/` from within `workflows/`) for an existing record covering materially the same subject. When the workflow doc's Procedure calls for extending an existing record on duplication (`capture-knowledge.md` step 6, `develop-topic.md` step 2), extend it instead of creating a near-duplicate.
5. **Confirm before writing.** Present the target file path, every chosen taxonomy value, and a section-by-section summary of the planned content. Wait for explicit approval before creating or editing the file. Do not treat silence or an unrelated reply as approval.
6. **Honor stop conditions.** When a workflow doc's "Stop conditions" trigger, halt immediately. State which condition triggered and which workflow (and its skill, if one exists yet) resolves it. Never proceed past a stated stop condition.
7. **Suggest, do not chain.** On a successful Output, name the next applicable skill in the pipeline and what it would need as Input. Do not invoke that skill automatically.

### Acceptance criteria

- [ ] `workflows/README.md` has a `## Skill execution contract` section with all 7 numbered points above present in substance (wording may be tightened, meaning must not drop).
- [ ] The section does not name specific taxonomy values inline (only table names), so it stays correct if `ONTOLOGY.md` is extended later.
- [ ] `rg -n "Skill execution contract" docs/100_brand/marketing/content/workflows/README.md` returns one match.

---

## Task 2: Knowledge template

**Type:** AFK.

**Blocked by:** Task 1 (references the contract's dedup-check language for consistency, not a hard technical dependency, but keep order).

**Files:**
- Create: `docs/100_brand/assets/templates/knowledge/README.md`
- Create: `docs/100_brand/assets/templates/knowledge/knowledge-record.md`

### What to build

`knowledge/README.md`, one paragraph matching the tone of `assets/templates/blueprints/README.md`:

```markdown
# Knowledge Templates

Knowledge Templates provide reusable scaffolding for a Knowledge record. They do not contain the reusable synthesis itself and do not replace the provenance a Source record carries.

- [Knowledge record](knowledge-record.md)
```

`knowledge-record.md`, frontmatter matching the observed pattern in `marketing/content/knowledge/short-form-anatomy.md` plus a `type: knowledge-template` (not `knowledge`, so it is never mistaken for an instance) and a bracketed-value convention matching `blueprints/short-form-video.md`:

```markdown
---
class: "100"
collection: brand
type: knowledge-template
status: active
owner: Daniel Hunt
updated: 2026-08-27
---

# Knowledge Record Template

Use this template to create a Knowledge record. Replace every bracketed field with real, attributable material.

## Header

- **Title:** [reusable subject, not a post title]
- **Knowledge Kind:** [one ONTOLOGY.md Knowledge Kind value]
- **Source:** [link to a Source record, or "none" if the material needs no separate provenance record]

## Reusable synthesis

[The smallest reusable synthesis, in the Brand's voice. Not a Topic, Blueprint, claim, or publication draft.]

## Provenance

- **Origin:** [where this came from]
- **Date or timeframe:** [when, or "unknown"]
- **Access conditions:** [any confidentiality, embargo, or attribution limits]
- **Firsthand context:** [if firsthand, the context and its verification limits; otherwise "n/a"]

## Evidence boundary

[What is verified evidence, what is firsthand account, what is interpretation, and what must not be stated as established fact.]

## Validation

- [ ] Knowledge Kind matches one `ONTOLOGY.md` value.
- [ ] Provenance is preserved (origin, timeframe, access conditions, context).
- [ ] Evidence boundary separates verified fact from interpretation and unknowns.
- [ ] Checked the existing Knowledge inventory; this is not materially duplicative of an existing record.
- [ ] Does not smuggle in Topic, Blueprint, or publication-level decisions.
```

### Acceptance criteria

- [ ] Both files exist at the paths above.
- [ ] `rg -n '^---$|^type: knowledge-template|^## Header|^## Reusable synthesis|^## Provenance|^## Evidence boundary|^## Validation' docs/100_brand/assets/templates/knowledge/knowledge-record.md` matches all 6 patterns.

---

## Task 3: Topic template

**Type:** AFK.

**Blocked by:** Task 1.

**Files:**
- Create: `docs/100_brand/assets/templates/topics/README.md`
- Create: `docs/100_brand/assets/templates/topics/topic-record.md`

### What to build

`topics/README.md`:

```markdown
# Topic Templates

Topic Templates provide reusable scaffolding for a Topic record. A Topic is a reusable subject, not a post, and not a Blueprint.

- [Topic record](topic-record.md)
```

`topic-record.md`:

```markdown
---
class: "100"
collection: brand
type: topic-template
status: active
owner: Daniel Hunt
updated: 2026-08-27
---

# Topic Record Template

Use this template to create a Topic record from one or more supporting Knowledge records. Replace every bracketed field.

## Header

- **Title:** [reusable subject]
- **Primary Theme:** [one ONTOLOGY.md / strategy Theme]
- **Topic Mode:** [Build, Offline, or Bridge]
- **Audience Segment:** [relevant Audience Segment]

## Premise

[The subject, and the need, problem, curiosity, or tension it addresses for the Audience Segment above.]

## Strategic fit

[Why this fits the Brand's strategy and the chosen Theme.]

## Supporting Knowledge

- [link to Knowledge record]
- [link to Knowledge record]

## Credibility boundary

[What the supporting Knowledge and Sources actually establish, and what they do not.]

## Open questions

- [question a later Blueprint must not treat as resolved]

## Validation

- [ ] Primary Theme and Topic Mode match `ONTOLOGY.md` / `strategy/README.md` values.
- [ ] Checked the existing Topic inventory; this is not materially duplicative of an existing Topic.
- [ ] Keeps channel choice, hook, CTA, publication copy, and treatment decisions out (those belong to a Blueprint).
- [ ] Open questions carried forward, not silently resolved.
```

### Acceptance criteria

- [ ] Both files exist at the paths above.
- [ ] `rg -n '^---$|^type: topic-template|^## Header|^## Premise|^## Strategic fit|^## Supporting Knowledge|^## Credibility boundary|^## Open questions|^## Validation' docs/100_brand/assets/templates/topics/topic-record.md` matches all 8 patterns.

---

## Task 4: Source template

**Type:** AFK.

**Blocked by:** Task 1.

**Files:**
- Create: `docs/100_brand/assets/templates/sources/README.md`
- Create: `docs/100_brand/assets/templates/sources/source-record.md`

### What to build

`sources/README.md`:

```markdown
# Source Templates

Source Templates provide reusable scaffolding for a Source record. A Source is provenance, not an automatically approved Brand claim.

- [Source record](source-record.md)
```

`source-record.md`:

```markdown
---
class: "100"
collection: brand
type: source-template
status: active
owner: Daniel Hunt
updated: 2026-08-27
---

# Source Record Template

Use this template to create a Source record. Replace every bracketed field.

## Header

- **Title:** [short identifying name]
- **Origin type:** [document, dataset, recording, interview, firsthand context, or other]

## Origin

[What this is and where it came from.]

## Access conditions

[Any confidentiality, embargo, licensing, or attribution requirements.]

## Verification limits

[What can and cannot be independently verified from this Source. State unknowns explicitly rather than omitting them.]

## Scope

[What this Source may be used to support, and what it may not, per the Brand's evidence and editorial-review conditions.]

## Validation

- [ ] Origin, access conditions, and verification limits are all stated (not omitted as implicitly fine).
- [ ] Checked the existing Source inventory; this is not materially duplicative of an existing Source.
- [ ] Not itself treated as an approved Brand claim.
```

### Acceptance criteria

- [ ] Both files exist at the paths above.
- [ ] `rg -n '^---$|^type: source-template|^## Header|^## Origin|^## Access conditions|^## Verification limits|^## Scope|^## Validation' docs/100_brand/assets/templates/sources/source-record.md` matches all 7 patterns.

---

## Task 5: Wire the templates index

**Type:** AFK.

**Blocked by:** Tasks 2, 3, 4.

**Files:**
- Modify: `docs/100_brand/assets/templates/README.md`

### What to build

Add three bullets to the existing list (after the Blueprint and Script lines, keeping the existing two):

```markdown
- [Knowledge Templates](knowledge/README.md) scaffold reusable Knowledge records.
- [Topic Templates](topics/README.md) scaffold reusable Topic records.
- [Source Templates](sources/README.md) scaffold reusable Source records.
```

### Acceptance criteria

- [ ] `rg -n 'Knowledge Templates|Topic Templates|Source Templates' docs/100_brand/assets/templates/README.md` returns 3 matches.
- [ ] All 5 links in the file resolve to real files (`blueprints/README.md`, `scripts/README.md`, `knowledge/README.md`, `topics/README.md`, `sources/README.md`).

---

## Common `SKILL.md` shape (read before Tasks 6 to 12)

Every skill in this plan shares one shape. State it once here; each task below gives only what differs.

```markdown
---
name: <skill-name>
description: <trigger description, third person, states when to use this skill and what it produces>
---

# <Title>

## Overview

<One or two sentences: what this skill produces and from what input, referencing the workflow doc by name.>

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/<workflow-file>.md` (this skill's Procedure, Input, Output, and Stop conditions)
- `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract` (taxonomy validation, dedup check, confirm-before-write, stop-condition routing, and chaining rules that apply to every step below)
- <any workflow-doc-specific required references, listed by path>

## Input

<How to gather Input: prefer an explicit argument when the user gives one; otherwise infer from the current conversation. List exactly what fields are needed, matching the workflow doc's "Input" section. If required Input is missing after checking both sources, ask for it rather than guessing.>

## Procedure

Follow `<workflow-file>.md`'s Procedure exactly, applying the Skill execution contract at each taxonomy-value or new-record decision point.

## Output

Write to `docs/100_brand/marketing/content/<collection>/<slug>.md` using `docs/100_brand/assets/templates/<template-dir>/<template-file>.md`. Derive `<slug>` by lowercasing the title and hyphenating. Confirm before writing, per the Skill execution contract.

## Stop conditions

<Restate this workflow doc's Stop conditions verbatim, plus which skill resolves each one.>

## Next step

<Name the next skill in the pipeline this Output typically feeds, and what Input it would need. State "none, this is a terminal step" where true.>

## Validation

<An `rg` command against the just-written file checking for its template's required section headers, mirroring the checks in Tasks 2 to 4.>
```

---

## Task 6: `to-knowledge` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 2, 5.

**Files:**
- Create: `.claude/skills/to-knowledge/SKILL.md`

### What to build

Fill the common shape for `capture-knowledge.md`:

- **name:** `to-knowledge`
- **description:** `Use when the user wants to capture raw material (an observation, experience, research finding, opinion, idea, question, lesson, process, framework, or evidence) from the current conversation or a supplied prompt into a reusable Knowledge record. Also trigger on "capture this as knowledge," "turn this into knowledge," or "add this to the brand's knowledge base." Writes Knowledge (and optionally Source) records under docs/100_brand/marketing/content/knowledge/.`
- **Overview:** produces one Knowledge record, and optionally one Source record, from raw material with its available context and provenance.
- **Required references:** `capture-knowledge.md`; the contract section; `../knowledge/README.md`; `../sources/README.md`; `../../../identity/README.md` (truthfulness, evidence, privacy, scars-not-wounds).
- **Input:** raw material (from an explicit argument or the current conversation), its origin, date or timeframe if known, access conditions, and relevant context. If the origin cannot be identified at all, treat this as a Stop condition, not a guess.
- **Output collection/template:** `docs/100_brand/marketing/content/knowledge/`, using `docs/100_brand/assets/templates/knowledge/knowledge-record.md`. If a Source record is also warranted (procedure step 2), write it to `docs/100_brand/marketing/content/sources/` using `docs/100_brand/assets/templates/sources/source-record.md` first, then link it from the Knowledge record's Source field.
- **Stop conditions (from the doc):** stop without creating Knowledge when the origin cannot be represented honestly, the material is only an unsupported claim, or privacy/confidentiality constraints prevent safe internal capture. Preserve as an explicitly labeled unknown when it may become usable after verification later. No upstream skill resolves this; it is a hard stop pending better material.
- **Next step:** `to-topic`, once one or more related Knowledge records exist to support a Topic premise.
- **Validation command:** `rg -n '^---$|^type: knowledge$|^## Header|^## Reusable synthesis|^## Provenance|^## Evidence boundary|^## Validation' docs/100_brand/marketing/content/knowledge/<slug>.md`

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-knowledge/SKILL.md` and matches the common shape.
- [ ] `description` frontmatter is a single line, third person, and names concrete trigger phrases (no vague "helps with knowledge" wording).
- [ ] Every path referenced in the file resolves to a real file created in Tasks 1 to 5.

---

## Task 7: `to-topic` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 3, 5, 6 (references `to-knowledge` as its typical upstream).

**Files:**
- Create: `.claude/skills/to-topic/SKILL.md`

### What to build

Fill the common shape for `develop-topic.md`:

- **name:** `to-topic`
- **description:** `Use when the user wants to develop a reusable Topic (subject or idea) from one or more existing Knowledge records. Also trigger on "turn this knowledge into a topic," "develop a topic," or "what should I plan content around." Writes Topic records under docs/100_brand/marketing/content/topics/.`
- **Overview:** produces one Topic record from one or more related Knowledge records with their supporting Sources and evidence boundaries.
- **Required references:** `develop-topic.md`; the contract section; `../topics/README.md`; `../../../strategy/README.md`; `../../../audience/README.md`; `../../../identity/README.md`.
- **Input:** one or more Knowledge records (explicit links, or identified from the conversation), the primary Theme and Topic Mode candidates, and the relevant Audience Segment.
- **Output collection/template:** `docs/100_brand/marketing/content/topics/`, using `docs/100_brand/assets/templates/topics/topic-record.md`.
- **Stop conditions (from the doc):** stop and return to `to-knowledge` when support is insufficient. Stop without creating a Topic when the subject is outside the Brand's strategic constraints, depends on private or customer-sensitive material that cannot be safely generalized, or would publish a wound rather than a scar.
- **Next step:** `to-blueprint`, once the Topic is ready (has a premise, strategic fit, and credibility boundary).
- **Validation command:** `rg -n '^---$|^type: topic$|^## Header|^## Premise|^## Strategic fit|^## Supporting Knowledge|^## Credibility boundary|^## Open questions|^## Validation' docs/100_brand/marketing/content/topics/<slug>.md`

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-topic/SKILL.md` and matches the common shape.
- [ ] Explicitly states the "stop and return to `to-knowledge`" routing (not just a generic stop).
- [ ] Every referenced path resolves to a real file.

---

## Task 8: `to-blueprint` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 5, 7.

**Files:**
- Create: `.claude/skills/to-blueprint/SKILL.md`

### What to build

Fill the common shape for `develop-blueprint.md`:

- **name:** `to-blueprint`
- **description:** `Use when the user wants to turn an approved Topic into a Topic-specific communication plan: objective, audience, angle, pattern, structure, hook, CTA, proof, and constraints. Also trigger on "plan this topic," "develop a blueprint," or "what's the angle for this." Writes Blueprint records under docs/100_brand/marketing/content/blueprints/.`
- **Overview:** produces one Blueprint from one Topic, its supporting Knowledge and Sources, a primary Audience Segment, and any Asset constraints.
- **Required references:** `develop-blueprint.md`; the contract section; `../blueprints/README.md`; `../../../strategy/README.md`; `../../../audience/README.md`; `../../../identity/README.md`; for short-form video specifically, `../../../assets/templates/blueprints/short-form-video.md`.
- **Input:** one Topic record, its Theme and Topic Mode, and (for short-form video) the intended Content Pattern.
- **Output collection/template:** `docs/100_brand/marketing/content/blueprints/`, using `docs/100_brand/assets/templates/blueprints/short-form-video.md` when the target is short-form video. State explicitly that no other Blueprint template exists yet; if the user needs a non-short-form-video Blueprint, stop and say a template does not exist for that format rather than improvising one (matches the design spec's "explicitly out of scope" item).
- **Stop conditions (from the doc):** stop and return to Knowledge capture when the proof is missing, the claim cannot be supported, or the Topic does not fit the Brand's strategic constraints.
- **Next step:** `to-hooks`, to select the opening Visual/Verbal Hook Type pairing for this Blueprint.
- **Validation command:** `rg -n '^---$|^## Brief|^## Opening choices|^## Story plan|^## Validation' docs/100_brand/marketing/content/blueprints/<slug>.md`

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-blueprint/SKILL.md` and matches the common shape.
- [ ] States the single-template limitation (short-form video only) as an explicit constraint, not silently.
- [ ] Every referenced path resolves to a real file.

---

## Task 9: `to-hooks` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 8.

**Files:**
- Create: `.claude/skills/to-hooks/SKILL.md`

### What to build

Fill the common shape for `generate-hook-options.md`. This skill does not create a new record file; it edits the Blueprint's "Opening choices" section in place, so the common shape's Output/Validation parts are adapted:

- **name:** `to-hooks`
- **description:** `Use when the user wants to generate and select Visual Hook Type / Verbal Hook Type opening pairings for an approved short-form Blueprint, using the Quilt Method. Also trigger on "give me hook options," "what's the opening for this," or "pick a hook." Edits the Opening choices section of an existing Blueprint record.`
- **Overview:** produces one selected opening pair (plus discarded options and rejection reasons) recorded on an already-approved Blueprint.
- **Required references:** `generate-hook-options.md`; the contract section; `../../../ONTOLOGY.md` (Visual Hook Type, Verbal Hook Type, Hook usage conditions); `../sources/colin-and-samir-short-form-anatomy.md`; `../knowledge/short-form-anatomy.md`; `../../../identity/README.md`; `../../../strategy/README.md`.
- **Input:** one approved Blueprint record (path), its Topic, audience promise, evidence boundary, available Assets, and any hook-type restrictions already on the Blueprint.
- **Output:** edit the target Blueprint's `## Opening choices` section in place, filling Visual Hook Type, Scroll Stopper / first frame, visual intent, Verbal Hook Type, open loop, and spoken/on-screen hook. Generate at least 3 pairings before narrowing to one, per the doc's Procedure. Confirm the selected pairing (and a short note on the rejected ones) before editing the file, per the contract.
- **Stop conditions:** reject any option that requires invented footage, unsupported facts, customer outcomes, celebrity likeness, or off-brand trend participation (Procedure step 3); apply the ontology's hook usage conditions (evidence-required, editorial-review-required) before final selection.
- **Next step:** `to-script`, to draft the full Script Asset from this Blueprint's now-selected opening.
- **Validation command:** `rg -n '^## Opening choices' -A 8 docs/100_brand/marketing/content/blueprints/<slug>.md` and confirm the six bracketed fields are filled, not still `[...]`.

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-hooks/SKILL.md`.
- [ ] Explicitly states it edits an existing Blueprint rather than creating a new record (this is the one skill of the seven that does not write a new file).
- [ ] Lists the "generate at least 3, then narrow to 1" requirement from the doc's Procedure, not just the end state.

---

## Task 10: `to-script` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 5, 9.

**Files:**
- Create: `.claude/skills/to-script/SKILL.md`

### What to build

Fill the common shape for `generate-short-form-script.md`:

- **name:** `to-script`
- **description:** `Use when the user wants to turn an approved short-form Blueprint (with its selected hooks) into a full Script Asset: shotlist, voiceover, and production cues. Also trigger on "write the script," "draft the shotlist," or "turn this blueprint into a script." Writes Script Assets under docs/100_brand/assets/scripts/.`
- **Overview:** produces one Script Asset from one approved Blueprint (including its selected hooks from `to-hooks`), linked Sources, and available Assets.
- **Required references:** `generate-short-form-script.md`; the contract section; `../../../assets/templates/scripts/short-form-stop-hook-payoff.md`; `../../../identity/README.md`; `../../../assets/README.md`.
- **Input:** one approved Blueprint (with Pattern, Purpose, Structure, and hook types already selected via `to-hooks`), its linked Sources, and available Assets.
- **Output collection/template:** `docs/100_brand/assets/scripts/`, using `docs/100_brand/assets/templates/scripts/short-form-stop-hook-payoff.md`, matching the naming pattern already used at `docs/100_brand/assets/scripts/the-bet.md`.
- **Restriction (from the doc's Taxonomy contract):** writes no new taxonomy values; the Script repeats the Blueprint's selected values for traceability. A Script may not change a Blueprint's Pattern, Structure, or hook types; if those need to change, stop and route back to `to-blueprint` rather than editing them here.
- **Stop conditions:** do not invent claims, evidence, footage, quotations, outcomes, personal experiences, or customer details (Prohibitions section); if real proof is missing, stop and route back to `to-knowledge`.
- **Next step:** `to-validate`, before this Script is treated as production-ready.
- **Validation command:** `rg -n '^---$|^## Header|^## Scroll Stopper|^## Development|^## Payoff|^## Script checks' docs/100_brand/assets/scripts/<slug>.md`

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-script/SKILL.md`.
- [ ] States the "may not change Pattern/Structure/hook types" restriction explicitly, with the stop-and-route-to-`to-blueprint` behavior.
- [ ] Every referenced path resolves to a real file.

---

## Task 11: `to-validate` skill

**Type:** AFK.

**Blocked by:** Tasks 1, 10.

**Files:**
- Create: `.claude/skills/to-validate/SKILL.md`

### What to build

Fill the common shape for `validate-script.md`. Like `to-hooks`, this skill does not create a record; it produces a verdict.

- **name:** `to-validate`
- **description:** `Use when the user wants to check whether a drafted Script is ready for production: promise/payoff fit, source coverage for every claim, hook usage conditions, asset availability, and brand voice rules. Also trigger on "validate this script," "is this ready to shoot," or "check this against brand rules." Produces a pass/revise/return verdict on an existing Script Asset.`
- **Overview:** checks one Script Asset against its primary Blueprint, linked Sources, related Assets, and intended Channel.
- **Required references:** `validate-script.md`; the contract section; `../../../ONTOLOGY.md` (Script relationship, Publication Format, hook taxonomies, Hook usage conditions); `../../../identity/README.md`; `../../../assets/templates/scripts/short-form-stop-hook-payoff.md`.
- **Input:** one Script Asset (path), its primary Blueprint, linked Sources, and the intended Publication format and Channel.
- **Checks to run** (from the doc, run all 5 and report each): opening promise explicit and Payoff fulfills it; every fact/statistic/quotation/outcome has a suitable linked Source; chosen hook types meet their evidence or editorial-review conditions from `ONTOLOGY.md`; every proposed visual/audio asset exists, is obtainable, or is explicitly marked a planned capture; the Script follows documentary restraint, observation-over-preaching, scars-not-wounds, and makes no unsupported performance claims.
- **Output:** one of three verdicts, stated plainly, never silently defaulted: (a) ready for production, (b) returned for revision with the specific gaps named per failed check, (c) returned to `to-knowledge` if evidence is insufficient. Restriction: writes no taxonomy values, only the verdict and gaps; reject outright any Script using an undefined taxonomy value or bypassing a required evidence/editorial-review condition.
- **Next step:** none if verdict (a); `to-script` (revise in place) for verdict (b); `to-knowledge` for verdict (c).
- **Validation command:** none (no file written on pass; if the Script itself is edited during revision, reuse the `to-script` validation command against it).

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-validate/SKILL.md`.
- [ ] Lists all 5 checks from the doc individually, not summarized into one line.
- [ ] States all 3 possible verdicts and where each one routes.

---

## Task 12: `to-taxonomy` skill

**Type:** AFK.

**Blocked by:** Task 1 (this is the skill every other skill's Stop condition can name, so it should exist before Task 13's final pass, but has no other file dependency).

**Files:**
- Create: `.claude/skills/to-taxonomy/SKILL.md`

### What to build

Fill the common shape for `propose-taxonomy-addition.md`. This skill edits `ONTOLOGY.md` directly rather than writing a new record.

- **name:** `to-taxonomy`
- **description:** `Use when a candidate Content Pattern, Content Purpose, Narrative Structure, Hook Type, Publication Format, Knowledge Kind, Topic Mode, or other controlled taxonomy value is needed but is not already defined in ONTOLOGY.md. Also trigger when another skill's Stop condition names this skill, or on "add a new [taxonomy value] to the ontology," "propose a taxonomy addition." Edits the taxonomy tables in docs/100_brand/ONTOLOGY.md after explicit approval; never adds a value silently.`
- **Overview:** turns a candidate controlled value that does not fit any existing `ONTOLOGY.md` entry into either an approved ontology update or a rejected, non-canonical proposal.
- **Required references:** `propose-taxonomy-addition.md`; `../../../ONTOLOGY.md` (full canonical taxonomy list for the target entity); `../sources/README.md`; `../../../identity/README.md`; `../../../strategy/README.md`.
- **Input:** the candidate value's name, the entity it attaches to (Knowledge, Topic, or Blueprint, per `ONTOLOGY.md`'s taxonomy tables), a definition, and why none of the existing values fit.
- **Procedure (from the doc):** record the proposed name, definition, intended entity, and why existing values do not fit; link at least one Source or verified internal example; define usage conditions including evidence and editorial-review requirements where relevant; obtain explicit approval before adding the value to the canonical ontology.
- **Output:** on approval, edit the matching row-set in the relevant `ONTOLOGY.md` taxonomy table (for example the "Blueprint taxonomies" or "Content and delivery taxonomies" table), adding the new value, its definition, and its provenance link, keeping the existing table format. On rejection, do not edit `ONTOLOGY.md`; keep the proposal only as local conversation context, per the doc's Output.
- **Restriction:** never treat a proposed value as selectable by another skill before this approval step completes. Skills must not silently add canonical taxonomy values.
- **Stop conditions:** none of its own beyond "no approval yet"; approval is a hard gate, not a default.
- **Next step:** whichever skill originally hit the missing-taxonomy-value stop condition, re-run now that the value exists.
- **Validation command:** `rg -n '<new value>' docs/100_brand/ONTOLOGY.md` should match the new row after approval, and should match nothing before it.

### Acceptance criteria

- [ ] File exists at `.claude/skills/to-taxonomy/SKILL.md`.
- [ ] States plainly that it edits `ONTOLOGY.md` itself, unlike every other skill in this plan.
- [ ] States the "approval is a hard gate" rule explicitly (no silent additions).

---

## Task 13: Final verification and changelog

**Type:** AFK, but do a full read-through, not just the automated checks.

**Blocked by:** Tasks 1 to 12, all complete.

**Files:**
- Modify: `docs/100_brand/CHANGELOG.md` (append)

### What to build

1. Run, and confirm clean output for, each `rg` validation command listed in Tasks 1 to 12.
2. Run `find .claude/skills -maxdepth 2 -name SKILL.md | sort` and confirm exactly 7 results: `to-blueprint`, `to-hooks`, `to-knowledge`, `to-script`, `to-taxonomy`, `to-topic`, `to-validate`.
3. Read all 7 `SKILL.md` files back to back and confirm every cross-reference between them (the "Next step" pointers) names a skill that actually exists among the 7, and every file path they reference resolves.
4. Append one entry to `docs/100_brand/CHANGELOG.md`, in the same format as the existing entries (Decision / Rationale / Files touched / Source / Implementation), dated 2026-08-27, summarizing: seven project-local skills built to execute the content workflow docs, three new upstream templates (Knowledge, Topic, Source) added to close a template gap the review surfaced, and a shared skill execution contract added to `workflows/README.md`.

### Acceptance criteria

- [ ] All `rg` checks from Tasks 1 to 12 pass.
- [ ] Exactly 7 `SKILL.md` files exist, named correctly.
- [ ] No dangling cross-reference between skills.
- [ ] `docs/100_brand/CHANGELOG.md` has one new entry at the top (or wherever the file's existing ordering convention places new entries), following the established Decision/Rationale/Files touched/Source/Implementation shape.
