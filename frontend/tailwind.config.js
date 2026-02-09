/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'bill-purple': '#8B7FC8',
        'bill-gray': '#4A5568',
      },
    },
  },
  plugins: [],
}
