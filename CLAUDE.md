# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal brand surface for Daniel Hunt (danielhunt.dev) — a single-page static site that serves as credibility + contact path for the content brand. Not a content publication itself (content lives on IG, X, YouTube, eventually a newsletter).

For brand strategy, persona, voice, typography, palette, marks, and visual rules: see [`docs/100_brand/IDENTITY.md`](docs/100_brand/IDENTITY.md) and [`docs/100_brand/VISUAL.md`](docs/100_brand/VISUAL.md) — these are the source of truth. Update them before changing anything brand-shaped on the site.

## Commands

There is no install step, no build step, and no framework. The deployable site is the `site/` directory, served as-is.

```bash
python3 -m http.server 8000 --directory site   # dev server at http://localhost:8000
# or: npx serve site
```

There are no tests or linting configured.

## Stack

- **Plain HTML + handwritten CSS + vanilla JS** — HTML-first, zero build
- **htmx 2.x** (vendored at `site/js/htmx.min.js`, no CDN) — powers the contact form
- **HTML web components** (`<site-nav>`, `<site-footer>` in `site/js/site.js`) — shared page chrome across pages
- **Google Fonts**: Instrument Serif (display, headlines/wordmark/monogram — single weight, regular + italic) + Inter (body + UI). No third font. No monospaced terminal aesthetic in public surfaces.
- Deployed to **GitHub Pages**: `actions/upload-pages-artifact` uploads `site/` directly on push to `main` (no build action)

## Architecture

Everything deployable lives in `site/`; everything else in the repo (docs, this file) is not published.

```
site/
  index.html          # the one-page site: head/meta + Hero, About, Contact (+ form)
  brand/index.html    # public brand-system reference, served at /brand
  css/site.css        # single stylesheet: tokens + reset + semantic classes
  js/site.js          # web components (<site-nav>, <site-footer>), mobile menu,
                      #   LA time, scroll-reveal IntersectionObserver
  js/htmx.min.js      # vendored htmx 2.x
  og.png              # committed static OG image (see note below)
  .nojekyll           # required — keeps GitHub Pages from running Jekyll
  favicon.svg, CNAME, robots.txt, sitemap.xml, humans.txt, llms.txt, images/
```

**Key facts:**

- **Head metadata is statically duplicated** in each HTML page (OG, Twitter, JSON-LD) because crawlers don't run JS. The visible shared chrome (nav/footer) is JS-rendered via web components — meaning no-JS visitors see content but no nav/footer; all content and SEO stays static.
- **`site/js/site.js`** holds the shared `SITE` constants (name, email, socials, location) for JS-rendered chrome; static page copy is written directly in the HTML.
- **Contact form** posts to Web3Forms via htmx (`hx-post` + `hx-swap="none"` + `hx-on::after-request` reading `event.detail.successful` to show an inline status). Two load-bearing details: the `htmx-config` meta tag sets `selfRequestsOnly:false` (htmx 2.x blocks cross-origin requests by default), and `hx-on::config-request` strips htmx's `HX-*` headers (Web3Forms' CORS preflight rejects them). The form keeps real `action`/`method` so it degrades to a native POST without JS.
- **Web3Forms access key**: the committed HTML contains `WEB3FORMS_KEY_PLACEHOLDER`; the deploy workflow `sed`-injects the `PUBLIC_WEB3FORMS_KEY` repo secret at deploy time (the key is public-by-design). Locally the form errors gracefully ("email me directly") unless you temporarily sed in a real key.
- **og.png is a committed static asset** (1200×630). It was generated once by the old satori + resvg pipeline, which lives in git history at `src/pages/og.png.ts` if it ever needs regenerating. `.gitignore` has a `!site/**/*.png` exception for it.

**Palette tokens** (in `site/css/site.css`):

- Cool pole (default): `--bg` white, `--text` ink (#111), `--muted` `--quiet` `--line` `--line-strong` derived grays
- Warm pole (situational): `--cream` warm canvas, `--espresso` warm structural
- Accent: `--accent` burgundy

**Scroll-reveal pattern:** Elements with class `reveal` animate into view via IntersectionObserver (defined in `site/js/site.js`). Staggered delays use `reveal-delay-1` through `reveal-delay-4`. The CSS/JS infrastructure exists but no current markup uses it.

**Brand surface phasing:**

- **Phase B (current)**: one-page brand surface — wordmark masthead + tagline + sub-thesis + currently-building/currently-in status block + contact links + contact form. Portrait demoted to About section. Gallery-frame discipline (work-as-protagonist, creator-as-curator).
- **Phase C (future, when content exists)**: site restructures as a publication home with Dispatches archive, Field Notes archive, Projects section, About, Contact.
