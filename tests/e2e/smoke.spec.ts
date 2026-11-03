import { test, expect, type Page } from '@playwright/test';
import { siteConfig } from '../../src/config/site';

// El test no surt mai del domini: les peticions a qualsevol altre host es
// tallen, i del botó de comanda només se'n comprova l'enllaç, sense clicar-lo.
test.beforeEach(async ({ page, baseURL }) => {
  const origin = new URL(baseURL!).origin;
  await page.route('**/*', (route) =>
    new URL(route.request().url()).origin === origin ? route.continue() : route.abort(),
  );
});

async function expectImagesLoaded(page: Page, selector: string) {
  const images = page.locator(selector);
  const count = await images.count();
  expect(count).toBeGreaterThan(0);
  for (let i = 0; i < count; i++) {
    const img = images.nth(i);
    await img.scrollIntoViewIfNeeded();
    await expect(img).toHaveJSProperty('complete', true);
    expect(await img.evaluate((el: HTMLImageElement) => el.naturalWidth)).toBeGreaterThan(0);
  }
}

test('portada: hero i botó de comanda cap a l\'SmartMenu d\'Àgora', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveTitle(/Frankfurt la Torre 2/);
  await expect(page.getByRole('heading', { level: 1 })).toContainText('La Torre 2');

  const cta = page.locator('.hero-cta').getByRole('link', { name: /Fer Comanda/ });
  await expect(cta).toBeVisible();
  await expect(cta).toHaveAttribute('href', siteConfig.smartMenuUrl);
  expect(new URL(siteConfig.smartMenuUrl).hostname).toBe('smartmenu.agorapos.com');

  // El botó flotant també ha de portar a l'SmartMenu
  await expect(page.locator('a.floating-cta')).toHaveAttribute('href', siteConfig.smartMenuUrl);

  await expectImagesLoaded(page, '.product-image img');
});

test('carta: entrepans amb nom, preus i foto', async ({ page }) => {
  const response = await page.goto('/carta');
  expect(response?.status()).toBe(200);

  await expect(page).toHaveTitle(/Carta/);

  const cards = page.locator('.entrepan-card');
  expect(await cards.count()).toBeGreaterThanOrEqual(10);

  for (const card of await cards.all()) {
    await expect(card.locator('h3')).not.toBeEmpty();
    await expect(card).toContainText(/\d+,\d{2}\s?€/);
  }

  await expect(cards.filter({ has: page.locator('h3', { hasText: /^Burguer$/ }) })).toHaveCount(1);
  await expectImagesLoaded(page, '.entrepan-image img');
});
