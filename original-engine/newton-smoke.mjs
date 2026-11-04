import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

async function audit(page, label) {
  const axe = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();
  const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
  if (serious.length) {
    const details = serious.map(v => ({
      id: v.id, impact: v.impact,
      nodes: v.nodes.slice(0, 10).map(n => ({ target: n.target, html: n.html, summary: n.failureSummary })),
    }));
    throw new Error(`${label} axe serious/critical violations: ${JSON.stringify(details)}`);
  }
}

async function checkBook(viewport, mobile) {
  const context = await browser.newContext({
    viewport, deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile, hasTouch: mobile, reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('response', r => { if (r.status() >= 400) errors.push(`HTTP ${r.status()} ${r.url()}`); });
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  try {
    const response = await page.goto(`${base}/original-engine/newton/`, { waitUntil: 'domcontentloaded', timeout: 20000 });
    if (!response?.ok()) throw new Error(`Interactive book HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1');
    await page.waitForFunction(() => {
      const a = window.__atlas, c = document.querySelector('#gl');
      return !!a?.E?.renderer && a.E.renderer.info.render.frame > 0 &&
        !!c && c.width > 0 && c.height > 0 &&
        !!(c.getContext('webgl2') || c.getContext('webgl'));
    }, undefined, { timeout: 25000 });

    const initial = await page.evaluate(() => ({
      title: document.querySelector('#sheet h1')?.textContent.trim(),
      pages: document.querySelectorAll('#dots button').length,
      frames: window.__atlas?.E?.renderer?.info?.render?.frame || 0,
      assemblies: Object.keys(window.__atlas?.E?.ASM || {}).length,
      canvas: [document.querySelector('#gl').width, document.querySelector('#gl').height],
      status: !!document.querySelector('.page-announcement[role="status"][aria-live="polite"]'),
    }));
    if (initial.title !== 'Законы Ньютона') throw new Error(`Unexpected opening page: ${initial.title}`);
    if (initial.pages !== 13) throw new Error(`Expected 13 book pages, found ${initial.pages}`);
    if (!initial.assemblies || !initial.frames || !initial.status) throw new Error('Three.js scene, rendered frame, or accessible page status is missing');

    const expectedTitles = [];
    for (let i = 0; i < 13; i++) {
      const dot = page.locator('#dots button').nth(i);
      await dot.click();
      await page.waitForFunction(index => location.hash === `#${index}` || (index === 0 && !location.hash), i, { timeout: 10000 });
      await page.waitForFunction(() => !!document.querySelector('#sheet h1')?.textContent.trim());
      expectedTitles.push(await page.locator('#sheet h1').innerText());
    }
    if (new Set(expectedTitles).size !== 13) throw new Error(`Page navigation produced duplicate/empty headings: ${expectedTitles.join(' | ')}`);

    await page.locator('#dots button').nth(1).click();
    await page.waitForFunction(() => location.hash === '#1');
    const picker = page.locator('select.scene-picker');
    await picker.waitFor();
    const optionCount = await picker.locator('option').count();
    if (optionCount < 2) throw new Error('Keyboard-accessible 3D scene object picker has no selectable objects');
    await picker.selectOption({ index: 1 });
    await page.locator('#plate[role="region"]').waitFor({ state: 'visible' });
    await picker.selectOption('');
    await page.locator('#plate[hidden]').waitFor();

    await audit(page, `Newton interactive book ${mobile ? 'mobile' : 'desktop'}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('Interactive book has horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS Newton interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 13 pages navigated, WebGL ${initial.canvas.join('×')}, ${initial.frames} initial renderer frames, scene picker, breakdown panel, serious/critical axe violations: 0`);
  } catch (e) {
    failures.push(`Newton interactive book ${mobile ? 'mobile' : 'desktop'}: ${e.message}`);
    console.error(`FAIL Newton interactive book ${mobile ? 'mobile' : 'desktop'}: ${e.message}`);
    if (errors.length) failures.push(`Newton book runtime/console: ${errors.join(' | ')}`);
  } finally {
    await context.close();
  }
}

async function checkChapterPage(viewport, mobile) {
  const context = await browser.newContext({
    viewport, deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile, hasTouch: mobile, reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('response', r => { if (r.status() >= 400) errors.push(`HTTP ${r.status()} ${r.url()}`); });
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  try {
    const response = await page.goto(`${base}/chapters/newton-laws.html`, { waitUntil: 'domcontentloaded', timeout: 20000 });
    if (!response?.ok()) throw new Error(`Chapter page HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Законы Ньютона', exact: true }).waitFor();
    const required = [
      '1. Первый закон: закон инерции',
      '2. Второй закон: связь силы и ускорения',
      '3. Интерактивный опыт: сила и ускорение',
      '4. Третий закон: действие и противодействие',
      '5. Проверьте себя',
    ];
    const headings = await page.locator('main.lesson > section h2').allTextContents();
    const missing = required.filter(h => !headings.includes(h));
    if (missing.length) throw new Error(`Missing lesson sections: ${missing.join('; ')}`);

    for (const [selector, value] of [['#force', '12'], ['#mass', '4'], ['#seconds', '2']]) {
      await page.locator(selector).evaluate((el, v) => {
        el.value = v; el.dispatchEvent(new Event('input', { bubbles: true }));
      }, value);
    }
    const stats = await Promise.all(['#acc', '#vel', '#pos'].map(s => page.locator(s).innerText()));
    if (!stats[0].includes('3,00') || !stats[1].includes('6,0') || !stats[2].includes('6,0')) {
      throw new Error(`Newton second-law model mismatch for F=12 N, m=4 kg, t=2 s: ${stats.join(' / ')}`);
    }
    const plot = await page.locator('#forceplot').evaluate(c => ({ w: c.width, h: c.height, context: !!c.getContext('2d') }));
    if (plot.w < 100 || plot.h < 80 || !plot.context) throw new Error('Force diagram canvas did not initialize');
    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно')) throw new Error('Chapter quiz rejected the correct answer');

    const labCanvas = page.locator('[data-physics-lab] .physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    await page.waitForFunction(() => {
      const c = document.querySelector('[data-physics-lab] .physics-stage canvas');
      return !!c && c.width > 0 && c.height > 0 && !!(c.getContext('webgl2') || c.getContext('webgl'));
    }, undefined, { timeout: 20000 });
    const lab = await labCanvas.evaluate(c => ({ w: c.width, h: c.height, label: c.getAttribute('aria-label') }));
    if (lab.w < 100 || lab.h < 100 || !lab.label) throw new Error('Chapter page WebGL lab did not render or lacks an accessible name');

    await audit(page, `Newton chapter page ${mobile ? 'mobile' : 'desktop'}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('Chapter page has horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS Newton chapter page ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — 5 sections, live F=ma model, force canvas, quiz, WebGL lab ${lab.w}×${lab.h}, serious/critical axe violations: 0`);
  } catch (e) {
    failures.push(`Newton chapter page ${mobile ? 'mobile' : 'desktop'}: ${e.message}`);
    console.error(`FAIL Newton chapter page ${mobile ? 'mobile' : 'desktop'}: ${e.message}`);
    if (errors.length) failures.push(`Newton page runtime/console: ${errors.join(' | ')}`);
  } finally {
    await context.close();
  }
}

try {
  await checkBook({ width: 1440, height: 900 }, false);
  await checkBook({ width: 390, height: 844 }, true);
  await checkChapterPage({ width: 1440, height: 900 }, false);
  await checkChapterPage({ width: 390, height: 844 }, true);
} finally {
  await browser.close();
}
if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
}
