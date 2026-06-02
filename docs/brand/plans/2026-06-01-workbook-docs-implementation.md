# Personal Brand Workbook Docs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Each task is one vertical slice. Pause for user review between tasks; do not chain.

**Goal:** Capture the workbook decisions from the 2026-06-01 `/grill-me` session across the brand docs and a dated snapshot, following the hybrid output structure locked at the end of grilling.

**Architecture:** Same three-doc model as the prior brand-refinement spec (`IDENTITY.md` for durable identity, `OPERATING.md` for revisable operational plan, `CHANGELOG.md` for append-only decision log), extended with one new doc and one dated snapshot:

- `AUDIENCE.md` (new): canonical home for audience-shaped brand material (tiers, pain list, ideation table, credibility and interest banks, differentiation, associations).
- `specs/2026-06-01-personal-brand-workbook.md` (new): full dated snapshot of all 15 workbook exercise answers.

**Tech stack:** Markdown only. No code changes. No tests in the traditional sense. Verification is visual and editorial, per the design spec's "user review checkpoint" approach.

**Source spec:** `docs/brand/specs/2026-06-01-workbook-docs-design.md` (must be read in full before starting). The source spec lists every locked decision and names the canonical home for each piece of material. Read it as the source of truth until task 4 produces the workbook snapshot.

**Brand vocabulary discipline:** No em-rules in any brand-shaped writing (`~/.claude/projects/-Users-danielhunt-projects-danielhunt-dev/memory/feedback_no_em_rules.md`). Use commas, periods, parens, mid-dots, asterisms, colons, or numbered sections. The existing IDENTITY.md and OPERATING.md voice is the tonal target.

---

## File Structure

| Path | Action | Purpose |
|---|---|---|
| `docs/brand/AUDIENCE.md` | Create | New canonical home for audience tiers, pain list, ideation table, credibility bank, interest bank, differentiation, associations |
| `docs/brand/IDENTITY.md` | Modify | Surgical additions: audience callout, brand statement, contrarians (brand + product), walking-in reframe, scout model |
| `docs/brand/OPERATING.md` | Modify | Surgical additions: editorial rules (viral handcuff preventive), Phase 0 capture targets, Phase 1 prep hooks, Ralston §15 rejection |
| `docs/brand/specs/2026-06-01-personal-brand-workbook.md` | Create | Full workbook snapshot, 15 exercises in workbook order, pointers to canonical homes |
| `docs/brand/CHANGELOG.md` | Modify (append) | One entry summarizing exercise and major decisions |
| `docs/brand/specs/2026-06-01-workbook-docs-design.md` | Already created | This plan's source spec |
| `docs/brand/VISUAL.md` | Untouched | Visual identity is out of scope |

No new directories needed.

---

## Task 1: Write AUDIENCE.md

**Type:** AFK. All decisions are locked. Full-content review at the end is the test checkpoint.

**Blocked by:** None. Can start immediately.

**User stories covered (from source spec):** 1, 3, 9, 11, 12, 13, 18, 20.

### What to build

A new `docs/brand/AUDIENCE.md` file holding the workbook's audience-shaped material in a coherent structure. The file should match the voice and structural discipline of the existing IDENTITY.md (numbered or bulleted sections, observation-coded prose, no preaching). It should cross-reference IDENTITY.md for the Brand Statement and contrarians (which live there as their canonical home) and should not duplicate them.

Sections required, in this order:

1. **Audience tiers.** Three tiers with definitions: B2 (primary, who I talk to), B1 (peer network, rare, who I talk with), A (spoken-about). For each tier, name the archetype, the current-state pain pattern, and how content addresses them.
2. **Painful Problems v0.** 12 numbered rows. Header note must state "v0, validate against 5+ peer-founder conversations in Phase 0." Group into Pre-leave/pre-entry, Building, and Bridge/offline blocks.
3. **Ideation Table v1.** 12 rows matching the pain list. Three columns: Painful Problem, Unique Solution (my POV), Credibility. Rows 8 to 10 marked as scout-mode credibility (currently figuring out, not authority).
4. **Credibility Bank v0.** W1, W1b (with flag: "AI skills" phrasing needs sharpening with user), W3 (origin moment, pair with S1 as the foundational story), W2 (deferred, Phase 0 capture target), S1 (paired with W3), S2 (deferred, watch-this-space gap).
5. **Interest Bank v0.** 5 curiosities/experiments split across Buckets A and B, 3 offline items in Bucket D, 4 honest questions plus 1 explicitly-open slot, Bucket C documented as intentionally empty (revisit Month 6).
6. **Differentiation Breakdown.** 4 rows. Tech-bro grind worship, build-in-public metrics theater, AI-rebrand hype-chasing, 20-years-pharma credentialism. Alt-A noted on the bench.
7. **Desired Associations.** 4 items (2 for, 2 against), symmetric across two axes (where the work points, how the work is done).

### Acceptance criteria

- [ ] File exists at `docs/brand/AUDIENCE.md`.
- [ ] All 7 sections present in the specified order.
- [ ] Pain list has 12 rows with the "v0, validate Phase 0" header.
- [ ] Ideation Table has 12 rows aligned 1-to-1 with the pain list.
- [ ] Credibility Bank explicitly marks W2 and S2 as deferred Phase 0 capture targets.
- [ ] Credibility Bank flags W1b "AI skills" phrasing for sharpening.
- [ ] W3 and S1 are described as the paired foundational brand story.
- [ ] Interest Bank Question #5 is documented as intentionally open (not back-filled).
- [ ] Interest Bank Bucket C is documented as intentionally empty (revisit Month 6).
- [ ] File cross-references IDENTITY.md for Brand Statement and contrarians; does not duplicate them.
- [ ] Voice matches existing IDENTITY.md (observation over preaching, scars not wounds).
- [ ] Zero em-rules. Use commas, periods, parens, mid-dots, colons, or numbered sections.
- [ ] User reviews full content and approves before Task 2 starts.

### Steps

- [ ] **Step 1: Read source spec end to end.** `docs/brand/specs/2026-06-01-workbook-docs-design.md`. Pay attention to the canonical-homes table and the small flags carried forward from grilling.
- [ ] **Step 2: Read existing IDENTITY.md.** Calibrate voice. Note the section structure, the use of blockquotes for principles, the "Internal-only design reference" callout pattern.
- [ ] **Step 3: Draft AUDIENCE.md.** All 7 sections. Cross-references in place. No em-rules.
- [ ] **Step 4: Self-review against acceptance criteria.** Fix any failure.
- [ ] **Step 5: Hand off to user for full-content review.** Wait for explicit approval before starting Task 2.

---

## Task 2: Apply workbook surgical updates to IDENTITY.md

**Type:** AFK. Surgical additions only. Diff-review is the test checkpoint.

**Blocked by:** Task 1 (AUDIENCE.md must exist so the audience callout in IDENTITY.md can cross-reference it).

**User stories covered:** 2, 10, 17, 19.

### What to build

Surgical additions to `docs/brand/IDENTITY.md`. Do not delete or restructure existing content. Do not touch any section not listed below.

Additions required:

1. **New "Audience" section** added after the existing "Audience experience" section. Brief tier definitions (B2 primary, B1 peer network, A spoken-about). Cross-reference AUDIENCE.md for the full definitions and the pain-list-shaped material.
2. **New "Brand Statement" section** placed adjacent to "Thesis" (likely immediately after Thesis or after the Public Referral Sentences section). Contains the locked statement: *I believe engineers who want work that compounds into the real world should walk into life sciences, not wait for permission from the incumbents.*
3. **New "Contrarians" section** containing both the brand-level contrarian (*Life sciences is the most underleveraged frontier in software. SWEs do not need 20 years inside; they need conviction.*) and the product-level contrarian (*GxP does not have to feel like GxP. Modern web-quality UX is buildable inside a regulated stack.*) and the bridge sentence (*You cannot build for scientists if you have forgotten how to be a person.*).
4. **Walking-in reframe and scout model** added to the Persona section as internal-only design references (matches the existing "Internal-only design reference" callout convention). The scout reference should mention Oscar Lindhardt's template as the structural parallel.

### Acceptance criteria

- [ ] All four additions present.
- [ ] No existing section is deleted, restructured, or otherwise modified outside these additions.
- [ ] Diff is clean and surgical.
- [ ] Audience section cross-references AUDIENCE.md.
- [ ] Brand Statement is reproduced verbatim from the source spec.
- [ ] Contrarians section includes both levels and the bridge.
- [ ] Walking-in reframe and scout model are marked internal-only, following the existing convention.
- [ ] Zero em-rules.
- [ ] User reviews diff and approves before Task 3 starts.

### Steps

- [ ] **Step 1: Read existing IDENTITY.md end to end.** Find the right insertion points.
- [ ] **Step 2: Make the four insertions.** Use Edit, not Write. Preserve untouched sections exactly.
- [ ] **Step 3: Self-review the diff against acceptance criteria.**
- [ ] **Step 4: Hand off to user for diff-review.** Wait for explicit approval before starting Task 3.

---

## Task 3: Apply workbook surgical updates to OPERATING.md

**Type:** AFK. Surgical additions only. Diff-review is the test checkpoint.

**Blocked by:** Task 1 (Editorial rules will reference the toggle context that AUDIENCE.md frames in audience terms).

**User stories covered:** 4, 14, 15, 16, 17.

### What to build

Surgical additions to `docs/brand/OPERATING.md`. Do not delete or restructure existing content. Do not touch any section not listed below.

Additions required:

1. **New "Editorial rules" section** (or extension of "Sustainability rules" if that fits better) containing the viral handcuff preventive principle: *the toggle controls, not the algorithm.* One paragraph. Explain the rule (if a Phase 0 fitness or compliance Reel goes 10× the average, the toggle still dictates the next post, not the engagement signal).
2. **New "Phase 0 capture targets" subsection** under Phasing (or as its own top-level section) listing: W2 (Datavial shipping win, captured when first design partner reports a measurable change), S2 (a wrong-assumption-I-unwound scar, captured as it emerges), Wrapping Paper library (daily 5-minute capture habit, Lindhardt and Dalen prioritized, single home in Notion or notes app).
3. **New "Phase 1 prep hooks"** subsection or appended bullets to the existing Phasing table. Two hooks: First Three Videos skeleton (Lindhardt/Dalen reference-coded, pointer to workbook snapshot for full skeleton), 4Cs intro framework skeleton (pointer to workbook snapshot for the skeleton).
4. **New "Documented brand decisions" or "Decisions log" section** containing the Ralston §15 rejection. One paragraph stating: the First Three Videos exercise as written is educator-coded ("5 key moments → lesson per moment → connect to viewer pain") and violates the IDENTITY.md "observation over preaching" guiding principle. Replaced with reference-coded skeleton (see workbook snapshot). Document this rejection so future me does not re-litigate the same trade when other frameworks suggest the same shape.

### Acceptance criteria

- [ ] All four additions present.
- [ ] No existing section is deleted, restructured, or otherwise modified outside these additions.
- [ ] Editorial rule (viral handcuff preventive) clearly states "toggle controls, not algorithm."
- [ ] Phase 0 capture targets explicitly name W2, S2, Wrapping Paper.
- [ ] Phase 1 prep hooks reference the workbook snapshot path (not just "the workbook" abstractly).
- [ ] Ralston §15 rejection is documented with its reasoning (educator-coded violates observation over preaching).
- [ ] Zero em-rules.
- [ ] User reviews diff and approves before Task 4 starts.

### Steps

- [ ] **Step 1: Read existing OPERATING.md end to end.** Identify natural insertion points.
- [ ] **Step 2: Make the four insertions.** Use Edit, not Write. Preserve untouched sections.
- [ ] **Step 3: Self-review the diff against acceptance criteria.**
- [ ] **Step 4: Hand off to user for diff-review.** Wait for explicit approval before starting Task 4.

---

## Task 4: Write workbook snapshot

**Type:** AFK. Mechanical compilation of all locked workbook answers. Full-content review at the end.

**Blocked by:** Tasks 1, 2, 3. The snapshot points at canonical homes; those homes must exist before the snapshot can link to them.

**User stories covered:** 1, 8, 11, 14, 15, 16.

### What to build

A new `docs/brand/specs/2026-06-01-personal-brand-workbook.md` file holding the full workbook snapshot. All 15 exercises in workbook order. Each answer points at its canonical home (IDENTITY, AUDIENCE, OPERATING) for the material that has been promoted there. Each answer includes the locked content as captured during grilling so the snapshot is self-contained for audit purposes.

Structure required:

1. **Frontmatter:** Date (2026-06-01), source workbook (Ralston, with PDF path), method (`/grill-me` session synthesis), status (Approved by Daniel; canonical homes assigned).
2. **Brand Positioning section** (workbook exercises 1 through 8). One sub-section per exercise. Each sub-section names the locked answer plus the canonical home path.
3. **Content Strategy section** (workbook exercises 9 through 15). Same structure. §13 4Cs and §15 First Three Videos sub-sections include the full Lindhardt/Dalen-coded skeleton. §15 also includes the Ralston-format rejection rationale.
4. **Deferred items list:** W2, S2, 4Cs expansion at Phase 1 prep, First Three Videos expansion at Phase 1 prep.
5. **Validation-needed items list:** Pain list (validate against 5+ peer-founder conversations in Phase 0), audience B2 pain resonance.
6. **Companion artifacts pointer:** the source-spec design doc (`docs/brand/specs/2026-06-01-workbook-docs-design.md`), the implementation plan (this file), the conversation log location.

### Acceptance criteria

- [ ] File exists at `docs/brand/specs/2026-06-01-personal-brand-workbook.md`.
- [ ] All 15 exercises represented in workbook order.
- [ ] Each exercise sub-section identifies its canonical home (or marks "snapshot only" if the material is not promoted).
- [ ] Brand Statement is reproduced verbatim.
- [ ] Pain list has 12 rows.
- [ ] Ideation Table has 12 rows.
- [ ] §15 sub-section contains both the rejection rationale and the Lindhardt/Dalen-coded skeleton.
- [ ] §13 sub-section contains the 4Cs skeleton.
- [ ] Deferred items list is explicit (W2, S2, 4Cs expansion, First Three Videos expansion).
- [ ] Validation-needed items list is explicit (pain list, B2 resonance).
- [ ] Voice matches existing brand specs in `docs/brand/specs/`.
- [ ] Zero em-rules.
- [ ] User reviews full content and approves before Task 5 starts.

### Steps

- [ ] **Step 1: Read source spec end to end.** `2026-06-01-workbook-docs-design.md`.
- [ ] **Step 2: Read AUDIENCE.md, IDENTITY.md updates, and OPERATING.md updates** to confirm canonical-home paths and verify what is actually written there.
- [ ] **Step 3: Read existing spec at `2026-05-28-brand-refinement-design.md`** to calibrate the spec-file voice.
- [ ] **Step 4: Draft the workbook snapshot.** All 15 exercises. Canonical-home pointers. Deferred and validation-needed lists.
- [ ] **Step 5: Self-review against acceptance criteria.**
- [ ] **Step 6: Hand off to user for full-content review.** Wait for explicit approval before starting Task 5.

---

## Task 5: Append CHANGELOG entry

**Type:** AFK. Trivial append. Diff-review is the test checkpoint.

**Blocked by:** Tasks 1, 2, 3, 4. CHANGELOG references the files touched, which must exist.

**User stories covered:** 5, 7.

### What to build

Append one dated entry to `docs/brand/CHANGELOG.md` summarizing the workbook exercise and the major decisions. Match the existing CHANGELOG format (read the file first to confirm the convention).

Entry should include:

1. **Date:** 2026-06-01.
2. **Title:** Personal brand workbook (Ralston) synthesized into brand docs.
3. **Summary paragraph:** one short paragraph describing the exercise (grilled answers to all 15 Ralston exercises against the existing `docs/brand/` material; new audience-shaped material consolidated in AUDIENCE.md; surgical additions to IDENTITY.md and OPERATING.md; full dated snapshot at `specs/2026-06-01-personal-brand-workbook.md`).
4. **Major decisions bullet list:**
   - Audience (B2) added as primary: software engineers and SaaS/AI founders looking for a frontier where their work compounds into real-world impact.
   - Brand Statement locked: *I believe engineers who want work that compounds into the real world should walk into life sciences, not wait for permission from the incumbents.*
   - Walking-in reframe established (forward, not "left").
   - Scout model adopted as the internal framing (Oscar Lindhardt template with non-zero experience).
   - Painful Problems v0 documented (12 rows, validate Phase 0).
   - Ideation Table v1 documented.
   - Ralston workbook §15 (First Three Videos exercise) rejected as educator-coded; replaced with Lindhardt/Dalen reference-coded skeleton.
5. **Files touched bullet list:** AUDIENCE.md (new), IDENTITY.md, OPERATING.md, specs/2026-06-01-personal-brand-workbook.md (new), CHANGELOG.md.

### Acceptance criteria

- [ ] CHANGELOG entry appended with 2026-06-01 date.
- [ ] Entry matches existing CHANGELOG format (read the file first).
- [ ] All seven major-decisions bullets present.
- [ ] Files-touched bullet list is complete.
- [ ] Brand Statement reproduced verbatim.
- [ ] Zero em-rules.
- [ ] User reviews diff and approves.

### Steps

- [ ] **Step 1: Read existing CHANGELOG.md** to confirm format and find the right place to append.
- [ ] **Step 2: Append the entry.** Use Edit, not Write.
- [ ] **Step 3: Self-review the diff against acceptance criteria.**
- [ ] **Step 4: Hand off to user for diff-review.** Workbook ships when user approves this entry.

---

## Post-completion

After Task 5 ships and is reviewed, the workbook is done. No further verification beyond the per-task review checkpoints. The next brand work should be the Phase 0 capture practice (pain list validation, W2 and S2 capture as they emerge, Wrapping Paper library habit), tracked in OPERATING.md.
