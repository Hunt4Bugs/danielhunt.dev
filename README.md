# danielhunt.dev

[![Deploy to GitHub Pages](https://github.com/Hunt4Bugs/danielhunt.dev/actions/workflows/deploy.yml/badge.svg)](https://github.com/Hunt4Bugs/danielhunt.dev/actions/workflows/deploy.yml)

Personal brand surface for Daniel Hunt — a single-page, zero-build static site that serves as the credibility and contact path for the content brand. Live at **[danielhunt.dev](https://danielhunt.dev)**.

## Stack

No framework, no bundler, no build step. Just HTML, handwritten CSS, and vanilla JS.

| Layer | Choice |
|---|---|
| Markup | Plain HTML, hand-authored per page |
| Styling | Handwritten CSS (`site/css/site.css`) — tokens + reset + semantic classes |
| Behavior | Vanilla JS + [htmx](https://htmx.org) 2.x (vendored, no CDN) for the contact form |
| Shared chrome | Native HTML web components (`<site-nav>`, `<site-footer>`) |
| Fonts | Satoshi Variable (display), Inter (body/UI), JetBrains Mono (data) |
| Hosting | GitHub Pages, deployed via GitHub Actions on every push to `main` |

## Local development

No install step. Serve `site/` with any static file server:

```bash
python3 -m http.server 8000 --directory site
# or
npx serve site
```

Then open [http://localhost:8000](http://localhost:8000).

> **Note:** the contact form's Web3Forms access key is injected at deploy time (see below). Locally it fails gracefully with a "email me directly" fallback unless you temporarily paste in a real key.

## Project structure

```
site/
├── index.html              # Spatial index — About, Contact, and profile-signal states
├── services/index.html     # Indexed Services page
├── brand/index.html        # Public brand-system reference
├── contact-card/index.html # noindex vCard save page (QR + headshot)
├── daniel-hunt.vcf         # Static vCard for the Save contact link
├── css/site.css            # Single stylesheet — tokens, reset, semantic classes
├── js/site.js              # Web components, theme, LA time, wordmark, scroll-reveal
├── js/htmx.min.js          # Vendored htmx 2.x
├── og.png                  # Committed 1200×630 OG image
├── favicon.svg, robots.txt, sitemap.xml, humans.txt, llms.txt, CNAME, images/
```

Everything under `site/` is deployed as-is. Everything else in this repo (`docs/`, this file) is not published.

## Deployment

Push to `main` and [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) uploads `site/` straight to GitHub Pages — no build. On each run the workflow injects the `PUBLIC_WEB3FORMS_KEY` repo secret into the committed HTML placeholder (the key is public-by-design, so this is just template substitution, not secret-keeping).

**One-time setup:**

1. GitHub repo → *Settings → Pages → Build and deployment → Source = **GitHub Actions***.
2. DNS at the domain registrar — point the apex `danielhunt.dev` at GitHub Pages:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
   and add a `CNAME` record for `www`:
   ```
   www → hunt4bugs.github.io
   ```
3. `site/CNAME` tells GitHub Pages which custom domain to serve. Once DNS resolves, enable **Enforce HTTPS** in the Pages settings.

## Design system

Dark-default palette with light-mode overrides, defined as CSS custom properties in `site/css/site.css`:

| Token | Role |
|---|---|
| `--bg-0` | Page background |
| `--surface-1` / `--surface-2` | Card and panel surfaces |
| `--text-1` / `--text-2` | Primary / muted text |
| `--accent-primary` | Systems (cyan) |
| `--accent-secondary` | Life sciences / data (lime) |
| `--accent-tertiary` | AI / models (violet) |
| `--accent-amber` | Strategy / caution (amber) |

8px spacing scale, 4/8/16/24px radii, 12px default glass blur.

For the full context map, identity, and voice, start at [`docs/10_brand/README.md`](docs/10_brand/README.md). For implementation-level tokens, type, and components, see [`docs/10_brand/assets/design.md`](docs/10_brand/assets/design.md).

## License

All rights reserved. Site content, brand assets, and design are not licensed for reuse.
