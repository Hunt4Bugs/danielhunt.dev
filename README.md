# danielhunt.dev

Personal brand surface for Daniel Hunt — custom software, automation & AI for business, built in public.

A single-page static site: plain HTML + handwritten CSS + vanilla JS, with [htmx](https://htmx.org) powering the contact form. No framework, no install step, no build step — the `site/` directory deploys as-is.

## Local development

```bash
python3 -m http.server 8000 --directory site   # http://localhost:8000
# or: npx serve site
```

The contact form errors gracefully in local dev (the committed HTML holds `WEB3FORMS_KEY_PLACEHOLDER`; the real key is injected at deploy time).

## Deployment

Push to `main` → `.github/workflows/deploy.yml` injects the `PUBLIC_WEB3FORMS_KEY` repo secret into `site/index.html` (the Web3Forms key is public-by-design) and uploads `site/` to GitHub Pages. The custom domain is set via `site/CNAME`.

## Brand

The brand's source of truth lives in the repo, not on the site:

- [`docs/brand/IDENTITY.md`](docs/brand/IDENTITY.md) — positioning, thesis, services, content pillars, voice
- [`docs/brand/VISUAL.md`](docs/brand/VISUAL.md) — typography, palette, marks, page furniture, imagery rules
- [`docs/brand/AUDIENCE.md`](docs/brand/AUDIENCE.md) / [`docs/brand/OPERATING.md`](docs/brand/OPERATING.md) — who it's for and how it operates
- [`docs/brand/specs/`](docs/brand/specs/) — dated strategy snapshots (latest: 2026-07-22)

A public rendering of the visual system is served at [danielhunt.dev/brand](https://danielhunt.dev/brand).

## Stack

- Plain HTML, single handwritten stylesheet (`site/css/site.css`), vanilla JS web components (`site/js/site.js`)
- htmx 2.x, vendored at `site/js/htmx.min.js`
- Google Fonts: Instrument Serif (display) + Inter (body/UI)
- GitHub Pages via `actions/upload-pages-artifact`

See [`CLAUDE.md`](CLAUDE.md) for the full architecture notes.
