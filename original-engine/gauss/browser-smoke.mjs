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
    const response = await page.goto(`${base}/chapters/gauss-law.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`chapter HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Закон Гаусса', exact: true }).first().waitFor();

    const required = [
      'Исследуйте явление в пространстве',
      'Введение',
      '1. Электрический поток',
      '2. Закон Гаусса',
      '3. Симметрия и применение',
      'Интерактивная модель: Поток электрического поля',
      'Проверьте себя',
    ];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`missing lesson sections: ${missing.join('; ')}`);
    const lessonText = await page.locator('main').innerText();
    if (!lessonText.includes('Гауссова поверхность — воображаемая замкнутая поверхность')) throw new Error('Gaussian surface is not clearly defined');
    if (!lessonText.includes('Для длинной равномерно заряженной нити')) throw new Error('cylindrical symmetry example is missing');
    if (!lessonText.includes('для большого равномерно заряженного листа')) throw new Error('planar symmetry example is missing');
    if (!lessonText.includes('НАПРЯЖЁННОСТЬ ПОЛЯ НА СФЕРЕ E = Φ/A')) throw new Error('spherical-symmetry field value is not identified clearly');

    const labCanvas = page.locator('.physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    const labState = await labCanvas.evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, webgl: !!gl, label: canvas.getAttribute('aria-label') };
    });
    if (!labState.webgl || labState.width < 100 || labState.height < 100) {
      throw new Error(`3D Gauss-law lab WebGL canvas did not initialize: ${JSON.stringify(labState)}`);
    }

    const readout = async id => (await page.locator(id).innerText()).replace(/\s+/g, ' ').trim();
    if (!(await readout('#r0')).includes('112,94 Н·м²/Кл')) throw new Error(`default closed-surface flux incorrect: ${await readout('#r0')}`);
    if (!(await readout('#r1')).includes('225,88 Н/Кл')) throw new Error(`default average field incorrect: ${await readout('#r1')}`);
    if (!(await readout('#r2')).includes('112,94 Н·м²/Кл')) throw new Error(`default oriented flux incorrect: ${await readout('#r2')}`);

    await page.locator('#p1').evaluate(el => { el.value = '1'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('112,94 Н·м²/Кл') || !(await readout('#r1')).includes('112,94 Н/Кл')) throw new Error('changing spherical area should preserve total flux and update the exact field on the sphere');
    await page.locator('#p2').evaluate(el => { el.value = '90'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r2')).includes('0,00 Н·м²/Кл')) throw new Error(`flux at 90° should be zero: ${await readout('#r2')}`);
    await page.locator('#p2').evaluate(el => { el.value = '180'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r2')).includes('-112,94 Н·м²/Кл')) throw new Error(`flux at 180° should be negative: ${await readout('#r2')}`);
    await page.locator('#p0').evaluate(el => { el.value = '2'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await readout('#r0')).includes('225,88 Н·м²/Кл')) throw new Error(`doubling enclosed charge should double total flux: ${await readout('#r0')}`);
    await page.locator('.answers button[data-answer="a"]').click();
    if (!(await readout('#feedback')).includes('Верно')) throw new Error('Gauss-law quiz rejected the correct answer');

    // Bring the lab into the viewport so its IntersectionObserver permits animation.
    await page.locator('[data-physics-lab]').scrollIntoViewIfNeeded();
    await page.waitForTimeout(150);
    const play = page.locator('.physics-lab-controls button');
    if ((await play.innerText()).trim() !== 'Продолжить') throw new Error('reduced-motion mode should begin with the 3D lab paused');
    // Keep the reduced-motion assertion, then switch to the normal preference to test both controls.
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    await page.waitForFunction(() => document.querySelector('.physics-lab-controls button')?.textContent?.trim() === 'Пауза');
    await play.click();
    if ((await play.innerText()).trim() !== 'Продолжить') throw new Error('3D lab pause control did not stop animation');
    await play.click();
    if ((await play.innerText()).trim() !== 'Пауза') throw new Error('3D lab play control did not resume animation');

    const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe found ${serious.length} serious/critical violation groups: ${serious.map(v => `${v.id} [${v.nodes.map(n => `${n.target.join(' ')}: ${n.failureSummary?.replace(/\\s+/g, ' ').slice(0, 240)}`).join('; ')}]`).join(' | ')}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (overflow) throw new Error('horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS Gauss-law lesson ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — ${required.length} sections, 3D WebGL, flux/angle/charge controls, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL Gauss-law lesson ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
    const response = await page.goto(`${base}/original-engine/gauss/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`book HTTP ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1', { timeout: 12000 });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 0 && canvas.height > 0 &&
        document.querySelectorAll('#dots button').length === 9 &&
        !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
    }, undefined, { timeout: 20000 });

    const guide = page.locator('#scene-guide');
    const sceneTopics = [
      'Поток электрического поля', 'Закон Гаусса для точечного заряда',
      'Бесконечная заряженная нить', 'Заряженный лист и металлическая пластина',
      'Проводящая сфера', 'Равномерно заряженная диэлектрическая сфера',
      'Заряженные стержни', 'Неравномерно заряженная изолирующая сфера',
      'Полая проводящая оболочка',
    ];
    await guide.locator('summary').click();
    const guideText = await guide.innerText();
    const missingTopics = sceneTopics.filter(topic => !guideText.includes(topic));
    if (missingTopics.length) throw new Error(`accessible scene guide is missing: ${missingTopics.join('; ')}`);
    if (await guide.locator('li').count() !== 9) throw new Error('accessible scene guide must describe all nine scenes');
    if (await page.locator('#gl').getAttribute('aria-describedby') !== 'scene-guide') {
      throw new Error('3D canvas is not programmatically associated with its text guide');
    }
    const guideLayout = await guide.evaluate(el => {
      const r = el.getBoundingClientRect();
      return { position: getComputedStyle(el).position, width: r.width, height: r.height };
    });
    if (guideLayout.position !== 'absolute' || guideLayout.width < 100 || guideLayout.height < 20) {
      throw new Error(`accessible scene guide is not visibly positioned over the 3D scene: ${JSON.stringify(guideLayout)}`);
    }

    const picker = page.locator('.scene-picker');
    await picker.waitFor({ state: 'visible' });
    if (await picker.locator('option').count() < 2) throw new Error('keyboard scene picker has no selectable objects');
    await picker.focus();
    await picker.press('ArrowDown');
    await picker.press('Enter');
    await page.waitForFunction(() => {
      const plate = document.querySelector('#plate');
      return plate && !plate.hidden && !!plate.querySelector('#scene-plate-title');
    });
    await page.waitForFunction(() => document.activeElement?.id === 'scene-plate-title', undefined, { timeout: 8000 }).catch(async () => {
      const active = await page.evaluate(() => ({ tag: document.activeElement?.tagName, id: document.activeElement?.id, className: document.activeElement?.className, text: document.activeElement?.textContent?.trim().slice(0, 80) }));
      throw new Error(`keyboard scene selection did not move focus to the text explanation; active element: ${JSON.stringify(active)}`);
    });
    await picker.selectOption('');
    if (!(await page.locator('#plate').evaluate(el => el.hidden))) throw new Error('empty picker option did not close the scene explanation');

    const announce = page.locator('.readout-announce');
    await announce.focus();
    await announce.press('Enter');
    await page.waitForFunction(() => document.querySelector('#readout-announcement')?.textContent?.includes('Текущие значения'));
    if (!(await page.locator('#readout-announcement').innerText()).includes('Текущие значения')) {
      throw new Error('current model values were not announced on demand');
    }
    const initial = await page.evaluate(() => ({
      title: document.querySelector('#sheet h1')?.textContent?.trim(),
      pages: document.querySelectorAll('#dots button').length,
      canvas: [document.querySelector('#gl').width, document.querySelector('#gl').height],
      webgl: !!(document.querySelector('#gl').getContext('webgl2') || document.querySelector('#gl').getContext('webgl')),
      overflow: document.documentElement.scrollWidth > innerWidth + 2,
    }));
    if (initial.title !== 'Поток электрического поля' || initial.pages !== 9 || !initial.webgl) {
      throw new Error(`book did not initialize correctly: ${JSON.stringify(initial)}`);
    }
    if (initial.canvas[0] < 100 || initial.canvas[1] < 100) throw new Error(`WebGL canvas too small: ${initial.canvas.join('×')}`);
    if (initial.overflow) throw new Error('interactive book has horizontal overflow');
    const pageTitles = [
      'Поток электрического поля', 'Закон Гаусса', 'Заряженная нить',
      'Заряженные листы и пластины', 'Металлическая сфера', 'Диэлектрическая сфера',
      'Заряженные стержни', 'Неравномерное распределение заряда', 'Проводники',
    ];
    for (let i = 0; i < pageTitles.length; i++) {
      await page.locator('#dots button').nth(i).evaluate(button => button.click());
      await page.waitForFunction(title => document.querySelector('#sheet h1')?.textContent?.trim() === title, pageTitles[i], { timeout: 15000 }).catch(async error => { const actual = await page.locator('#sheet h1').textContent().catch(() => '(missing)'); throw new Error(`page ${i + 1} expected '${pageTitles[i]}', got '${actual?.trim()}' — ${error.message}`); });
    }
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS Gauss-law interactive book ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — 9 pages, WebGL ${initial.canvas.join('×')}, navigation to conductors`);
  } catch (error) {
    failures.push(`book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL Gauss-law book ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
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
console.log('PASS Gauss-law browser smoke: 4/4 desktop/mobile lesson and interactive-book runs');
