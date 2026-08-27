---
name: to-taxonomy
description: Use when a candidate Content Pattern, Content Purpose, Narrative Structure, Hook Type, Publication Format, Knowledge Kind, Topic Mode, or other controlled taxonomy value is needed but is not already defined in ONTOLOGY.md. Also trigger when another skill's Stop condition names this skill, or on "add a new [taxonomy value] to the ontology," "propose a taxonomy addition." Edits the taxonomy tables in docs/100_brand/ONTOLOGY.md after explicit approval; never adds a value silently.
---

# To Taxonomy

## Overview

This skill turns a candidate controlled value that does not fit any existing entry in `docs/100_brand/ONTOLOGY.md` into either an approved ontology update or a rejected, non-canonical proposal, following `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`.

Two things make this skill different from every other skill in `.claude/skills/`:

1. **It edits `docs/100_brand/ONTOLOGY.md` directly.** `to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, and `to-validate` each write or edit their own Content record under `docs/100_brand/marketing/content/`. This skill does not write a Content record at all: on approval, its entire Output is an edit to the canonical taxonomy tables inside `docs/100_brand/ONTOLOGY.md` itself.
2. **Approval is a hard gate, not a default.** No candidate value is ever added to `docs/100_brand/ONTOLOGY.md` without an explicit, affirmative approval captured in the current conversation. This holds even when the case for the new value looks obviously correct, even when the requesting skill's Stop condition made the need self-evident, and even when a Source or internal example is already linked. Absent that approval, the correct Output is no edit at all, per `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Output: "Skills must not silently add canonical taxonomy values."

This skill is the escape hatch named in `docs/100_brand/marketing/content/workflows/README.md`'s Skill execution contract, step 2: "If a needed value is not in the table, stop and name `to-taxonomy` as the next step." It is also the one skill that contract explicitly carves out as an exception: "`to-taxonomy` is the exception these route to when a controlled value is missing, not a follower of this contract." Every other skill validates the taxonomy contract, checks for duplicates, confirms before writing, honors stop conditions, and suggests (without chaining) the next skill, all per that shared contract. This skill does not inherit any of that; its own four-step Procedure (below) is the complete contract it follows.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md` (this skill's Procedure, Input, and Output)
- `docs/100_brand/ONTOLOGY.md` (the full canonical taxonomy list for the target entity, and the exact table structure to edit)
- `docs/100_brand/marketing/content/sources/README.md` (what a Source record is, for the provenance-link requirement)
- `docs/100_brand/identity/README.md` (voice, evidence, and brand-fit boundaries the new value must respect)
- `docs/100_brand/strategy/README.md` (positioning, Themes, and editorial constraints the new value must respect)

Do not proceed from memory of a prior run; re-read `docs/100_brand/ONTOLOGY.md` at run time, since its tables may have changed since the last time this skill ran.

Note: unlike the other six skills, this skill does not also read or link `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract`. That contract explicitly names this skill as its exception, so citing it here as a doc this skill "follows" would misstate the relationship. Read the contract section only to understand how upstream skills describe handing off to this one, not as a procedure this skill itself executes.

## Input

Gather all of the following before proceeding. If any item is missing, ask for it; do not guess or infer a definition on the requester's behalf.

- **The candidate value's name.**
- **The entity it attaches to**: Knowledge, Topic, or Blueprint, matched against the "Applied to" column of the relevant table in `docs/100_brand/ONTOLOGY.md` (for example, a Hook Type attaches to Blueprint; a Knowledge Kind attaches to Knowledge).
- **A definition** of what the value means and when it applies.
- **Why none of the existing values fit**: which existing values in that taxonomy's row were considered and rejected, and why.
- **Which skill and which specific run originally hit the missing-taxonomy-value stop condition.** Capture this concretely: the skill name (for example `to-blueprint`), and enough detail about that specific run to make the handoff back meaningful to a fresh session later, such as the target Topic, Blueprint, or Script file path it was operating on, or a short summary of the in-progress task. "To-blueprint needs a new Content Pattern" is not enough on its own; "to-blueprint, drafting a Blueprint for the Topic at docs/100_brand/marketing/content/topics/<slug>.md, needs a Content Pattern value for a serialized-drop format" is. Without this, the Next step below has nothing concrete to hand back to.

If the requester cannot supply the blocked skill and run, ask for it before proceeding; do not substitute a generic "re-run whatever needed this."

## Procedure

Follow `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Procedure exactly:

1. **Record the proposal.** State the proposed name, definition, intended entity, and why existing values do not fit, using the Input gathered above.
2. **Link provenance.** Link at least one Source record from `docs/100_brand/marketing/content/sources/` or a verified internal example (an existing Knowledge, Topic, Blueprint, or Publication record) that supports the proposed value. A proposal with no linked Source or verified example is incomplete; do not proceed to approval without one.
3. **Define usage conditions.** State any evidence requirements or editorial-review requirements the value carries, following the existing pattern in `docs/100_brand/ONTOLOGY.md`'s "Hook usage conditions" table (for example, values built on a statistic or quotation carry an evidence requirement; values touching trends, public figures, or exaggeration carry an editorial-review requirement). Not every value needs a usage condition; state explicitly when none applies.
4. **Obtain explicit approval.** Present the full proposal (name, entity, definition, rejected-alternatives reasoning, provenance link, usage conditions, and the exact edit described in Output below) and wait for an explicit, affirmative approval in the current conversation. Silence or an unrelated reply is not approval. Do not proceed to Output without it.

## Output

**On approval:** edit `docs/100_brand/ONTOLOGY.md` directly. No other file changes.

First, locate the correct table and row:

- If the value belongs to an existing taxonomy (its taxonomy name already has a row in the "Blueprint taxonomies," "Content and delivery taxonomies," or "Supporting taxonomies" table), find that row by matching the "Taxonomy" column (for example "Content Pattern") and the "Applied to" column (for example "Blueprint").
- If the value is a Hook Type carrying a usage condition, also locate the matching row (or add a new row) in the separate "Hook usage conditions" table.

Then edit within the existing row-and-column structure without disturbing other rows:

- **Values column**: append the new value's name to the end of the existing comma-separated list in that cell, keeping the existing `, ` separator style. Do not reorder the existing values.
- **Definition column** (present on the "Blueprint taxonomies" and "Content and delivery taxonomies" tables, absent on "Supporting taxonomies"): these tables define the taxonomy as a whole in one cell, not one definition per value. Follow the file's existing pattern of embedding a short per-value usage note in that shared cell when a value needs disambiguation (see the existing Content Pattern row's "Use `Story` for storytelling and `Educational` for explanatory teaching" clause) rather than adding a new column. Add the new value's definition and provenance link the same way: a short clause appended to the cell, citing the linked Source or internal example by its file path (for example "(see docs/100_brand/marketing/content/sources/<slug>.md)").
  For a row in the "Supporting taxonomies" table (Audience Relationship, Asset Type, Media Type, Metric Name; no Definition column exists there): append only to the Values cell, per the bullet above. Do not add a Definition column, and do not stuff the definition or provenance link into the Values cell. The definition and provenance link gathered in Input/Procedure steps 1-2 are not persisted into `ONTOLOGY.md` for this table; they exist only as the approved proposal in the current conversation, since this table's format has no field for them.
- **Hook usage conditions table**: if step 3 of the Procedure found an evidence or editorial-review requirement, append the new value's name to the "Hook types" cell of the matching existing "Condition" row. If neither existing condition fits, add a new row to that table following its existing two-column format, placed after the existing rows.
- **No existing row matches at all** (the value is a genuinely new taxonomy category, not a new value inside an existing one): add a new row to the appropriate table, following that table's existing column order, placed at the bottom of that table's rows. Do not reorder or renumber existing rows. Choose among "Blueprint taxonomies," "Content and delivery taxonomies," and "Supporting taxonomies" by matching the new taxonomy's entity (Knowledge, Topic, Blueprint, Content, or Publication) against each table's existing "Applied to" values, and by whether the value is likely to need a per-value disambiguation note (favor a table with a Definition column when it is, "Supporting taxonomies" when it is not).

Preserve the file's existing minimal single-space pipe formatting (`| cell | cell |`); these tables are not padded to visually align columns, so do not introduce column padding that the rest of the table lacks.

**On rejection, or when approval is never given:** do not edit `docs/100_brand/ONTOLOGY.md`. Keep the proposal only as local conversation context, per `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Output. Do not write it anywhere else, and do not treat the proposed value as selectable by any other skill.

## Stop conditions

Approval is a hard gate, not a default: this skill has no stop condition of its own beyond "no approval yet." If the Procedure reaches step 4 and explicit approval is not given in the current conversation, whether because it is refused, deferred, or simply never addressed, the correct outcome is no ontology edit. Do not add the value "provisionally," "for now," or on the assumption that approval is likely; there is no silent or partial addition.

## Next step

Hand off back to whichever skill and run were captured in Input as originally blocked. Name that skill explicitly (for example "`to-blueprint`, resume the Blueprint draft for `docs/100_brand/marketing/content/topics/<slug>.md`") and confirm the new value now appears in `docs/100_brand/ONTOLOGY.md` before that skill re-validates its taxonomy contract and continues. If no specific blocked skill/run was captured at Input, say so plainly rather than inventing one.

## Validation

```
rg -n '^\| <Taxonomy name> \|.*<new value>' docs/100_brand/ONTOLOGY.md
```

Anchor on the literal markdown row prefix for the specific taxonomy (for example `| Content Pattern |`), not a bare search for `<new value>`: an unanchored match can be satisfied by an unrelated Definition clause, a mermaid diagram class name, or a substring of an existing word, none of which confirm the edit landed in the right row. This should match nothing before approval, and should match the new entry, in the correct taxonomy's row, after approval. If a usage condition was also added, separately confirm it with `rg -n '^\| <Condition> \|.*<new value>' docs/100_brand/ONTOLOGY.md` against the "Hook usage conditions" table.
