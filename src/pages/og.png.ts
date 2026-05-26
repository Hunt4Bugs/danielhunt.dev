import type { APIRoute } from 'astro';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';

async function fetchFont(family: string, weight: number): Promise<ArrayBuffer> {
  const url = `https://fonts.googleapis.com/css2?family=${family}:wght@${weight}&display=swap`;
  const css = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (compatible; og-image-generator)',
    },
  }).then((r) => r.text());

  const match = css.match(/src: url\((.+?)\) format\('(opentype|truetype|woff2)'\)/);
  if (!match) throw new Error(`Could not find font URL for ${family} ${weight}`);
  return fetch(match[1]).then((r) => r.arrayBuffer());
}

// Brand tokens — mirror exact hex values from src/styles/global.css.
// CSS var name → hex shown for each. Update both if either changes.
const TOKEN = {
  bg: '#FFFFFF',       // --bg (255 255 255) — primary canvas
  text: '#111111',     // --text (17 17 17) — ink, primary text
  muted: '#5A5A5A',    // --muted (90 90 90) — secondary text
  quiet: '#8A8F91',    // --quiet (138 143 145) — tertiary text, captions
  line: '#E2E2E2',     // --line (226 226 226) — hairline structural rules
  espresso: '#2B1F1A', // --espresso (43 31 26) — warm-pole structural
  accent: '#6B1F2B',   // --accent (107 31 43) — burgundy
};

// Load the portrait as a data URI so satori can embed it.
function loadPortraitDataUri(): string {
  const imagePath = path.join(process.cwd(), 'public', 'images', 'daniel-hunt-headshot.jpeg');
  const buf = fs.readFileSync(imagePath);
  return `data:image/jpeg;base64,${buf.toString('base64')}`;
}

export const GET: APIRoute = async () => {
  // Fraunces for masthead + monogram. Inter for headline (has fl in "offline"), deck, and metadata.
  const [frauncesData, interBoldData, interLightData, interMediumData] = await Promise.all([
    fetchFont('Fraunces', 500),
    fetchFont('Inter', 700),
    fetchFont('Inter', 300),
    fetchFont('Inter', 500),
  ]);

  const portraitSrc = loadPortraitDataUri();

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          display: 'flex',
          width: '1200px',
          height: '630px',
          backgroundColor: TOKEN.bg,
          fontFamily: 'Inter',
        },
        children: [
          // LEFT COLUMN — text panel (cool pole, 65% width)
          {
            type: 'div',
            props: {
              style: {
                display: 'flex',
                flexDirection: 'column',
                width: '780px',
                height: '630px',
                padding: '64px 72px',
                backgroundColor: TOKEN.bg,
              },
              children: [
                // Top: DH monogram anchor
                {
                  type: 'div',
                  props: {
                    style: { display: 'flex' },
                    children: [
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '32px',
                            fontFamily: 'Fraunces',
                            fontWeight: 500,
                            color: TOKEN.espresso,
                            letterSpacing: '0.02em',
                            textTransform: 'uppercase',
                            lineHeight: 1,
                            margin: 0,
                          },
                          children: 'DH',
                        },
                      },
                    ],
                  },
                },

                // Middle: masthead + hairline + headline + deck
                {
                  type: 'div',
                  props: {
                    style: {
                      flex: 1,
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'center',
                    },
                    children: [
                      // Wordmark masthead
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '72px',
                            fontFamily: 'Fraunces',
                            fontWeight: 500,
                            color: TOKEN.espresso,
                            letterSpacing: '0.05em',
                            textTransform: 'uppercase',
                            lineHeight: 1,
                            margin: 0,
                          },
                          children: 'Daniel Hunt',
                        },
                      },

                      // Burgundy hairline — the single emphatic accent
                      {
                        type: 'div',
                        props: {
                          style: {
                            display: 'flex',
                            width: '88px',
                            height: '3px',
                            backgroundColor: TOKEN.accent,
                            marginTop: '32px',
                            marginBottom: '32px',
                          },
                          children: [],
                        },
                      },

                      // Headline — stacked to reinforce the Build / Offline toggle
                      {
                        type: 'div',
                        props: {
                          style: {
                            display: 'flex',
                            flexDirection: 'column',
                          },
                          children: [
                            {
                              type: 'p',
                              props: {
                                style: {
                                  fontSize: '62px',
                                  fontFamily: 'Inter',
                                  fontWeight: 700,
                                  color: TOKEN.text,
                                  lineHeight: 1.04,
                                  margin: 0,
                                },
                                children: 'Build in public.',
                              },
                            },
                            {
                              type: 'p',
                              props: {
                                style: {
                                  fontSize: '62px',
                                  fontFamily: 'Inter',
                                  fontWeight: 700,
                                  color: TOKEN.text,
                                  lineHeight: 1.04,
                                  margin: 0,
                                },
                                children: 'Live offline.',
                              },
                            },
                          ],
                        },
                      },

                      // Deck — the sub-thesis
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '24px',
                            fontFamily: 'Inter',
                            fontWeight: 300,
                            color: TOKEN.muted,
                            lineHeight: 1.4,
                            marginTop: '24px',
                            marginBottom: 0,
                          },
                          children: 'Tech, movement, and culture.',
                        },
                      },
                    ],
                  },
                },

                // Bottom: editorial metadata row
                {
                  type: 'div',
                  props: {
                    style: {
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    },
                    children: [
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '15px',
                            fontFamily: 'Inter',
                            fontWeight: 500,
                            color: TOKEN.espresso,
                            letterSpacing: '0.24em',
                            textTransform: 'uppercase',
                            margin: 0,
                          },
                          children: 'danielhunt.dev',
                        },
                      },
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '13px',
                            fontFamily: 'Inter',
                            fontWeight: 500,
                            color: TOKEN.quiet,
                            letterSpacing: '0.24em',
                            textTransform: 'uppercase',
                            margin: 0,
                          },
                          children: 'Simi Valley · 2026',
                        },
                      },
                    ],
                  },
                },
              ],
            },
          },

          // RIGHT COLUMN — portrait panel (warm pole, 35% width, full-bleed)
          {
            type: 'div',
            props: {
              style: {
                display: 'flex',
                width: '420px',
                height: '630px',
                position: 'relative',
                borderLeft: `1px solid ${TOKEN.line}`,
              },
              children: [
                {
                  type: 'img',
                  props: {
                    src: portraitSrc,
                    width: 420,
                    height: 630,
                    style: {
                      width: '420px',
                      height: '630px',
                      objectFit: 'cover',
                      objectPosition: '50% 24%',
                    },
                  },
                },
              ],
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      fonts: [
        { name: 'Fraunces', data: frauncesData, weight: 500, style: 'normal' },
        { name: 'Inter', data: interBoldData, weight: 700, style: 'normal' },
        { name: 'Inter', data: interLightData, weight: 300, style: 'normal' },
        { name: 'Inter', data: interMediumData, weight: 500, style: 'normal' },
      ],
    },
  );

  const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
  const png = resvg.render().asPng();

  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000' },
  });
};
