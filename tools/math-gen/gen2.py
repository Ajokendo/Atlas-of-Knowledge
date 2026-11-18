# -*- coding: utf-8 -*-
"""Компактный слой над gen.py: глава описывается данными, модели — функциями JS."""
import json
from gen import *
from h5 import LINK, qz, stdhint, stdnote
from MJS import MJS
from MJS2 import MJS2
import chapters as REG

def _t(x): return x if isinstance(x, tuple) else (x, x)
def paras(s): return ''.join('<p>%s</p>' % p for p in s.strip().split('\n\n'))

BLK = {
 'I':   (('ОСНОВЫ · 1–4 КЛАССЫ', 'BASICS · GRADES 1–4'), None),
 'II':  (('ОСНОВЫ · 1–6 КЛАССЫ', 'BASICS · GRADES 1–6'), ('prealgebra-2e', 'Prealgebra 2e')),
 'III': (('ОСНОВЫ · 5–6 КЛАССЫ', 'BASICS · GRADES 5–6'), ('prealgebra-2e', 'Prealgebra 2e')),
 'IV':  (('ОСНОВЫ · 6–7 КЛАССЫ', 'BASICS · GRADES 6–7'), ('elementary-algebra-2e', 'Elementary Algebra 2e')),
 'V':   (('ОСНОВЫ / УГЛУБЛЁННО · 7–9 КЛАССЫ', 'BASICS / ADVANCED · GRADES 7–9'), None),
 'VI':  (('ОСНОВЫ / УГЛУБЛЁННО · 8–10 КЛАССЫ', 'BASICS / ADVANCED · GRADES 8–10'), ('intermediate-algebra-2e', 'Intermediate Algebra 2e')),
 'VII': (('УГЛУБЛЁННО · 9–11 КЛАССЫ', 'ADVANCED · GRADES 9–11'), ('algebra-and-trigonometry-2e', 'Algebra and Trigonometry 2e')),
 'VIII':(('УГЛУБЛЁННО · 10–12 КЛАССЫ', 'ADVANCED · GRADES 10–12'), ('calculus-volume-1', 'Calculus Volume 1')),
 'IX':  (('УГЛУБЛЁННО · 10–12 КЛАССЫ', 'ADVANCED · GRADES 10–12'), None),
 'X':   (('ОСНОВЫ / УГЛУБЛЁННО · 7–12 КЛАССЫ', 'BASICS / ADVANCED · GRADES 7–12'), ('introductory-statistics-2e', 'Introductory Statistics 2e')),
}

def M(title, ctrls, st, cap_ru, cap_en, label, js, vb='0 0 600 250'):
    return dict(title=_t(title), ctrls=ctrls, st=[_t(x) for x in st], cap=(cap_ru, cap_en), label=_t(label), js=js, vb=vb)

def S(sid, h_ru, h_en, text, fm=None, model=None):
    return dict(id=sid, h=(h_ru, h_en), text=_t(text), fm=fm, model=model)

def TK(title, q, g, s, a):
    return dict(title=_t(title), q=_t(q), g=_t(g), s=_t(s), a=_t(a))

def Q(rq, eq, ok, w1, w2, rx, ex=None):
    ok, w1, w2, rx = _t(ok), _t(w1), _t(w2), _t(rx)
    ex = rx if ex is None else ex
    ex = ex if ex is not None else rx[1]
    if isinstance(ex, tuple): ex = ex[1]
    return qz(rq, ok[0], w1[0], w2[0], rx[0], eq, ok[1], w1[1], w2[1], ex)

def chapter(n, slug, block, title, lead, riddle, answer_h, answer, sections, tasks, quiz, src=(), note=None, desc=None, level=None, hint=None):
    title, lead, riddle, answer_h, answer = _t(title), _t(lead), _t(riddle), _t(answer_h), _t(answer)
    nums = [c[0] for c in REG.CHAPTERS]
    i = nums.index(n)
    def nav(j):
        c = REG.CHAPTERS[j]
        return (c[1], 'Глава %s · %s' % (c[0], c[2]), 'Chapter %s · %s' % (c[0], c[3]))
    prev = nav(i - 1) if i > 0 else ('../index.html', 'Содержание', 'Contents')
    nxt = nav(i + 1) if i + 1 < len(nums) else ('../index.html', 'Конец построенной части — к содержанию', 'End of the finished part — to the contents')
    lv = level or BLK[block][0]
    # секции и модели
    secs, MODELS, LABR, LABE, tocs = [], [], {}, {}, [('riddle', 'Загадка', 'Puzzle')]
    k = 0
    first_model_title = None
    for s in sections:
        left = bd(*[paras(x) for x in s['text']])
        if s['fm']:
            f = s['fm']; ft = f[0]
            left += formula(bi(*ft) if isinstance(ft, tuple) else ft, f[1], f[2])
        lab = ''
        if s['model']:
            k += 1; m = s['model']; mid = 'm%d' % k
            ctrl_html, ids, sel = '', [], {}
            for c in m['ctrls']:
                if c[0] == 'r':
                    _, cid, ru, en, mn, mx, st, val = c
                    ctrl_html += slider('%s_%s' % (mid, cid), ru, en, mn, mx, st, val); ids.append(cid)
                else:
                    _, cid, ru, en, ro, eo, dflt = c
                    ctrl_html += select('%s_%s' % (mid, cid), ru, en); ids.append(cid); sel[cid] = [ro, eo, dflt]
            sh = stats([('%ss%d' % (mid, j), a, b) for j, (a, b) in enumerate(m['st'])])
            lab = model(k, m['title'][0].upper(), m['title'][1].upper(), mid + 'Svg', m['vb'], ctrl_html, sh, mid + 'Fb', m['cap'][0], m['cap'][1])
            if first_model_title is None: first_model_title = m['title']
            MODELS.append('{k:%d,svg:"%sSvg",ids:%s,sel:%s,fn:function(v,q){%s}}' % (k, mid, json.dumps(ids), json.dumps(sel, ensure_ascii=False), m['js']))
            LABR[mid + 'Svg'], LABE[mid + 'Svg'] = m['label']
        secs.append(section(s['id'], s['h'][0], s['h'][1], left, lab))
        tocs.append((s['id'], s['h'][0].split(':')[0][:22], s['h'][1].split(':')[0][:22]))
    tocs += [('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')]
    tasks_html = [task(j + 1, t['title'][0], t['title'][1], t['q'][0], t['q'][1], t['g'][0], t['g'][1], t['s'][0], t['s'][1], t['a'][0], t['a'][1], j == 0) for j, t in enumerate(tasks)]
    h = hint or (first_model_title[0].capitalize(), first_model_title[1].capitalize())
    # источники
    srcs = []
    if src: srcs.append(('Тема —', 'The topic —', ', '.join(LINK(u, t) for t, u in src)))
    bk = BLK[block][1]
    if bk: srcs.append(('Учебник —', 'A textbook —', LINK('https://openstax.org/books/%s/pages/1-introduction' % bk[0], 'OpenStax %s' % bk[1])))
    else: srcs.append(('Программа и стандарты —', 'Syllabus and standards —', LINK('https://openstax.org/subjects/math', 'OpenStax Math')))
    nt = note or ('Сюжет, числа и задачи придуманы для атласа.', 'The story, numbers and problems were invented for the atlas.')
    nt = _t(nt)
    runtime = r'''
const MODELS=[%s];
MODELS.forEach(M=>{M.q=id=>$("m"+M.k+"_"+id);M.run=function(){const v={};M.ids.forEach(id=>{v[id]=+M.q(id).value});
 const r=M.fn(v,M.q)||{};
 M.ids.forEach(id=>{const e=M.q(id),o=$("m"+M.k+"_"+id+"Out");if(o&&e.type==="range"){const st=e.step||"1",dp=(st.split(".")[1]||"").length;o.textContent=dp?fmt(+e.value,dp):e.value}});
 $(M.svg).innerHTML=r.svg||"";(r.st||[]).forEach((x,i)=>{const el=$("m"+M.k+"s"+i);if(el)el.innerHTML=x});$("m"+M.k+"Fb").textContent=r.fb||""};
 M.ids.forEach(id=>M.q(id).addEventListener("input",M.run))});
const LAB={ru:%s,en:%s};
function drawAll(){MODELS.forEach(M=>{Object.keys(M.sel||{}).forEach(id=>fillSel("m"+M.k+"_"+id,M.sel[id][lang==="ru"?0:1],M.sel[id][2]));M.run()})}
const T={ru:{},en:{}};
''' % (','.join(MODELS), json.dumps(LABR, ensure_ascii=False), json.dumps(LABE, ensure_ascii=False))
    c = dict(n=n, slug=slug, block=block, level_ru=lv[0], level_en=lv[1], title=title,
        desc=desc or ('Глава %d Атласа математики: %s.' % (int(n), title[0])),
        lead=lead, toc=tocs,
        riddle=(paras(riddle[0]), paras(riddle[1])), hint=stdhint(*h),
        sections=secs, tasks=tasks_html, quiz=quiz, answer_h=answer_h, answer=(paras(answer[0]), paras(answer[1])),
        sources=srcs, note=stdnote(nt[0], nt[1]), prev=prev, next=nxt, js=MJS + MJS2 + runtime)
    build(c)
