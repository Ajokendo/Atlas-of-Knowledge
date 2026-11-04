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
    const response = await page.goto(`${base}/chapters/fluids.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`chapter HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Жидкости', exact: true }).first().waitFor();

    const labCanvas = page.locator('.physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    const labState = await labCanvas.evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, webgl: !!gl };
    });
    if (!labState.webgl || labState.width < 100 || labState.height < 100) {
      throw new Error(`3D fluids-lab WebGL canvas did not initialize: ${JSON.stringify(labState)}`);
    }

    const required = [
      'Введение', '1. Плотность вещества', '2. Давление', '3. Давление внутри жидкости',
      '4. Закон Паскаля и гидравлические машины', '5. Сила Архимеда',
      '6. Почему тела плавают или тонут', '7. Движение жидкости: уравнение непрерывности',
      '8. Уравнение Бернулли', '9. Закон Торричелли',
      'Интерактивная модель: давление и выталкивающая сила', 'Проверьте себя',
    ];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`missing lesson sections: ${missing.join('; ')}`);

    const readout = async id => (await page.locator(id).innerText()).replace(/\\s+/g, ' ').trim();
    if (!(await readout('#r0')).includes('19600 Па')) throw new Error(`default gauge pressure should be 19600 Pa, got ${await readout('#r0')}`);
    if (!(await readout('#r1')).includes('196,00 Н')) throw new Error(`default buoyancy should be 196 N, got ${await readout('#r1')}`);
    await page.locator('#p0').evaluate(el => { el.value = '4'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('39200 Па')) throw new Error('depth slider did not double hydrostatic pressure');
    await page.locator('#p1').evaluate(el => { el.value = '500'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r1')).includes('98,00 Н')) throw new Error('density slider did not halve buoyant force');
    await page.locator('.answers button[data-answer="a"]').click();
    if (!(await readout('#feedback')).includes('Верно')) throw new Error('fluids quiz rejected the correct answer');

    const play = page.locator('.physics-lab-controls button');
    if ((await play.innerText()).trim() !== 'Продолжить') throw new Error('reduced-motion mode should begin with the 3D lab paused');
    await play.click();
    if ((await play.innerText()).trim() !== 'Пауза') throw new Error('3D lab play control did not start animation');
    await play.click();
    if ((await play.innerText()).trim() !== 'Продолжить') throw new Error('3D lab pause control did not stop animation');

    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe found ${serious.length} serious/critical violation groups: ${serious.map(v => v.id).join(', ')}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS fluids lesson ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${required.length} sections, 3D WebGL lab ${labState.width}×${labState.height}, pressure/buoyancy controls, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL fluids lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
    const response = await page.goto(`${base}/original-engine/fluids/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`book HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1', { timeout: 12000 });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 0 && canvas.height > 0 &&
        document.querySelectorAll('#dots button').length === 9 &&
        !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
    }, undefined, { timeout: 20000 });
    const initial = await page.evaluate(() => ({
      title: document.querySelector('#sheet h1')?.textContent?.trim(),
      pages: document.querySelectorAll('#dots button').length,
      canvas: [document.querySelector('#gl').width, document.querySelector('#gl').height],
      webgl: !!(document.querySelector('#gl').getContext('webgl2') || document.querySelector('#gl').getContext('webgl')),
      overflow: document.documentElement.scrollWidth > innerWidth + 2,
    }));
    if (initial.title !== 'Жидкости' || initial.pages !== 9 || !initial.webgl) throw new Error(`book did not initialize correctly: ${JSON.stringify(initial)}`);
    if (initial.canvas[0] < 100 || initial.canvas[1] < 100) throw new Error(`WebGL canvas too small: ${initial.canvas.join('×')}`);
    if (initial.overflow) throw new Error('interactive book has horizontal overflow');
    await page.locator('#dots button').nth(8).evaluate(button => button.click());
    await page.waitForFunction(() => document.querySelector('#sheet h1')?.textContent?.trim() === 'Закон Торричелли', undefined, { timeout: 8000 });
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS fluids interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 9 pages, WebGL ${initial.canvas.join('×')}, page navigation to Torricelli`);
  } catch (error) {
    failures.push(`book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL fluids book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
console.log('PASS fluids browser smoke: 4/4 desktop/mobile lesson and interactive-book runs');
