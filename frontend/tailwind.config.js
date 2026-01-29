/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx}", "./public/index.html"],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: "#1A3D7C",
        },
      },
    },
  },
  plugins: [],
};
