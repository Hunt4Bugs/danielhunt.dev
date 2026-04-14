# danielhunt.dev

Personal site for Daniel Hunt — built with [Astro](https://astro.build) and Tailwind CSS, deployed to GitHub Pages on the custom domain **danielhunt.dev**.

## Local development

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output → ./dist
npm run preview
```

## TODO before going live

1. **Social URLs** — `src/components/Footer.astro`: replace the three `href: '#'` placeholders with your real LinkedIn / X / YouTube URLs.
2. **Contact form key** — `src/components/Contact.astro`: replace `YOUR_ACCESS_KEY` with a free [Web3Forms](https://web3forms.com) access key (just enter `contact@danielhunt.dev` on their site, they email you a key — no signup needed).
3. **OG image** *(optional)* — drop a 1200×630 `og.png` in `public/` and add `<meta property="og:image" content="/og.png" />` in `src/layouts/Layout.astro`.

## Deployment

Push to `main` and the GitHub Action in `.github/workflows/deploy.yml` builds with Astro and deploys to GitHub Pages. The first time:

1. **Create the repo** (already done — `Hunt4Bugs/danielhunt.dev`).
2. Push:
   ```bash
   git remote add origin https://github.com/Hunt4Bugs/danielhunt.dev.git
   git push -u origin main
   ```
3. **Enable Pages**: GitHub repo → *Settings → Pages → Build and deployment → Source = **GitHub Actions***.
4. **DNS**: at your domain registrar, point `danielhunt.dev` at GitHub Pages with these `A` records (apex):

   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

   And a `CNAME` record for `www`:
   ```
   www → hunt4bugs.github.io
   ```
5. The `public/CNAME` file in this repo tells GitHub Pages which custom domain to serve. Once DNS resolves, enable **Enforce HTTPS** in the Pages settings.

## Stack

- Astro 4 (static)
- Tailwind CSS 3
- `@astrojs/sitemap` for `sitemap-index.xml`
- Hosted on GitHub Pages

## Brand

Light + Deep Autumn palette (defined in `tailwind.config.mjs`):

| Token        | Hex      | Use                          |
|--------------|----------|------------------------------|
| `cream`      | #FAF6EF  | Page background              |
| `parchment`  | #F1E9D8  | Surface tint                 |
| `espresso`   | #2B1D14  | Primary text / headings      |
| `cocoa`      | #5A4434  | Body copy                    |
| `rust`       | #A0432A  | Primary accent / CTA         |
| `rustDark`   | #7E3320  | Hover                        |
| `mustard`    | #B8862F  | Eyebrow / numerals           |
| `forest`     | #2F5249  | Reserved                     |

Type: Fraunces (display) + Inter (UI), via Google Fonts.
