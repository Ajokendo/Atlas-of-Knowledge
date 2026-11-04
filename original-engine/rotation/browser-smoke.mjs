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
    const response = await page.goto(`${base}/chapters/rotation.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`chapter HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Вращение', exact: true }).first().waitFor();

    const labCanvas = page.locator('.physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    const labState = await labCanvas.evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, webgl: !!gl };
    });
    if (!labState.webgl || labState.width < 100 || labState.height < 100) {
      throw new Error(`3D rotation-lab WebGL canvas did not initialize: ${JSON.stringify(labState)}`);
    }

    const formula = page.locator('[data-physics-formula]');
    if (!(await formula.innerText()).includes('α = τ / I = 2 / 1,05')) {
      throw new Error(`default rotation model should calculate α = 2/1.05, got ${await formula.innerText()}`);
    }
    await page.locator('[data-phase]').evaluate(el => {
      el.value = '100';
      el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    if (!(await formula.innerText()).includes('α = τ / I = 2 / 2,00')) {
      throw new Error('rotation inertia control did not recalculate angular acceleration');
    }
    const labPlay = page.locator('.physics-lab-controls button');
    if ((await labPlay.innerText()).trim() !== 'Продолжить') throw new Error('reduced-motion mode should begin with the 3D lab paused');
    await labPlay.click();
    if ((await labPlay.innerText()).trim() !== 'Пауза') throw new Error('3D lab play control did not start animation');
    await labPlay.click();
    if ((await labPlay.innerText()).trim() !== 'Продолжить') throw new Error('3D lab pause control did not stop animation');

    const required = [
      'Введение',
      '1. Угловое перемещение, скорость и ускорение',
      '2. Как связаны вращение и движение по окружности',
      '3. Момент силы: как сила поворачивает тело',
      '4. Момент инерции и второй закон для вращения',
      '5. Равновесие: силы и моменты',
      '6. Вращательная энергия, работа и мощность',
      '7. Момент импульса и его сохранение',
      '8. Как исследовать вращение',
      'Интерактивная модель: момент силы на рычаге',
      'Проверьте себя',
    ];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`missing lesson sections: ${missing.join('; ')}`);

    const readout = async id => (await page.locator(id).innerText()).replace(/\\s+/g, ' ').trim();
    if (!(await readout('#r0')).includes('8,00 Н·м')) throw new Error(`default torque should be 8 N·m, got ${await readout('#r0')}`);
    await page.locator('#p2').evaluate(el => { el.value = '0'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('0,00 Н·м')) throw new Error('force parallel to lever should produce zero torque');
    await page.locator('#p2').evaluate(el => { el.value = '90'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.locator('.answers button[data-answer="c"]').click();
    if (!(await readout('#feedback')).includes('Верно')) throw new Error('rotation quiz rejected the correct answer');

    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe found ${serious.length} serious/critical violation groups: ${serious.map(v => v.id).join(', ')}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS rotation lesson ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${required.length} sections, 3D WebGL lab ${labState.width}×${labState.height}, inertia/torque controls, zero-torque edge case, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL rotation lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
    const response = await page.goto(`${base}/original-engine/rotation/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`book HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1', { timeout: 12000 });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 0 && canvas.height > 0 &&
        document.querySelectorAll('#dots button').length === 15 &&
        canvas.getContext('webgl2') !== null || canvas.getContext('webgl') !== null;
    }, undefined, { timeout: 20000 });
    const initial = await page.evaluate(() => ({
      title: document.querySelector('#sheet h1')?.textContent?.trim(),
      pages: document.querySelectorAll('#dots button').length,
      canvas: [document.querySelector('#gl').width, document.querySelector('#gl').height],
      webgl: !!(document.querySelector('#gl').getContext('webgl2') || document.querySelector('#gl').getContext('webgl')),
      overflow: document.documentElement.scrollWidth > innerWidth + 2,
    }));
    if (!initial.title || initial.pages !== 15 || !initial.webgl) throw new Error(`book did not initialize correctly: ${JSON.stringify(initial)}`);
    if (initial.canvas[0] < 100 || initial.canvas[1] < 100) throw new Error(`WebGL canvas too small: ${initial.canvas.join('×')}`);
    if (initial.overflow) throw new Error('interactive book has horizontal overflow');
    await page.locator('#dots button').nth(1).click();
    await page.waitForFunction(() => document.querySelector('#sheet h1')?.textContent?.trim() === 'Два пассажира', undefined, { timeout: 8000 });
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS rotation interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 15 pages, WebGL ${initial.canvas.join('×')}, ${initial.pages} indexed pages, page navigation`);
  } catch (error) {
    failures.push(`book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL rotation book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
console.log('PASS rotation browser smoke: 4/4 desktop/mobile lesson and interactive-book runs');
