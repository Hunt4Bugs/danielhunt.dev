/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        // Light + Deep Autumn palette
        cream: '#FAF6EF',
        parchment: '#F1E9D8',
        espresso: '#2B1D14',
        cocoa: '#5A4434',
        rust: '#A0432A',
        rustDark: '#7E3320',
        mustard: '#B8862F',
        forest: '#2F5249',
      },
      fontFamily: {
        serif: ['Fraunces', 'Georgia', 'serif'],
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
