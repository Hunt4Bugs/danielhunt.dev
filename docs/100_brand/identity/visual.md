# Daniel Hunt — Visual Identity

The visual identity is an editorial publication crossed with a scientific journal, an art gallery, and a computational exhibit. Four converging metaphors. Same discipline.

For brand strategy, persona, and content principles, see [Identity](README.md) and [Strategy](../strategy/README.md). For implementation tokens, typography, geometry, components, and modes, see [design](../assets/design.md).

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
- Precise
- Computational, never dashboard-like

The aesthetic should not feel:

- Overly polished
- Hyper-luxury
- Performative
- Influencer-coded
- Sterile
- Corporate
- Fake cinematic
- Generic SaaS
- Tech-influencer dashboard

## The gallery frame

The site, dispatches, and content surfaces are framed as a publication and a gallery. Three implications.

**Work is the protagonist.** The creator is the curator, not the subject. The page is the white wall; the work hangs on it.

**Design recedes.** Whitespace, restraint, generous margins. The frame is quiet. The content speaks.

**Captions and labels are deferential.** Small, elegant, supporting. They point to the work; they do not compete with it.

**The visual object leads.** A photograph, video frame, diagram, or generative data object is the composition's protagonist. Interface exists only to locate, annotate, or contextualize that object.

> **The work is a visualization with just enough interface to understand it — never an interface decorated with a visualization.**

## The toggle, expressed visually

The brand's two halves (Build / Offline) are signaled through *atmospheric temperature*, not through different fonts or different content categories.

| Mode | Tonal pole | Frame | Reads like |
|---|---|---|---|
| Build | Dark / clinical — ink black, graphite, cloud white | Field report, lab notes | A digital laboratory at night |
| Offline | Atmospheric / editorial — the same dark frame with warmer photography | Magazine dispatch | A serious magazine feature |

Same typography, brand mark, spacing, and component grammar. Light mode is a supported preview state, not a separate brand.

## Typography

Three-role system.

**Satoshi Variable** — display. Used for hero headlines, major statements, wordmark, and monogram. Bold, contemporary, technical, and human.

**Inter** — body copy, UI, captions, utility text, and lower-thirds.

**JetBrains Mono** — data, code, coordinates, statuses, labels, and tables. It is the instrumentation voice, not the long-form voice.

Exact weights, scales, and fallbacks live in [design](../assets/design.md).

## Palette

### Brand palette (UI and design system)

The palette has two surfaces: a **brand concept layer** (the names used in this document and in design conversation) and the **CSS implementation layer** (the tokens that actually exist in [`site/css/site.css`](../../../site/css/site.css)). Both must stay in sync. When a value changes, update both layers and regenerate the committed `site/og.png` so the preview image reflects the new values.

| Brand concept | CSS var | Hex | Role |
|---|---|---|---|
| Ink Black | `--bg-0` | `#0A0C10` | Default dark canvas. |
| Graphite | `--surface-1` | `#14171C` | Panels, fields, and compact surfaces. |
| Soft Gray | `--surface-2` | `#1F232A` | Stronger surfaces and borders. |
| Cloud White | `--text-1` | `#F5F7FA` | Primary text. |
| Muted Text | `--text-2` | `#A1A7B3` | Supporting text and labels. |
| Electric Cyan | `--accent-primary` | `#00E5FF` | Software, systems, and infrastructure. |
| Acid Green | `--accent-secondary` | `#A6FF00` | Life sciences, data, and active state. |
| Daylight Green | `--accent-secondary-ui` | `#4A7000` in light mode | Accessible text, focus, and active state on light surfaces. Resolves to Acid Green in dark mode. |
| Ultraviolet | `--accent-tertiary` | `#B26BFF` | AI, models, and experimentation. |
| Signal Amber | `--accent-amber` | `#FFB020` | Strategy, business, and caution. |

Dark mode is the default digital laboratory. Light mode is a supported daylight preview with the same typography, spacing, hierarchy, components, and visualization grammar. Bright Acid Green remains the visualization color. Daylight Green replaces it only in light-mode interface text, focus, and state where contrast is functional.

**Typography stays neutral. Data earns color.** Choose one signal family per artifact, based on the subject. Signal colors may mark values, paths, key points, annotations, or a single terminal word; they do not become gradients, headline fills, or decorative chrome. There is no permanent brand color beyond the neutral system.

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
| Wordmark | `DANIEL HUNT` — all caps, Satoshi Variable, intentional letter-spacing | Site masthead, video intro card, anywhere with space |
| Monogram | `DH` — Satoshi Variable, no periods, no frame, no interlocking | Avatars, watermarks, sign-offs, compact contexts |
| `{D}` tribute | Internal codename | Repo, doc titles, source comments, X bio. Not a public brand mark. |

The wordmark must be composed *masthead-style* — anchored to a corner or margin, integrated with the page. Never composed as a monument-to-the-creator with a figure standing behind the letters.

The monogram is the wordmark *compressed*, not redesigned. Same family, same voice, smaller container. Recognition comes through repetition, not ornament.

## Page furniture

**No em-rules as page furniture.** Em-rules (`—`) are not used as section dividers, decorative breaks, sign-offs, watermarks, or typographic flourishes anywhere on the brand's public surfaces.

This rule is scoped to *page furniture* — the structural and decorative roles em-rules typically play in editorial design. It does **not** restrict the em-dash as a grammatical punctuation mark in long-form prose, where it functions as ordinary English punctuation rather than a typographic mark.

Acceptable furniture:

- Whitespace as the primary section break
- Numbered or named section labels in JetBrains Mono — `01`, `02`, or `01 · ON BUILDING`
- Mid-dot `·` for metadata separators — `DANIEL HUNT · SIMI VALLEY · 2026`
- Asterism `⁂` (centered) as a stronger break when a mark is required
- Hairline structural CSS rules (1px solid `--line`) for UI dividers — these are *structural*, not typographic
- Coordinates, timestamps, accession numbers, and status labels in small system mono when they establish the context of a visual object

## Information surfaces and visualization language

**Cards are instruments, not decoration.** An information surface earns its place only when it reveals a system state, source, method, annotation, or useful value. It is not a container for generic KPIs, decorative chips, or a conventional dashboard grid.

For the default content artifact, use:

1. One photograph, video frame, diagram, or data object
2. One hero visualization or computational object
3. One or two information surfaces at most
4. One editorial statement
5. Micro metadata that makes the object legible
6. One signal family selected by the topic

The visualization may pass behind and in front of a photographed subject. It should feel discovered in the image rather than placed on top of it: use occlusion, a restrained glow in dark mode, and annotations that attach to real points or regions.

Avoid dashboard conventions: KPI matrices, generic performance percentages, standard SaaS chart cards, large floating white panels, rainbow gradient headlines, and more than two competing surfaces. A static chart should be composed as an exhibit, not a report.

### Component grammar

| Component | Purpose | Rules |
|---|---|---|
| Exhibit label | Names or locates the primary object | Hairline edge, mono label, compact values; quiet enough to sit on media. |
| Instrument panel | Exposes a small set of real states | 3 to 6 rows, key/value alignment, no decorative metric uplift. |
| Annotation | Connects a fact to a point in the visual | Numbered, precise, anchored by a line or marker. |
| Data object | Carries the expressive color and motion | One primary object per composition; color encodes meaning. |
| Editorial statement | Gives the artifact its human point of view | Large Satoshi; always neutral. |

### Drop caps

Long-form dispatch openers may begin with a Satoshi drop cap, roughly 3-line height, in the neutral text color.

### Byline

Format: `DANIEL HUNT · [CITY] · [DATE]` in JetBrains Mono, around 12px, `--text-2`.

### Captions

Inter, 13–14px, `--text-2`, hanging directly below figures. No rule line above or below. Whitespace does the work.

### Pull quotes

Satoshi, larger than body, indented or set off with spacing or a hairline. Pull-quote typography stays neutral.

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

Preferred colors (from the content/mood palette): espresso, charcoal, olive, stone, ash, terracotta, umber, muted earth tones.

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

The site uses one clean black-and-white portrait as the featured media object. The title and instrumentation remain separate from the photograph so the person is contextualized rather than decorated.

### Near-term (Phase B)

The site uses a full-viewport spatial index for the profile surface and a dedicated, indexed Services route for commercial detail.

- Lead with the masthead wordmark `DANIEL HUNT`; on pointer hover or keyboard focus, it may temporarily become the active destination label
- Use the bento composition as navigation rather than a dashboard: About, Services, Contact, one profile signal, and one direct professional path
- Keep `Build in public. Live offline.` persistent in the profile header; use the dominant navigational tile for Services
- Use one clean black-and-white portrait exactly once on the home screen; do not repeat it as an avatar or place interface over the face or body
- Pair the portrait with one compact data object carrying Acid Green as the active Life Sciences / public-signal accent
- Keep all other typography and interface surfaces neutral; the accent appears only in state, focus, and the data object
- Preserve the same information architecture in daylight mode and on mobile, where the bento reflows into a four-row profile index
- Keep About and Contact as in-page detail states. Services links to `/services/`, where all offers and examples are server-delivered, semantic, and visible without interaction
- Keep the Services page interface-led: neutral glass panels, no repeated portrait, and Acid Green reserved for state and focus
- Give the Services hero one labeled connection map that starts with the business problem and routes to the five public capabilities. Pair each offer with one quiet line icon using the same signal family
- Tagline tense stays present (`Build` / `Live`), not past (`Built` / `Lived`)

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
| Site (Phase B, current) | Cool with warm spreads | Wordmark hero | Spatial index plus Services route; gallery discipline |
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
