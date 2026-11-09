import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import { mkdirSync } from 'node:fs';

const moduleName = process.env.MODULE;
const expectedPages = Number(process.env.EXPECTED_PAGES);
if (!moduleName || !Number.isInteger(expectedPages) || expectedPages < 2) {
  throw new Error('Set MODULE and EXPECTED_PAGES for the interactive-book smoke test');
}

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const screenshotDir = process.env.SCREENSHOT_DIR;
if (screenshotDir) mkdirSync(screenshotDir, { recursive: true });
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
    const response = await page.goto(`${base}/original-engine/${moduleName}/`, { waitUntil: 'domcontentloaded', timeout: 25000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => {
      const c = document.querySelector('#gl');
      return c && c.width > 100 && c.height > 100 && !!(c.getContext('webgl2') || c.getContext('webgl'));
    }, null, { timeout: 30000 });

    const dots = page.locator('#dots button');
    if (await dots.count() !== expectedPages) throw new Error(`expected ${expectedPages} pages, got ${await dots.count()}`);
    const canvas = await page.locator('#gl').evaluate(c => ({ width: c.width, height: c.height }));

    for (let i = 0; i < expectedPages; i++) {
      if (mobile && i > 0) {
        const next = page.locator('#sheet .turn');
        if (await next.count() !== 1) throw new Error(`page ${i} has no mobile next-page control`);
        await next.click();
        await page.waitForFunction(n => location.hash === `#${n}`, i);
        await page.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n + 1, i);
      } else if (!mobile) {
        await dots.nth(i).click();
        await page.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n + 1, i);
      }
      if (!(await page.locator('#sheet h1').innerText()).trim()) throw new Error(`page ${i + 1} has no title`);
      if (!(await page.locator('#readout').innerText()).trim()) throw new Error(`page ${i + 1} has no live readout`);
      if (screenshotDir) {
        const suffix = String(i + 1).padStart(2, '0');
        await page.screenshot({ path: `${screenshotDir}/${moduleName}-${mobile ? 'mobile' : 'desktop'}-${suffix}.png` });
      }
    }

    if (moduleName === 'energy' && !mobile) {
      const layout = await page.evaluate(() => {
        const hint = document.querySelector('#hint');
        const readout = document.querySelector('#readout');
        return {
          hintDisplay: getComputedStyle(hint).display,
          hintRight: hint.getBoundingClientRect().right,
          readoutLeft: readout.getBoundingClientRect().left
        };
      });
      if (layout.hintDisplay !== 'none' && layout.hintRight > layout.readoutLeft - 4) {
        throw new Error('desktop figure hint overlaps the live readout');
      }
    }
    if (moduleName === 'energy' && mobile) {
      const layout = await page.evaluate(() => {
        const rect = selector => {
          const el = document.querySelector(selector);
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return { top: r.top, bottom: r.bottom, left: r.left, right: r.right };
        };
        return {
          title: rect('#figtitle'),
          picker: rect('.scene-picker'),
          figure: rect('.figure'),
          readout: rect('#readout'),
          hintDisplay: getComputedStyle(document.querySelector('#hint')).display
        };
      });
      if (!layout.title || !layout.picker || layout.picker.top < layout.title.bottom + 4) {
        throw new Error('mobile scene selector overlaps the figure title');
      }
      if (layout.hintDisplay !== 'none') throw new Error('desktop mouse/keyboard hint remains on the mobile figure');
      if (!layout.readout || layout.readout.left < layout.figure.left || layout.readout.right > layout.figure.right + 1) {
        throw new Error('mobile live readout extends outside the figure');
      }
    }

    const picker = page.locator('select.scene-picker');
    if (await picker.count() !== 1 || await picker.locator('option').count() < 2) {
      throw new Error('accessible scene picker is missing usable objects');
    }
    await picker.selectOption({ index: 1 });
    await page.waitForFunction(() => {
      const plate = document.querySelector('#plate');
      return plate && !plate.hidden && !!plate.querySelector('#scene-plate-title');
    });
    await page.locator('#plate .close').click();
    await page.waitForFunction(() => document.querySelector('#plate')?.hidden);

    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) {
      throw new Error('horizontal overflow');
    }
    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe serious/critical: ${serious.map(v => v.id).join(', ')}`);
    if (errors.length) throw new Error(errors.join(' | '));

    console.log(`PASS ${moduleName} ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${expectedPages}/${expectedPages} pages, WebGL ${canvas.width}×${canvas.height}, scene picker, overflow 0, axe serious/critical 0`);
  } catch (error) {
    failures.push(`${moduleName} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
