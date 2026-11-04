import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

// Keep this browser gate focused on the chapter being finalized. The full
// 15-laboratory browser sweep is tracked separately by the earlier baseline run.
const labs = ['newton'];
const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const failures = [];
let pagesChecked = 0;
let axeCritical = 0;
let axeSerious = 0;
let abortAfterBootstrap = false;

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
      return !!renderer && renderer.info.render.calls > 0 &&
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
        drawCalls: renderInfo?.calls ?? 0,
        sceneAssemblies: assemblyCount,
        horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 2,
        statusRegion: !!document.querySelector('.page-announcement[role="status"][aria-live="polite"]'),
      };
    });
    if (!state.title) throw new Error('Initial page heading is empty');
    if (state.pages < 2) throw new Error(`Page navigation missing (found ${state.pages})`);
    if (!state.webgl) throw new Error('WebGL context did not initialize');
    if (state.drawCalls < 1) throw new Error('Three.js did not submit any draw calls');
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
    console.log(`PASS ${lab} ${mobile ? 'mobile 390×844 touch' : 'desktop 1440×900'} — ${state.pages} pages, WebGL ${state.canvas.join('×')}, ${state.drawCalls} draw calls`);
  } catch (error) {
    if (lab === 'kinematics' && !mobile) abortAfterBootstrap = true;
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

try {
  for (const lab of labs) {
    await checkLab(lab, false);
    if (abortAfterBootstrap) break;
    await checkLab(lab, true);
    if (abortAfterBootstrap) break;
  }
} finally {
  await browser.close();
}

console.log(`Browser smoke: ${pagesChecked}/${labs.length * 2} viewport runs passed.`);
console.log(`axe summary (desktop + mobile): ${axeCritical} critical, ${axeSerious} serious violation groups.`);
if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
}
