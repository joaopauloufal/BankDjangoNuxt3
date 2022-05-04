import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/docs/directory-structure/nuxt.config
export default defineNuxtConfig({
  css: [
    '@oruga-ui/oruga-next/src/scss/oruga-full-vars.scss'
  ],
  build: {
    transpile: [/oruga/]
  },
  ssr: false
})
