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
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  try {
    const response = await page.goto(`${base}/chapters/electrostatics.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`chapter HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Электростатика', exact: true }).first().waitFor();

    const required = [
      'Введение', '1. Электрический заряд', '2. Как тела электризуются',
      '3. Закон Кулона', '4. Принцип суперпозиции',
      '5. Электрическое поле и его напряжённость', '6. Силовые линии поля',
      '7. Электрический диполь', '8. Поля протяжённых заряженных тел',
      '9. Заряд в однородном электрическом поле',
      'Интерактивная модель: Закон Кулона', 'Проверьте себя',
    ];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`missing lesson sections: ${missing.join('; ')}`);

    const labCanvas = page.locator('.physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    const labState = await labCanvas.evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, webgl: !!gl };
    });
    if (!labState.webgl || labState.width < 100 || labState.height < 100) {
      throw new Error(`3D electrostatics lab WebGL canvas did not initialize: ${JSON.stringify(labState)}`);
    }
    await page.waitForFunction(() => document.querySelector('.physics-stage canvas')?.getAttribute('aria-label')?.includes('эквипотенциальных контуров'));
    const bookLink = page.getByRole('link', { name: /интерактивную девятистраничную книгу по электростатике/i });
    if (!(await bookLink.getAttribute('href'))?.includes('../original-engine/electrostatics/')) throw new Error('link to the detailed electrostatics book is missing');

    const readout = async id => (await page.locator(id).innerText()).replace(/\s+/g, ' ').trim();
    if (!(await readout('#r0')).includes('5,3925 Н')) throw new Error(`default Coulomb force should be 5.3925 N, got ${await readout('#r0')}`);
    if (!(await readout('#r1')).includes('1797510 Н/Кл')) throw new Error(`default field should be about 1.79751e6 N/C, got ${await readout('#r1')}`);
    if (!(await readout('#r2')).includes('Отталкивание')) throw new Error('equal-sign charges should repel');
    const diagram = page.locator('#visual');
    const initialDiagram = await diagram.evaluate(canvas => {
      const ctx = canvas.getContext('2d');
      const pixels = ctx?.getImageData(0, 0, canvas.width, canvas.height).data;
      let painted = 0;
      if (pixels) for (let i = 3; i < pixels.length; i += 4) if (pixels[i] > 0) painted++;
      return { width: canvas.width, height: canvas.height, distance: canvas.dataset.distance, interaction: canvas.dataset.interaction, paintedPixels: painted };
    });
    if (initialDiagram.width < 100 || initialDiagram.height < 100 || initialDiagram.distance !== '0.10' || initialDiagram.interaction !== 'repulsion' || initialDiagram.paintedPixels < 500) throw new Error(`Coulomb diagram did not render its initial state: ${JSON.stringify(initialDiagram)}`);
    await page.locator('#sign2').selectOption('-1');
    if (!(await readout('#r2')).includes('Притяжение')) throw new Error('opposite-sign charges should attract');
    if (await diagram.getAttribute('data-interaction') !== 'attraction') throw new Error('charge diagram did not switch to attraction');
    if (!(await readout('#r0')).includes('5,3925 Н')) throw new Error('changing charge sign should not change the force magnitude');
    await page.locator('#p2').evaluate(el => { el.value = '0.2'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('1,3481 Н')) throw new Error('doubling distance should reduce Coulomb force to one quarter');
    if (await diagram.getAttribute('data-distance') !== '0.20') throw new Error('charge diagram did not update the distance');
    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await readout('#feedback')).includes('Верно')) throw new Error('electrostatics quiz rejected the correct answer');

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
    console.log(`PASS electrostatics lesson ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${required.length} sections, 3D WebGL lab ${labState.width}×${labState.height}, signed Coulomb control, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL electrostatics lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
    const response = await page.goto(`${base}/original-engine/electrostatics/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
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
    if (initial.title !== 'Электрический заряд' || initial.pages !== 9 || !initial.webgl) throw new Error(`book did not initialize correctly: ${JSON.stringify(initial)}`);
    if (initial.canvas[0] < 100 || initial.canvas[1] < 100) throw new Error(`WebGL canvas too small: ${initial.canvas.join('×')}`);
    if (initial.overflow) throw new Error('interactive book has horizontal overflow');
    await page.locator('#dots button').nth(8).evaluate(button => button.click());
    await page.waitForFunction(() => document.querySelector('#sheet h1')?.textContent?.trim() === 'Однородное электрическое поле', undefined, { timeout: 8000 });
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS electrostatics interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 9 pages, WebGL ${initial.canvas.join('×')}, page navigation to uniform field`);
  } catch (error) {
    failures.push(`book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL electrostatics book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('PASS electrostatics browser smoke: 4/4 desktop/mobile lesson and interactive-book runs');
