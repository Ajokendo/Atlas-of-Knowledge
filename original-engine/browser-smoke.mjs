import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

// Chapter 1 (kinematics) is the current browser-validation target.
// The complete 15-laboratory browser sweep remains a separate future gate.
const labs = ['kinematics'];
const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
let pagesChecked = 0;
let axeCritical = 0;
let axeSerious = 0;
let abortAfterDesktopBootstrap = false;

const browser = await chromium.launch({
  headless: true,
  args: ['--enable-webgl', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-gl=angle', '--use-angle=swiftshader'],
});

async function checkLab(lab, mobile) {
  const context = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(10000);
  const runtimeErrors = [];
  page.on('response', response => {
    if (response.status() >= 400) runtimeErrors.push(`HTTP ${response.status()} ${response.url()}`);
  });
  page.on('pageerror', error => runtimeErrors.push(error.message));
  page.on('console', message => {
    if (message.type() === 'error') runtimeErrors.push(message.text());
  });
  try {
    const response = await page.goto(`${base}/original-engine/${lab}/`, {
      waitUntil: 'domcontentloaded',
      timeout: 15000,
    });
    if (!response || !response.ok()) throw new Error(`HTTP response ${response?.status() ?? 'missing'}`);
    await page.waitForSelector('#sheet h1', { timeout: 10000 });
    await page.waitForFunction(() => {
      const canvas = document.querySelector('#gl');
      return canvas && canvas.width > 0 && canvas.height > 0 &&
        document.querySelector('.page-announcement') &&
        document.querySelectorAll('#dots button').length > 0;
    }, undefined, { timeout: 10000 });

    await page.waitForFunction(() => {
      const atlas = window.__atlas;
      const renderer = atlas?.E?.renderer;
      return !!renderer && renderer.info.render.frame > 0 &&
        Object.keys(atlas.E.ASM || {}).length > 0;
    }, undefined, { timeout: 15000 });

    const state = await page.evaluate(() => {
      const canvas = document.querySelector('#gl');
      const atlas = window.__atlas;
      const renderInfo = atlas?.E?.renderer?.info?.render;
      const assemblyCount = Object.keys(atlas?.E?.ASM || {}).length;
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return {
        title: document.querySelector('#sheet h1')?.textContent?.trim(),
        pages: document.querySelectorAll('#dots button').length,
        canvas: [canvas.width, canvas.height],
        webgl: !!gl,
        renderedFrames: renderInfo?.frame ?? 0,
        sceneAssemblies: assemblyCount,
        horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 2,
        statusRegion: !!document.querySelector('.page-announcement[role="status"][aria-live="polite"]'),
      };
    });
    if (!state.title) throw new Error('Initial page heading is empty');
    if (state.pages < 2) throw new Error(`Page navigation missing (found ${state.pages})`);
    if (!state.webgl) throw new Error('WebGL context did not initialize');
    if (state.renderedFrames < 1) throw new Error('Three.js did not render a frame');
    if (state.sceneAssemblies < 1) throw new Error('Three.js scene contains no registered assemblies');
    if (state.horizontalOverflow) throw new Error('Horizontal page overflow at this viewport');
    if (!state.statusRegion) throw new Error('Accessible page status region is missing');

    const axe = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
    const critical = axe.violations.filter(v => v.impact === 'critical');
    const serious = axe.violations.filter(v => v.impact === 'serious');
    axeCritical += critical.length;
    axeSerious += serious.length;
    for (const v of [...critical, ...serious]) {
      console.log(`AXE ${v.impact} ${lab} ${mobile ? 'mobile' : 'desktop'}: ${v.id} — ${v.help} (${v.nodes.length} nodes)`);
      for (const node of v.nodes) console.log(`AXE NODE ${lab} ${mobile ? 'mobile' : 'desktop'}: ${JSON.stringify({ target: node.target, html: node.html, summary: node.failureSummary })}`);
    }
    if (critical.length || serious.length) throw new Error(`axe found ${critical.length} critical and ${serious.length} serious accessibility violation group(s)`);

    const before = state.title;
    if (mobile) {
      const next = page.locator('#sheet button[data-turn]').first();
      if (!(await next.count())) throw new Error('Mobile next-page button is missing');
      await next.click();
    } else {
      const secondDot = page.locator('#dots button').nth(1);
      if (!(await secondDot.count())) throw new Error('Desktop page-navigation control is missing');
      await secondDot.click();
    }
    await page.waitForFunction(oldTitle =>
      document.querySelector('#sheet h1')?.textContent?.trim() !== oldTitle, before, { timeout: 15000 });

    if (!mobile) {
      await page.locator('#dots button').nth(0).click();
      await page.waitForFunction(() => location.hash === '' || location.hash === '#0', null, { timeout: 10000 });
      await page.evaluate(() => document.activeElement?.blur());
      await page.keyboard.press('ArrowRight');
      await page.waitForFunction(oldTitle =>
        document.querySelector('#sheet h1')?.textContent?.trim() !== oldTitle, before, { timeout: 15000 });
      await page.keyboard.press('ArrowLeft');
      await page.waitForFunction(oldTitle =>
        document.querySelector('#sheet h1')?.textContent?.trim() === oldTitle, before, { timeout: 15000 });
    }
    pagesChecked++;
    console.log(`PASS ${lab} ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — ${state.pages} pages, WebGL ${state.canvas.join('×')}, ${state.renderedFrames} renderer frames`);
  } catch (error) {
    if (lab === 'kinematics' && !mobile) abortAfterDesktopBootstrap = true;
    failures.push(`${lab} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
    console.error(`FAIL ${lab} ${mobile ? 'mobile' : 'desktop'}: ${error.message}`);
  } finally {
    if (runtimeErrors.length) {
      failures.push(`${lab} ${mobile ? 'mobile' : 'desktop'} console/runtime errors: ${runtimeErrors.join(' | ')}`);
      console.error(`RUNTIME ${lab} ${mobile ? 'mobile' : 'desktop'}: ${runtimeErrors.join(' | ')}`);
    }
    await context.close();
  }
}

async function checkChapterPage() {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    reducedMotion: 'reduce',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(10000);
  const runtimeErrors = [];
  page.on('response', response => {
    if (response.status() >= 400) runtimeErrors.push(`HTTP ${response.status()} ${response.url()}`);
  });
  page.on('pageerror', error => runtimeErrors.push(error.message));
  page.on('console', message => {
    if (message.type() === 'error') runtimeErrors.push(message.text());
  });
  try {
    const response = await page.goto(`${base}/chapters/kinematics.html`, {
      waitUntil: 'domcontentloaded',
      timeout: 15000,
    });
    if (!response || !response.ok()) throw new Error(`Chapter page HTTP response ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Кинематика', exact: true }).waitFor();
    await page.waitForFunction(() => {
      const frame = document.querySelector('.kinematics-lab-frame iframe');
      const doc = frame?.contentDocument;
      const atlas = doc?.defaultView?.__atlas;
      return !!doc?.querySelector('#sheet h1') &&
        !!atlas?.E?.renderer &&
        atlas.E.renderer.info.render.frame > 0 &&
        !!doc.querySelector('#gl')?.getContext('webgl2');
    }, undefined, { timeout: 25000 });

    const headings = await page.locator('main h2').allTextContents();
    const required = [
      '1.1. Положение, путь и перемещение',
      '1.2. Скорость и быстрота',
      '1.3. Ускорение',
      '1.4. Графики движения',
      '1.5. Кинематические уравнения',
      '1.6. Движение тела, брошенного под углом',
      '1.7. Системы отсчёта и относительная скорость',
      '1.8. Переправа через реку',
      '1.9. Кинематика с помощью математического анализа: переменное ускорение',
      '1.10. Движение, заданное функцией x(t)',
    ];
    const missing = required.filter(title => !headings.includes(title));
    if (missing.length) throw new Error(`Chapter sections missing or out of order: ${missing.join('; ')}`);
    const sectionPositions = required.map(title => headings.indexOf(title));
    if (sectionPositions.some((position, i) => position < 0 || (i > 0 && position <= sectionPositions[i - 1]))) {
      throw new Error('Chapter 1 section order does not match the expected sequence');
    }

    await page.locator('#v').evaluate(el => {
      el.value = '10';
      el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    await page.locator('#t').evaluate(el => {
      el.value = '4';
      el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    if (!(await page.locator('#distance').innerText()).includes('40')) {
      throw new Error('Uniform-motion slider did not update distance to 40 m');
    }

    await page.locator('#klV').evaluate(el => {
      el.value = '20';
      el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    if (!(await page.locator('#klVOut').innerText()).includes('20')) {
      throw new Error('Projectile-motion speed slider did not update its readout');
    }

    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно')) {
      throw new Error('Chapter knowledge-check did not accept the correct answer');
    }

    const axe = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
    const critical = axe.violations.filter(v => v.impact === 'critical');
    const serious = axe.violations.filter(v => v.impact === 'serious');
    axeCritical += critical.length;
    axeSerious += serious.length;
    for (const violation of [...critical, ...serious]) {
      console.error(`AXE chapter page ${violation.impact}: ${violation.id} — ${violation.help} (${violation.nodes.length} nodes)`);
      for (const node of violation.nodes) {
        console.error(`AXE NODE chapter page: ${JSON.stringify({ target: node.target, html: node.html, summary: node.failureSummary })}`);
      }
    }
    if (critical.length || serious.length) {
      throw new Error(`chapter page axe found ${critical.length} critical and ${serious.length} serious violation group(s)`);
    }
    if (runtimeErrors.length) throw new Error(`Chapter page console/runtime errors: ${runtimeErrors.join(' | ')}`);
    console.log(`PASS chapter page — ${required.length} ordered sections, embedded Three.js/WebGL 2 frame, motion sliders, projectile slider, quiz; ${headings.length} headings`);
  } catch (error) {
    failures.push(`chapter page: ${error.message}`);
    console.error(`FAIL chapter page: ${error.message}`);
    if (runtimeErrors.length) {
      failures.push(`chapter page console/runtime errors: ${runtimeErrors.join(' | ')}`);
      console.error(`RUNTIME chapter page: ${runtimeErrors.join(' | ')}`);
    }
  } finally {
    await context.close();
  }
}

async function checkCircularChapterPage() {
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: 'reduce' });
  const page = await context.newPage();
  page.setDefaultTimeout(10000);
  const errors = [];
  page.on('response', response => { if (response.status() >= 400) errors.push(`HTTP ${response.status()} ${response.url()}`); });
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  try {
    const response = await page.goto(`${base}/chapters/circular-motion.html`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (!response || !response.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    await page.getByRole('heading', { name: 'Движение по окружности', exact: true }).waitFor();
    const bookFrame = page.frameLocator('iframe[title="Интерактивная лаборатория: движение по окружности, силы и орбиты"]');
    await bookFrame.locator('#gl').waitFor({ state: 'visible' });
    const bookWebGL = await bookFrame.locator('#gl').evaluate(canvas => {
      const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
      return { width: canvas.width, height: canvas.height, context: !!gl };
    });
    if (!bookWebGL.context || bookWebGL.width < 100 || bookWebGL.height < 100) throw new Error('Original circular-motion Three.js scene did not initialize a drawable WebGL canvas');
    const required = ['1. Линейная и угловая скорость','Угловые величины и радианная мера','Связь периода, частоты и скорости','2. Центростремительное ускорение','Направление скорости и ускорения','Неравномерное движение по окружности','3. Сила, обеспечивающая поворот','Применение: повороты, вращение и орбиты'];
    const headings = await page.locator('main h2').allTextContents();
    const missing = required.filter(h => !headings.includes(h));
    if (missing.length) throw new Error(`Missing lesson sections: ${missing.join('; ')}`);
    await page.locator('#p0').evaluate(el => { el.value = '12'; el.dispatchEvent(new Event('input', { bubbles: true })); });
    if (!(await page.locator('#o0').innerText()).includes('12')) throw new Error('Speed control did not update its readout');
    if (!(await page.locator('#r0').innerText()).includes('7,20')) throw new Error('Centripetal acceleration did not recalculate for v=12 m/s and r=20 m');
    await page.locator('.answers button[data-answer="b"]').click();
    if (!(await page.locator('#feedback').innerText()).includes('Верно')) throw new Error('Circular-motion quiz rejected the correct answer');
    const axe = await new AxeBuilder({ page }).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
    const serious = axe.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
    if (serious.length) throw new Error(`axe found ${serious.length} serious/critical violation groups: ${serious.map(v=>v.id).join(', ')}`);
    if (errors.length) throw new Error(errors.join(' | '));
    console.log(`PASS circular-motion chapter — original Three.js/WebGL book ${bookWebGL.width}×${bookWebGL.height}, ${required.length} sections, live calculation controls, quiz, WCAG serious/critical: 0`);
  } catch (error) {
    failures.push(`circular-motion chapter: ${error.message}`);
    console.error(`FAIL circular-motion chapter: ${error.message}`);
    if (errors.length) failures.push(`circular-motion page errors: ${errors.join(' | ')}`);
  } finally { await context.close(); }
}

try {
  for (const lab of labs) {
    await checkLab(lab, false);
    if (abortAfterDesktopBootstrap) break;
    await checkLab(lab, true);
    if (abortAfterDesktopBootstrap) break;
  }
  await checkChapterPage();
  await checkCircularChapterPage();
} finally {
  await browser.close();
}

console.log(`Browser smoke: ${pagesChecked}/${labs.length * 2} lab viewport runs passed, plus chapter page integration.`);
console.log(`axe summary (desktop + mobile): ${axeCritical} critical, ${axeSerious} serious violation groups.`);
if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
}
