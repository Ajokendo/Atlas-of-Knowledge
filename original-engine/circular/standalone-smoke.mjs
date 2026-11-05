import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const browser = await chromium.launch({ headless: true });
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
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => {
    if (m.type() === 'error' && !/fonts\\.googleapis|cdn\\.jsdelivr/i.test(m.text())) errors.push(m.text());
  });

  try {
    const response = await page.goto(`${base}/chapters/circular-motion.html`, { waitUntil: 'domcontentloaded' });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForFunction(() => document.querySelector('#r0')?.textContent?.includes('5,00'));
    const initial = await page.locator('.stats').innerText();
    if (!initial.includes('5,00 м/с²') || !initial.includes('10,00 Н') || !initial.includes('12,57 с')) {
      throw new Error(`unexpected initial model values: ${initial}`);
    }

    await page.locator('#p0').evaluate(el => { el.value = '20'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.waitForFunction(() => document.querySelector('#r0')?.textContent?.includes('20,00'));
    await page.locator('#p1').evaluate(el => { el.value = '40'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.waitForFunction(() => document.querySelector('#r0')?.textContent?.includes('10,00'));
    await page.locator('#p2').evaluate(el => { el.value = '4'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    const changed = await page.locator('.stats').innerText();
    if (!changed.includes('10,00 м/с²') || !changed.includes('40,00 Н') || !changed.includes('12,57 с')) {
      throw new Error(`unexpected recalculated model values: ${changed}`);
    }
    await page.locator('.answers button[data-answer="a"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Попробуйте ещё раз')) throw new Error('incorrect quiz answer was not rejected');
    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно!')) throw new Error('correct quiz answer was not accepted');

    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('horizontal overflow');
    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe serious/critical: ${serious.map(v => v.id).join(', ')}`);
    if (errors.length) throw new Error(errors.join(' | '));

    const dir = '/tmp/physics-visual-review/circular';
    const fs = await import('node:fs/promises');
    await fs.mkdir(dir, { recursive: true });
    await page.screenshot({ path: `${dir}/${mobile ? 'mobile' : 'desktop'}-model-and-quiz.png`, fullPage: true });
    console.log(`PASS circular standalone ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — controls, recalculation, quiz, overflow 0, axe serious/critical 0`);
  } catch (error) {
    failures.push(`circular standalone ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
