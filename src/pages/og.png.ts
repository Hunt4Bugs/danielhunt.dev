import type { APIRoute } from 'astro';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';

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

// Brand tokens (kept in sync with src/styles/global.css and docs/brand/VISUAL.md)
const TOKEN = {
  white: '#FFFFFF',
  ink: '#111111',
  gray: '#6B6B6B',
  quietGray: '#9B9B9B',
  espresso: '#2B1F1A',
  accent: '#6B1F2B', // burgundy
};

export const GET: APIRoute = async () => {
  // Fraunces for the masthead + monogram (no ff/fl letter sequences in "DANIEL HUNT" or "DH").
  // Inter for the headline ("Live offline." contains fl) + body + URL.
  const [frauncesData, interBoldData, interLightData, interRegularData] = await Promise.all([
    fetchFont('Fraunces', 500),
    fetchFont('Inter', 700),
    fetchFont('Inter', 300),
    fetchFont('Inter', 500),
  ]);

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          display: 'flex',
          flexDirection: 'column',
          width: '1200px',
          height: '630px',
          backgroundColor: TOKEN.white,
          padding: '72px 88px',
          fontFamily: 'Inter',
        },
        children: [
          // Top: DH monogram anchor (gallery-curator placement)
          {
            type: 'div',
            props: {
              style: { display: 'flex' },
              children: [
                {
                  type: 'p',
                  props: {
                    style: {
                      fontSize: '34px',
                      fontFamily: 'Fraunces',
                      fontWeight: 500,
                      color: TOKEN.espresso,
                      letterSpacing: '0.02em',
                      textTransform: 'uppercase',
                      margin: 0,
                      lineHeight: 1,
                    },
                    children: 'DH',
                  },
                },
              ],
            },
          },

          // Middle: masthead + burgundy hairline + headline + deck
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
                      fontSize: '96px',
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
                      marginTop: '36px',
                      marginBottom: '36px',
                    },
                    children: [],
                  },
                },

                // Headline — the brand thesis, stacked to visually reinforce the Build / Offline toggle
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
                            fontSize: '76px',
                            fontFamily: 'Inter',
                            fontWeight: 700,
                            color: TOKEN.ink,
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
                            fontSize: '76px',
                            fontFamily: 'Inter',
                            fontWeight: 700,
                            color: TOKEN.ink,
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
                      fontSize: '26px',
                      fontFamily: 'Inter',
                      fontWeight: 300,
                      color: TOKEN.gray,
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

          // Bottom: URL + location as editorial metadata (mid-dot separated)
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
                      fontSize: '16px',
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
                      fontSize: '14px',
                      fontFamily: 'Inter',
                      fontWeight: 500,
                      color: TOKEN.quietGray,
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
    {
      width: 1200,
      height: 630,
      fonts: [
        { name: 'Fraunces', data: frauncesData, weight: 500, style: 'normal' },
        { name: 'Inter', data: interBoldData, weight: 700, style: 'normal' },
        { name: 'Inter', data: interLightData, weight: 300, style: 'normal' },
        { name: 'Inter', data: interRegularData, weight: 500, style: 'normal' },
      ],
    },
  );

  const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
  const png = resvg.render().asPng();

  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000' },
  });
};
