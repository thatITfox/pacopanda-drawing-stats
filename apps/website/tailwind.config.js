/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
  content: [
		"./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
	],
  theme: {
    extend: {
      fontFamily: {
        "inter": ["Inter", ...defaultTheme.fontFamily.sans],
        "open-sans": ["Open Sans", ...defaultTheme.fontFamily.sans],
        "jetbrains-mono": ["JetBrains Mono", ...defaultTheme.fontFamily.mono]
      }
    },
  },
  plugins: [],
}
