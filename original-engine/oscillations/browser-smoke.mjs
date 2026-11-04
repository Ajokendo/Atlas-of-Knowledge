import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

async function checkLesson(mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(12000);
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  try {
    const response = await page.goto(`${base}/chapters/oscillations.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`chapter HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Колебания', exact: true }).waitFor();

    const labCanvas = page.locator('.physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    const labState = await labCanvas.evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, webgl: !!gl };
    });
    if (!labState.webgl || labState.width < 100 || labState.height < 100) {
      throw new Error(`3D spring-lab WebGL canvas did not initialize: ${JSON.stringify(labState)}`);
    }

    await page.locator('[data-phase]').evaluate(el => {
      el.value = '100';
      el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    if (!(await page.locator('[data-physics-formula]').innerText()).includes('A = 1,00 м')) {
      throw new Error('3D laboratory amplitude control did not recalculate its physical readout');
    }
    const labPlay = page.locator('.physics-lab-controls button');
    if ((await labPlay.innerText()).trim() !== 'Продолжить') throw new Error('reduced-motion mode should begin with the 3D lab paused');
    await labPlay.click();
    if ((await labPlay.innerText()).trim() !== 'Пауза') throw new Error('3D lab play control did not start animation');
    await labPlay.click();
    if ((await labPlay.innerText()).trim() !== 'Продолжить') throw new Error('3D lab pause control did not stop animation');
    const required = [
      'Введение',
      '1. Период и частота',
      '2. Пружинный маятник',
      '3. Гармонические колебания',
      '4. Маятник и приближение малых углов',
      '5. Превращение энергии',
      '6. Затухающие и вынужденные колебания',
      '7. Как исследовать колебания',
      'Интерактивная модель: Пружинный маятник',
      'Проверьте себя',
    ];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`missing lesson sections: ${missing.join('; ')}`);

    const canvas = page.locator('#visual');
    await canvas.waitFor({ state: 'visible' });
    const graph = await canvas.evaluate(el => ({ width: el.width, height: el.height }));
    if (graph.width < 260 || graph.height < 160) throw new Error(`oscillation graph canvas too small: ${graph.width}×${graph.height}`);

    const readout = async id => (await page.locator(id).innerText()).replace(/\\s+/g, ' ').trim();
    if (!(await readout('#r0')).includes('0,889')) throw new Error(`default spring period should be 0.889 s, got ${await readout('#r0')}`);
    if (!(await readout('#r1')).includes('1,125')) throw new Error(`default frequency should be 1.125 Hz, got ${await readout('#r1')}`);
    if (!(await readout('#r2')).includes('7,071')) throw new Error(`default angular frequency should be 7.071 rad/s, got ${await readout('#r2')}`);

    await page.locator('#p0').evaluate(el => { el.value = '4'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('1,777')) throw new Error(`fourfold mass should double period, got ${await readout('#r0')}`);
    await page.locator('#p0').evaluate(el => { el.value = '1'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.locator('.answers button[data-answer="a"]').click();
    if (!(await readout('#feedback')).includes('Верно')) throw new Error('oscillations quiz rejected the correct answer');

    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe found ${serious.length} serious/critical violation groups: ${serious.map(v => v.id).join(', ')}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS oscillations lesson ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${required.length} sections, 3D WebGL lab ${labState.width}×${labState.height}, amplitude/play/pause controls, period/frequency graph, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL oscillations lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    if (errors.length) failures.push(`lesson runtime errors: ${errors.join(' | ')}`);
  } finally {
    await context.close();
  }
}

async function checkInteractiveBook(mobile) {
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
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  try {
    const response = await page.goto(`${base}/original-engine/oscillations/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`book HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1', { timeout: 12000 });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      const atlas = window.__atlas;
      return canvas && canvas.width > 0 && canvas.height > 0 &&
        document.querySelectorAll('#dots button').length === 12 &&
        atlas?.E?.renderer?.info?.render?.frame > 0 &&
        Object.keys(atlas.E.ASM || {}).length > 0;
    }, undefined, { timeout: 20000 });
    const initial = await page.evaluate(() => ({
      title: document.querySelector('#sheet h1')?.textContent?.trim(),
      pages: document.querySelectorAll('#dots button').length,
      canvas: [document.querySelector('#gl').width, document.querySelector('#gl').height],
      assemblies: Object.keys(window.__atlas.E.ASM || {}).length,
      overflow: document.documentElement.scrollWidth > innerWidth + 2,
    }));
    if (!initial.title || initial.pages !== 12 || initial.assemblies < 1) throw new Error(`book did not initialize correctly: ${JSON.stringify(initial)}`);
    if (initial.canvas[0] < 100 || initial.canvas[1] < 100) throw new Error(`WebGL canvas too small: ${initial.canvas.join('×')}`);
    if (initial.overflow) throw new Error('interactive book has horizontal overflow');
    const before = await page.locator('#folio').innerText();
    await page.locator('#dots button').nth(1).evaluate(button => button.click());
    await page.waitForFunction(previous => document.querySelector('#folio')?.textContent?.trim() !== previous, before, { timeout: 8000 });
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS oscillations interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 12 pages, WebGL ${initial.canvas.join('×')}, ${initial.assemblies} scene assemblies, page navigation`);
  } catch (error) {
    failures.push(`book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL oscillations book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    if (errors.length) failures.push(`book runtime errors: ${errors.join(' | ')}`);
  } finally {
    await context.close();
  }
}

try {
  for (const mobile of [false, true]) await checkLesson(mobile);
  for (const mobile of [false, true]) await checkInteractiveBook(mobile);
} finally {
  await browser.close();
}
if (failures.length) {
  console.error(failures.join('\\n'));
  process.exit(1);
}
console.log('PASS oscillations browser smoke: 4/4 desktop/mobile lesson and interactive-book runs');
