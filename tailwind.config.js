/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Templates in your main templates directory
    "./templates/**/*.html",
    
    // Templates in your Django apps
    "./core/templates/**/*.html",
    "./quotes/templates/**/*.html", 
    "./blog/templates/**/*.html",
    
    // Include JavaScript files if you're using Tailwind classes in JS
    // "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        }
      },
      fontFamily: {
        'sans': ['Inter', 'ui-sans-serif', 'system-ui'],
      }
    },
  },
  plugins: [],
}