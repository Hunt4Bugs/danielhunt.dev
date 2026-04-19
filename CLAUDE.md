# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal consulting site for Daniel Hunt (danielhunt.dev) — a single-page static site. Not a Next.js project.

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
- **Google Fonts**: Fraunces (display/serif) + Inter (UI/sans)
- Deployed to **GitHub Pages** via `withastro/action@v3` on push to `main`

## Architecture

Single-page site with one route (`src/pages/index.astro`) that composes section components in order: Nav → Hero → Services → About → Faq → Contact → Footer.

**Key files:**
- `src/data/site.ts` — single source of truth for all brand copy, services list, FAQs, social URLs, and SEO keywords. Components import from here rather than hardcoding content.
- `src/layouts/Layout.astro` — HTML shell, font loading, SEO component, and scroll-reveal script.
- `src/components/SEO.astro` — meta tags, Open Graph, and JSON-LD structured data.
- `src/styles/global.css` — base styles, scroll-reveal animations, grain overlay texture.
- `tailwind.config.mjs` — custom color palette (cream/parchment/espresso/cocoa/rust/mustard/forest) and font families.

**Scroll-reveal pattern:** Elements with class `reveal` are animated into view via IntersectionObserver (defined in Layout.astro). Staggered delays use `reveal-delay-1` through `reveal-delay-4` (safelisted in Tailwind config).

## Setup TODO

- Contact form reads its Web3Forms access key from the `PUBLIC_WEB3FORMS_KEY` env var. Set it locally in `.env` and as a GitHub Actions secret of the same name so it's injected at build time. Without it, the form degrades to an inline "email directly" message instead of submitting.
