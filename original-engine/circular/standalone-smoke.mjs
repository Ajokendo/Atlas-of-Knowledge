import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

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

    // Also inspect the interactive-book chrome: on phones the mouse hint must
    // give way to the touch selector, and the selector must sit below the title.
    const book = await context.newPage();
    book.setDefaultTimeout(20000);
    const bookResponse = await book.goto(`${base}/original-engine/circular/`, { waitUntil: 'domcontentloaded' });
    if (!bookResponse?.ok()) throw new Error(`interactive book HTTP ${bookResponse?.status() ?? 'missing'}`);
    await book.waitForSelector('#sheet h1');
    await book.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 100 && canvas.height > 100 && !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
    }, null, { timeout: 30000 });
    await book.waitForFunction(() => !!document.querySelector('.scene-picker'), null, { timeout: 15000 });
    await book.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 100 && canvas.height > 100;
    });
    const chrome = await book.evaluate(() => {
      const rect = el => { const r = el.getBoundingClientRect(); return { top: r.top, bottom: r.bottom, left: r.left, right: r.right }; };
      return {
        hintDisplay: getComputedStyle(document.querySelector('#hint')).display,
        pickerDisplay: getComputedStyle(document.querySelector('.scene-picker')).display,
        title: rect(document.querySelector('#figtitle')),
        picker: rect(document.querySelector('.scene-picker')),
        figure: rect(document.querySelector('.figure'))
      };
    });
    if (mobile && chrome.hintDisplay !== 'none') throw new Error('mobile mouse hint should be hidden');
    if (mobile && chrome.pickerDisplay === 'none') throw new Error('mobile scene picker should be visible');
    if (mobile && chrome.picker.top < chrome.title.bottom - 2) throw new Error('mobile scene picker overlaps the scene title');
    if (await book.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('interactive book horizontal overflow');
    const dots = book.locator('#dots button');
    if (await dots.count() !== 13) throw new Error(`expected 13 scene pages, got ${await dots.count()}`);
    for (let i = 0; i < 13; i++) {
      if (mobile && i > 0) {
        const next = book.locator('#sheet .turn');
        if (await next.count() !== 1) throw new Error(`mobile page ${i + 1} has no next-page control`);
        await next.click();
        await book.waitForFunction(n => location.hash === `#${n}`, i);
      } else if (!mobile) {
        await dots.nth(i).click();
      }
      await book.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n + 1, i);
      if (!(await book.locator('#sheet h1').innerText()).trim()) throw new Error(`page ${i + 1} has no title`);
      await book.waitForTimeout(120);
      if (mobile) {
        const clipped = await book.evaluate(() => {
          const f = document.querySelector('.figure').getBoundingClientRect();
          return [...document.querySelectorAll('#labels .lbl')].filter(el => {
            const style = getComputedStyle(el), r = el.getBoundingClientRect();
            return style.display !== 'none' && Number(style.opacity) > 0.5 && el.textContent.trim() &&
              (r.left < f.left - 1 || r.right > f.right + 1 || r.top < f.top - 1 || r.bottom > f.bottom + 1);
          }).map(el => el.textContent.trim());
        });
        if (clipped.length) throw new Error(`mobile page ${i + 1} has clipped 3D labels: ${clipped.join(', ')}`);
      }
      await book.screenshot({ path: `${dir}/${mobile ? 'mobile' : 'desktop'}-book-page-${String(i + 1).padStart(2, '0')}.png`, fullPage: false, timeout: 60000, animations: 'disabled' });
    }
    await book.close();
    console.log(`PASS circular standalone ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — controls, recalculation, quiz, responsive book chrome, overflow 0, axe serious/critical 0`);
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
