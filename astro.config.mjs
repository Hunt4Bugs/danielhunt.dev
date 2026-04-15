import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'http://hunt4bugs.github.io',
  base: '/danielhunt.dev',
  integrations: [tailwind()],
});
