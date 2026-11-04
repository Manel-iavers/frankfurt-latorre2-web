import { defineConfig, devices } from '@playwright/test';

// Smoke E2E sobre el build estàtic servit amb `astro preview`.
// Local: `npm run build && npm run test:e2e`. Al CI ho fa el workflow e2e.yml.
export default defineConfig({
  testDir: './tests/e2e',
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? [['github'], ['list']] : 'list',
  use: {
    baseURL: 'http://127.0.0.1:4321',
    trace: 'retain-on-failure',
  },
  projects: [
    { name: 'mobile', use: { ...devices['Pixel 7'] } },
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
  ],
  webServer: {
    // --ignore-lock força el primer pla: Astro 7 posa `astro preview` en segon
    // pla quan detecta que l'executa un agent d'IA, i Playwright ho veu com que
    // el servidor ha caigut.
    command: 'npx astro preview --host 127.0.0.1 --port 4321 --ignore-lock',
    url: 'http://127.0.0.1:4321',
    reuseExistingServer: !process.env.CI,
  },
});
