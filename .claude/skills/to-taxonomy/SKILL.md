---
name: to-taxonomy
description: Use when a candidate Content Pattern, Content Purpose, Narrative Structure, Hook Type, Publication Format, Knowledge Kind, Topic Mode, Theme, Audience Segment, Channel, or other controlled taxonomy value is needed but is not already defined in its owning canonical context. Also trigger when another skill's Stop condition names this skill, or on "add a new [taxonomy value] to the ontology," "propose a taxonomy addition." Edits docs/100_brand/ONTOLOGY.md, or the Theme, Audience Segment, or Channel registry that actually owns the candidate, after explicit approval; never adds a value silently.
---

# To Taxonomy

## Overview

This skill turns a candidate controlled value that does not fit any existing entry in its owning canonical context into either an approved update to that context or a rejected, non-canonical proposal, following `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`. The owning canonical context is `docs/100_brand/ONTOLOGY.md` for most taxonomies, but the Theme, Audience Segment, or Channel registry for those three specifically (see Output below).

Two things make this skill different from every other skill in `.claude/skills/`:

1. **It edits the owning canonical context directly, not always `docs/100_brand/ONTOLOGY.md`.** `to-knowledge`, `to-topic`, `to-blueprint`, `to-hooks`, `to-script`, and `to-validate` each write or edit their own Content record under `docs/100_brand/marketing/content/`. This skill does not write a Content record at all: on approval, its entire Output is an edit to whichever context actually owns the candidate's meaning. Per `docs/100_brand/ONTOLOGY.md`'s "Entities versus taxonomies" section: "Controlled vocabularies remain with the context that owns their meaning. This ontology owns Content taxonomies. Strategy owns Theme, Audience owns Audience Segment, and Channels owns Channel." For a Knowledge Kind, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook Type, Publication Format, or any other genuinely new taxonomy category not owned by one of those three registries, the edit target is `docs/100_brand/ONTOLOGY.md`. For a Theme, the edit target is the Theme registry in `docs/100_brand/strategy/README.md`. For an Audience Segment, it is the Audience Segment registry in `docs/100_brand/audience/README.md`. For a Channel, it is the Channel registry in `docs/100_brand/channels/README.md`. Do not default to `ONTOLOGY.md` for a Theme, Audience Segment, or Channel candidate; that is no longer the owning context for those three.
2. **Approval is a hard gate, not a default.** No candidate value is ever added to its owning canonical context, whether `docs/100_brand/ONTOLOGY.md` or one of the three registries, without an explicit, affirmative approval captured in the current conversation. This holds even when the case for the new value looks obviously correct, even when the requesting skill's Stop condition made the need self-evident, and even when a Source or internal example is already linked. Absent that approval, the correct Output is no edit at all, per `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Output: "Skills must not silently add canonical values."

This skill is the escape hatch named in `docs/100_brand/marketing/content/workflows/README.md`'s Skill execution contract, step 2: "If a needed value is not in the table, stop and name `to-taxonomy` as the next step." It is also the one skill that contract explicitly carves out as an exception: "`to-taxonomy` is the exception these route to when a controlled value is missing, not a follower of this contract." Every other skill validates the taxonomy contract, checks for duplicates, confirms before writing, honors stop conditions, and suggests (without chaining) the next skill, all per that shared contract. This skill does not inherit any of that; what makes it self-contained instead is its own four-step Procedure (below), together with Output's four-way routing logic and the rules and rationale carried in the Work Item tracking section.

## Required references

Before acting, read:

- `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md` (this skill's Work Item contract, Procedure, Input, and Output)
- `docs/100_brand/ONTOLOGY.md` (the full canonical taxonomy list and exact table structure to edit for every entity except Theme, Audience Segment, and Channel; also its "Entities versus taxonomies" section, which states which context owns each vocabulary)
- `docs/100_brand/strategy/README.md`, `docs/100_brand/audience/README.md`, and `docs/100_brand/channels/README.md` (owner-specific registries when the candidate is a Theme, Audience Segment, or Channel; `docs/100_brand/strategy/README.md` also carries positioning and editorial constraints the new value must respect regardless of entity type)
- `docs/100_brand/marketing/content/work-items/README.md` (the Work Item identifier format and its required frontmatter and body)
- `docs/100_brand/marketing/content/sources/README.md` (what a Source record is, for the provenance-link requirement)
- `docs/100_brand/identity/README.md` (voice, evidence, and brand-fit boundaries the new value must respect)

Do not proceed from memory of a prior run; re-read `docs/100_brand/ONTOLOGY.md` at run time, since its tables may have changed since the last time this skill ran.

Note: unlike the other six skills, this skill does not also read or link `docs/100_brand/marketing/content/workflows/README.md#skill-execution-contract`. That contract explicitly names this skill as its exception, so citing it here as a doc this skill "follows" would misstate the relationship. Read the contract section only to understand how upstream skills describe handing off to this one, not as a procedure this skill itself executes.

## Input

Gather all of the following before proceeding. If any item is missing, ask for it; do not guess or infer a definition on the requester's behalf.

- **The candidate value's name.**
- **The entity it attaches to.** Either Knowledge, Topic, Blueprint, Publication, Script, or Work Item, matched against the "Applied to" column of the relevant table in `docs/100_brand/ONTOLOGY.md` (for example, a Hook Type attaches to Blueprint; a Knowledge Kind attaches to Knowledge, matching that workflow doc's own Input line: "a candidate Content Pattern, Purpose, Narrative Structure, Hook Type, Format, or other controlled value"). Note that Script has no "Applied to" value that is literally just "Script": it appears only inside the Publication Format row's compound value, "Publication; intended by Script and Script Template." Match on that compound value when the candidate's entity is Script. Or, when the candidate is itself a Theme, an Audience Segment, or a Channel, say so directly: these three have no "Applied to" column of their own since they are not `ONTOLOGY.md` rows at all, and the registry that owns them (`docs/100_brand/strategy/README.md`, `docs/100_brand/audience/README.md`, or `docs/100_brand/channels/README.md`) determines the Output target, per Overview above.
- **A definition** of what the value means and when it applies.
- **Why none of the existing values fit**: which existing values in that taxonomy's row (or registry) were considered and rejected, and why.
- **For an Audience Segment candidate only, a proposed Stable code.** A short code in the shape of the existing `B2`, `B1`, `A`, and `SERVICES` codes in the Audience Segment registry's "Stable code" column. Nothing else in this workflow supplies this value; gather it explicitly from the requester rather than inferring one from the Segment name.
- **Which skill and which specific run originally hit the missing-taxonomy-value stop condition.** Capture this concretely: the skill name (for example `to-blueprint`), and enough detail about that specific run to make the handoff back meaningful to a fresh session later, such as the target Topic, Blueprint, or Script file path it was operating on, or a short summary of the in-progress task. "To-blueprint needs a new Content Pattern" is not enough on its own; "to-blueprint, drafting a Blueprint for the Topic at docs/100_brand/marketing/content/topics/<slug>.md, needs a Content Pattern value for a serialized-drop format" is. Without this, the Next step below has nothing concrete to hand back to, and the Work Item's primary subject and predecessor (see Work Item tracking below) have nothing to point at.

If the requester cannot supply the blocked skill and run, ask for it before proceeding; do not substitute a generic "re-run whatever needed this."

## Procedure

Follow `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Procedure exactly:

1. **Record the proposal.** State the proposed name, definition, intended entity, and why existing values do not fit, using the Input gathered above.
2. **Link provenance.** Link at least one Source record from `docs/100_brand/marketing/content/sources/` or a verified internal example (an existing Knowledge, Topic, Blueprint, or Publication record) that supports the proposed value. A proposal with no linked Source or verified example is incomplete; do not proceed to approval without one.
3. **Define usage conditions.** State any evidence requirements or editorial-review requirements the value carries, following the existing pattern in `docs/100_brand/ONTOLOGY.md`'s "Hook usage conditions" table (for example, values built on a statistic or quotation carry an evidence requirement; values touching trends, public figures, or exaggeration carry an editorial-review requirement). Not every value needs a usage condition; state explicitly when none applies.
4. **Obtain explicit approval before adding the value to its owning canonical context.** Present the full proposal (name, entity, definition, rejected-alternatives reasoning, provenance link, usage conditions, and the exact edit described in Output below) and wait for an explicit, affirmative approval in the current conversation. Silence or an unrelated reply is not approval. Do not proceed to Output without it.

## Output

Before any table-editing mechanics apply, the first step is determining which of four targets the candidate belongs to, using the entity gathered in Input:

- **Theme** → the Theme registry table in `docs/100_brand/strategy/README.md`.
- **Audience Segment** → the Audience Segment registry table in `docs/100_brand/audience/README.md`.
- **Channel** → the Channel registry table in `docs/100_brand/channels/README.md`.
- **Everything else** (Knowledge Kind, Topic Mode, Content Pattern, Content Purpose, Narrative Structure, Visual Hook Type, Verbal Hook Type, Publication Format, or any genuinely new taxonomy category that is not one of the three registries above) → the matching taxonomy table in `docs/100_brand/ONTOLOGY.md`.

This follows `docs/100_brand/ONTOLOGY.md`'s own "Entities versus taxonomies" section directly. Do not default to `ONTOLOGY.md` for a Theme, Audience Segment, or Channel candidate; that is no longer the owning context for those three.

**On approval:** edit the target file identified above. No other file changes beyond the Work Item record (see Work Item tracking below).

### Target: `docs/100_brand/ONTOLOGY.md`

First, locate the correct table and row within `ONTOLOGY.md`:

- If the value belongs to an existing taxonomy (its taxonomy name already has a row in the "Blueprint taxonomies," "Content and delivery taxonomies," or "Supporting taxonomies" table), find that row by matching the "Taxonomy" column (for example "Content Pattern") and the "Applied to" column (for example "Blueprint").
- If the value is a Hook Type carrying a usage condition, also locate the matching row (or add a new row) in the separate "Hook usage conditions" table.

Then edit within the existing row-and-column structure without disturbing other rows:

- **Values column**: append the new value's name to the end of the existing comma-separated list in that cell, keeping the existing `, ` separator style. Do not reorder the existing values.
- **Definition column** (present on the "Blueprint taxonomies" and "Content and delivery taxonomies" tables, absent on "Supporting taxonomies"): these tables define the taxonomy as a whole in one cell, not one definition per value. Follow the file's existing pattern of embedding a short per-value usage note in that shared cell when a value needs disambiguation (see the existing Content Pattern row's "Use `Story` for storytelling and `Educational` for explanatory teaching" clause) rather than adding a new column. Add the new value's definition and provenance link the same way: a short clause appended to the cell, citing the linked Source or internal example by its file path (for example "(see docs/100_brand/marketing/content/sources/<slug>.md)").
  For a row in the "Supporting taxonomies" table (Audience Relationship, Asset Type, Media Type, Metric Name; no Definition column exists there): append only to the Values cell, per the bullet above. Do not add a Definition column, and do not stuff the definition or provenance link into the Values cell. The definition and provenance link gathered in Input/Procedure steps 1-2 are not persisted into `ONTOLOGY.md` for this table; they exist only as the approved proposal in the current conversation, since this table's format has no field for them.
- **Hook usage conditions table**: if step 3 of the Procedure found an evidence or editorial-review requirement, append the new value's name to the "Hook types" cell of the matching existing "Condition" row. If neither existing condition fits, add a new row to that table following its existing two-column format, placed after the existing rows.
- **No existing row matches at all** (the value is a genuinely new taxonomy category, not a new value inside an existing one, but still one `ONTOLOGY.md` itself owns rather than one of the three registries): add a new row to the appropriate table, following that table's existing column order, placed at the bottom of that table's rows. Do not reorder or renumber existing rows. Choose among "Blueprint taxonomies," "Content and delivery taxonomies," and "Supporting taxonomies" by matching the new taxonomy's entity (Knowledge, Topic, Blueprint, Content, or Publication) against each table's existing "Applied to" values, and by whether the value is likely to need a per-value disambiguation note (favor a table with a Definition column when it is, "Supporting taxonomies" when it is not).

Preserve the file's existing minimal single-space pipe formatting (`| cell | cell |`); these tables are not padded to visually align columns, so do not introduce column padding that the rest of the table lacks.

### Target: Theme registry (`docs/100_brand/strategy/README.md`)

The Theme registry table has two columns, `| Theme | Meaning |`. Append one new row at the bottom of the table's existing five rows, in this shape:

`| <Theme name> | <one-sentence meaning> |`

There is no separate Definition column and no usage-conditions table for Themes; the Meaning cell carries the full definition on its own. Do not reorder or renumber the existing rows, and preserve the table's existing minimal single-space pipe formatting, matching `ONTOLOGY.md`'s own convention (no column padding).

### Target: Audience Segment registry (`docs/100_brand/audience/README.md`)

The Audience Segment registry table has four columns, `| Segment | Stable code | Audience Relationship | Use |`. Append one new row at the bottom of the table's existing four rows, in this shape:

`| <Segment name> | <Stable code gathered in Input> | <Addressed, Spoken-with, or Spoken-about> | <one-sentence use> |`

The Audience Relationship value must be one of the three values already defined in `docs/100_brand/ONTOLOGY.md`'s "Supporting taxonomies" table (`Audience Relationship | Audience Segment | Addressed, Spoken-with, Spoken-about`); do not invent a fourth relationship value here, and confirm the chosen one with the approver as part of the proposal in Procedure step 1. The Stable code is the short code gathered in Input (matching the shape of the existing `B2`, `B1`, `A`, `SERVICES` codes); nothing else in this workflow supplies it. Do not reorder or renumber the existing rows, and preserve the same minimal pipe formatting.

### Target: Channel registry (`docs/100_brand/channels/README.md`)

The Channel registry table has four columns, `| Channel | Status | Compatible Publication Formats | Role |`. Append one new row at the bottom of the table's existing five rows, in this shape:

`| <Channel name> | <Status> | <Compatible Publication Formats> | <one-sentence role> |`

Compatible Publication Formats must use real Publication Format values from `docs/100_brand/ONTOLOGY.md`'s "Content and delivery taxonomies" table (Text Post, Thread, Carousel, Short-form Video, Long-form Video, Article, Newsletter); do not invent a Format that is not already in that list, since a genuinely new Format would itself need to go through the `ONTOLOGY.md` target above first, before it could be cited here. For a Channel supporting more than one Format, list them comma-separated in the same cell, matching X's and Instagram's existing rows (e.g. `Text Post, Thread`). Status is presumably one of `Active`, `Planned`, or `Future`, per the existing table's own rows, but this is inferred from those rows rather than a formally defined enum documented elsewhere in `ONTOLOGY.md` or the registry docs; present it to the approver as inferred, not as an asserted governed taxonomy, and flag if a genuinely new Status value seems needed. Do not reorder or renumber the existing rows, and preserve the same minimal pipe formatting.

### On rejection

**On rejection, or when approval is never given:** do not edit the target file identified above. Retain the proposal in the Work Item's own body (see Work Item tracking below) rather than only as local conversation context, per `docs/100_brand/marketing/content/workflows/propose-taxonomy-addition.md`'s Output: "a rejected proposal retained in the Work Item." Do not write the proposal anywhere else, and do not treat the proposed value as selectable by any other skill.

### Work Item tracking

Also create one Work Item record under `docs/100_brand/marketing/content/work-items/`, on every run regardless of outcome, per the Skill execution contract's point 7 (cited here for the mechanic, not as a contract this skill otherwise follows; see Overview), `propose-taxonomy-addition.md`'s own Work Item contract, and `docs/100_brand/marketing/content/work-items/README.md`'s required frontmatter and body. This skill's Work Item shape is genuinely unusual among the seven skills in `.claude/skills/`, for two reasons:

**`primary_subject` cannot be a file path to the proposed value itself.** Unlike every sibling skill's `primary_subject` (a Topic, Blueprint, or Script Asset that already has real identity and a file path), a proposed controlled value is an abstract thing with no domain record of its own; there is no `docs/100_brand/marketing/content/taxonomy-proposals/<slug>.md` to point at. Of the two candidate fixes, this skill uses **the originating blocked skill's own target record path** (for example, the in-progress Blueprint draft, Topic, or Script the blocked run was operating on when it hit the missing-value stop condition), not the target registry file path (`ONTOLOGY.md` or the specific registry). Reasoning: the registry file is shared across every taxonomy proposal ever made against it, so using it as `primary_subject` would make many unrelated Work Items carry the identical value and would say nothing about which specific proposal this run represents; the blocked skill's target record, by contrast, is the concrete file this specific proposal exists in service of, mirroring how `to-blueprint`'s own `primary_subject` points to the pre-existing Topic that grounds its work, not to the Blueprint file it is itself producing. Use the file path captured in Input's "which skill and which specific run" item. In the rare case that blocked run never reached the point of creating any file (it stopped mid-Procedure, before any Output), no real path exists yet; record this honestly in the Work Item's "Decisions and assumptions" section and use the blocked skill's name plus the one-line task summary gathered in Input as the identifying reference in place of a path, rather than inventing one. In this case, set the `primary_subject` frontmatter field itself to the literal string `no file on file; see Decisions and assumptions`, and put the blocked skill's name plus the one-line task summary in the "Decisions and assumptions" section as described above. Use this exact string every time this fallback applies, so `primary_subject` stays a predictable, greppable marker rather than a fresh ad hoc phrase per run.

**Entry and successful exit stage are both Validate**, per `propose-taxonomy-addition.md`'s Work Item contract: "this governance operation does not advance the subject's Content lifecycle." Unlike `to-blueprint`'s Plan-then-Draft transition or `to-validate`'s Review-then-Produce transition, this skill's Work Item never transitions `current_stage`; create it at `current_stage: Validate` and leave it there through completion, whatever the outcome. This is a deliberate side quest against the blocked skill's own Work Item, not a step that advances the proposed value's (nonexistent) lifecycle.

**Creates:** a local proposal in the Work Item itself, not a separate file. The name, definition, entity, rejected-alternatives reasoning, provenance link, and usage conditions gathered in Procedure steps 1-3 go directly into this Work Item's body (its "Inputs" and "Decisions and assumptions" sections); there is no separate proposal record for it to live in.

**Updates:** the owning canonical context identified above (`ONTOLOGY.md` or the specific registry) only after explicit approval, per the Taxonomy contract's "Writes" line: "nothing until explicit approval."

**Required predecessors:** a workflow encounter demonstrating existing values do not fit, that is, the blocked skill and run captured in Input. Record it using the same "which skill and which specific run" detail gathered there. When no target record file exists at all yet (the same case handled in the `primary_subject` discussion above, where the blocked run stopped mid-Procedure before any Output), skip the field lookup entirely and use the prose fallback directly, below. Otherwise, when that blocked run already has its own Work Item on file (check its target record's "Creating Work Item" Header field, the same lookup mechanic `to-blueprint` and `to-validate` use for their own predecessors), link it directly. When it does not, because the blocked run stopped before ever writing a Work Item of its own, or the field is still the unfilled `[link]` placeholder, record the predecessor as prose instead of a broken link: the blocked skill's name and the task summary from Input, following the same "no Work Item on file" fallback those sibling skills use.

**Possible next workflows:** resume the originating workflow after approval, otherwise use an existing value or end the originating execution, per `propose-taxonomy-addition.md`'s Work Item contract. See Next step below for how this skill actually names that handoff.

Set outcome fields as follows:

- **Approved:** once the target file is edited and confirmed, set `work_state: Completed` and `status: archived`; this Work Item's own job (running the proposal to an approved canonical update) is finished. `current_stage` stays `Validate`.
- **Rejected, or approval never given:** set `work_state: Blocked` and repository `status: blocked` (see Stop conditions below), and record the actual missing approval, and why, in the Work Item's own prose fields. `current_stage` stays `Validate`.

Confirm before writing, per Procedure step 4 above (which already establishes the approval gate) and the point-7 citation earlier in this section: present the target file (registry or `ONTOLOGY.md` row), the full proposal, and the Work Item's planned content together, as one approval, not a second round after the canonical edit is already presented.

## Stop conditions

Approval is a hard gate, not a default: this skill has no stop condition of its own beyond "no approval yet." If the Procedure reaches step 4 and explicit approval is not given in the current conversation, whether because it is refused, deferred, or simply never addressed, the correct outcome is no edit to the target file identified in Output, whichever of the four it was. Do not add the value "provisionally," "for now," or on the assumption that approval is likely; there is no silent or partial addition.

Even when this skill stops here, it still creates or updates the Work Item recording the block rather than producing nothing with no record of the attempt: set `work_state: Blocked` (the matching Work Item State value in `docs/100_brand/ONTOLOGY.md`) and repository `status: blocked`, matching the pattern the sibling skills use when the underlying evidence, approval, or dependency genuinely does not exist yet, and record the actual missing approval in the Work Item's own prose fields, per `docs/100_brand/marketing/content/work-items/README.md` and the Work Item tracking subsection above. The underlying block was never resolved, so the Work Item stays `Blocked`, not `Completed`.

## Next step

Hand off back to whichever skill and run were captured in Input as originally blocked, per this Work Item's "Possible next workflows" (resume the originating workflow after approval, otherwise use an existing value or end the originating execution). Name that skill explicitly (for example "`to-blueprint`, resume the Blueprint draft for `docs/100_brand/marketing/content/topics/<slug>.md`") and confirm the new value now appears in its target file (`docs/100_brand/ONTOLOGY.md`, or the Theme, Audience Segment, or Channel registry, whichever Output used) before that skill re-validates its taxonomy contract and continues. If no specific blocked skill/run was captured at Input, say so plainly rather than inventing one.

## Validation

For a value added to `docs/100_brand/ONTOLOGY.md`:

```
rg -n '^\| <Taxonomy name> \|.*<new value>' docs/100_brand/ONTOLOGY.md
```

Anchor on the literal markdown row prefix for the specific taxonomy (for example `| Content Pattern |`), not a bare search for `<new value>`: an unanchored match can be satisfied by an unrelated Definition clause, a mermaid diagram class name, or a substring of an existing word, none of which confirm the edit landed in the right row. This should match nothing before approval, and should match the new entry, in the correct taxonomy's row, after approval. If a usage condition was also added, separately confirm it with `rg -n '^\| <Condition> \|.*<new value>' docs/100_brand/ONTOLOGY.md` against the "Hook usage conditions" table.

For a Theme added to the Theme registry:

```
rg -n '^\| <Theme name> \|' docs/100_brand/strategy/README.md
```

For an Audience Segment added to the Audience Segment registry:

```
rg -n '^\| <Segment name> \|' docs/100_brand/audience/README.md
```

For a Channel added to the Channel registry:

```
rg -n '^\| <Channel name> \|' docs/100_brand/channels/README.md
```

Anchor all three registry checks on the literal row prefix (the candidate's own name as the first cell), the same reasoning as the `ONTOLOGY.md` check above: each registry's Meaning, Use, or Role cell is free text and could otherwise produce a false-positive match unrelated to the actual row. Each of these three should match nothing before approval, and should match exactly the new row after approval.

The Work Item record's filename embeds today's date and a slug that cannot be predicted in advance, so no fixed `rg` command is given for it here. Spot-check its required frontmatter and body sections by hand against `docs/100_brand/marketing/content/work-items/README.md`'s spec instead, including the unusual `primary_subject` and `current_stage: Validate` fields described in Work Item tracking above.
