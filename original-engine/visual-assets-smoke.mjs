import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import { mkdir } from 'node:fs/promises';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const pages = [
  { path: '/chapters/magnetism.html', count: 1, title: 'Chapter 14' },
  { path: '/chapters/induction.html', count: 3, title: 'Chapter 15' },
];
const failures = [];
const screenshotDir = '/tmp/physics-visual-review';
await mkdir(screenshotDir, { recursive: true });
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

for (const mobile of [false, true]) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  for (const item of pages) {
    try {
      const response = await page.goto(base + item.path, { waitUntil: 'networkidle', timeout: 25000 });
      if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
      const images = page.locator('figure.visual-figure img');
      if (await images.count() !== item.count) throw new Error(`expected ${item.count} visual images, got ${await images.count()}`);
      await page.waitForFunction(() => [...document.querySelectorAll('figure.visual-figure img')].every(img => img.complete && img.naturalWidth > 0 && img.naturalHeight > 0));
      const states = await images.evaluateAll(nodes => nodes.map(img => ({
        src: img.getAttribute('src'),
        width: img.naturalWidth,
        height: img.naturalHeight,
        alt: img.getAttribute('alt')?.trim() || '',
        caption: img.closest('figure')?.querySelector('figcaption')?.innerText?.trim() || '',
        hasRu: !!img.closest('figure')?.querySelector('figcaption [lang="ru"]'),
        hasEn: !!img.closest('figure')?.querySelector('figcaption [lang="en"]'),
      })));
      if (!mobile) {
        for (let i = 0; i < states.length; i++) {
          const file = states[i].src.split('/').pop().replace(/\\.svg$/i, '.png');
          await images.nth(i).screenshot({ path: `${screenshotDir}/${file}` });
        }
      }
      for (const state of states) {
        if (!state.alt || state.alt.length < 40) throw new Error(`missing meaningful alt text: ${state.src}`);
        if (!state.caption || !state.hasRu || !state.hasEn) throw new Error(`missing bilingual caption: ${state.src}`);
        if (state.width < 600 || state.height < 300) throw new Error(`unexpected SVG dimensions: ${state.src} ${state.width}×${state.height}`);
      }
      if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('horizontal overflow');
      const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
      const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
      if (serious.length) throw new Error(`axe serious/critical: ${serious.map(v => v.id).join(', ')}`);
      if (errors.length) throw new Error(errors.join(' | '));
      console.log(`PASS ${item.title} visuals ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${states.length} SVG(s) loaded, bilingual captions, meaningful alt text, no overflow, axe serious/critical 0`);
    } catch (error) {
      failures.push(`${item.title} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
      console.error('FAIL', failures[failures.length - 1]);
    }
  }
  await context.close();
}
await browser.close();
if (failures.length) {
  for (const failure of failures) console.error('FAIL', failure);
  process.exit(1);
}
console.log('PASS Physics visual assets smoke: 4/4 chapter/viewport runs');
