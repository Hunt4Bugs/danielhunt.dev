# Brand Kit — Figma Variables (import guide)

This folder ships the danielhunt.dev brand system as a **design-tokens file**
([`brand-kit.tokens.json`](./brand-kit.tokens.json)) you can import straight into Figma
as native **Variables** — colour modes, type scale, and spacing — without rebuilding
anything by hand.

The values are the canonical ones from [`IDENTITY.md`](./IDENTITY.md),
[`VISUAL.md`](./VISUAL.md), and `site/css/site.css`. Those docs remain the source of
truth; this JSON is a generated projection of them for Figma.

> **Why a JSON import instead of the live Figma MCP connector?**
> The Figma connector attached to the remote build environment is the read-only
> (Dev Mode export) variant — it exposes only `download_assets`, not the authoring tool
> `use_figma`. So the kit is delivered as an importable token file. If/when a Figma MCP
> with write access is connected, the same tokens can instead be pushed directly as
> variables + text styles (the standby plan is in the repo's plan notes).

Target file: **https://www.figma.com/design/jhdVDcNWMLMtFoB7uizWeT/brand-kit**

---

## What you get after import

A `Color mode` variable collection with **two modes**:

| Variable | `Build / Cool` | `Offline / Warm` |
| --- | --- | --- |
| `bg` | `#FFFFFF` white | `#F3EFE8` cream |
| `text` | `#111111` ink | `#2B1F1A` espresso |
| `muted` | `#5A5A5A` | `#5A5A5A` |
| `quiet` | `#8A8F91` | `#8A8F91` |
| `line` | `#E2E2E2` | `#E2E2E2` |
| `lineStrong` | `#C8C8C8` | `#C8C8C8` |
| `accent` | `#6B1F2B` burgundy | `#6B1F2B` burgundy |

> The pole is defined by **canvas + primary text** (`bg`/`text`); the neutral greys and
> the burgundy accent are intentionally held constant across both modes — "same accent,
> mode shifts via proportion of warm vs cool." Tune the Offline greys later if you want
> warm-tinted structure.

A `Foundations` collection (single mode) with:

- **`type/font`** — `serif` = Instrument Serif, `sans` = Inter
- **`type/size`** — the full scale resolved to px (`heroTitle` 136 → `value` 10)
- **`type/lineHeight`** and **`type/letterSpacing`** — as % (e.g. wordmark tracking `6%`)
- **`space/*`** — section padding, container max, stack rhythm, gaps, paddings, radius

The raw **`palette`** set (white, ink, cream, espresso, burgundy, plus the
photography **mood** colours terracotta…onyx) feeds the semantic colours as a *source*
set, so it resolves into the mode values rather than creating duplicate variables.

> The seven **mood** hexes are **approximations** of the named photography/wardrobe
> palette (the docs name them but give no hex). Treat them as a starting point to
> calibrate against real graded footage.

---

## Import steps (Tokens Studio for Figma — free)

1. In the Figma file, open **Plugins → Browse plugins → "Tokens Studio for Figma"** and
   run it (a.k.a. *Figma Tokens*).
2. In the plugin: **⚙ / menu → Import** (or the **Tools → Load from file/preset**), and
   choose **single file**. Paste or upload the contents of
   [`brand-kit.tokens.json`](./brand-kit.tokens.json).
   - The plugin reads the `$themes` and `$metadata` blocks, so the token **sets**
     (`palette`, `mode/build`, `mode/offline`, `type`, `space`) and the **themes**
     (`Build / Cool`, `Offline / Warm`, `Foundations`) load automatically.
3. Open the **Themes** tab and confirm three themes exist in two groups
   (`Color mode`, `Foundations`).
4. Click **Export → Export to Figma → Variables** (Styles & Variables panel). Select
   **all themes**. Tokens Studio creates:
   - a **`Color mode`** collection with `Build / Cool` + `Offline / Warm` modes, and
   - a **`Foundations`** collection with the `type/*` and `space/*` variables.
5. (Optional) Also **Export → Text styles** if you want Instrument Serif / Inter text
   styles generated from the `type` tokens.

If you prefer the official **"Variables Import"** plugin instead, it accepts the same
JSON, but Tokens Studio is recommended because it understands the `$themes` → modes
mapping out of the box.

---

## Verifying the import

- The **Local variables** panel (right sidebar → **Variables**) shows a `Color mode`
  collection; switching its mode toggles `bg`/`text` between the cool and warm poles.
- `accent` reads `#6B1F2B` in both modes.
- `Foundations` holds the type scale and spacing values matching `site/css/site.css`.

## Re-generating

Edit the brand docs / `site/css/site.css`, update the matching values in
`brand-kit.tokens.json`, re-import, and re-export. Keep this file in lock-step with the
source-of-truth docs — it is a projection, not a second source of truth.
