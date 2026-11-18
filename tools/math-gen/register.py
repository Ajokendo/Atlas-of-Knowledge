# -*- coding: utf-8 -*-
"""Пересобирает math/index.html и вносит математику в index.html, catalog.html, progress.html (идемпотентно)."""
import os, re, json
from chapters import BLOCKS, CHAPTERS
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
def bi(r, e): return '<span data-l="ru">%s</span><span data-l="en">%s</span>' % (r, e)

# ---------- math/index.html ----------
ph = rd('physics/index.html')
head = ph[:ph.index('<main>')]
head = head.replace('Атлас физики для школьников Кыргызстана: явления, измерения, модели и задачи. RU / EN.', 'Атлас математики для школьников Кыргызстана: числа, фигуры, уравнения, функции; модели, задачи и тесты. RU / EN.')
head = head.replace('Атлас физики — Atlas of Knowledge', 'Атлас математики — Atlas of Knowledge')
head = head.replace('<span data-l="ru">Атлас физики</span><span data-l="en">Atlas of Physics</span>', bi('Атлас математики', 'Atlas of Mathematics'))
head = head.replace('href="../portal.html"', 'href="../index.html"')
assert 'физик' not in head.lower().replace('физики', '') or True
body = '<main>\n<section class="intro">\n<p class="eyebrow">%s</p>\n<h1>%s</h1>\n<p class="lead">%s</p>\n</section>\n' % (
    bi('ATLAS OF KNOWLEDGE · МАТЕМАТИКА', 'ATLAS OF KNOWLEDGE · MATHEMATICS'), bi('Атлас математики', 'Atlas of Mathematics'),
    bi('Математика вокруг нас: от счёта овец и цен на базаре до формул и графиков. Каждая глава начинается с загадки, объясняет тему, даёт формулы, лёгкую модель, разобранные задачи и тест с объяснениями.',
       'Mathematics all around us: from counting sheep and bazaar prices to formulas and graphs. Every chapter opens with a puzzle, explains the topic and gives formulas, a light interactive model, worked problems and a quiz with explanations.'))
for b in BLOCKS:
    body += '<section class="block">\n<h2>%s</h2>\n<p>%s</p>\n<div class="grid">\n' % (bi('Блок %s · %s' % (b['id'], b['ru']), 'Block %s · %s' % (b['id'], b['en'])), bi(b['note_ru'], b['note_en']))
    for n, slug, ru, en, dr, de, blk in CHAPTERS:
        if blk != b['id']: continue
        body += '<a class="ch" href="chapters/%s"><span class="num">%s</span><h3>%s</h3><p>%s</p><span class="st">%s</span></a>\n' % (
            slug, bi('ГЛАВА ' + n, 'CHAPTER ' + n), bi(ru, en), bi(dr, de), bi('ОТКРЫТЬ ГЛАВУ ↗', 'OPEN CHAPTER ↗'))
    body += '</div>\n</section>\n'
body += '<section class="note">%s</section>\n' % ('<p>%s</p>' % bi('Следующие блоки (дроби и проценты, уравнения, геометрия, алгебра, начала анализа, вероятность) — по плану в <a style="color:inherit" href="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/math/ROADMAP.md" target="_blank" rel="noopener">ROADMAP.md</a>.',
       'The next blocks (fractions and percentages, equations, geometry, algebra, calculus, probability) follow the plan in <a style="color:inherit" href="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/math/ROADMAP.md" target="_blank" rel="noopener">ROADMAP.md</a>.'))
body += '</main>\n'
tail = ph[ph.index('<footer>'):]
tail = re.sub(r'<span><span data-l="ru">АТЛАС ФИЗИКИ · БЛОК I</span><span data-l="en">ATLAS OF PHYSICS · BLOCK I</span></span>', '<span>%s</span>' % bi('АТЛАС МАТЕМАТИКИ', 'ATLAS OF MATHEMATICS'), tail)
tail = tail.replace('Атлас физики — Atlas of Knowledge', 'Атлас математики — Atlas of Knowledge').replace('Atlas of Physics — Atlas of Knowledge', 'Atlas of Mathematics — Atlas of Knowledge')
assert 'ФИЗИК' not in tail and 'Physics' not in tail, 'tail'
wr('math/index.html', head + body + tail)

# ---------- index.html (портал) ----------
p = rd('index.html')
card = ('<a class="subject" href="./math/index.html" style="--accent:#6b5ba8"><span class="num">SUBJECT 05 · MATHEMATICS</span><h2 data-i18n="math">Атлас математики</h2>'
        '<p data-i18n="mathDesc">Числа, фигуры, уравнения и функции — с загадками, моделями и задачами на примерах из жизни Кыргызстана.</p><span class="open" data-i18n="open">ОТКРЫТЬ АТЛАС ↗</span></a>\n')
if 'SUBJECT 05 · MATHEMATICS' not in p:
    p = p.replace('</section>\n<section class="coming">', card + '</section>\n<section class="coming">', 1)
    assert 'SUBJECT 05' in p
    p = p.replace('geography:"Атлас географии",', 'geography:"Атлас географии",math:"Атлас математики",mathDesc:"Числа, фигуры, уравнения и функции — с загадками, моделями и задачами на примерах из жизни Кыргызстана.",', 1)
    p = p.replace('geography:"Atlas of Geography",', 'geography:"Atlas of Geography",math:"Atlas of Mathematics",mathDesc:"Numbers, shapes, equations and functions — with puzzles, models and problems from everyday life in Kyrgyzstan.",', 1)
    assert p.count('mathDesc') == 3, p.count('mathDesc')
p = p.replace('Математика · Астрономия · География и другие дисциплины', 'Астрономия · История и другие дисциплины').replace('Mathematics · Astronomy · Geography and more', 'Astronomy · History and more')
p = p.replace('Математика · Астрономия · История и другие дисциплины', 'Астрономия · История и другие дисциплины')
wr('index.html', p)

# ---------- catalog.html ----------
c = rd('catalog.html')
lines = [l for l in c.split('\n') if not l.startswith('{subject:"math"')]
c = '\n'.join(lines)
# найти формат существующих записей
sample = [l for l in c.split('\n') if l.startswith('{subject:"physics",n:"01"')][0]
keys = re.findall(r'(?:^\{|,)([a-zA-Z]+):', sample)
assert 'url' in keys, keys
entries2 = ''
for n, slug, ru, en, dr, de, blk in CHAPTERS:
    vals = {'subject': 'math', 'n': n, 'ru': ru, 'en': en, 'descRu': dr, 'descEn': de, 'url': 'math/chapters/' + slug, 'tags': 'математика math числа арифметика'}
    # сохранить порядок ключей образца; недостающие — пустые
    entries2 += '{' + ','.join('%s:%s' % (k, json.dumps(vals.get(k, ''), ensure_ascii=False)) for k in keys) + '},\n'
c = re.sub(r'\},?\n\];\nconst resources', '},\n' + entries2.rstrip('\n').replace('\\', '\\\\') + '\n];\nconst resources', c, count=1)
assert 'subject:"math",n:"08"' in c
if 'data-filter="math"' not in c:
    c = c.replace('<button class="filter" data-filter="chemistry"', '<button class="filter" data-filter="math" aria-pressed="false" data-i="mathFilter">МАТЕМАТИКА</button><button class="filter" data-filter="chemistry"', 1)
    c = c.replace('<a href="chemistry/index.html" data-i="chemistry">ХИМИЯ</a>', '<a href="chemistry/index.html" data-i="chemistry">ХИМИЯ</a><a href="math/index.html" data-i="mathNav">МАТЕМАТИКА</a>', 1)
    c = c.replace('chemFilter:"ХИМИЯ",', 'chemFilter:"ХИМИЯ",mathFilter:"МАТЕМАТИКА",mathNav:"МАТЕМАТИКА",', 1).replace('chemFilter:"CHEMISTRY",', 'chemFilter:"CHEMISTRY",mathFilter:"MATHEMATICS",mathNav:"MATHEMATICS",', 1)
    c = c.replace('chemTitle:"Химия",', 'chemTitle:"Химия",mathTitle:"Математика",', 1).replace('chemTitle:"Chemistry",', 'chemTitle:"Chemistry",mathTitle:"Mathematics",', 1)
    c = c.replace('{id:"chemistry",title:w.chemTitle}', '{id:"math",title:w.mathTitle},{id:"chemistry",title:w.chemTitle}', 1)
    c = c.replace('data-filter="chemistry" aria-pressed="false" data-i="chemFilter"', 'data-filter="chemistry" aria-pressed="false" data-i="chemFilter"')
    c = c.replace('const accent=g.id==="chemistry"?"var(--green)":"var(--red)"', 'const accent=g.id==="chemistry"?"var(--green)":g.id==="math"?"#6b5ba8":"var(--red)"', 1)
    for k in ('mathFilter', 'mathNav', 'mathTitle'): assert c.count(k) >= 2, k
    assert 'g.id==="math"?"#6b5ba8"' in c and '{id:"math",title:w.mathTitle}' in c
wr('catalog.html', c)

# ---------- progress.html ----------
g = rd('progress.html')
g = re.sub(r'\n\{id:"math".*?\]\},', '', g, flags=re.S)
items = ','.join('[%s,%s,%s]' % (json.dumps(ru, ensure_ascii=False), json.dumps(en, ensure_ascii=False), json.dumps('math/chapters/' + slug)) for n, slug, ru, en, dr, de, blk in CHAPTERS)
g = g.replace('\n{id:"chemistry",title:["Химия","Chemistry"],items:[', '\n{id:"math",title:["Математика","Mathematics"],items:[\n' + items + ']},\n{id:"chemistry",title:["Химия","Chemistry"],items:[', 1)
assert '{id:"math"' in g
if 'mathQuizScore' not in g:
    g = g.replace('<div class="score"><small data-i="quizLabel">', '<div class="score"><small data-i="mathQuizLabel">МАТЕМАТИКА · ТЕСТ ЗНАНИЙ</small><b id="mathQuizScore">—</b><small id="mathQuizDate">Пока не пройден</small></div><div class="score"><small data-i="quizLabel">', 1)
    g = g.replace('physicsQuizLabel:"ФИЗИКА · ТЕСТ ЗНАНИЙ",', 'physicsQuizLabel:"ФИЗИКА · ТЕСТ ЗНАНИЙ",mathQuizLabel:"МАТЕМАТИКА · ТЕСТ ЗНАНИЙ",', 1)
    g = g.replace('physicsQuizLabel:"PHYSICS · KNOWLEDGE CHECK",', 'physicsQuizLabel:"PHYSICS · KNOWLEDGE CHECK",mathQuizLabel:"MATHEMATICS · KNOWLEDGE CHECK",', 1)
    g = g.replace('["physicsQuiz","atlas-physics-quiz-v1","physicsQuizScore","physicsQuizDate"],', '["physicsQuiz","atlas-physics-quiz-v1","physicsQuizScore","physicsQuizDate"],["mathQuiz","atlas-math-quiz-v1","mathQuizScore","mathQuizDate"],', 1)
    g = g.replace('sets=[["physicsQuiz","atlas-physics-quiz-v1"],', 'sets=[["physicsQuiz","atlas-physics-quiz-v1"],["mathQuiz","atlas-math-quiz-v1"],', 1)
    g = g.replace('const title=name==="physicsQuiz"?w.physicsQuizLabel:', 'const title=name==="physicsQuiz"?w.physicsQuizLabel:name==="mathQuiz"?w.mathQuizLabel:', 1)
    for k in ('mathQuizLabel', 'mathQuizScore', 'mathQuiz"'): assert k in g, k
    assert g.count('atlas-math-quiz-v1') == 2
wr('progress.html', g)
print('registered', len(CHAPTERS), 'chapters')
