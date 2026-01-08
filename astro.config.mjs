import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://frankfurtlatorre2.com',
  compressHTML: true,
  integrations: [sitemap()],
});
