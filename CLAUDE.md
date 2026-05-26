# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal brand surface for Daniel Hunt (danielhunt.dev) — a single-page static site that serves as credibility + contact path for the content brand. Not a content publication itself (content lives on IG, X, YouTube, eventually a newsletter). Not a Next.js project.

For brand strategy, persona, voice, typography, palette, marks, and visual rules: see [`docs/brand/IDENTITY.md`](docs/brand/IDENTITY.md) and [`docs/brand/VISUAL.md`](docs/brand/VISUAL.md) — these are the source of truth. Update them before changing anything brand-shaped on the site.

## Commands

```bash
npm install          # install dependencies
npm run dev          # dev server at http://localhost:4321
npm run build        # static build → ./dist
npm run preview      # preview production build locally
```

There are no tests or linting configured.

## Stack

- **Astro 4** (static output, no SSR)
- **Tailwind CSS 3** via `@astrojs/tailwind`
- **Google Fonts**: Fraunces (display + serif, headlines/wordmark/monogram) + Inter (body + UI). No third font. No monospaced terminal aesthetic in public surfaces.
- Deployed to **GitHub Pages** via `withastro/action@v3` on push to `main`

## Architecture

Single-page site with one route (`src/pages/index.astro`) composing section components in order: Nav → Hero → About → Contact → Footer.

A separate `/brand` page (`src/pages/brand.astro`) serves as the public-facing brand-system reference (wordmark, monogram, palette, typography, principles).

**Key files:**

- `src/data/site.ts` — single source of truth for brand copy (name, tagline, sub-thesis, location, socials, SEO keywords). Components import from here rather than hardcoding.
- `src/layouts/Layout.astro` — HTML shell, font loading (Fraunces + Inter), SEO component, scroll-reveal script.
- `src/components/SEO.astro` — meta tags, Open Graph, JSON-LD structured data.
- `src/pages/og.png.ts` — runtime OG image generator (satori + resvg). Renders the brand's Open Graph preview.
- `src/styles/global.css` — base styles, palette tokens (cool pole + warm pole + accent), display/wordmark/monogram classes, scroll-reveal animations.
- `tailwind.config.mjs` — registers `font-sans` (Inter) and `font-serif` (Fraunces). Color tokens are CSS variables consumed by Tailwind utilities.

**Palette tokens** (in `global.css`):

- Cool pole (default): `--bg` white, `--text` ink (#111), `--muted` `--quiet` `--line` `--line-strong` derived grays
- Warm pole (situational): `--cream` warm canvas, `--espresso` warm structural
- Accent: `--accent` burgundy

**Scroll-reveal pattern:** Elements with class `reveal` animate into view via IntersectionObserver (defined in Layout.astro). Staggered delays use `reveal-delay-1` through `reveal-delay-4` (safelisted in Tailwind config).

**Brand surface phasing:**

- **Phase B (current)**: one-page brand surface — wordmark masthead + tagline + sub-thesis + currently-building/currently-in status block + contact links. Portrait demoted to About section. Gallery-frame discipline (work-as-protagonist, creator-as-curator).
- **Phase C (future, when content exists)**: site restructures as a publication home with Dispatches archive, Field Notes archive, Projects section, About, Contact.

## Setup TODO

- Contact form reads its Web3Forms access key from the `PUBLIC_WEB3FORMS_KEY` env var. Set it locally in `.env` and as a GitHub Actions secret of the same name so it's injected at build time. Without it, the form degrades to an inline "email directly" message instead of submitting.
