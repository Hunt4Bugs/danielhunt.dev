# Daniel Hunt — Design System

Version 1.0. This file is the reusable implementation contract for the website, social graphics, video titles, charts, carousels, and future brand surfaces. `IDENTITY.md` owns meaning and voice. `VISUAL.md` owns photography and editorial art direction. This file owns tokens, typography, geometry, components, and modes.

## Principles

1. **Data-first.** Lead with insight. Design reveals the story.
2. **Quiet interface.** Remove noise. Elevate what matters.
3. **Visualization as hero.** Make data beautiful, legible, and alive.
4. **Technical but human.** Pair engineering rigor with empathy and clarity.
5. **Modular and reusable.** Build once; compose everywhere.

## Color tokens

Dark mode is the default. Light mode is a supported preview or situational mode, not a separate visual language.

```css
:root {
  --bg-0: 10 12 16;               /* #0A0C10 · Ink Black */
  --surface-1: 20 23 28;          /* #14171C · Graphite */
  --surface-2: 31 35 42;          /* #1F232A · Soft Gray */
  --text-1: 245 247 250;          /* #F5F7FA · Cloud White */
  --text-2: 161 167 179;          /* #A1A7B3 · Muted text */
  --accent-primary: 0 229 255;    /* #00E5FF · Electric Cyan */
  --accent-secondary: 166 255 0;  /* #A6FF00 · Acid Green */
  --accent-tertiary: 178 107 255; /* #B26BFF · Ultraviolet */
  --accent-amber: 255 176 32;     /* #FFB020 · Signal Amber */
}
```

### Accent selection

Accent colors are semantic and swappable by topic. Choose one lead accent per artifact. Supporting accents may appear only when the data requires multiple series.

| Topic | Lead token | Role |
|---|---|---|
| Software, systems, infrastructure | `--accent-primary` | Electric cyan |
| Life sciences, data, active status | `--accent-secondary` | Acid green |
| AI, models, experimentation | `--accent-tertiary` | Ultraviolet |
| Strategy, business, caution | `--accent-amber` | Signal amber |

Typography remains neutral. Accent color belongs to data, state, focus, and a single meaningful word or marker. Never use a multicolor headline gradient.

### Light mode

Light mode maps the same system into daylight conditions:

```css
[data-theme="light"] {
  --bg-0: 245 247 250;
  --surface-1: 255 255 255;
  --surface-2: 231 235 240;
  --text-1: 10 12 16;
  --text-2: 91 98 109;
}
```

For review and brand production, append `?theme=light` or `?theme=dark` to a local site URL. The preview is URL-scoped and does not change the dark default or store a visitor preference.

## Typography

| Role | Family | Weight | Use |
|---|---|---:|---|
| Display | Satoshi Variable | 700 | Hero headlines and major statements |
| Body | Inter | 400 | Paragraphs and interfaces |
| Mono / data | JetBrains Mono | 400 | Data, code, coordinates, labels, and tables |
| Caption | Inter | 500 | Supporting information and labels |

- Display: `clamp(3.5rem, 9vw, 8.5rem)`, line-height `0.96–1.02`, letter-spacing `-0.04em`. Use the upper end when adjacent lines contain descenders and capitals that would otherwise collide.
- Section heading: `clamp(2rem, 5vw, 4.5rem)`, line-height `1`.
- Body: `1rem–1.125rem`, line-height `1.6–1.8`.
- Metadata: `0.6875rem–0.75rem`, line-height `1.4`, tracking `0.08–0.14em`.

## Spacing and geometry

The base unit is 8px.

| Token | Value |
|---|---:|
| `--space-1` | 4px |
| `--space-2` | 8px |
| `--space-3` | 12px |
| `--space-4` | 16px |
| `--space-6` | 24px |
| `--space-8` | 32px |
| `--space-12` | 48px |
| `--space-16` | 64px |
| `--space-24` | 96px |
| `--space-32` | 128px |

| Token | Value | Use |
|---|---:|---|
| `--radius-sm` | 4px | Tiny controls |
| `--radius-md` | 8px | Buttons, fields, compact labels |
| `--radius-lg` | 16px | Panels and media frames |
| `--radius-xl` | 24px | Large feature surfaces |
| `--radius-full` | 9999px | Status dots and pills |

Borders are 1px and low contrast. Default blur is 12px. Shadows are deep and diffuse; they must never make the interface feel glossy or consumer-app-like.

## Surfaces

### Base surface

Use `--bg-0` for the canvas. Major sections are separated by space or a 1px `--surface-2` rule.

### Instrument panel

Use `--surface-1` at 78–88% opacity with a `--surface-2` border and 12px backdrop blur. An instrument panel exposes a real state, method, source, or small group of values. It is never a decorative empty card.

### Glass overlay

Use only over photography or visualization. Maximum two overlays in one composition. The subject remains unobstructed, and the overlay must disclose useful information.

### Spatial index tile

The Vexoo-derived profile index uses a lighter frosted treatment than an instrument panel: a 4% dark-mode / 5% light-mode `--text-1` tint over a transparent base, a low-contrast inset edge, and backdrop blur. These calibrated values produce the same perceived 8% tint as the pure black/white reference while preserving the brand's off-neutral Ink Black and Cloud White canvases. Desktop uses 10px blur and a 32px radius; mobile uses 4px blur and `--radius-xl` (24px). Hover changes the identity wordmark rather than lifting or outlining the tile. Acid Green remains reserved for keyboard focus and active state.

## Components

- **Status label:** mono text, one 6px semantic dot, no filled chip unless selected.
- **Button:** neutral by default; lead accent on hover and focus. Minimum 44px target.
- **Field:** `--surface-1` fill, `--surface-2` border, accent focus ring.
- **Exhibit label:** mono metadata paired with a real object, image, coordinate, date, or status.
- **Instrument panel:** 3–6 concise key/value rows; no invented KPIs.
- **Profile signal:** a compact identity/status instrument pairing a handle and real state with one visualization object. On portrait-led surfaces, use the visualization instead of repeating the portrait as an avatar.
- **Chart container:** restrained frame, faint axes, semantic series colors, direct labels where possible.
- **Navigation:** quiet, compact, neutral, with one semantic active marker.

## Visualization language

- Data is the expressive layer; interface is the quiet layer.
- Prefer direct labels, sparse gridlines, and one highlighted point.
- Use cyan and violet for distinct series; green for active, correct, or improving; amber for caution or business context.
- Use color to encode meaning, not decoration.
- Do not use rainbow gradients, generic KPI walls, conventional dashboard grids, or charts without a real data source.

## Content templates

1. **Photo + overlay:** one documentary frame, one useful instrument panel, micro metadata.
2. **Editorial carousel:** one large statement, one supporting paragraph, page number, and one accent family.
3. **Visualization hero:** one chart or data object carries the composition; interface recedes.
4. **Short-form cover:** one statement, one small label, and one signal marker.
5. **Cinematic profile:** one large monochrome portrait, one editorial identity block, and one compact profile signal. The portrait appears once and remains free of decorative overlays.
6. **Spatial index:** a full-viewport navigation composition with one neutral wordmark, one monochrome portrait, one profile-signal data object, and a small set of functional destination cards. Hover or focus may replace the wordmark with the active destination label. Cards remain neutral; the selected topic supplies one semantic accent.

## Photography

Use real documentary photography. For the website, portraits are black-and-white unless a specific editorial story earns color. Never synthesize a replacement likeness. Do not place decorative graphics over a portrait unless the artifact explicitly needs an information overlay.

## Motion

Motion should clarify hierarchy: a single load reveal, a deliberate hover/focus transition, or a data-state change. Respect `prefers-reduced-motion`. Avoid ambient motion that competes with the content.

## Governance

- New brand components must consume these tokens rather than introduce raw colors, one-off radii, or arbitrary spacing.
- When the same pattern appears twice, promote it into a named component.
- `site/css/site.css` is the website implementation of this contract.
- `site/brand/index.html` is the public specimen page.
- Review dark mode, light mode, desktop, and mobile before approving a reusable component.
