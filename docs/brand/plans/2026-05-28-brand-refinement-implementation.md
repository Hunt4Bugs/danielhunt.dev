# Brand Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the brand documentation in `docs/brand/` to reflect the Ralston-framework brand refinement spec (`docs/brand/specs/2026-05-28-brand-refinement-design.md`). Rewrite IDENTITY.md to separate public from internal vocabulary and update content/format decisions. Create OPERATING.md to hold the revisable operational plan. Create CHANGELOG.md to log brand decisions over time.

**Architecture:** Three-document model. IDENTITY.md is the durable identity and design scaffolding (changes rarely). OPERATING.md is the revisable operational plan with cadence, phasing, and learning agenda (changes quarterly). CHANGELOG.md is the append-only decision log (one entry per meaningful brand choice).

**Tech Stack:** Markdown only. No code changes. No tests in the traditional sense. Verification is visual / editorial.

**Source spec:** `docs/brand/specs/2026-05-28-brand-refinement-design.md` (must be read in full before starting).

---

## File Structure

| Path | Action | Purpose |
|---|---|---|
| `docs/brand/IDENTITY.md` | Modify | 7 distinct edits to sections per spec Section A |
| `docs/brand/OPERATING.md` | Create | New operational plan per spec Section B |
| `docs/brand/CHANGELOG.md` | Create | Brand decision log per spec Section C |
| `docs/brand/specs/2026-05-28-brand-refinement-design.md` | Already created, not yet committed | The source spec |

No new directories needed (`docs/brand/`, `docs/brand/specs/`, `docs/brand/plans/` already exist).

---

## Task 1: Add Public Referral Sentences section to IDENTITY.md

**Files:**
- Modify: `docs/brand/IDENTITY.md` (insert new section between the Thesis section and the Persona section, i.e. after line 11 / before line 13)

**Why:** IDENTITY.md currently has no top-level section establishing which sentences are for public use. Adding this section up-front establishes the vocabulary discipline before any internal-only design references appear.

- [ ] **Step 1: Insert new section after Thesis section**

Find the existing line `## The Persona` (currently line 13) and insert the following section immediately before it:

```markdown
## Public Referral Sentences

Two sentences in industry-standard vocabulary. These are what someone says about Daniel to a third party.

- **Build half:** *He builds Life Sciences products.*
- **Offline half:** *A tech founder seeking human connection through movement, food, and culture.*

These appear in bios, captions, sponsor decks, media kits, and the site copy.

### Vocabulary discipline

Public-facing brand language splits into four layers.

**Public taglines (memorable brand phrases that appear in captions, lower-thirds, the site, sign-offs):**

- *Build in public. Live offline.* (the thesis tagline)
- *Tech, movement, and culture.* (the sub-thesis)

**Public referral sentences (descriptive, used in bios and third-party references):**

- *He builds Life Sciences products.* (Build half)
- *A tech founder seeking human connection through movement, food, and culture.* (Offline half)

**Editorial discipline phrases (primarily internal rules, occasional public surface):**

- *Scars, not wounds.* (Build-half editorial rule)
- *Memory, not photoshoot.* (Visual rule)

**Internal-only design references (do not appear in public copy):**

- *Maker-Mover*
- *Tech builder* (use *tech founder* or *software engineer* in public)
- Direct named comparisons to *Bourdain*, *Adrian Per*, *Kirx Diaz*, *Daniel Dalen*, *Oscar Lindhardt*

The internal-only references remain below as design scaffolding that explains why the brand looks and sounds the way it does. They are not what the brand says about itself in public.

```

- [ ] **Step 2: Verify section renders correctly**

Read the file back. Confirm the new section sits between Thesis and Persona, and all four sub-layers are present.

---

## Task 2: Mark the Persona section as internal-only

**Files:**
- Modify: `docs/brand/IDENTITY.md` (the existing `## The Persona` section, currently lines 13 to 21)

**Why:** The Persona section contains "Maker-Mover" which the spec marks as internal-only. Adding a banner at the top of the section makes the discipline visible at the point of reading.

- [ ] **Step 1: Add banner at top of Persona section**

Locate the `## The Persona` heading. Immediately after the heading and before the existing `**The Maker-Mover.**` line, insert this banner:

```markdown
> **Internal-only design reference.** The Maker-Mover persona below is design scaffolding that informs the brand's tone and structure. It does not appear in public copy. See Public Referral Sentences for what to use in bios and captions.

```

The section content (Maker-Mover description, the contradiction-is-the-brand framing) stays unchanged.

- [ ] **Step 2: Verify the banner renders as a blockquote**

The leading `>` should cause the banner to render as a callout. The Persona content below should remain readable.

---

## Task 3: Update Build half section

**Files:**
- Modify: `docs/brand/IDENTITY.md` (the existing `## Build half: what it is` section, currently lines 53 to 63)

**Why:** Three changes required by the spec: (1) talking-head dispatches are retired as a standalone format and become segments within the cinematic vlog, (2) the 80/20 Life Sciences content topic mix is added, (3) LinkedIn is added to the surface list.

- [ ] **Step 1: Replace the entire Build half section**

Find the section starting with `## Build half: what it is` and replace from that heading through the end of the section (just before `## Offline half: what it is`) with:

```markdown
## Build half: what it is

**Flagship artifact**: Datavial — a Life Sciences SaaS for pharma lab operations. The build half's load-bearing project. The work is real, the domain is regulated, the credibility is earned.

**Future verticals**: Legal Tech — same playbook, different industry. Possible expansion once Datavial has visible traction.

**Content topic mix**: 80% Life Sciences specific (GxP, 21 CFR Part 11, lab ops realities, regulatory navigation, design partner stories anonymized, Datavial scars, named industry incumbents like Veeva / Benchling / Dotmatics / LabVantage, the open problems in pharma software). 20% general operator material (founder lessons, branding, systems thinking) reused without diluting the Life Sciences signal.

**Format**:

- **YouTube long-form cinematic vlog** — the hero artifact. Weaves Life Sciences work, travel, training, and observation into one episode. Talking-head segments are integrated into the vlog when needed, not standalone outputs.
- **X build journaling** — real-time fragments, shipping notes, micro-observations.
- **LinkedIn** — Phase 0 and Phase 1 presence-only (monthly posts, profile current). Phase 2 escalates to weekly distribution with case studies and technical articles once Datavial has 3 to 5 named customers.
- **Instagram** — Reels and carousels carry build-half observation when relevant. Primarily offline-half territory.

**Editorial rule**: scars, not wounds. The build half is retrospective, not confessional. Discuss healed lessons. Wounds belong in private.

**Brand role for outcome**: indirect credibility moat, not GTM. Datavial sells through its own go-to-market motion (outbound, design partners, conferences, referrals). The personal brand creates name-leak into pharma networks so Daniel's name eventually comes up in industry referrals.

```

- [ ] **Step 2: Verify the section reads cleanly**

Confirm the 80/20 topic mix is named, cinematic vlog is the hero format, talking-head dispatches no longer appear as a standalone format, and LinkedIn is listed with its phased role.

---

## Task 4: Update Offline half section

**Files:**
- Modify: `docs/brand/IDENTITY.md` (the existing `## Offline half: what it is` section, currently lines 65 to 77)

**Why:** Three changes: (1) YouTube cinematic vlog becomes the hero (was: "future surface"), (2) IG Reels transition to cutdowns post-YouTube-launch (was: "current hero surface"), (3) production/tonal references stay but the section gets simplified since the References table holds them anyway.

- [ ] **Step 1: Replace the entire Offline half section**

Find the section starting with `## Offline half: what it is` and replace through the end of the section (just before `## What the brand is not`) with:

```markdown
## Offline half: what it is

**Lens**: movement, food, culture, observation, human connection.

**Format**:

- **YouTube long-form cinematic vlog** — the hero. Episodes weave training, travel, food, conversation, and observation. Same visual grammar as the build half, presented under unified production discipline.
- **Instagram Reels** — Phase 0 standalone short-form practicing cinematic discipline. Phase 1 onward, cutdowns from YouTube hero episodes.
- **Instagram Carousels** — biweekly written reflection.

**Travel cadence**: twice yearly (Thailand, plus Japan / Vietnam / etc.). Each trip is treated as a batch-shoot opportunity for 3 to 4 episodes worth of YouTube footage.

**Production and tonal references**: see the References table below. Internal-only — do not name in public copy.

```

- [ ] **Step 2: Verify the section**

Confirm YouTube is named as hero, IG role distinguishes Phase 0 vs Phase 1, travel cadence preserves the twice-yearly rhythm, and named references (Bourdain, Adrian Per) no longer appear in the section body.

---

## Task 5: Add Surface Map section

**Files:**
- Modify: `docs/brand/IDENTITY.md` (insert new section after `## Offline half: what it is`, before `## What the brand is not`)

**Why:** The spec calls for an explicit four-platform surface map showing role per phase. Currently IDENTITY.md has no consolidated surface table. This section makes the four-platform discipline visible at a glance and explicitly names the deferred channels.

- [ ] **Step 1: Insert new Surface Map section**

After the Offline half section ends and before `## What the brand is not`, insert:

```markdown
## Surface map

Four platforms Daniel controls. No external dependencies (no podcasts, no trade publications, no conferences as content channels).

| Platform | Phase 0 role | Phase 1 role | Phase 2 role |
|---|---|---|---|
| **X** | 4 to 6 posts per week. Build-journal fragments, Life Sciences observations, micro-notes. | Same. | Same. |
| **Instagram** | Standalone weekly Reel + biweekly carousel. Practicing cinematic short-form discipline. | Reels become cutdowns from YouTube hero episodes. Carousels continue. | Same as Phase 1. |
| **LinkedIn** | Presence-only. Profile current. 1 to 2 posts per month. | Same as Phase 0. | **Active distribution.** Weekly post tied to Datavial case studies, regulatory navigation, technical operator pieces. |
| **YouTube** | Not launched. | Monthly cinematic vlog. Hero artifact. | Same as Phase 1. |

Deliberately excluded:

- Podcasts (no guest appearances, no own podcast)
- Trade publications (Pharmaceutical Engineering, BioPharm International, etc.)
- Conferences as content channels (deferred until Datavial GTM specifically demands)

These exclusions are revisable. They prevent overload during Phase 0.

```

- [ ] **Step 2: Verify the section**

Confirm all four platforms are listed with phase columns. Confirm exclusions are explicit. Confirm the section sits between Offline half and What-the-brand-is-not.

---

## Task 6: Update References table

**Files:**
- Modify: `docs/brand/IDENTITY.md` (the existing `## References we borrow from` section, currently lines 97 to 104)

**Why:** Two changes: (1) Daniel Dalen and Oscar Lindhardt are elevated to structural references (was: Dalen as "awareness of high-craft production"), (2) reference type column is added to distinguish structural vs tonal vs production-craft.

- [ ] **Step 1: Replace the References table**

Find `## References we borrow from` and replace the section through the end of the table with:

```markdown
## References we borrow from

| Reference | What we borrow | What we leave | Type |
|---|---|---|---|
| Anthony Bourdain | Tone, voice, pacing, observational ethos, travel arc | Cynicism, addiction memoir, fame | Tonal |
| Adrian Per / Kirx Diaz | Production grammar, cinematic short-form discipline | Lifestyle-as-only-narrative | Production craft |
| Daniel Dalen | Structural template: real career in serious industry, documented cinematically. Awareness of high-craft production. | Pushed teal-green grade, luxury-corporate feel | Structural |
| Oscar Lindhardt | Structural template: documenting the journey into a serious industry as the brand spine | — | Structural |
| Iman Gadzhi | The 6-point brand framework as scaffolding only | Hustle gospel, self-monumentalizing aesthetic | Methodological |

All references are **internal-only**. They explain the brand's design choices. They are not named in public copy. See Public Referral Sentences for the language to use publicly.

```

- [ ] **Step 2: Verify the table**

Confirm Dalen and Oscar Lindhardt are both marked "Structural." Confirm the internal-only note is present at the bottom. Confirm the table has a Type column.

---

## Task 7: Rewrite Mission section

**Files:**
- Modify: `docs/brand/IDENTITY.md` (the existing `## Mission` section, currently lines 170 to 176)

**Why:** The spec's biggest critique of the current IDENTITY.md is that the Mission reads as a values statement rather than a concrete outcome statement. This task replaces it with a rewrite that anchors values to outcomes.

- [ ] **Step 1: Replace the Mission section**

Find `## Mission` and replace through the end of the file with:

```markdown
## Mission

Build credible, durable products in Life Sciences and adjacent regulated industries. Document modern life through movement, food, culture, systems, conversation, and observation. Compound a credibility moat over years so the name eventually carries the work.

The build half exists to ship real products and earn the credibility moat. The offline half exists to stay curious, present, and human. Neither dominates the other.

To prove that a tech founder can choose presence and depth over reach and noise.

### Outcome anchors

- **Primary:** Datavial and future Life Sciences products as the primary income stream. Possible expansion to Legal Tech.
- **Secondary:** Content brand as serendipity engine. Sponsorships and creator collabs lag the primary by years and are accepted as inbound, not pursued.
- **Compound:** Operator/peer network as ambient outcome, not a targeted motion.

See `docs/brand/OPERATING.md` for the revisable operational plan that turns these outcomes into a phased schedule.

```

- [ ] **Step 2: Verify the section**

Confirm the Mission now references Life Sciences explicitly. Confirm the Outcome Anchors subsection lists primary, secondary, and compound outcomes. Confirm the cross-reference to OPERATING.md is present.

---

## Task 8: Commit IDENTITY.md changes

**Files:**
- Stage: `docs/brand/IDENTITY.md`

- [ ] **Step 1: Review the full diff before committing**

Run: `git diff docs/brand/IDENTITY.md`

Confirm all seven edits are present and the file flows coherently from top to bottom.

- [ ] **Step 2: Stage and commit**

Ask Daniel for commit approval first (per project rule: only commit when requested).

When approved, run:

```bash
git add docs/brand/IDENTITY.md
git commit -m "$(cat <<'EOF'
docs(brand): refine IDENTITY per Ralston framework

Apply the brand refinement spec to IDENTITY.md:
- Add Public Referral Sentences and Vocabulary Discipline section
- Mark Persona section (Maker-Mover) as internal-only design reference
- Update Build half: 80/20 Life Sciences topic mix, cinematic vlog hero, LinkedIn added
- Update Offline half: YouTube cinematic vlog as hero, IG cutdowns post-launch
- Add Surface Map section with four-platform, phase-by-phase table
- Elevate Daniel Dalen and Oscar Lindhardt to structural references
- Rewrite Mission section as outcome statement anchored to Life Sciences

Source: docs/brand/specs/2026-05-28-brand-refinement-design.md

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Create OPERATING.md

**Files:**
- Create: `docs/brand/OPERATING.md`

**Why:** OPERATING.md holds the revisable operational plan that IDENTITY.md should not. Cadences, phasing, learning agenda, success criteria all live here. Quarterly review point.

- [ ] **Step 1: Create the file with full content**

Create `docs/brand/OPERATING.md` with the following content:

```markdown
# Brand Operating Plan

**Source spec:** `docs/brand/specs/2026-05-28-brand-refinement-design.md`
**Identity:** `docs/brand/IDENTITY.md`
**Review cadence:** quarterly

This document holds the revisable operational plan. Cadences, phasing, learning agenda, and success criteria live here. Identity-level decisions (persona, voice, referral sentences, vocabulary discipline) live in IDENTITY.md and change rarely. Operating decisions in this file are expected to evolve as evidence accumulates.

---

## Surface map

Four platforms. No external dependencies.

| Platform | Phase 0 role | Phase 1 role | Phase 2 role |
|---|---|---|---|
| **X** | 4 to 6 posts per week. Build-journal fragments, Life Sciences observations, micro-notes. | Same. | Same. |
| **Instagram** | Standalone weekly Reel + biweekly carousel. Practicing cinematic discipline. | Reels become cutdowns from YouTube hero episodes. Carousels continue. | Same as Phase 1. |
| **LinkedIn** | Presence-only. Profile current. 1 to 2 posts per month. | Same as Phase 0. | Active distribution. Weekly post tied to Datavial case studies, regulatory navigation, technical pieces. |
| **YouTube** | Not launched. | Monthly cinematic vlog. Hero artifact. | Same as Phase 1. |

## Build-half content mix

80/20 Life Sciences first. 80% Life Sciences specific (GxP, 21 CFR Part 11, lab ops realities, regulatory navigation, design partner stories anonymized, Datavial scars, named industry incumbents like Veeva / Benchling / Dotmatics / LabVantage, the open problems). 20% general operator material reused without diluting the Life Sciences signal.

## Format

Cinematic vlog as YouTube hero. Same unified production grammar across build half and offline half. IG cutdowns (Phase 1+). X fragments. LinkedIn presence-only initially, technical pieces later.

Talking-head video dispatches as a standalone format are retired. Talking-head segments are integrated within the cinematic vlog where needed.

## Cadence

| Surface | Phase 0 | Phase 1+ |
|---|---|---|
| YouTube | Not launched | Monthly |
| Instagram Reel | Weekly standalone | Weekly (cutdowns) |
| Instagram Carousel | Biweekly | Biweekly |
| X | 4 to 6 per week | 4 to 6 per week |
| LinkedIn | 1 to 2 per month | 1 to 2 per month (Phase 1), weekly (Phase 2) |

### Fallback cadence

When life demands it, YouTube drops to bimonthly. **Bimonthly is not a failure event.** It is the defined backup that prevents brand-quit reactions to missed months.

## Travel cadence

Twice yearly. Thailand, plus Japan / Vietnam / etc. per the existing rotation.

**Next trip:** June 23 to July 12, 2026.

Each trip is treated as a batch-shoot opportunity for 3 to 4 episodes worth of YouTube footage.

## YouTube launch criteria

Trigger: the trip after the June/July 2026 trip. Estimated December 2026 or January 2027.

Conditions:

1. Two finished YouTube episodes in reserve (buffer rule).
2. A documented editing workflow Daniel has executed end-to-end at least twice in DaVinci Resolve.
3. The launch episode itself is in production.

If conditions are not met by the next trip, push launch to the trip after that. No penalty. The plan tolerates a slipped launch.

The June 2026 trip is the **production dress rehearsal**, not the launch. Heavy shooting, no launch pressure. Footage becomes Phase 0 IG Reels material and a sandbox for editing practice.

## Sustainability rules

1. **Batch shooting around travel weeks.** Each trip produces 3 to 4 episodes of YouTube footage, not 1.
2. **Two-episode buffer at all times.** Buffer of 1 is a warning signal.
3. **Fallback cadence defined.** Bimonthly is the backup. Explicit, not failure.
4. **Brother's help is bonus, not load-bearing.** Routine workflow does not depend on him.

## Phasing

| Phase | Window | Focus |
|---|---|---|
| **Phase 0 prep** | May 28 to June 22, 2026 | Open X and IG posting. Practice on-camera 5 min per day. Begin learning DaVinci Resolve. Pre-trip planning. |
| **Phase 0 dress rehearsal** | June 23 to July 12, 2026 | First trip. Heavy shooting. No launch pressure. Production sandbox. |
| **Phase 0 main** | July 12 to roughly December 2026 | IG and X cadence sustained. Edit trip footage into Reels series. Develop production craft. LinkedIn profile current with monthly posts. |
| **Phase 1** | December 2026 or January 2027 onward | YouTube launches with next-trip Episode 1. Monthly YouTube + weekly IG cutdowns + daily X + monthly LinkedIn. |
| **Phase 2** | When Datavial has 3 to 5 named customers worth case-studying | LinkedIn escalates to weekly active distribution. Technical articles. Case studies. |

## Learning agenda

### Urgent (next 6 months)

**1. Cinematic short-form production craft.**

- NLE is DaVinci Resolve (license already held). Use its color grading and Fairlight audio post as craft-stretching tools, not just the timeline.
- Study Dalen and Oscar Lindhardt frame-by-frame. Replicate one of their edits as an exercise.
- Ship 4 IG Reels before June 23, 2026 as deliberate practice.
- Avoid the teal-green grade. Resolve's color tools make this easy to fall into and easy to avoid if conscious.

Success bar: by end of Phase 0 main (December 2026), Daniel can edit a 10 to 15 minute cinematic vlog in 15 to 20 hours rather than 40+.

**2. Content batching and production systems.**

- Shoot 3 to 5x more footage than needed.
- Document file organization, folder structure, proxy workflow, asset naming.
- Travel batching: shoot for 4 episodes per trip.
- Cross-format asset reuse: same shoot feeds YouTube + IG Reels + X frames + LinkedIn images.

Success bar: by end of Phase 0 main, a written production manual specific to Daniel's setup exists.

**3. On-camera presence.**

- Record self daily for 5 minutes. Do not post. Goal is comfort, not output.
- By June 23, deliver a 90-second voiceover in one or two takes.

Success bar: by end of Phase 0 main, Daniel does not flinch on camera and can deliver Bourdain-tonal voiceover on first or second take.

### Deferred but on the list

**4. Life Sciences operator literacy.** Broader industry fluency beyond Datavial's niche. Multi-year arc. Subscribe to Endpoints News, BioPharma Dive, Pharma Manufacturing. Read 3 to 5 pharma industry annual reports. Follow 30 to 50 Life Sciences operators on LinkedIn.

**5. Platform-native writing.** X grammar (fragments, threads, conversational) vs LinkedIn grammar (structured hook + thesis + evidence + CTA). Develops naturally through publishing.

**6. Editorial restraint.** Holding the brand line against off-brand-but-engagement-positive content. Weekly editorial review starting in Phase 1.

## Phase 0 prep checklist (May 28 to June 22, 2026)

Concrete, daily-level tasks for the next 4 weeks.

- [ ] Open X account posting cadence (4 to 6 per week). First post by end of week 1.
- [ ] Open Instagram account posting cadence (weekly Reel + biweekly carousel). First Reel by end of week 2.
- [ ] LinkedIn profile review and update. First Phase 0 post by end of week 2.
- [ ] DaVinci Resolve daily practice (30 minutes minimum). Goal: import / cut / basic color / export workflow comfortable by end of week 4.
- [ ] On-camera daily practice (5 minutes). Record but do not post. Goal: 90-second voiceover in 1 to 2 takes by June 22.
- [ ] Study sessions: 2 Daniel Dalen videos and 2 Oscar Lindhardt videos studied frame-by-frame with notes. By end of week 2.
- [ ] Frame-by-frame edit replication exercise: pick one Dalen or Lindhardt sequence and replicate its edit in Resolve. By end of week 4.
- [ ] Trip prep: shot list for the June 23 to July 12 trip drafted. Gear check. File-organization plan for the trip footage. By June 22.
- [ ] Buffer rule preparation: identify what each Phase 0 main IG Reel will be sourced from (trip footage primarily, supplemented by other local footage as needed).

## Success criteria

Evaluable at month 3 (end of August 2026) and month 6 (end of November 2026).

### Month 3 checkpoint

- X: 50+ posts shipped. Voice and topic mix recognizable as Life Sciences-weighted.
- IG: 8+ standalone Reels shipped. Visible craft progression from first to most recent.
- LinkedIn: profile current. 2 to 3 posts shipped.
- Production: DaVinci Resolve used for at least 6 edits. On-camera 5 min/day discipline held.
- June trip footage: organized, in editing pipeline.

### Month 6 checkpoint

- X: 100+ posts shipped. Engagement signal honest (not vanity).
- IG: 20+ standalone Reels shipped. Craft visibly closer to reference set.
- LinkedIn: 5+ posts shipped. Profile audience starting to skew Life Sciences-adjacent.
- Production manual: drafted.
- YouTube episode 1: in production. Buffer episode 2 in early edit.
- Launch trigger conditions: trackable. Realistic estimate for Phase 1 start.

If at month 6 the urgent learning items have not moved meaningfully, this operating plan needs revision rather than redoubled effort.

## Open questions and risks

**Production craft risk.** Cinematic short-form has a real learning curve. The plan assumes Daniel reaches usable craft by end of Phase 0 main (December 2026). If craft lags, Phase 1 launch slips to mid-2027. Launch criteria are conditional, not date-locked.

**Sustainability risk.** Monthly YouTube + weekly IG + daily X + LinkedIn + Datavial is heavy. The fallback cadence (bimonthly YouTube) is the safety valve. The risk is that Daniel does not take it when needed and burns out instead.

**Audience-fit risk.** The 80/20 Life Sciences content mix may attract a smaller audience than a generic operator brand. Trade-off accepted in the spec. Revisit at month 6 with honest data: is the audience trending toward Life Sciences-adjacent viewers or general SaaS operators?

**Sponsorship risk.** Outcome C (sponsorships) is expected to lag the primary outcome by years. If sponsorship revenue is needed earlier, the brand may face pressure to drift toward Adrian-Per-style cinematic lifestyle, which converts faster but dilutes the Life Sciences positioning. The plan should not change to chase sponsorship revenue unless explicitly re-deciding the outcome ranking.

**Trip-dependency risk.** YouTube launch is anchored to the trip after June 2026. If travel cadence slips, launch slips with it. Acceptable trade-off but tracked.

```

- [ ] **Step 2: Verify the file**

Confirm: surface map present, cadence tables present, fallback cadence explicit, phasing table present, Phase 0 prep checklist present with concrete tasks, learning agenda has urgent 3 and deferred 3, success criteria has month 3 and month 6 checkpoints, risks section present.

---

## Task 10: Commit OPERATING.md and the spec doc

**Files:**
- Stage: `docs/brand/OPERATING.md`
- Stage: `docs/brand/specs/2026-05-28-brand-refinement-design.md` (the spec, not yet committed)
- Stage: `docs/brand/plans/2026-05-28-brand-refinement-implementation.md` (this plan, not yet committed)

- [ ] **Step 1: Review what will be committed**

Run: `git status` and `git diff --stat docs/brand/`

Confirm OPERATING.md is staged for creation along with the spec and plan.

- [ ] **Step 2: Stage and commit**

Ask Daniel for commit approval first.

When approved, run:

```bash
git add docs/brand/OPERATING.md docs/brand/specs/2026-05-28-brand-refinement-design.md docs/brand/plans/2026-05-28-brand-refinement-implementation.md
git commit -m "$(cat <<'EOF'
docs(brand): add OPERATING plan, spec, and implementation plan

- docs/brand/specs/2026-05-28-brand-refinement-design.md
  Brand refinement design spec derived from Caleb Ralston's reverse-order
  framework (outcome -> known for -> what to do -> what to learn).

- docs/brand/OPERATING.md
  Revisable operational plan with surface map, cadence, phasing, learning
  agenda, Phase 0 prep checklist, success criteria. Quarterly review point.

- docs/brand/plans/2026-05-28-brand-refinement-implementation.md
  Stepwise implementation plan that produced this commit and the IDENTITY
  updates.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: Create CHANGELOG.md

**Files:**
- Create: `docs/brand/CHANGELOG.md`

**Why:** Append-only brand decision log. Lets future-Daniel remember why each meaningful brand choice was made. First entry is this spec.

- [ ] **Step 1: Create the file with first entry**

Create `docs/brand/CHANGELOG.md` with the following content:

```markdown
# Brand Changelog

Append-only log of meaningful brand decisions. One entry per choice. Newest entries at the top.

Format per entry:

- Date (YYYY-MM-DD)
- Decision (one line)
- Rationale (1 to 3 sentences, why this choice over the alternatives)
- Source (link to spec, PR, or conversation)

---

## 2026-05-28: Brand refinement via Ralston framework

**Decision:** Apply Caleb Ralston's reverse-order brand framework (outcome → known for → what to do → what to learn) to refine the brand. Settle on hybrid operator-creator positioning with Datavial and future Life Sciences products as primary income, content brand as serendipity engine and indirect credibility moat.

**Rationale:** The existing IDENTITY.md captured persona and voice well but left three things under-defined: the desired outcome (read as values, not outcome), the public-facing referral sentence (no industry-standard version existed), and the operational plan (no cadence, no phasing, no learning agenda). Working through Ralston's four steps in sequence produced concrete decisions on all three: two public referral sentences in industry-standard vocabulary ("He builds Life Sciences products" / "A tech founder seeking human connection through movement, food, and culture"), a four-platform surface map with phased roles, and a learning agenda focused on cinematic short-form production craft as the urgent gap.

**Source:** `docs/brand/specs/2026-05-28-brand-refinement-design.md`

**Implementation:** `docs/brand/plans/2026-05-28-brand-refinement-implementation.md`

```

- [ ] **Step 2: Verify the file**

Confirm: format-per-entry description is present, first entry is dated 2026-05-28, rationale explains why this choice over alternatives, source links to the spec.

---

## Task 12: Commit CHANGELOG.md

**Files:**
- Stage: `docs/brand/CHANGELOG.md`

- [ ] **Step 1: Stage and commit**

Ask Daniel for commit approval.

When approved, run:

```bash
git add docs/brand/CHANGELOG.md
git commit -m "$(cat <<'EOF'
docs(brand): add brand decision changelog

Append-only log of meaningful brand decisions. First entry: 2026-05-28
brand refinement via Caleb Ralston's reverse-order framework.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Self-Review

**1. Spec coverage:**

| Spec section | Plan task |
|---|---|
| Public Referral Sentences | Task 1 |
| Vocabulary discipline (4 layers) | Task 1 |
| Mark Maker-Mover etc. internal-only | Tasks 1, 2 |
| Mission rewrite as outcome statement | Task 7 |
| Build half: 80/20 + cinematic vlog + LinkedIn | Task 3 |
| Offline half: YouTube hero + IG cutdowns | Task 4 |
| Surface map with LinkedIn | Task 5 |
| References update (Dalen, Lindhardt structural) | Task 6 |
| OPERATING.md new doc | Task 9 |
| CHANGELOG.md new doc | Task 11 |
| Phase 0 prep checklist | Task 9 (embedded in OPERATING.md) |
| DaVinci Resolve as named NLE | Task 9 (in OPERATING.md learning agenda) |
| Trip date June 23 to July 12 | Task 9 |
| Sustainability rules | Task 9 |
| Success criteria month 3 / 6 | Task 9 |
| Open questions / risks | Task 9 |

All spec sections have a corresponding task.

**2. Placeholder scan:** No "TBD", "TODO", or vague requirements. All content is complete and inline. Commit messages are full text. File contents are full text.

**3. Type consistency:** No types or method signatures (documentation only). Cross-document references are consistent (IDENTITY.md ↔ OPERATING.md ↔ CHANGELOG.md ↔ spec doc paths all match).

**4. Ambiguity:** NLE and GTM are expanded on first use in the spec and the plan inherits that. "Named customers" left somewhat loose but consistent with the spec's treatment.

No issues found.
