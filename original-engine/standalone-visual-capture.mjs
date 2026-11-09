import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const pages = [
  ['kinematics', '/chapters/kinematics.html'],
  ['newton', '/chapters/newton-laws.html'],
  ['circular', '/chapters/circular-motion.html'],
  ['energy', '/chapters/work-energy.html'],
  ['momentum', '/chapters/momentum.html'],
  ['oscillations', '/chapters/oscillations.html'],
  ['rotation', '/chapters/rotation.html'],
  ['fluids', '/chapters/fluids.html'],
  ['electrostatics', '/chapters/electrostatics.html'],
  ['gauss', '/chapters/gauss-law.html'],
  ['potential', '/chapters/electric-potential.html'],
  ['capacitors', '/chapters/capacitors.html'],
  ['circuits', '/chapters/circuits.html'],
  ['magnetism', '/chapters/magnetism.html'],
  ['induction', '/chapters/induction.html'],
];

const root = '/tmp/physics-visual-review/all-standalone';
await mkdir(root, { recursive: true });
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});
const failures = [];

for (const mobile of [false, true]) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  page.on('pageerror', error => failures.push(`runtime ${mobile ? 'mobile' : 'desktop'}: ${error.message}`));
  page.on('console', message => {
    if (message.type() === 'error' && !/fonts\\.googleapis|cdn\\.jsdelivr/i.test(message.text())) {
      failures.push(`console ${mobile ? 'mobile' : 'desktop'}: ${message.text()}`);
    }
  });

  for (const [slug, path] of pages) {
    try {
      const response = await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 25000 });
      if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
      await page.locator('main').waitFor({ state: 'visible' });
      await page.evaluate(async () => { await document.fonts.ready; return true; });
      const targets = page.locator('main img, main canvas, main iframe');
      const count = await targets.count();
      for (let i = 0; i < count; i++) await targets.nth(i).scrollIntoViewIfNeeded();
      await page.waitForFunction(() => [...document.querySelectorAll('main img')].every(img => img.complete && img.naturalWidth > 0));
      await page.waitForFunction(() => [...document.querySelectorAll('main canvas')].every(canvas => canvas.width > 0 && canvas.height > 0));
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(250);
      const state = await page.evaluate(() => ({
        title: document.querySelector('main h1')?.innerText?.trim() || document.title,
        images: [...document.querySelectorAll('main img')].length,
        canvases: [...document.querySelectorAll('main canvas')].length,
        iframes: [...document.querySelectorAll('main iframe')].length,
        width: document.documentElement.scrollWidth,
        viewport: innerWidth,
      }));
      if (state.width > state.viewport + 2) throw new Error(`horizontal overflow ${state.width - state.viewport}px`);
      await page.screenshot({
        path: `${root}/${slug}-${mobile ? 'mobile' : 'desktop'}.png`,
        fullPage: true,
        animations: 'disabled',
        timeout: 60000,
      });
      console.log(`CAPTURE ${slug} ${mobile ? 'mobile' : 'desktop'} — ${state.images} images, ${state.canvases} canvases, ${state.iframes} iframes`);
    } catch (error) {
      failures.push(`${slug} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
      console.error(`FAIL ${slug} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    }
  }
  await context.close();
}

await browser.close();
if (failures.length) {
  for (const failure of failures) console.error('FAIL', failure);
  process.exit(1);
}
console.log('PASS standalone visual capture: all 15 chapters × desktop/mobile');
