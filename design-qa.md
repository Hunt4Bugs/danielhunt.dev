# Design QA — Vexoo-branded spatial profile index

Date: 2026-08-25

Local implementation: `http://localhost:8002/`

Target: `https://vexoo.framer.website/`

## Comparison target

- Source visual truth, desktop dark home: `/tmp/vexoo-home-desktop-dark.png`
- Source visual truth, mobile dark home: `/tmp/vexoo-home-mobile-dark.png`
- Implementation, desktop dark home: `/tmp/daniel-vexoo-desktop-dark-final.png`
- Implementation, mobile dark home: `/tmp/daniel-vexoo-mobile-dark-postfix.png`
- Implementation, desktop light home: `/tmp/daniel-vexoo-desktop-light-postfix.png`
- Implementation, mobile light home: `/tmp/daniel-vexoo-mobile-light-postfix.png`
- Implementation detail states: `/tmp/daniel-vexoo-about-final.png`, `/tmp/daniel-vexoo-field-final.png`, `/tmp/daniel-vexoo-contact-final.png`
- Post-feedback glass blend: `test-artifacts/glass-blend/light-wide-hover.png`, `test-artifacts/glass-blend/dark-wide-hover.png`, `test-artifacts/glass-blend/light-mobile-hover.png`
- Live-source material captures: `test-artifacts/vexoo-material/source-desktop-light.png`, `test-artifacts/vexoo-material/source-desktop-dark.png`, `test-artifacts/vexoo-material/source-mobile-dark.png`
- Final material implementation: `test-artifacts/vexoo-material/local-desktop-light.png`, `test-artifacts/vexoo-material/local-desktop-dark.png`, `test-artifacts/vexoo-material/local-mobile-dark.png`

## Viewport and normalization

| Comparison | Source pixels | Implementation pixels | CSS viewport | Density | Normalization |
| --- | ---: | ---: | ---: | ---: | --- |
| Desktop home | 1440 × 1024 | 1440 × 1024 | 1440 × 1024 | 1× | Equal-size browser captures; each scaled to 720 × 512 only for the combined full-view board |
| Mobile home | 390 × 844 | 390 × 844 | 390 × 844 | 1× | Direct 1:1 comparison; no source or implementation scaling |
| Final desktop material | 1680 × 945 | 1680 × 945 | 1680 × 945 | 1× | Direct 1:1 comparison; source and implementation joined horizontally without scaling |
| Final mobile material | 390 × 844 | 390 × 844 | 390 × 844 | 1× | Direct 1:1 comparison; source and implementation joined horizontally without scaling |
| Tablet resilience | n/a | 768 × 900 | 768 × 900 | 1× | Implementation-only breakpoint check |

States compared: dark home, light home, desktop card hover, mobile reflow, About, Build / Offline, Contact, and home/back navigation.

## Full-view comparison evidence

- Desktop combined comparison: `/tmp/compare-vexoo-desktop-full-final.png`
- Mobile combined comparison: `/tmp/compare-vexoo-mobile-full-final.png`
- Final desktop light material comparison: `test-artifacts/vexoo-material/compare-desktop-light.png`
- Final mobile dark material comparison: `test-artifacts/vexoo-material/compare-mobile-dark.png`

The implementation preserves the reference's defining composition: fixed viewport, 16px outer gutter, 16px desktop / 12px mobile grid gap, 32px desktop / 24px mobile card radii, a two-row desktop bento that becomes the same four-row mobile bento, one large blurred identity wordmark, one portrait, and a two-card right rail. At 390 × 844, all six implementation card rectangles match the source positions and dimensions exactly.

Intentional brand substitutions are visible but do not change the spatial system: the source portrait is replaced with Daniel's real monochrome headshot, the software-logo strip becomes the canonical profile-signal data object, Resume becomes a real LinkedIn path, and Portfolio becomes the `Build in public. Live offline.` thesis.

## Focused region comparison evidence

- Desktop header, wordmark, and first-row crop: `/tmp/compare-vexoo-desktop-top-final.png`
- Hover state: `/tmp/daniel-vexoo-desktop-hover-final.png`
- Contact form and typography: `/tmp/daniel-vexoo-contact-final.png`

Focused review confirmed that the header alignment, wordmark overlap, first-row card baseline, Lucide arrow sizing, card label padding, and live theme control retain the source's optical rhythm. Live CSS inspection established the actual Vexoo tile material: transparent base, restrained tint layer, inset edge, 10px desktop / 4px mobile backdrop blur, and 32px desktop / 24px mobile radius. The local implementation now reproduces that behavior with calibrated brand-token tints, allowing the identity wordmark to soften through the tile rather than simulating the effect with a text shadow. The canonical Satoshi / Inter / JetBrains Mono stack intentionally replaces Vexoo's Open Sauce fonts; the uppercase wordmark follows `VISUAL.md` rather than copying the source's mixed-case identity.

## Required fidelity surfaces

### Fonts and typography

- Passed. Satoshi Variable is used for the wordmark and detail display text, Inter for body/UI, and JetBrains Mono for metadata.
- The wordmark remains a neutral typographic object; no accent gradient or burgundy appears.
- Desktop, tablet, and mobile wordmark wrapping/truncation were checked. The final 390px wordmark fits inside the viewport at 52.65px without overflow.

### Spacing and layout rhythm

- Passed. Desktop card tracks match the source's 340 / 1052 first-row and 696 / 340 / 340 second-row proportions at 1440px.
- Mobile card rectangles match the source: `358×177`, `358×177`, `173×177`, `173×177`, `173×141`, `173×141` at the same coordinates.
- Tablet 768 × 900 preserves the four-column composition without horizontal overflow or header collision.

### Colors and visual tokens

- Passed. All interface colors consume the documented RGB tokens: Ink Black, Graphite, Soft Gray, Cloud White, and Muted.
- Acid Green is the single lead accent for active/focus/public-signal state. Electric Cyan, Ultraviolet, Signal Amber, and burgundy are not used decoratively on this artifact.
- Dark is the default; light mode maps the same structure through the documented daylight token values.
- Spatial tiles use the documented component tokens: 4% dark / 5% light `--text-1` tint, theme-specific inset edge, 10px desktop / 4px mobile backdrop blur, and no opaque `--surface-1` fill.

### Image quality and asset fidelity

- Passed. The real 1586 × 1982 headshot is used once, with CSS grayscale and a stable crop; it is not regenerated, duplicated, or overlaid.
- The 576 × 384 profile-signal image is a real raster asset and keeps one Acid Green state point.
- Visible arrows use a locally stored Lucide icon asset rather than a text glyph, CSS drawing, or inline SVG.

### Copy and content

- Passed. All visible copy is grounded in `IDENTITY.md`: Life Sciences product work, `Build in public. Live offline.`, `Tech, movement, and culture.`, and the build/offline toggle.
- No invented KPIs, client claims, employment history, portfolio projects, or unavailable publication routes were introduced.

### Interaction, responsiveness, and accessibility

- Passed. About, Build / Offline, Contact, home/back, theme switching, URL-scoped theme state, hover/focus wordmark changes, external links, and browser history work.
- Contact inputs have programmatic labels, required validation, autocomplete values, and a real POST fallback. The external form was not submitted during QA.
- All visible controls meet or exceed 44px target size, including the visually compact theme switch.
- The portrait and signal have appropriate alt text; decorative arrows are empty-alt.
- Reduced-motion rules cover card, wordmark, portrait, icon, and theme transitions.
- Browser console errors/warnings checked after the final pass: none.

## Comparison history

### Iteration 1 — blocked

- [P2] Mobile wordmark truncated Daniel's name at 390px.
  - Fix: reduced the mobile wordmark scale to `13.5vw` with a 52.65px rendered size and re-captured the 390 × 844 state.
  - Post-fix evidence: `/tmp/daniel-vexoo-mobile-dark-final.png` and `/tmp/daniel-vexoo-mobile-dark-postfix.png`.
- [P2] Programmatic focus on the detail heading exposed the browser's default blue outline as a large irregular box.
  - Fix: retained focus transfer for accessibility and suppressed only the heading's visual outline.
  - Post-fix evidence: `/tmp/daniel-vexoo-about-final.png`.

### Iteration 2 — blocked

- [P2] The light-theme switch thumb inherited the light canvas color and disappeared against its track.
  - Fix: allowed the thumb to inherit `--text-1`, producing a black thumb in light mode and a white thumb in dark mode.
  - Post-fix evidence: `/tmp/daniel-vexoo-desktop-light-postfix.png` and `/tmp/daniel-vexoo-mobile-light-postfix.png`.

### Iteration 3 — passed

- Re-captured desktop and mobile home states after all fixes.
- Rechecked the five required fidelity surfaces, tablet resilience, live interactions, semantic controls, form labels, theme URL state, and browser console.
- No actionable P0, P1, or P2 findings remain.

### Iteration 4 — blocked after live-source material comparison

- [P2] The hovered identity wordmark sat above the bento grid, so its lower shadow read as a dark printed ledge rather than part of the glass composition.
  - First fix: moved the wordmark behind the card plane, added a diffuse shadow, and reduced the card fill.
  - Post-fix evidence: `test-artifacts/glass-blend/light-wide-hover.png`, `test-artifacts/glass-blend/dark-wide-hover.png`, and `test-artifacts/glass-blend/light-mobile-hover.png`.
- [P2] The first fix still used a 78% `--surface-1` fill and 12px blur, making the tiles read as opaque panels instead of the Vexoo reference's transparent frosted material.
  - Evidence: user-supplied reference plus live-source CSS measurement on `https://vexoo.framer.website/`.

### Iteration 5 — passed

- Replaced the opaque fill and radial treatment with calibrated transparent tints: 4% in dark mode and 5% in light mode over the brand's off-neutral canvases.
- Matched the source material behavior: 10px desktop / 4px mobile blur, 32px desktop / 24px mobile radii, and a theme-specific low-contrast inset edge.
- Removed the simulated wordmark shadow, card lift, and hover outline. The wordmark now blurs solely through the tile plane; Acid Green remains on keyboard focus and active state.
- Rechecked desktop light, desktop dark, and 390 × 844 dark states with normalized side-by-side comparisons. No actionable P0, P1, or P2 findings remain.
- Post-fix evidence: `test-artifacts/vexoo-material/compare-desktop-light.png` and `test-artifacts/vexoo-material/compare-mobile-dark.png`.

## Residual P3 notes

- The template's Open Sauce type is intentionally replaced by the canonical brand fonts.
- The source Framer badge and source-specific logos are intentionally omitted.
- The source's separate detail routes are implemented as in-page states to preserve this repository's single-page static architecture.

## Implementation checklist

- [x] Vexoo desktop and mobile source captured through the full page and key states
- [x] Branded home composition implemented with exact token usage
- [x] One monochrome headshot only
- [x] One branded profile-signal visualization
- [x] Dark and light modes verified
- [x] Desktop, tablet, and mobile verified
- [x] Hover, focus, navigation, and form structure verified
- [x] Source and implementation compared in combined images
- [x] Console checked with no errors or warnings

final result: passed
