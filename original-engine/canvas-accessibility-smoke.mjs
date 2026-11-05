import { chromium } from 'playwright';

const base = process.env.BASE_URL || 'http://127.0.0.1:4173';
const pages = [
  'kinematics.html', 'newton-laws.html', 'circular-motion.html', 'work-energy.html',
  'momentum.html', 'oscillations.html', 'rotation.html', 'fluids.html',
  'electrostatics.html', 'gauss-law.html', 'electric-potential.html',
  'capacitors.html', 'circuits.html', 'magnetism.html', 'induction.html',
];
const generic = /трёхмерная интерактивная модель физического явления|график изменения физической величины во времени|схематическая визуализация физических величин|интерактивная трёхмерная модель|параметр физической модели|расчёт по формулам физики/i;
const failures = [];
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
page.setDefaultTimeout(12000);

for (const file of pages) {
  try {
    const response = await page.goto(`${base}/chapters/${file}`, { waitUntil: 'domcontentloaded', timeout: 20000 });
    if (!response?.ok()) throw new Error(`HTTP ${response?.status() ?? 'missing'}`);
    const result = await page.evaluate(() => ({
      canvases: [...document.querySelectorAll('canvas')].map(c => c.getAttribute('aria-label')?.trim() || ''),
      labs: [...document.querySelectorAll('section[data-physics-lab]')].map(el => el.getAttribute('aria-label')?.trim() || ''),
      phases: [...document.querySelectorAll('[data-phase-name]')].map(el => el.textContent?.trim() || ''),
      formulas: [...document.querySelectorAll('[data-physics-formula]')].map(el => el.textContent?.trim() || ''),
    }));
    if (!result.canvases.length) throw new Error('no canvas visual found');
    const bad = [
      ...result.canvases.filter(label => !label || label.length < 25 || generic.test(label)),
      ...result.labs.filter(label => !label || label.length < 25 || generic.test(label)),
      ...result.phases.filter(label => !label || label.length < 6 || generic.test(label)),
      ...result.formulas.filter(label => !label || label.length < 5 || generic.test(label)),
    ];
    if (bad.length) throw new Error(`generic or missing accessible labels: ${bad.join(' | ')}`);
    console.log(`PASS ${file} — ${result.canvases.length} canvas labels, ${result.labs.length} lab labels, contextual phase/formula text`);
  } catch (error) {
    failures.push(`${file}: ${error.message}`);
    console.error('FAIL', failures[failures.length - 1]);
  }
}
await browser.close();
if (failures.length) process.exit(1);
console.log('PASS canvas accessibility labels: 15/15 chapter pages');
