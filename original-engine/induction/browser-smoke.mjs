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
    const response = await page.goto(`${base}/original-engine/induction/`, { waitUntil: 'domcontentloaded', timeout: 20000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => { const c = document.querySelector('#gl'); return c && c.width > 100 && c.height > 100 && !!(c.getContext('webgl2') || c.getContext('webgl')); }, null, { timeout: 25000 });
    const dots = page.locator('#dots button');
    if (await dots.count() !== 10) throw new Error(`expected 10 pages, got ${await dots.count()}`);
    const canvas = await page.locator('#gl').evaluate(c => ({ w:c.width,h:c.height }));
    for (let i=0;i<10;i++) {
      if (mobile && i > 0) {
        const next = page.locator('#sheet .turn');
        if (await next.count() !== 1) throw new Error(`page ${i} has no mobile next-page control`);
        await next.click();
        await page.waitForFunction(n => location.hash === `#${n}`, i);
        await page.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n+1, i);
      } else if (!mobile) {
        await dots.nth(i).click();
        await page.waitForFunction(n => Number(document.querySelector('#folio')?.textContent) === n+1, i);
      }
      if (!(await page.locator('#sheet h1').innerText()).trim()) throw new Error(`page ${i+1} has no title`);
      if (!(await page.locator('#readout').innerText()).trim()) throw new Error(`page ${i+1} has no live readout`);
      if (i === 4) {
        const motionalEmf = await page.locator('#sheet').innerText();
        if (!motionalEmf.includes('|q|E') || !motionalEmf.includes('|q|vB')) throw new Error('motional-emf balance must use charge magnitudes for either charge sign');
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
    console.log(`PASS induction ${mobile?'mobile 390×844':'desktop 1440×900'} — 10/10 pages navigated, WebGL ${canvas.w}×${canvas.h}, live readouts, overflow 0, axe serious/critical 0`);
  } catch(e) { failures.push(`${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL induction ${mobile?'mobile':'desktop'}: ${e.message}`); }
  finally { await context.close(); }
}

async function runDynamic(mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1, isMobile: mobile, hasTouch: mobile,
    reducedMotion: 'no-preference'
  });
  const page = await context.newPage(); page.setDefaultTimeout(15000);
  await page.emulateMedia({ reducedMotion: 'no-preference' });
  try {
    const response = await page.goto(`${base}/original-engine/induction/`, { waitUntil: 'domcontentloaded' });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => document.querySelector('#gl')?.width > 100);
    await page.waitForFunction(() => window.__atlas && document.querySelector('#readout')?.textContent.includes('Φ') && document.querySelector('#readout')?.textContent.includes('ε'));
    // Keep the pointer outside the 3D canvas: hovering a scene object intentionally pauses its clock.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(350);
    const before = await page.locator('#readout').innerText();
    const cursorBefore = await page.locator('circle[data-cursor="phi0"]').first().evaluate(el => [el.getAttribute('cx'), el.getAttribute('cy')]);
    await page.waitForTimeout(2000);
    const after = await page.locator('#readout').innerText();
    const cursorAfter = await page.locator('circle[data-cursor="phi0"]').first().evaluate(el => [el.getAttribute('cx'), el.getAttribute('cy')]);
    const motion = await page.evaluate(() => ({ reduced: matchMedia('(prefers-reduced-motion: reduce)').matches, ready: !!window.__atlas }));
    if (before === after && cursorBefore.join(',') === cursorAfter.join(',')) throw new Error(`animation stalled: ${JSON.stringify({ before, after, cursorBefore, cursorAfter, motion })}`);
    if (before === after) console.warn('readout text unchanged at display precision; graph cursor moved');
    if (cursorBefore.join(',') === cursorAfter.join(',')) console.warn('graph cursor unchanged; readout changed');
    console.log(`PASS induction flux dynamic ${mobile?'mobile':'desktop'} — live state responds (readout ${before === after ? 'stable at display precision' : 'changed'}, graph cursor ${cursorBefore.join(',') === cursorAfter.join(',') ? 'stable' : 'moved'})`);
  } catch(e) { failures.push(`dynamic ${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL induction flux dynamic ${mobile?'mobile':'desktop'}: ${e.message}`); }
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
    const response = await page.goto(`${base}/chapters/induction.html`, { waitUntil: 'domcontentloaded' });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForFunction(() => document.querySelector('#r0')?.textContent.trim().length > 0);
    const equations = await page.locator('.equation').allInnerTexts();
    if (!equations.some(x => x.includes('εср') && x.includes('ΔΦ/Δt') && x.includes('dΦ/dt'))) throw new Error('Faraday law must distinguish average and instantaneous emf');
    const before = await page.locator('#r0').innerText();
    await page.locator('#p0').evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); }, '200');
    await page.waitForFunction(v => document.querySelector('#r0')?.textContent !== v, before);
    const after = await page.locator('#r0').innerText();
    const number = v => Number(v.trim().split(/\s+/)[0].replace(',', '.'));
    if (!(number(after) > number(before))) throw new Error(`calculator did not increase: ${before} → ${after}`);
    await page.locator('button[data-answer="b"]').click();
    await page.waitForFunction(() => document.querySelector('#feedback')?.textContent.includes('Верно!'));
    const visuals = page.locator('figure.visual-figure img');
    if (await visuals.count() !== 3) throw new Error('Chapter 15 must contain all three integrated induction visuals');
    for (let i = 0; i < 3; i++) await visuals.nth(i).scrollIntoViewIfNeeded();
    await page.waitForFunction(() => [...document.querySelectorAll('figure.visual-figure img')].length === 3 && [...document.querySelectorAll('figure.visual-figure img')].every(img => img.complete && img.naturalWidth > 0));
    const visualStates = await visuals.evaluateAll(nodes => nodes.map(img => ({ alt: img.alt, currentSrc: img.currentSrc, caption: img.closest('figure')?.querySelector('figcaption')?.innerText || '', ru: !!img.closest('figure')?.querySelector('figcaption [lang="ru"]'), en: !!img.closest('figure')?.querySelector('figcaption [lang="en"]') })));
    for (const visual of visualStates) {
      if (!visual.alt || visual.alt.length < 40 || !visual.ru || !visual.en || !visual.caption) throw new Error('Chapter 15 visual needs meaningful alt text and bilingual caption');
      if (mobile && !visual.currentSrc.includes('-mobile.svg')) throw new Error('Chapter 15 mobile layout was not selected');
      if (!mobile && visual.currentSrc.includes('-mobile.svg')) throw new Error('Chapter 15 desktop layout was not selected');
    }
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)) throw new Error('horizontal overflow');
    console.log(`PASS Chapter 15 Faraday calculator ${mobile?'mobile':'desktop'} — slider, quiz, 3 responsive SVGs, bilingual captions, alt text, overflow 0`);
  } catch(e) { failures.push(`lesson ${mobile?'mobile':'desktop'}: ${e.message}`); console.error(`FAIL Chapter 15 Faraday calculator ${mobile?'mobile':'desktop'}: ${e.message}`); }
  finally { await context.close(); }
}

await run(false); await run(true); await runDynamic(false); await runDynamic(true); await runLesson(false); await runLesson(true); await browser.close();
if (failures.length) process.exit(1);
