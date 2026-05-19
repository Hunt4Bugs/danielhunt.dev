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

export const GET: APIRoute = async () => {
  const [frauncesData, interLightData, interRegularData] = await Promise.all([
    fetchFont('Fraunces', 700),
    fetchFont('Inter', 300),
    fetchFont('Inter', 400),
  ]);

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          width: '1200px',
          height: '630px',
          backgroundColor: '#FFFFFF',
          padding: '80px',
          fontFamily: 'Inter',
        },
        children: [
          // Top: name label
          {
            type: 'p',
            props: {
              style: {
                fontSize: '16px',
                fontFamily: 'Inter',
                fontWeight: 400,
                color: '#9B9B9B',
                letterSpacing: '0.15em',
                textTransform: 'uppercase',
                margin: 0,
              },
              children: 'Daniel Hunt',
            },
          },
          // Center: main copy
          {
            type: 'div',
            props: {
              style: {
                display: 'flex',
                flexDirection: 'column',
                gap: '24px',
              },
              children: [
                {
                  type: 'div',
                  props: {
                    style: {
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '0px',
                    },
                    children: [
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '88px',
                            fontFamily: 'Fraunces',
                            fontWeight: 700,
                            color: '#111111',
                            lineHeight: 1.05,
                            margin: 0,
                          },
                          children: 'Built in Public.',
                        },
                      },
                      {
                        type: 'p',
                        props: {
                          style: {
                            fontSize: '88px',
                            fontFamily: 'Fraunces',
                            fontWeight: 700,
                            color: '#111111',
                            lineHeight: 1.05,
                            margin: 0,
                          },
                          children: 'Lived offline.',
                        },
                      },
                    ],
                  },
                },
                {
                  type: 'p',
                  props: {
                    style: {
                      fontSize: '28px',
                      fontFamily: 'Inter',
                      fontWeight: 300,
                      color: '#6B6B6B',
                      margin: 0,
                      lineHeight: 1.4,
                    },
                    children: 'Tech, culture, and movement.',
                  },
                },
              ],
            },
          },
          // Bottom: URL
          {
            type: 'p',
            props: {
              style: {
                fontSize: '14px',
                fontFamily: 'Inter',
                fontWeight: 400,
                color: '#C4C4C4',
                letterSpacing: '0.05em',
                margin: 0,
              },
              children: 'danielhunt.dev',
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      fonts: [
        { name: 'Fraunces', data: frauncesData, weight: 700, style: 'normal' },
        { name: 'Inter', data: interLightData, weight: 300, style: 'normal' },
        { name: 'Inter', data: interRegularData, weight: 400, style: 'normal' },
      ],
    },
  );

  const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
  const png = resvg.render().asPng();

  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000' },
  });
};
