import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

// Dedicated Chapter 13 regression test: run independently from the full chapter matrix.
const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const browser = await chromium.launch({ headless: true, args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'] });
const failures = [];

async function run(mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce'
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => {
    if (m.type() === 'error' && !/fonts\\.googleapis|cdn\\.jsdelivr/i.test(m.text())) errors.push(m.text());
  });

  try {
    const response = await page.goto(`${base}/chapters/circuits.html`, { waitUntil: 'domcontentloaded', timeout: 25000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForFunction(() => {
      const c = document.querySelector('#visual');
      return c && c.width > 100 && c.height > 100 && c.getContext('2d');
    });

    const drawing = await page.locator('#visual').evaluate(c => {
      const x = c.getContext('2d');
      const pixels = x.getImageData(0, 0, c.width, c.height).data;
      let changed = 0;
      for (let i = 0; i < pixels.length; i += 4) {
        if (pixels[i] < 235 || pixels[i + 1] < 235 || pixels[i + 2] < 235) changed++;
      }
      return { width: c.width, height: c.height, changed };
    });
    if (drawing.changed < 100) throw new Error('circuit schematic canvas appears blank');
    const label = await page.locator('#visual').getAttribute('aria-label');
    if (!label?.includes('замкнутой электрической цепи') || !label.includes('направление условного тока')) {
      throw new Error('schematic canvas has no meaningful Russian accessible description');
    }

    const initial = await page.locator('#r0').innerText();
    if (!initial.includes('2,000') && !initial.includes('2,00') && !initial.includes('2,0')) {
      throw new Error(`expected I = 2 A at U=12 V, R=6 Ω; got ${initial}`);
    }
    await page.locator('#p1').evaluate(el => { el.value = '12'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    const changed = await page.locator('#r0').innerText();
    if (!changed.includes('1,000') && !changed.includes('1,00') && !changed.includes('1,0')) {
      throw new Error(`expected I = 1 A after R changes to 12 Ω; got ${changed}`);
    }
    if (!(await page.locator('#r1').innerText()).includes('12')) throw new Error('power did not update to 12 W');
    await page.locator('[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно')) throw new Error('quiz answer feedback failed');

    await page.waitForFunction(() => {
      const c = document.querySelector('.physics-stage canvas');
      return c && c.width > 100 && c.height > 100 && !!(c.getContext('webgl2') || c.getContext('webgl'));
    }, null, { timeout: 30000 });
    await page.locator('.physics-stage canvas').focus();
    await page.keyboard.press('ArrowRight');
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) {
      throw new Error('horizontal overflow');
    }

    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe serious/critical: ${serious.map(v => v.id).join(', ')}`);
    if (errors.length) throw new Error(errors.join(' | '));

    console.log(`PASS standalone Chapter 13 ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — schematic painted (${drawing.changed} pixels), Ohm recalculation, power, quiz, WebGL, keyboard, overflow 0, axe serious/critical 0`);
  } catch (error) {
    failures.push(`Chapter 13 standalone ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
  } finally {
    await context.close();
  }
}

await run(false);
await run(true);
await browser.close();
if (failures.length) {
  for (const failure of failures) console.error('FAIL', failure);
  process.exit(1);
}
