# Brand Changelog

Append-only log of meaningful brand decisions. One entry per choice. Newest entries at the top.

Format per entry:

- Date (YYYY-MM-DD)
- Decision (one line)
- Rationale (1 to 3 sentences, why this choice over the alternatives)
- Source (link to spec, PR, or conversation)

---

## 2026-08-26: Short-form Script Assets and templates established

**Decision:** Keep Blueprint as the reusable Topic-specific communication plan. Add Script and Script Template as Asset subtypes, and add source-derived short-form hook taxonomies, templates, and skill-reference workflows.

**Rationale:** A Script is publication-oriented authored material, while a Blueprint must remain reusable across scripts, carousels, threads, and articles. The short-form method now supports reliable generation without treating unverified platform-performance claims as Brand facts.

**Source:** User-provided *3 Step Formula for High Impact Short Form* PDF and user-approved implementation plan on 2026-08-26.

**Implementation:** [Brand ontology v1](ONTOLOGY.md), [short-form Source](marketing/content/sources/colin-and-samir-short-form-anatomy.md), [Script Template](assets/templates/scripts/short-form-stop-hook-payoff.md), and [Content workflows](marketing/content/workflows/README.md).

---

## 2026-08-26: Brand ontology and context map established

**Decision:** Establish `Brand` as the root domain and document Identity, Strategy, Audience, Offers, Assets, Channels, Marketing, Analytics, and Relationships as bounded contexts. Treat Marketing as a first-class peer domain that owns Content, Campaigns, Distribution, Growth, and Funnel.

**Rationale:** The existing corpus held clear material but organized several cross-cutting concepts inside identity and operating documents. The ontology preserves durable brand meaning while giving reusable content work, assets, channel delivery, and learning clear ownership without introducing a database or automation system prematurely.

**Source:** User-approved Brand Ontology v1 design on 2026-08-26.

**Implementation:** [Brand domain map](README.md), [Brand ontology v1](ONTOLOGY.md), and the context references under `docs/100_brand/`.

---

## 2026-08-25: Services hero and offer visuals strengthened

**Decision:** Replace the oversized sentence-length Services H1 with a three-part editorial title, add one labeled capability map to the hero, and pair each service with a restrained line icon.

**Rationale:** At 1280 by 720, the previous title occupied 438 pixels and pushed the hero to 1,018 pixels. The new hierarchy reduces the title to 229 pixels and the hero to 704 pixels while explaining how the five offers connect to one business problem. One signal family keeps the additional visual detail consistent with the computational exhibit system.

**Source:** User-directed Services visual and readability refinement on 2026-08-25.

**Implementation:** `docs/100_brand/DESIGN.md`, `docs/100_brand/VISUAL.md`, `docs/200_site/ARCHITECTURE.md`, `site/services/index.html`, `site/css/site.css`

---

## 2026-08-25: Accessible daylight green established

**Decision:** Keep Acid Green as the dark-mode and visualization signal, then map light-mode interface text, focus, and active state to Daylight Green `#4A7000` through `--accent-secondary-ui`.

**Rationale:** Acid Green reaches only 1.16:1 contrast on the Cloud White canvas. Daylight Green reaches 5.42:1 while retaining the same semantic color family, so the light theme gains clarity without changing the brand's data palette.

**Source:** User-directed light-mode contrast refinement on 2026-08-25.

**Implementation:** `docs/100_brand/DESIGN.md`, `docs/100_brand/VISUAL.md`, `site/css/site.css`, `site/index.html`, `site/services/index.html`

---

## 2026-08-25: Workflow Automation prioritized and Lead Management consolidated

**Decision:** Move Workflow Automation to the first public offer and combine Lead Response Automation with Appointment Booking and Follow-Up under Lead Management.

**Rationale:** Workflow Automation is the broadest commercial entry point. Lead Management gives business owners one recognizable place for inquiry response, qualification, routing, booking, and follow-up without splitting one customer journey across two cards.

**Source:** User-directed Services hierarchy refinement on 2026-08-25.

**Implementation:** `docs/100_brand/IDENTITY.md`, `docs/200_site/ARCHITECTURE.md`, `site/index.html`, `site/services/index.html`, `site/css/site.css`, `site/llms.txt`

---

## 2026-08-25: Public Services list simplified

**Decision:** Present six customer-recognizable offers instead of leading the page with Sales Systems, Marketing Systems, Operations Systems, and Custom Software categories.

**Rationale:** Concrete names such as Lead Response Automation and Appointment Booking and Follow-Up reduce the translation required from a local business owner. The four-part taxonomy remains useful for internal organization, while the public page now pairs each service with one plain-language description.

**Source:** User feedback and structural review of the Landon Scales Services page on 2026-08-25. The reference informed the flat service-list pattern only. Its copy, claims, out-of-scope marketing programs, and service guarantees were not adopted.

**Implementation:** `docs/100_brand/IDENTITY.md`, `docs/200_site/ARCHITECTURE.md`, `site/index.html`, `site/services/index.html`, `site/css/site.css`, `site/llms.txt`

---

## 2026-08-25: Commercial Services route and taxonomy established

**Decision:** Move Services to `/services/` and define the offer through Sales Systems, Marketing Systems, Operations Systems, and Custom Software.

**Rationale:** A dedicated static route makes concrete service examples visible to visitors and crawlers without requiring a click or JavaScript. It also separates the broader commercial-services audience from the Life Sciences editorial audience while keeping one technology-led brand system.

**Source:** User-approved Vexoo hover, concrete Services, and SEO landing-page plan on 2026-08-25.

**Implementation:** `docs/100_brand/IDENTITY.md`, `docs/100_brand/AUDIENCE.md`, `docs/100_brand/DESIGN.md`, `docs/100_brand/VISUAL.md`, `docs/200_site/ARCHITECTURE.md`, `site/index.html`, `site/services/index.html`, `site/css/site.css`, `site/js/site.js`, `site/sitemap.xml`, `site/llms.txt`

---

## 2026-08-25: Services replaces the repeated thesis tile

**Decision:** Move `Build in public. Live offline.` into the persistent profile header and repurpose the dominant navigation tile as Services.

**Rationale:** The prior composition repeated the thesis in the header hierarchy and the largest tile without adding a new destination. Services gives the dominant tile a clear commercial purpose while keeping the offer narrow, evidence-backed, and consistent with the Life Sciences product narrative.

**Source:** User-directed site refinement on 2026-08-25.

**Implementation:** `docs/100_brand/IDENTITY.md`, `docs/100_brand/VISUAL.md`, `site/index.html`, `site/css/site.css`, `site/js/site.js`

---

## 2026-08-25: Spatial profile index adopted

**Decision:** Replace the prior cinematic profile stage with a Vexoo-derived, full-viewport spatial index while retaining the canonical `design.md` system and one-page architecture.

**Rationale:** The index gives the brand a more immediate social-profile rhythm without duplicating the portrait or drifting into dashboard UI. One monochrome headshot carries the human layer, the profile-signal object carries the active Acid Green state, and the remaining surfaces stay neutral and navigational.

**Source:** User-selected Vexoo Framer template, adapted to Daniel Hunt's canonical identity and visual rules on 2026-08-25.

**Implementation:** `docs/100_brand/DESIGN.md`, `docs/100_brand/VISUAL.md`, `site/index.html`, `site/css/site.css`, `site/js/site.js`

---

## 2026-08-25: Cinematic social-profile stage adopted

**Decision:** Use a framed social-profile composition for the Phase B homepage: one clean black-and-white portrait, one editorial identity block, and one compact Dataland signal visualization in place of a repeated portrait avatar.

**Rationale:** The composition brings the cinematic scale and social immediacy of the selected references into the existing computational exhibit system without turning the site into a dashboard or duplicating the creator image. The portrait stays human and unedited; the visualization carries the expressive system language.

**Source:** Product Design ideation and selected hybrid of options 2 and 1, refined on 2026-08-25.

**Implementation:** `docs/100_brand/DESIGN.md`, `docs/100_brand/VISUAL.md`, `site/index.html`, `site/css/site.css`, `site/js/site.js`, `site/images/profile-signal-v1.png`

---

## 2026-08-24: Legacy burgundy accent removed

**Decision:** Remove burgundy from the public interface and use only the topic-led `design.md` accents: Acid Green, Electric Cyan, Ultraviolet, and Signal Amber.

**Rationale:** A fixed personality color conflicts with the visualization-first system, in which color conveys the subject's data or context and typography remains neutral.

**Source:** Follow-up to ChatGPT conversation “AI Inspiration Reflection” (`6a8c7cbc-7088-83ea-8f96-6988a8447475`)

---

## 2026-08-24: Computational exhibit system added

**Decision:** Extend the visual system with an archival light mode, a digital-laboratory dark mode, and visualization-first content grammar.

**Rationale:** The previous system established editorial and gallery restraint but did not specify how technical work should coexist with cinematic media. The new rules make data or media the protagonist, constrain cards to functional instruments, and keep color semantic rather than decorative.

**Source:** ChatGPT conversation “AI Inspiration Reflection” (`6a8c7cbc-7088-83ea-8f96-6988a8447475`)

**Implementation:** `docs/100_brand/VISUAL.md`, `site/css/site.css`, `site/index.html`, `site/brand/index.html`

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

- `docs/100_brand/AUDIENCE.md` (new)
- `docs/100_brand/IDENTITY.md` (surgical additions: Brand Statement, Contrarians, Audience, Walking-In Scout)
- `docs/100_brand/OPERATING.md` (surgical additions: Editorial rules, Phase 0 capture targets, Phase 1 prep hooks, Documented brand decisions)
- `docs/100_brand/specs/2026-06-01-personal-brand-workbook.md` (new)
- `docs/100_brand/CHANGELOG.md` (this entry)

**Source:** `docs/100_brand/specs/2026-06-01-workbook-docs-design.md`

**Implementation:** `docs/100_brand/plans/2026-06-01-workbook-docs-implementation.md`

---

## 2026-05-28: Brand refinement via Ralston framework

**Decision:** Apply Caleb Ralston's reverse-order brand framework (outcome → known for → what to do → what to learn) to refine the brand. Settle on hybrid operator-creator positioning with Datavial and future Life Sciences products as primary income, content brand as serendipity engine and indirect credibility moat.

**Rationale:** The existing IDENTITY.md captured persona and voice well but left three things under-defined: the desired outcome (read as values, not outcome), the public-facing referral sentence (no industry-standard version existed), and the operational plan (no cadence, no phasing, no learning agenda). Working through Ralston's four steps in sequence produced concrete decisions on all three: two public referral sentences in industry-standard vocabulary ("He builds Life Sciences products" / "A tech founder seeking human connection through movement, food, and culture"), a four-platform surface map with phased roles, and a learning agenda focused on cinematic short-form production craft as the urgent gap.

**Source:** `docs/100_brand/specs/2026-05-28-brand-refinement-design.md`

**Implementation:** `docs/100_brand/plans/2026-05-28-brand-refinement-implementation.md`
