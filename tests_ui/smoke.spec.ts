import { test, expect } from '@playwright/test';

test('Homepage loads correctly', async ({ page }) => {
  await page.goto('/'); // automaticky sa spojí s baseURL
  await expect(page).toHaveTitle(/STORE/i);
  await expect(page.locator('#nava')).toContainText('PRODUCT STORE');
});
