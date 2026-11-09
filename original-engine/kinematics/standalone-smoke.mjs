import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import AxeBuilder from '@axe-core/playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const output = '/tmp/physics-visual-review/chapter1-standalone';
await mkdir(output, { recursive: true });
const failures = [];
const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

for (const mobile of [false, true]) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const runtimeErrors = [];
  page.on('pageerror', error => runtimeErrors.push(error.message));
  page.on('console', message => {
    if (message.type() === 'error' && !/fonts\\.googleapis|cdn\\.jsdelivr/i.test(message.text())) runtimeErrors.push(message.text());
  });

  try {
    const response = await page.goto(base + '/chapters/kinematics.html', { waitUntil: 'domcontentloaded', timeout: 25000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.locator('main h1').waitFor({ state: 'visible' });
    await page.locator('#klPlay').waitFor({ state: 'visible' });
    await page.locator('#feedback').waitFor({ state: 'attached' });
    await page.waitForFunction(() => ['klScene', 'klGraph', 'plot'].every(id => {
      const c = document.getElementById(id);
      return c && c.width > 0 && c.height > 0 && !!c.getContext('2d');
    }));

    const initial = await page.evaluate(() => ({
      title: document.querySelector('main h1')?.textContent?.trim(),
      canvases: [...document.querySelectorAll('main canvas')].map(c => [c.id, c.width, c.height]),
      iframeTitle: document.querySelector('main iframe')?.title || '',
      overflow: document.documentElement.scrollWidth > innerWidth + 2,
      initialSpeed: document.querySelector('#klVOut')?.textContent,
      initialRange: document.querySelector('#distance')?.textContent,
      signedVelocityDefinition: document.querySelector('main')?.innerText.includes('v — проекция скорости на ось x'),
    }));
    if (initial.title !== 'Кинематика') throw new Error('Standalone chapter title is missing');
    if (initial.canvases.length < 3 || initial.canvases.some(c => c[1] < 1 || c[2] < 1)) throw new Error('One or more standalone canvases did not initialise');
    if (!initial.iframeTitle.includes('Кинематика')) throw new Error('The embedded 3D laboratory iframe has no descriptive title');
    if (initial.overflow) throw new Error('Horizontal overflow on the standalone chapter page');
    if (!initial.initialSpeed || !initial.initialRange) throw new Error('Initial model readouts are missing');
    if (!initial.signedVelocityDefinition) throw new Error('Uniform-motion text does not identify v as the signed x-axis velocity projection');

    // Projectile model: change all physical parameters and verify derived values.
    const setRange = async (id, value) => page.locator('#' + id).evaluate((el, v) => {
      el.value = String(v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }, value);
    await setRange('klV', 20);
    await setRange('klA', 60);
    await setRange('klG', 10);
    await setRange('klT', 0.5);
    const projectile = await page.evaluate(() => ({
      speed: document.querySelector('#klVOut').textContent,
      angle: document.querySelector('#klAOut').textContent,
      gravity: document.querySelector('#klGOut').textContent,
      time: Number(document.querySelector('#klT').value),
      height: Number(document.querySelector('#klY').textContent.replace(',', '.').replace(' м', '')),
      range: Number(document.querySelector('#klX').textContent.replace(',', '.').replace(' м', '')),
      expectedHeight: 20 * Math.sin(Math.PI / 3) * 0.5 - 0.5 * 10 * 0.25,
      expectedRange: 20 * Math.cos(Math.PI / 3) * 0.5,
    }));
    if (!projectile.speed.includes('20,0') || !projectile.angle.includes('60') || !projectile.gravity.includes('10,00')) throw new Error('Projectile controls did not update their readouts');
    if (Math.abs(projectile.height - projectile.expectedHeight) > 0.02 || Math.abs(projectile.range - projectile.expectedRange) > 0.02) throw new Error('Projectile model outputs do not match the equations');

    await page.locator('#klPlay').click();
    await page.waitForFunction(() => Number(document.querySelector('#klT').value) > 0.55, undefined, { timeout: 5000 });
    await page.locator('#klPause').click();
    const pausedAt = Number(await page.locator('#klT').inputValue());
    await page.waitForTimeout(120);
    const stillAt = Number(await page.locator('#klT').inputValue());
    if (Math.abs(stillAt - pausedAt) > 0.002) throw new Error('Pause control did not stop the projectile animation');
    await page.locator('#klReset').click();
    if (Number(await page.locator('#klT').inputValue()) !== 0) throw new Error('Reset control did not return the projectile to t = 0');

    // Uniform-motion model and graph.
    await setRange('v', 7);
    await setRange('t', 3);
    const uniform = await page.evaluate(() => ({
      distance: document.querySelector('#distance').textContent,
      position: document.querySelector('#position').textContent,
      speed: document.querySelector('#speed').textContent,
    }));
    if (!uniform.distance.includes('21') || !uniform.position.includes('21') || !uniform.speed.includes('7')) {
      throw new Error('Uniform-motion controls did not recalculate s = vt');
    }

    // The standalone knowledge-check must provide both negative and positive feedback.
    await page.locator('.answers button[data-answer="a"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Не совсем') ||
        await page.locator('.answers button[data-answer="a"]').getAttribute('data-result') !== 'incorrect') {
      throw new Error('Standalone quiz did not mark an incorrect answer');
    }
    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно') ||
        await page.locator('.answers button[data-answer="b"]').getAttribute('data-result') !== 'correct') {
      throw new Error('Standalone quiz did not mark the correct answer');
    }

    const axe = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
    const serious = axe.violations.filter(v => v.impact === 'serious' || v.impact === 'critical');
    if (serious.length) throw new Error('axe found serious/critical violations: ' + serious.map(v => v.id).join(', '));

    await page.screenshot({
      path: `${output}/kinematics-standalone-${mobile ? 'mobile' : 'desktop'}.png`,
      fullPage: true,
      animations: 'disabled',
      timeout: 60000,
    });
    if (runtimeErrors.length) throw new Error('Runtime errors: ' + runtimeErrors.join(' | '));
    console.log(`PASS standalone Kinematics ${mobile ? 'mobile' : 'desktop'}: projectile controls, play/pause/reset, uniform-motion graph, quiz, canvas, responsive layout, axe serious/critical 0`);
  } catch (error) {
    failures.push(`Kinematics standalone ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error('FAIL', failures[failures.length - 1]);
  }
  await context.close();
}

await browser.close();
if (failures.length) process.exit(1);
console.log('PASS Chapter 1 standalone desktop/mobile smoke');
