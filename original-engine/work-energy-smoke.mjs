import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

async function check(viewport, mobile) {
  const context = await browser.newContext({
    viewport,
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('response', response => {
    if (response.status() >= 400) errors.push(`HTTP ${response.status()} ${response.url()}`);
  });
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => {
    if (message.type() === 'error') errors.push(message.text());
  });

  try {
    const response = await page.goto(`${base}/chapters/work-energy.html`, {
      waitUntil: 'domcontentloaded',
      timeout: 20000,
    });
    if (!response || !response.ok()) throw new Error(`Chapter page HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Работа и энергия', exact: true }).waitFor();

    const sectionHeadings = await page.locator('main.lesson > section h2').allTextContents();
    const required = [
      'Введение',
      '1. Механическая работа',
      '2. Теорема о кинетической энергии',
      '3. Кинетическая и потенциальная энергия',
      '4. Закон сохранения механической энергии',
      '5. Мощность',
      'Интерактивная модель: Кинетическая энергия тела',
      '6. Коэффициент полезного действия',
      'Проверьте себя',
    ];
    const missing = required.filter(title => !sectionHeadings.includes(title));
    if (missing.length) throw new Error(`Missing lesson sections: ${missing.join('; ')}`);

    const controls = page.locator('#p0, #p1, #p2');
    if (await controls.count() !== 3) throw new Error('Expected three energy-model sliders');
    await page.locator('#p0').evaluate(el => { el.value = '4'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.locator('#p1').evaluate(el => { el.value = '20'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    await page.locator('#p2').evaluate(el => { el.value = '10'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    const readouts = await Promise.all(['#o0', '#o1', '#o2', '#r0', '#r1', '#r2'].map(sel => page.locator(sel).innerText()));
    if (!readouts[0].includes('4') || !readouts[1].includes('20') || !readouts[2].includes('10')) {
      throw new Error(`Slider readouts did not update: ${readouts.slice(0, 3).join(' / ')}`);
    }
    if (!readouts[3].includes('800') || !readouts[4].includes('392') || !readouts[5].includes('1192')) {
      throw new Error(`Energy calculation mismatch for m=4 kg, v=20 m/s, h=10 m: ${readouts.slice(3).join(' / ')}`);
    }

    const chart = await page.locator('#visual').evaluate(canvas => ({
      width: canvas.width, height: canvas.height,
      hasContext: !!canvas.getContext('2d'),
    }));
    if (chart.width < 100 || chart.height < 80 || !chart.hasContext) {
      throw new Error('Energy comparison chart did not initialize');
    }

    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно')) {
      throw new Error('Chapter knowledge-check did not accept the correct answer');
    }

    const labCanvas = page.locator('[data-physics-lab] .physics-stage canvas');
    await labCanvas.waitFor({ state: 'visible' });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('[data-physics-lab] .physics-stage canvas');
      return !!canvas && canvas.width > 0 && canvas.height > 0 &&
        !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
    }, undefined, { timeout: 20000 });
    const lab = await labCanvas.evaluate(canvas => ({
      width: canvas.width, height: canvas.height,
      webgl: !!(canvas.getContext('webgl2') || canvas.getContext('webgl')),
      accessibleName: canvas.getAttribute('aria-label'),
    }));
    if (lab.width < 100 || lab.height < 100 || !lab.webgl || !lab.accessibleName) {
      throw new Error('3D energy lab canvas is not drawable or lacks an accessible description');
    }

    const axe = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) {
      const details = serious.map(v => ({
        id: v.id,
        impact: v.impact,
        nodes: v.nodes.slice(0, 12).map(n => ({
          target: n.target,
          summary: n.failureSummary,
          html: n.html,
          checks: [...(n.any || []), ...(n.all || []), ...(n.none || [])].map(c => ({
            message: c.message,
            data: c.data,
          })),
        })),
      }));
      throw new Error(`axe found serious/critical violations: ${JSON.stringify(details)}`);
    }
    const hasOverflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    if (hasOverflow) throw new Error('Horizontal page overflow');
    if (errors.length) throw new Error(errors.join(' | '));

    console.log(`PASS work-energy ${mobile ? 'mobile 390×844' : 'desktop 1440×900'} — 9 sections, live energy calculations, canvas chart, quiz, WebGL lab ${lab.width}×${lab.height}, serious/critical axe violations: 0`);
  } catch (error) {
    failures.push(`work-energy ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL work-energy ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    if (errors.length) failures.push(`runtime/console errors: ${errors.join(' | ')}`);
  } finally {
    await context.close();
  }
}

try {
  await check({ width: 1440, height: 900 }, false);
  await check({ width: 390, height: 844 }, true);
} finally {
  await browser.close();
}
if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
}
