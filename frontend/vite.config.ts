import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: process.env.VITE_HOST || '0.0.0.0',
    port: parseInt(process.env.VITE_PORT || '8080'),
    watch: {
      usePolling: true
    }
  }
})
