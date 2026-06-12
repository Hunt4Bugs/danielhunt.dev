# Daniel Hunt — Visual Identity

The visual identity is an editorial publication crossed with a scientific journal crossed with an art gallery. Three converging metaphors. Same discipline.

For brand strategy, persona, and content principles, see [IDENTITY.md](IDENTITY.md).

## Core visual philosophy

The visuals communicate movement, atmosphere, curiosity, reflection, humanity.

The aesthetic should feel:

- Lived-in
- Cinematic but restrained
- Grounded
- Textured
- Intentional
- Observant
- Human

The aesthetic should not feel:

- Overly polished
- Hyper-luxury
- Performative
- Influencer-coded
- Sterile
- Corporate
- Fake cinematic

## The gallery frame

The site, dispatches, and content surfaces are framed as a publication and a gallery. Three implications.

**Work is the protagonist.** The creator is the curator, not the subject. The page is the white wall; the work hangs on it.

**Design recedes.** Whitespace, restraint, generous margins. The frame is quiet. The content speaks.

**Captions and labels are deferential.** Small, elegant, supporting. They point to the work; they do not compete with it.

## The toggle, expressed visually

The brand's two halves (Build / Offline) are signaled through *atmospheric temperature*, not through different fonts or different content categories.

| Mode | Tonal pole | Frame | Reads like |
|---|---|---|---|
| Build | Cool / clinical — white, ink, gray dominant | Field report, lab notes | A scientific journal article |
| Offline | Warm / editorial — cream, espresso dominant | Magazine dispatch | A serious magazine feature |

Same typography. Same brand mark. Same accent. The mode shifts via *proportion* of warm vs. cool.

## Typography

Two-font system.

**Instrument Serif** — display, serif. Used for headlines, drop caps, brand wordmark, monogram, byline. Sharp, contemporary editorial voice; one weight (regular + italic), which enforces restraint.

**Inter** — body copy, UI, captions, utility text, lower-thirds. Neutral, clean, doesn't fight Instrument Serif.

Use Instrument Serif for the wordmark and major headlines — display roles only; it ships in a single weight and is not a long-form text face. Use Inter for everything else, including long-form body.

No third font. No monospaced terminal aesthetic in public surfaces. The `{D}` tribute lives in repo and X bio, not in the typography.

## Palette

### Brand palette (UI and design system)

The palette has two surfaces: a **brand concept layer** (the names used in this document and in design conversation) and the **CSS implementation layer** (the tokens that actually exist in [`site/css/site.css`](../../site/css/site.css)). Both must stay in sync. When a value changes, update both layers and regenerate the committed `site/og.png` so the preview image reflects the new values.

| Brand concept | CSS var | Hex | Role |
|---|---|---|---|
| White | `--bg` | `#FFFFFF` | Primary canvas. Default for both modes. Dominant in Build mode. |
| Ink | `--text` | `#111111` | Primary text, structural elements. Clinical pole. |
| Muted gray | `--muted` | `#5A5A5A` | Secondary text. |
| Quiet gray | `--quiet` | `#8A8F91` | Tertiary text, captions, swatch labels. |
| Hairline | `--line` | `#E2E2E2` | Hairline structural rules. UI dividers. |
| Hairline strong | `--line-strong` | `#C8C8C8` | Stronger structural rules. |
| Cream | `--cream` | `#F3EFE8` | Situational secondary canvas. Magazine-style content blocks, Offline-mode spreads. |
| Espresso | `--espresso` | `#2B1F1A` | Warm-pole structural element. Masthead, logo, Offline-mode headers, warmth anchor. |
| Burgundy | `--accent` | `#6B1F2B` | The single personality color. Logo mark, hover/focus, key markers, pull quotes. |

### Content / mood palette (not the design system)

These appear in *photography, wardrobe, environments, atmospheric description* — never as UI tokens. They are vocabulary for content production, not design tokens.

- Terracotta — earth, movement, travel
- Olive — utilitarian, outdoor, military-influenced
- Umber — wood grain, leather, depth
- Stone — natural fiber, calm
- Ash — urban realism, concrete
- Charcoal — cinematic shadow
- Onyx — depth, night

## Brand mark system

| Element | Form | Where |
|---|---|---|
| Wordmark | `DANIEL HUNT` — all caps, Instrument Serif, intentional letter-spacing | Site masthead, video intro card, anywhere with space |
| Monogram | `DH` — Instrument Serif, no periods, no frame, no interlocking | Avatars, watermarks, sign-offs, compact contexts |
| `{D}` tribute | Internal codename | Repo, doc titles, source comments, X bio. Not a public brand mark. |

The wordmark must be composed *masthead-style* — anchored to a corner or margin, integrated with the page. Never composed as a monument-to-the-creator with a figure standing behind the letters.

The monogram is the wordmark *compressed*, not redesigned. Same family, same voice, smaller container. Recognition comes through repetition, not ornament.

## Page furniture

**No em-rules as page furniture.** Em-rules (`—`) are not used as section dividers, decorative breaks, sign-offs, watermarks, or typographic flourishes anywhere on the brand's public surfaces.

This rule is scoped to *page furniture* — the structural and decorative roles em-rules typically play in editorial design. It does **not** restrict the em-dash as a grammatical punctuation mark in long-form prose, where it functions as ordinary English punctuation rather than a typographic mark.

Acceptable furniture:

- Whitespace as the primary section break
- Numbered or named section labels in small-caps Instrument Serif — `I.`, `II.`, or `I · ON BUILDING`
- Mid-dot `·` for metadata separators — `DANIEL HUNT · SIMI VALLEY · 2026`
- Asterism `⁂` (centered) as a stronger break when a mark is required
- Hairline structural CSS rules (1px solid `--line`) for UI dividers — these are *structural*, not typographic

### Drop caps

Long-form dispatch openers begin with an Instrument Serif drop cap, roughly 3-line height, in `--espresso` (Offline mode) or `--text` (Build mode).

### Byline

Format: `DANIEL HUNT · [CITY] · [DATE]` in small-caps Inter, around 12px, `--quiet`.

### Captions

Inter italic, 13–14px, `--quiet`, hanging directly below figures. No rule line above or below. Whitespace does the work.

### Pull quotes

Instrument Serif Italic, larger than body, indented or set off with `--accent` for the opening mark.

## Imagery style

The brand commits to **cinematic-high-production *technique* applied to documentary *subject matter*, with Bourdain *restraint* in post.**

| Layer | Direction |
|---|---|
| Shoot | Intentional camera. Gimbal acceptable. Controlled framing. Color grade in post. |
| Subject | Real moments. Real people. Real environments. No staged "lifestyle" shots. |
| Sound | Natural sound preferred. Music used sparingly, never as wall-to-wall bed. |
| Cuts | Edits that breathe. No rapid MTV pacing. Silences are allowed. |
| VO and captions | Sparse. Literary. Observational. Never explanatory. |

The polish is in the *craft*. Not in the *grammar*.

## Color grading

Focus on:

- Warm highlights
- Soft contrast
- Natural skin tones
- Deep shadows
- Muted saturation
- Filmic softness

Avoid:

- Teal/orange extremes
- Pushed greens (Dalen-coded)
- HDR over-processing
- Over-sharpening
- Heavy LUT dependency

The image should feel natural, atmospheric, grounded, emotionally honest.

## Lighting

Prefer: natural light, golden hour, cloudy daylight, practical indoor lighting, tungsten warmth, moody nighttime lighting, diffused shadows.

Avoid: overexposed influencer lighting, hyper-bright studio lighting, color-heavy RGB setups.

## Cinematic feel

The visual identity resembles documentary filmmaking, cinematic travel films, reflective urban photography, grounded lifestyle storytelling.

The camera should feel observational, patient, immersive, human.

Avoid excessive transitions, over-editing, hyperactive pacing, empty "cinematic" montages.

Emotion comes from environments, pacing, framing, texture, movement, silence, human moments.

## Environments

Preferred environments:

- Cafés, local restaurants
- Airports, train stations
- Martial arts gyms
- Streets, alleyways, rooftops
- Small apartments, hotel rooms
- Night walks, rainy streets, city mornings
- Bookstores, convenience stores
- Recovery spaces

The world should feel explored, participated in, lived through. Not staged for content.

## Wardrobe

Wardrobe should feel minimal, functional, textured, mature, grounded, timeless.

Preferred colors (from the content/mood palette): espresso, charcoal, olive, stone, ash, burgundy, umber, muted earth tones.

Preferred textures: heavyweight cotton, wool, washed fabrics, technical fabrics, leather, canvas.

Avoid: loud logos, hypebeast aesthetics, trendy fashion, excessive jewelry, luxury signaling.

The creator should look naturally put together. Functional, lived-in, understated.

## Photography and framing

Preferred:

- Environmental storytelling
- Negative space
- Candid moments
- Movement
- Reflections, layering
- Observational compositions

Subjects should feel immersed in environments, moving through spaces, naturally present.

Avoid:

- Constant eye contact with camera
- Forced poses
- Exaggerated reactions
- Main-character framing

## Site implications

The current site is a portrait-led hero with the creator as visual focal point. This directly contradicts the gallery frame and must be restructured.

### Near-term (Phase B)

The site stays a one-page brand surface, but the hero shifts to gallery-compliant.

- Lead with wordmark `DANIEL HUNT` at masthead scale
- Tagline `Build in public. Live offline.` directly under
- Sub-thesis `Tech, movement, and culture.` directly under that
- One featured-work slot: a single image, a recent dispatch headline, or a quiet status block (`Currently building Datavial · Currently in Simi Valley`)
- Portrait demotes to the About section, smaller (~28rem max), captioned, framed
- Contact links accessible but not the visual anchor
- Tagline tense: present (`Build` / `Live`), not past (`Built` / `Lived`)

### Future (Phase C)

When content fills it, the site restructures as a publication home:

- **Masthead** — wordmark + thesis
- **Dispatches** — archive of offline cinematic shorts
- **Field Notes** — archive of build talking-head + linked X threads
- **Projects** — Datavial, Roundz, others, framed as field reports, not portfolio brag
- **About** — the curator's bio, smaller, secondary
- **Contact**

## Cross-surface application

| Surface | Dominant pole | Mark | Notes |
|---|---|---|---|
| Site (Phase B, current) | Cool with warm spreads | Wordmark hero | Gallery discipline |
| Site (Phase C, future) | Cool with warm spreads | Wordmark masthead | Publication structure |
| IG profile | Cool / clinical | Monogram avatar | Offline content lives here |
| IG Reel covers | Mode-appropriate | Wordmark or monogram corner | Cinematic, restrained |
| IG carousels | Mode-appropriate | Monogram sign-off on final slide | Editorial templating |
| X profile | Cool / clinical, `{D}` in bio | Monogram avatar | Build journaling lives here |
| Talking-head lower-third | Cool / clinical | Monogram + wordmark | Build retrospectives |
| YouTube channel art | TBD when activated | TBD | Future surface |

## Overall feeling

The brand should visually feel like:

> Someone thoughtfully moving through the modern world trying to understand it better — making things with his hands while keeping his eyes off the screen.

The visuals create: curiosity, calmness, emotional texture, grounded inspiration, reflection, perspective.

Not: envy, intimidation, perfection, hyper-performance, unattainable luxury.
