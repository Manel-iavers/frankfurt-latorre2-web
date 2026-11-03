import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.latorre2.com',
  // Sense barra final: el Worker serveix /carta i redirigeix /carta/ cap aquí,
  // així el sitemap i els canonical apunten a la URL que respon 200.
  trailingSlash: 'never',
  compressHTML: true,
  integrations: [sitemap()],
});
