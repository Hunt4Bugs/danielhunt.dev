# Personal Brand Workbook Docs Design

**Date:** 2026-06-01
**Method:** Synthesis from `/grill-me` session against Ralston's "How to Start Your Personal Brand" workbook (65 pages, 15 exercises).
**Status:** Approved by Daniel. Pending file-by-file writing with user review checkpoints between each.
**Companion:** workbook answer snapshot will live at `docs/100_brand/specs/2026-06-01-personal-brand-workbook.md` after writing.

---

## Problem Statement

Daniel has just completed a long grilling session against the Ralston personal-brand workbook. The session produced substantial new brand material: a primary audience tier never named in the existing docs, a locked Brand Statement in the Ralston "I believe" format, a forward-orientation reframe (walking *into* life sciences rather than "having left" pharma), a scout model framing, a painful problems list, an ideation table, credibility and interest banks, differentiation breakdown, desired associations, content strategy specifics, and a rejection of one workbook exercise on principle.

None of this material exists yet in `docs/100_brand/`. The existing IDENTITY.md and OPERATING.md are strong on persona, voice, references, surfaces, cadence, and phasing, but they do not contain: the audience definition, the brand statement, the pain list, the ideation table, or the workbook-derived editorial rules.

Without writing it down, the new brand decisions will drift, get re-litigated, or be forgotten. Daniel needs the workbook output captured before context decays.

## Solution

Capture the workbook decisions across the brand docs and a dated workbook snapshot, following the hybrid output structure locked at the end of grilling.

Canonical material that should compound (audience, brand statement, scout reframe, contrarians) absorbs into IDENTITY.md as surgical additions. New audience-shaped material (audience tiers, painful problems, ideation table, credibility bank, interest bank, differentiation, associations) consolidates into a new `docs/100_brand/AUDIENCE.md`. Operational and editorial decisions absorb into OPERATING.md. A full dated workbook snapshot at `docs/100_brand/specs/2026-06-01-personal-brand-workbook.md` holds every answer in workbook order for audit and future reference. The CHANGELOG records the exercise.

Files are written one at a time with a user review checkpoint between each, so tone and framing issues surface early and do not cascade.

## User Stories

1. As Daniel, I want a single dated artifact that captures every workbook answer, so I can later see the state of my brand thinking as of 2026-06-01 without re-running the exercise.
2. As Daniel, I want the canonical brand identity material (audience, brand statement, contrarians, scout reframe) absorbed into IDENTITY.md, so I reference one place for who-the-brand-is.
3. As Daniel, I want the audience-focused material (audience tiers, painful problems, ideation table, credibility and interest banks, differentiation, associations) consolidated in a new AUDIENCE.md, so audience-shaped content decisions have a clear home.
4. As Daniel, I want the new editorial rules (viral handcuff preventive principle, Phase 0 capture targets, Phase 1 prep hooks, Ralston §15 rejection) added to OPERATING.md, so operational decisions stay with operational context.
5. As Daniel, I want a CHANGELOG entry that summarizes the exercise and surfaces the major decisions, so anyone reading the changelog can see the brand history.
6. As Daniel, I want all writing to honor the existing brand vocabulary (no em-rules, observation over preaching, scars not wounds, memory not photoshoot), so the new material reads coherent with the docs already written.
7. As Daniel, I want each file written and reviewed one at a time, so I can catch tone or framing issues before they cascade across files.
8. As a future agent looking at the brand docs, I want clear pointers between the workbook snapshot and the canonical homes (IDENTITY, AUDIENCE, OPERATING), so I can trace where any decision originated.
9. As Daniel, I want the three audience tiers (B2 primary, B1 peer network, A spoken-about) named and defined in writing, so future content decisions have a clear filter for who I am addressing.
10. As Daniel, I want the brand statement and scout reframe documented at identity level, so the forward-orientation (walking in, not "left") becomes the canonical framing rather than the backward-leaving framing.
11. As Daniel, I want the painful problems list marked "v0, validate against 5+ peer-founder conversations in Phase 0," so future me does not treat the list as finished.
12. As Daniel, I want W2 and S2 in the credibility bank explicitly marked as Phase 0 capture targets, so I know to watch for them as Datavial ships.
13. As Daniel, I want Bucket C in the interest bank documented as "intentionally empty, revisit Month 6," so I do not accidentally fill it with brand-process content prematurely.
14. As Daniel, I want the Ralston §15 rejection documented as a brand decision with its reason (educator-coded structure violates observation over preaching), so I do not re-litigate the same trade when other frameworks suggest the same shape.
15. As Daniel, I want the Lindhardt and Dalen reference-coded First Three Videos skeleton stored as the canonical Phase 1 prep starting point, so the work is not blank when launch arrives.
16. As Daniel, I want the 4Cs intro framework skeleton stored similarly, so it expands cleanly at Phase 1 prep.
17. As Daniel, I want existing IDENTITY.md and OPERATING.md sections preserved exactly where the surgical updates do not touch them, so I do not lose work already locked.
18. As Daniel, I want the bridge pain (#11) and the two new offline-coded pains (Offline-A and Offline-B) explicitly tagged in AUDIENCE.md, so the offline-half content pillars are legible and the toggle's 50/50 spirit has a content-strategy backing.
19. As Daniel, I want the product-level contrarian (GxP does not have to feel like GxP) named in IDENTITY.md alongside the brand-level contrarian, so Datavial product decisions have a one-line touchstone.
20. As Daniel, I want the W1b credibility entry flagged for sharpening ("AI skills" reads buzzy), so a future revision turns it into concrete language.

## Implementation Decisions

### Files

Five files, written one at a time, reviewed between each.

1. **`docs/100_brand/AUDIENCE.md`** (new). Holds: three audience tiers (B2 primary, B1 peer network, A spoken-about) with definitions; painful problems v0 (12 rows, "validate Phase 0" header); ideation table v1 (12 rows); credibility bank v0 (W1, W1b, W3, W2 deferred, S1, S2 deferred); interest bank v0 (5 curiosities/experiments split between Buckets A and B, 3 offline items in Bucket D, 4 honest questions + 1 explicitly open, Bucket C intentionally empty); differentiation breakdown (4 rows); desired associations (2 for, 2 against). The Brand Statement and the brand-level and product-level contrarians live in IDENTITY.md, not duplicated here; AUDIENCE.md cross-references them.

2. **`docs/100_brand/IDENTITY.md`** (surgical update). Add a new "Audience" section after "Audience experience" naming the three tiers. Add a new "Brand Statement" section adjacent to "Thesis" containing the locked statement. Add the walking-in reframe and scout model as internal-only design references in the Persona section. Add the product-level contrarian alongside the existing brand-level material (likely in a new "Contrarians" section or appended to the Thesis section). Do not delete or restructure existing content. No em rules.

3. **`docs/100_brand/OPERATING.md`** (surgical update). Add an "Editorial rules" section containing the viral handcuff preventive principle ("the toggle controls, not the algorithm"). Add to phasing or a new "Phase 0 capture targets" subsection: W2, S2, Wrapping Paper library as habits to watch for. Add Phase 1 prep hooks pointing to the workbook snapshot for First Three Videos skeleton and 4Cs framework expansion. Add the Ralston §15 rejection as a documented brand decision (one paragraph; link to workbook snapshot for full reasoning).

4. **`docs/100_brand/specs/2026-06-01-personal-brand-workbook.md`** (new). Full workbook snapshot. All 15 exercises in workbook order. Each answer pointed at its canonical home (IDENTITY for brand statement and contrarians, AUDIENCE for pain list and ideation table, OPERATING for editorial rules). Deferred items marked explicitly: W2, S2, 4Cs expansion, First Three Videos expansion. Validation-needed items marked explicitly: pain list, audience B2 resonance.

5. **`docs/100_brand/CHANGELOG.md`** (append entry). Dated entry summarizing the exercise and the major decisions. One short paragraph plus a bullet list of files touched.

### Writing order (locked)

`AUDIENCE.md` first because it is the longest and contains the most new material; getting tone and vocabulary right here calibrates the rest. Then `IDENTITY.md` updates (the surgical additions reference what is already in AUDIENCE.md). Then `OPERATING.md` updates. Then the workbook snapshot (which references all of the above). Then the CHANGELOG entry.

### Canonical homes for each piece of material

| Material | Canonical home | Mentioned elsewhere |
|---|---|---|
| Audience tiers (B2/B1/A) | AUDIENCE.md | Referenced in IDENTITY.md "Audience" section and OPERATING.md content mix |
| Brand Statement | IDENTITY.md | Cross-referenced in AUDIENCE.md and workbook snapshot |
| Brand-level contrarian | IDENTITY.md | Cross-referenced in AUDIENCE.md and ideation table |
| Product-level contrarian | IDENTITY.md | Cross-referenced in AUDIENCE.md ideation table row 5 |
| Bridge: "you can't build for scientists if you've forgotten how to be a person" | IDENTITY.md | Cross-referenced in AUDIENCE.md offline rows |
| Walking-in reframe + scout model | IDENTITY.md (internal-only scaffolding) | Workbook snapshot |
| Painful Problems v0 | AUDIENCE.md | Workbook snapshot |
| Ideation Table v1 | AUDIENCE.md | Workbook snapshot |
| Credibility Bank v0 | AUDIENCE.md | Workbook snapshot |
| Interest Bank v0 | AUDIENCE.md | Workbook snapshot |
| Differentiation Breakdown | AUDIENCE.md | Workbook snapshot |
| Desired Associations | AUDIENCE.md | Workbook snapshot |
| Editorial rule: viral handcuff preventive | OPERATING.md | Workbook snapshot |
| Phase 0 capture targets (W2, S2, Wrapping Paper) | OPERATING.md | Workbook snapshot |
| Ralston §15 rejection | OPERATING.md | Workbook snapshot |
| First Three Videos skeleton (Lindhardt/Dalen-coded) | Workbook snapshot (primary) | OPERATING.md hook for Phase 1 prep |
| 4Cs intro framework skeleton | Workbook snapshot (primary) | OPERATING.md hook for Phase 1 prep |
| Brand Prison Test answers (Steps 1-6) | Workbook snapshot only | (no canonical promotion needed; toggle in IDENTITY.md handles the operational concern) |
| Sustainable Foundation specifics | Workbook snapshot only | (cross-reference to OPERATING.md which already holds the operational answer) |

### Naming and convention discipline

- Spec file follows existing `YYYY-MM-DD-name-design.md` convention (matches `2026-05-28-brand-refinement-design.md`).
- New `AUDIENCE.md` follows existing brand-doc naming (uppercase short name, matches IDENTITY/VISUAL/OPERATING).
- Workbook snapshot uses descriptive name (`2026-06-01-personal-brand-workbook.md`), not a `-design` or `-implementation` suffix, because it is neither: it is a dated input artifact.
- No em rules in any brand-shaped writing. Use commas, periods, parens, mid-dots, asterisms, colons, or numbered sections.

### Cross-reference discipline

Every file points at its companions. AUDIENCE.md references IDENTITY.md for brand statement and contrarians. IDENTITY.md references AUDIENCE.md for the full audience definition. OPERATING.md references the workbook snapshot for the §15 rejection reasoning. The workbook snapshot references every canonical home.

## Testing Decisions

This is documentation work, not feature work. "Tests" become **user review checkpoints**, not assertions.

### What makes a good review

Review prompts per file:

1. Does the new material match what was locked during grilling? (Compare against the conversation log or the handoff doc.)
2. Does the prose voice match the existing IDENTITY.md style? (Observation over preaching, scars not wounds, memory not photoshoot, no algorithm posturing.)
3. Are any em rules present? (Should be zero. Replace with commas, periods, parens, colons, mid-dots, numbered sections.)
4. Are cross-references between files correct?
5. For surgical updates: are untouched sections actually untouched?

### Which files get review

- **AUDIENCE.md** (new): full-content review.
- **IDENTITY.md** (surgical update): diff-review. Untouched sections must remain bit-identical.
- **OPERATING.md** (surgical update): diff-review.
- **Workbook snapshot** (new): full-content review with extra attention to deferred items being marked correctly.
- **CHANGELOG.md** (append): diff-review of the appended entry only.

### Prior art

The existing spec at `docs/100_brand/specs/2026-05-28-brand-refinement-design.md` and plan at `docs/100_brand/plans/2026-05-28-brand-refinement-implementation.md` define the tone and structural discipline this project uses. The new workbook snapshot and this design spec should match.

The existing IDENTITY.md defines the brand voice. New prose written into IDENTITY.md or AUDIENCE.md should be indistinguishable in style from the prose already there.

### Test for "are we done"

After the fifth file is reviewed and approved, the workbook is shipped. The CHANGELOG entry is the marker. No further verification is needed beyond the per-file reviews.

## Out of Scope

- Re-litigating any decision locked during grilling. If the writing agent disagrees with a locked answer, push back to the user first; do not silently rewrite.
- Writing actual content for X, IG, LinkedIn, or YouTube posts. The Ideation Table is a backlog of *what could be made*, not a publishing plan or a script.
- Filming, editing, or other production work for the YouTube launch. The First Three Videos skeleton is a Phase 1 starting point, not a script.
- W2 and S2 enumeration. These are Phase 0 capture targets, captured as they emerge from real work, not invented now.
- Pain list validation interviews. Listening work happens in Phase 0; this PRD only ships the list as v0 with the validation requirement noted.
- Visual identity changes. VISUAL.md is untouched.
- Changes to the `2026-05-28-brand-refinement-design.md` spec or the companion plan. Those are historic; this PRD layers on top of them, it does not amend them.

## Further Notes

### Date context

Today is 2026-06-01. Datavial is pre-design-partner. Phase 0 prep is active (May 28 to June 22, 2026 window). YouTube launches Phase 1 with the trip after June 2026 (estimated December 2026 or January 2027).

### Issue tracker

The matt-pocock PRD skill assumes an active GitHub issue tracker with a `ready-for-agent` label vocabulary. This project does not have that setup (`gh repo view` returns 0 issues, no labels visible). The project tracks decisions through dated specs in `docs/100_brand/specs/` and plans in `docs/100_brand/plans/`. This PRD is therefore stored as a spec file in that location rather than published to an issue tracker.

### Companion artifacts

- Full handoff doc lives at the temp path produced during the `/handoff` step earlier in this session.
- Conversation log holds the complete grilling reasoning, including the 13 numbered grilling questions and the final output-structure decision.
- The Ralston workbook PDF itself lives at `~/Library/Mobile Documents/com~apple~CloudDocs/Archive/books/How to Start Your Personal Brand Workbook (Full).pdf`.

### Brand memory note (system-wide)

No em rules in any brand-shaped writing. User memory file `feedback_no_em_rules.md`. Use commas, periods, parens, mid-dots, asterisms, colons, or numbered sections.

### Small flags carried forward from grilling

- **W1b "AI skills" phrasing** reads buzzy. When writing AUDIENCE.md credibility bank, the writing agent should add a brief note that the phrasing needs sharpening with the user (what was the actual work? internal LLM tooling? prompt library? use-case prioritization?).
- **W3 and S1 pair as one foundational story.** Surface this in AUDIENCE.md or the workbook snapshot. They are different angles on the same insight and together they form the brand's origin story; treating them as separate atomic items loses that.
- **S2 is the structural gap to watch for the next 12 months.** Most-resonant scar type for audience (B2) because it gives them permission to be wrong on their own walk.
- **Interest Bank question #5 is intentionally open.** Honest scout mode requires not fabricating. Capture as it emerges; do not back-fill.
