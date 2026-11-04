import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
const browser = await chromium.launch({ headless: true, args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'] });

async function run(mobile) {
  const context = await browser.newContext({ viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 }, deviceScaleFactor: mobile ? 2 : 1, isMobile: mobile, hasTouch: mobile, reducedMotion: 'reduce' });
  const page = await context.newPage(); page.setDefaultTimeout(15000);
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error' && !/fonts\.googleapis|cdn\.jsdelivr/i.test(m.text())) errors.push(m.text()); });
  try {
    const response = await page.goto(`${base}/original-engine/magnetism/`, { waitUntil: 'domcontentloaded', timeout: 20000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => { const c = document.querySelector('#gl'); return c && c.width > 100 && c.height > 100 && !!(c.getContext('webgl2') || c.getContext('webgl')); }, null, { timeout: 25000 });
    const dots = page.locator('#dots button');
    if (await dots.count() !== 9) throw new Error(`expected 9 pages, got ${await dots.count()}`);
    const canvas = await page.locator('#gl').evaluate(c => ({ w:c.width,h:c.height }));
    for (let i=0;i<9;i++) {
      if (mobile && i < 8) {
        const next = page.locator('#sheet .turn');
        if (await next.count() !== 1) throw new Error(`page ${i+1} has no mobile next-page control`);
        await next.click();
        await page.waitForFunction(n => location.hash === `#${n}`, i+1);
      } else if (!mobile) {
        await dots.nth(i).click();
        await page.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n+1, i);
      } else {
        await page.waitForFunction(() => !document.querySelector('#sheet .turn'));
      }
      if (!(await page.locator('#sheet h1').innerText()).trim()) throw new Error(`page ${i+1} has no title`);
      if (!(await page.locator('#readout').innerText()).trim()) throw new Error(`page ${i+1} has no live readout`);
      if (i === 3) {
        const selectorText = await page.locator('#sheet').evaluate(el => el.textContent.replace(/\s+/g, ''));
        if (!selectorText.includes('|q|E') || !selectorText.includes('|q|vB')) throw new Error('velocity-selector balance must compare force magnitudes');
        if (!selectorText.includes('|ΔV_H|') || !selectorText.includes('n|q|A')) throw new Error('Hall-voltage magnitude must use |q| and preserve carrier-sign distinction');
      }
    }
    const picker = page.locator('select.scene-picker');
    if (await picker.count() !== 1 || await picker.locator('option').count() < 2) throw new Error('accessible scene picker is missing usable objects');
    await picker.selectOption({ index: 1 });
    await page.waitForFunction(() => { const p = document.querySelector('#plate'); return p && !p.hidden; });
    await page.waitForFunction(() => document.querySelectorAll('#facts tr').length > 0);
    await page.locator('#plate .close').click();
    await page.waitForFunction(() => document.querySelector('#plate')?.hidden);
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('horizontal overflow');
    const axe = await new AxeBuilder({ page }).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe serious/critical: ${serious.map(v=>v.id).join(', ')}`);
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS magnetism ${mobile?'mobile 390×844':'desktop 1440×900'} — 9/9 pages navigated, WebGL ${canvas.w}×${canvas.h}, live readouts, overflow 0, axe serious/critical 0`);
  } catch(e) { failures.push(`${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL magnetism ${mobile?'mobile':'desktop'}: ${e.message}`); }
  finally { await context.close(); }
}

async function runDynamic(mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1, isMobile: mobile, hasTouch: mobile,
    reducedMotion: 'no-preference'
  });
  const page = await context.newPage(); page.setDefaultTimeout(15000);
  try {
    const response = await page.goto(`${base}/original-engine/magnetism/`, { waitUntil: 'domcontentloaded' });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => document.querySelector('#gl')?.width > 100);
    await page.waitForFunction(() => window.__atlas && document.querySelector('#readout')?.textContent.trim().length > 0);
    if (mobile) await page.locator('#sheet .turn').click(); else await page.locator('#dots button').nth(1).click();
    await page.waitForFunction(() => location.hash === '#1');
    // The shared book intentionally pauses its clock while the pointer hovers over a scene/control.
    // Move away after navigation so this test measures animation rather than the hover-to-pause UX.
    await page.mouse.move(10, 10);
    await page.waitForFunction(() => document.querySelector('#readout')?.textContent.includes('θ'));
    await page.waitForTimeout(350);
    const before = await page.locator('#readout').innerText();
    const cursorBefore = await page.locator('circle[data-cursor="rhr"]').first().evaluate(el => [el.getAttribute('cx'), el.getAttribute('cy')]);
    await page.waitForTimeout(1200);
    const after = await page.locator('#readout').innerText();
    const cursorAfter = await page.locator('circle[data-cursor="rhr"]').first().evaluate(el => [el.getAttribute('cx'), el.getAttribute('cy')]);
    if (before === after) throw new Error('animated readout did not change with time');
    if (cursorBefore.join(',') === cursorAfter.join(',')) throw new Error('live graph cursor did not move with time');
    console.log(`PASS magnetism RHR dynamic ${mobile?'mobile':'desktop'} — readout and graph cursor update`);
  } catch(e) { failures.push(`dynamic ${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL magnetism RHR dynamic ${mobile?'mobile':'desktop'}: ${e.message}`); }
  finally { await context.close(); }
}


async function runLesson(mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1, isMobile: mobile, hasTouch: mobile,
    reducedMotion: 'reduce'
  });
  const page = await context.newPage(); page.setDefaultTimeout(15000);
  try {
    const response = await page.goto(`${base}/chapters/magnetism.html`, { waitUntil: 'domcontentloaded' });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForFunction(() => document.querySelector('#r0')?.textContent.trim().length > 0);
    const equations = await page.locator('.equation').allInnerTexts();
    if (!equations.some(x => x.includes('|q|E') && x.includes('|q|vB'))) throw new Error('velocity-selector balance must compare force magnitudes');
    if (equations.some(x => x.includes('qE = |q|vB'))) throw new Error('signed qE notation is invalid for the magnitude balance');
    const before = await page.locator('#r0').innerText();
    await page.locator('#p1').evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); }, '2000');
    await page.waitForFunction(v => document.querySelector('#r0')?.textContent !== v, before);
    const after = await page.locator('#r0').innerText();
    const number = v => Number(v.trim().split(/\s+/)[0].replace(',', '.'));
    if (!(number(after) > number(before))) throw new Error(`calculator did not increase: ${before} → ${after}`);
    await page.locator('button[data-answer="b"]').click();
    await page.waitForFunction(() => document.querySelector('#feedback')?.textContent.includes('Верно!'));
    if (await page.locator('.note').filter({ hasText: 'IMAGE PLACEHOLDER' }).count() < 1) throw new Error('image-first placeholders are missing');
    const imageFirst = await page.evaluate(() => { const marker = [...document.querySelectorAll('.note')].find(el => el.textContent.includes('IMAGE PLACEHOLDER')); const firstTopic = [...document.querySelectorAll('section h2')].find(el => el.textContent.includes('1. Магнитное поле')); return !!marker && !!firstTopic && !!(marker.compareDocumentPosition(firstTopic) & Node.DOCUMENT_POSITION_FOLLOWING); });
    if (!imageFirst) throw new Error('Chapter 14 illustration marker must precede detailed topic text');
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('horizontal overflow');
    console.log(`PASS Chapter 14 Lorentz-force calculator ${mobile?'mobile':'desktop'} — slider calculation, quiz, placeholders, overflow 0`);
  } catch(e) { failures.push(`lesson ${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL Chapter 14 Lorentz-force calculator ${mobile?'mobile':'desktop'}: ${e.message}`); }
  finally { await context.close(); }
}

await run(false); await run(true); await runDynamic(false); await runDynamic(true); await runLesson(false); await runLesson(true); await browser.close();
if (failures.length) process.exit(1);
