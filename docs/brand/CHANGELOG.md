# Brand Changelog

Append-only log of meaningful brand decisions. One entry per choice. Newest entries at the top.

Format per entry:

- Date (YYYY-MM-DD)
- Decision (one line)
- Rationale (1 to 3 sentences, why this choice over the alternatives)
- Source (link to spec, PR, or conversation)

---

## 2026-06-01: Personal brand workbook synthesized into brand docs

**Decision:** Synthesize the Ralston personal-brand workbook session (15 exercises) into the brand docs. Promote canonical material to `IDENTITY.md` and a new `AUDIENCE.md`. Add editorial rules and Phase 0 capture targets to `OPERATING.md`. Preserve the full workbook output as a dated snapshot at `specs/2026-06-01-personal-brand-workbook.md`.

**Rationale:** The workbook session surfaced material the existing docs were missing: a named audience tier (B2), an explicit Brand Statement in Ralston format, a forward-orientation reframe (walking in, not "left"), and an ideation table backing the toggle's content cadence. The hybrid output (canonical promotion plus a dated snapshot) preserves auditability without diluting the everyday brand-reference surface. The workbook's §15 (First Three Videos) was rejected as educator-coded and replaced with a Lindhardt and Dalen reference-coded skeleton; the rejection is documented in OPERATING.md so it does not get re-litigated when other frameworks suggest the same shape.

**Major decisions:**

- Audience (B2) added as primary: software engineers and SaaS or AI founders looking for a frontier where their existing skills compound into real-world impact.
- Brand Statement locked: *I believe engineers who want work that compounds into the real world should walk into life sciences, not wait for permission from the incumbents.*
- Walking-in reframe established (forward orientation, not "left pharma").
- Scout model adopted as internal framing (Oscar Lindhardt template with non-zero life sciences experience).
- Painful Problems v0 documented (12 rows; validate against 5+ peer-founder conversations in Phase 0).
- Ideation Table v1 documented (12 rows backing the toggle's content cadence).
- Ralston workbook §15 (First Three Videos) rejected as educator-coded; replaced with Lindhardt and Dalen reference-coded skeleton.

**Files touched:**

- `docs/brand/AUDIENCE.md` (new)
- `docs/brand/IDENTITY.md` (surgical additions: Brand Statement, Contrarians, Audience, Walking-In Scout)
- `docs/brand/OPERATING.md` (surgical additions: Editorial rules, Phase 0 capture targets, Phase 1 prep hooks, Documented brand decisions)
- `docs/brand/specs/2026-06-01-personal-brand-workbook.md` (new)
- `docs/brand/CHANGELOG.md` (this entry)

**Source:** `docs/brand/specs/2026-06-01-workbook-docs-design.md`

**Implementation:** `docs/brand/plans/2026-06-01-workbook-docs-implementation.md`

---

## 2026-05-28: Brand refinement via Ralston framework

**Decision:** Apply Caleb Ralston's reverse-order brand framework (outcome → known for → what to do → what to learn) to refine the brand. Settle on hybrid operator-creator positioning with Datavial and future Life Sciences products as primary income, content brand as serendipity engine and indirect credibility moat.

**Rationale:** The existing IDENTITY.md captured persona and voice well but left three things under-defined: the desired outcome (read as values, not outcome), the public-facing referral sentence (no industry-standard version existed), and the operational plan (no cadence, no phasing, no learning agenda). Working through Ralston's four steps in sequence produced concrete decisions on all three: two public referral sentences in industry-standard vocabulary ("He builds Life Sciences products" / "A tech founder seeking human connection through movement, food, and culture"), a four-platform surface map with phased roles, and a learning agenda focused on cinematic short-form production craft as the urgent gap.

**Source:** `docs/brand/specs/2026-05-28-brand-refinement-design.md`

**Implementation:** `docs/brand/plans/2026-05-28-brand-refinement-implementation.md`
