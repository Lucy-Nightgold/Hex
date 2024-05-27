/** @type {import('tailwindcss').config} */
module.exports = {
    mode: "jit",
    content: [
        "./templates/*.html",
        "./static/src/*.js",
        "./templates/*.html.j2"
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
