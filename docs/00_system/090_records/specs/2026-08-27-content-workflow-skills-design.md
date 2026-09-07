# Content Workflow Skills Design

**Date:** 2026-08-27
**Method:** Synthesis from a `/grill-me` session on turning the seven `docs/100_brand/marketing/content/workflows/*.md` docs into orchestrating Claude Code skills.
**Status:** Approved by Daniel. Pending implementation per the companion plan.
**Companion:** implementation steps live at `docs/100_brand/plans/2026-08-27-content-workflow-skills-implementation.md`.

---

## Problem statement

`docs/100_brand/marketing/content/workflows/` already holds seven rigorously specified workflow docs (Capture Knowledge, Develop Topic, Develop Blueprint, Generate Hook Options, Generate Short-Form Script, Validate Script, Propose Taxonomy Addition). Each one has Required references, a Taxonomy contract (reads/writes against the controlled vocabularies in `ONTOLOGY.md`, with an explicit escape hatch to Propose Taxonomy Addition for missing values), Input, Procedure, Output, and Stop conditions. `workflows/README.md` already says these "define the minimum behavior for future content-generation skills. They are not executable skills themselves."

No skill exists yet to execute them. Daniel wants project skills, modeled on Mat Pocock's skills repo, that orchestrate gathering the required Input and following each documented Procedure, rather than freeform prompting each time.

A parallel plugin, `skillstack`, already ships similarly named skills (`brand-init`, `brand-script`, `to-script`, `grill-my-hook`, `perform-audit`, `brand-audit`, `brand-post`, `brand-script-review`) but hardcodes a generic `docs/brand/` layout. `LIBRARY_MAP.md` explicitly retires that unnumbered path for this repo, and `skillstack` has no awareness of this repo's ontology (Knowledge Kind, Topic Mode, evidence boundaries, taxonomy contracts). It is out of scope: not modified, not depended on.

While scoping this, the review surfaced a second, smaller gap: three of the seven entities involved (Knowledge, Topic, Source) have no fill-in-blank template, unlike Blueprint (`assets/templates/blueprints/short-form-video.md`) and Script (`assets/templates/scripts/short-form-stop-hook-payoff.md`). `assets/templates/README.md` states "a skill must use the template's required checks before producing a record," so this has to be closed before the skills that write those record types can work correctly.

---

## Decisions locked

1. **Location.** New skills are project-local to this repo, at `.claude/skills/<name>/SKILL.md`. The repo has no `.claude/skills/` directory yet. `skillstack` is untouched.

2. **Scope.** One skill per workflow doc, all seven, in this first pass: `to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, `to-validate`, `to-taxonomy`.

3. **Naming.** The `to-X` mnemonic style Daniel proposed, extended consistently, rather than mirroring the workflow filenames verbatim.

4. **Missing templates.** Author three new generic templates (Knowledge, Topic, Source) under `docs/100_brand/assets/templates/`, following the existing Blueprint/Script template shape (frontmatter + fill-in-blank sections + validation checklist). Blueprint keeps its current short-form-video-only template; no change there. Blueprint is not a template "for" Knowledge/Topic/Source: per `ONTOLOGY.md`, a Blueprint is a Topic-specific communication plan that reads Knowledge/Topic/Source as input and points toward Publications. The new templates are separate, one per upstream entity.

5. **Contract rigor.** Each skill enforces its workflow doc's Taxonomy contract and dedup check for real: it reads `ONTOLOGY.md`'s controlled tables and validates every proposed value against them, and it searches the target collection directory for materially duplicative existing records before creating a new one. This is what makes it orchestration rather than a template-filler.

6. **Confirm before write.** Every skill presents the drafted record (target path, chosen taxonomy values, key content) and waits for explicit approval before creating or editing a file.

7. **Pipeline chaining.** On success, a skill names the next applicable skill in the pipeline and what it would need as Input (for example, "run `to-topic` next with this Knowledge record"). It never invokes the next skill automatically.

8. **Shared contract.** The taxonomy-validation and dedup-check mechanic is written once, as a new "Skill execution contract" section in `docs/100_brand/marketing/content/workflows/README.md` (which already exists to define behavior for future content-generation skills), and every skill's `SKILL.md` points to it instead of restating it.

---

## Explicitly out of scope for this pass

- Modifying or extending the `skillstack` plugin.
- A generic (non-short-form-video) Blueprint template. Current production is 100% short-form/cinematic-vlog per `marketing/content/README.md`; a second Blueprint template is speculative until another Content Pattern or Publication Format actually ships.
- Automatic pipeline execution (a skill invoking the next skill for you). Deferred; may revisit once the seven skills have been used in practice.
- A record template or dedicated output path for `to-taxonomy`'s own working notes. Per `propose-taxonomy-addition.md`, its Output is either an approved edit directly to `ONTOLOGY.md`'s taxonomy tables or a rejected proposal kept only as local conversation context, so no new file type is needed for it.
