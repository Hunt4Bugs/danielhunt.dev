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
  cream: '#F3EFE8',    // --cream (243 239 232) — warm canvas, used here as overlay typography color
  espresso: '#2B1F1A', // --espresso (43 31 26) — warm-pole structural
  accent: '#6B1F2B',   // --accent (107 31 43) — burgundy
};

// Load the portrait as a data URI so satori can embed it at build time.
function loadPortraitDataUri(): string {
  const imagePath = path.join(process.cwd(), 'public', 'images', 'daniel-hunt-headshot.jpeg');
  const buf = fs.readFileSync(imagePath);
  return `data:image/jpeg;base64,${buf.toString('base64')}`;
}

export const GET: APIRoute = async () => {
  // Fraunces for the wordmark (no ff/fl letters in "DANIEL HUNT").
  // Inter for the tagline ("Live offline." contains fl → ligature-safe in Inter).
  const [frauncesData, interLightData, interMediumData] = await Promise.all([
    fetchFont('Fraunces', 500),
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
          position: 'relative',
          width: '1200px',
          height: '630px',
          backgroundColor: TOKEN.espresso,
          fontFamily: 'Inter',
        },
        children: [
          // Layer 1 — full-bleed portrait
          {
            type: 'img',
            props: {
              src: portraitSrc,
              width: 1200,
              height: 630,
              style: {
                position: 'absolute',
                top: 0,
                left: 0,
                width: '1200px',
                height: '630px',
                objectFit: 'cover',
                objectPosition: 'center 18%',
              },
            },
          },

          // Layer 2 — warm espresso gradient overlay
          // Top: barely tinted (lets the face read). Bottom: heavy espresso, ensures text legibility.
          {
            type: 'div',
            props: {
              style: {
                position: 'absolute',
                top: 0,
                left: 0,
                width: '1200px',
                height: '630px',
                display: 'flex',
                backgroundImage:
                  'linear-gradient(180deg, rgba(43, 31, 26, 0.08) 0%, rgba(43, 31, 26, 0.15) 40%, rgba(43, 31, 26, 0.55) 68%, rgba(43, 31, 26, 0.88) 88%, rgba(17, 17, 17, 0.96) 100%)',
              },
              children: [],
            },
          },

          // Layer 3 — text overlay, anchored to bottom-left
          {
            type: 'div',
            props: {
              style: {
                position: 'absolute',
                top: 0,
                left: 0,
                width: '1200px',
                height: '630px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'flex-end',
                padding: '72px 88px',
              },
              children: [
                // Wordmark — true cover-poster scale
                {
                  type: 'p',
                  props: {
                    style: {
                      fontSize: '112px',
                      fontFamily: 'Fraunces',
                      fontWeight: 500,
                      color: TOKEN.cream,
                      letterSpacing: '0.05em',
                      textTransform: 'uppercase',
                      lineHeight: 1,
                      margin: 0,
                    },
                    children: 'Daniel Hunt',
                  },
                },

                // Burgundy hairline — the single emphatic brand accent
                {
                  type: 'div',
                  props: {
                    style: {
                      display: 'flex',
                      width: '72px',
                      height: '3px',
                      backgroundColor: TOKEN.accent,
                      marginTop: '28px',
                      marginBottom: '24px',
                    },
                    children: [],
                  },
                },

                // Tagline — the brand thesis, one line, restrained
                {
                  type: 'p',
                  props: {
                    style: {
                      fontSize: '32px',
                      fontFamily: 'Inter',
                      fontWeight: 300,
                      color: 'rgba(243, 239, 232, 0.92)',
                      margin: 0,
                      lineHeight: 1.3,
                      letterSpacing: '0.005em',
                    },
                    children: 'Build in public. Live offline.',
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
