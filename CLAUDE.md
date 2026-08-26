# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal brand surface for Daniel Hunt (danielhunt.dev) — a single-page static site that serves as credibility + contact path for the content brand. Not a content publication itself (content lives on IG, X, YouTube, eventually a newsletter).

For brand strategy and voice, see [`docs/100_brand/IDENTITY.md`](docs/100_brand/IDENTITY.md). For visual art direction, see [`docs/100_brand/VISUAL.md`](docs/100_brand/VISUAL.md). For implementation tokens, type, geometry, and components, see [`docs/100_brand/DESIGN.md`](docs/100_brand/DESIGN.md). Update the relevant source before changing anything brand-shaped on the site.

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
- **HTML web components** (`<site-nav>`, `<site-footer>` in `site/js/site.js`) — shared page chrome for auxiliary pages
- **Fonts**: Satoshi Variable (display/wordmark), Inter (body/UI), and JetBrains Mono (data/metadata).
- Deployed to **GitHub Pages**: `actions/upload-pages-artifact` uploads `site/` directly on push to `main` (no build action)

## Architecture

Everything deployable lives in `site/`; everything else in the repo (docs, this file) is not published.

```
site/
  index.html          # spatial index + in-page About and Contact states
  services/index.html # indexed Services page with crawlable offer details
  brand/index.html    # public brand-system reference, served at /brand
  css/site.css        # single stylesheet: tokens + reset + semantic classes
  js/site.js          # web components, theme + history state, LA time,
                      #   wordmark interaction, scroll-reveal observer
  js/htmx.min.js      # vendored htmx 2.x
  og.png              # committed static OG image (see note below)
  .nojekyll           # required — keeps GitHub Pages from running Jekyll
  favicon.svg, CNAME, robots.txt, sitemap.xml, humans.txt, llms.txt, images/
```

**Key facts:**

- **Head metadata is statically duplicated** in each HTML page (OG, Twitter, JSON-LD) because crawlers don't run JS. Main-page identity chrome and content are static HTML; auxiliary-page shared chrome is JS-rendered through web components.
- **`site/js/site.js`** holds shared `SITE` constants and auxiliary web components, plus the shared URL-scoped theme and live LA time. Home-only hover/focus wordmark, hash navigation, and history behavior are guarded to the spatial index. Static page copy remains in HTML.
- **Contact form** posts to Web3Forms via htmx (`hx-post` + `hx-swap="none"` + `hx-on::after-request` reading `event.detail.successful` to show an inline status). Two load-bearing details: the `htmx-config` meta tag sets `selfRequestsOnly:false` (htmx 2.x blocks cross-origin requests by default), and `hx-on::config-request` strips htmx's `HX-*` headers (Web3Forms' CORS preflight rejects them). The form keeps real `action`/`method` so it degrades to a native POST without JS.
- **Web3Forms access key**: the committed HTML contains `WEB3FORMS_KEY_PLACEHOLDER`; the deploy workflow `sed`-injects the `PUBLIC_WEB3FORMS_KEY` repo secret at deploy time (the key is public-by-design). Locally the form errors gracefully ("email me directly") unless you temporarily sed in a real key.
- **og.png is a committed static asset** (1200×630). It was generated once by the old satori + resvg pipeline, which lives in git history at `src/pages/og.png.ts` if it ever needs regenerating. `.gitignore` has a `!site/**/*.png` exception for it.

**Design tokens** (in `site/css/site.css`, canonicalized in `docs/100_brand/DESIGN.md`):

- Dark default: `--bg-0`, `--surface-1`, `--surface-2`, `--text-1`, `--text-2`
- Semantic accents: `--accent-primary` (systems), `--accent-secondary` (life sciences/data), `--accent-tertiary` (AI/models), `--accent-amber` (strategy/caution)
- 8px spacing scale, 4/8/16/24px radii, and 12px default glass blur

**Scroll-reveal pattern:** Elements with class `reveal` animate into view via IntersectionObserver (defined in `site/js/site.js`). Staggered delays use `reveal-delay-1` through `reveal-delay-4`. The CSS/JS infrastructure exists but no current markup uses it.

**Brand surface phasing:**

- **Phase B (current)**: spatial profile index with a dedicated Services route. The home keeps the persistent `Build in public. Live offline.` header role, hover/focus wordmark, one monochrome portrait, one profile-signal data object, in-page About and Contact states, and a contact form. `/services/` is interface-led and repeats neither the portrait nor click-dependent copy. Gallery-frame discipline remains: the portrait appears once and the data object carries the active accent.
- **Phase C (future, when content exists)**: site restructures as a publication home with Dispatches archive, Field Notes archive, Projects section, About, Contact.
