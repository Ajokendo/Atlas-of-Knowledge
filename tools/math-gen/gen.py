# -*- coding: utf-8 -*-
"""Общий шаблон глав физики: собирает HTML-страницу главы из данных."""
import json, re

import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
BASE = os.path.join(ROOT, 'math', 'chapters') + '/'
HEAD_SRC = os.path.join(ROOT, 'physics', 'chapters', '03-motion-and-forces.html')
os.makedirs(BASE, exist_ok=True)
HEAD = '\n'.join(open(HEAD_SRC, encoding='utf-8').read().split('\n')[:40])

def bi(ru, en):
    return '<span data-l="ru">%s</span><span data-l="en">%s</span>' % (ru, en)

def bd(ru, en):
    return '<div data-l="ru">%s</div><div data-l="en">%s</div>' % (ru, en)

def formula(text, ru, en):
    return '<div class="formula">%s<small>%s</small></div>' % (text, bi(ru, en))

def callout(ru, en):
    return '<p class="callout">%s</p>' % bi(ru, en)

def table(h_ru, h_en, rows):
    th = ''.join('<th>%s</th>' % bi(a, b) for a, b in zip(h_ru, h_en))
    body = ''
    for r in rows:
        body += '<tr>' + ''.join('<td>%s</td>' % (bi(*c) if isinstance(c, tuple) else c) for c in r) + '</tr>'
    return '<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, body)

def slider(i, ru, en, mn, mx, st, val):
    return ('<div class="controls"><label for="%s">%s: <strong id="%sOut"></strong></label>'
            '<input id="%s" type="range" min="%s" max="%s" step="%s" value="%s"></div>') % (i, bi(ru, en), i, i, mn, mx, st, val)

def select(i, ru, en):
    return '<div class="controls"><label for="%s">%s</label><select id="%s"></select></div>' % (i, bi(ru, en), i)

def buttons(items):
    out = '<div class="controls">'
    for i, ru, en, ghost in items:
        out += '<button class="act%s" type="button" id="%s">%s</button>' % (' ghost' if ghost else '', i, bi(ru, en))
    return out + '</div>'

def stats(items):
    return '<div class="stats" aria-live="polite">' + ''.join(
        '<div class="stat"><small>%s</small><strong id="%s"></strong></div>' % (bi(ru, en), i) for i, ru, en in items) + '</div>'

def model(n, t_ru, t_en, svg_id, vb, controls, stat_html, fb_id, cap_ru, cap_en):
    return ('<div class="lab"><p class="eyebrow">%s</p><svg id="%s" viewBox="%s" role="img" aria-label=""></svg>%s%s'
            '<p class="fb" id="%s" aria-live="polite"></p><p class="caption">%s</p></div>') % (
        bi('МОДЕЛЬ %d · %s' % (n, t_ru), 'MODEL %d · %s' % (n, t_en)), svg_id, vb, controls, stat_html, fb_id, bi(cap_ru, cap_en))

def section(sid, h_ru, h_en, left, lab=''):
    return '<section class="section" id="%s"><h2>%s</h2><div class="two"><div>%s</div>%s</div></section>' % (sid, bi(h_ru, h_en), left, lab)

def task(n, t_ru, t_en, q_ru, q_en, g_ru, g_en, s_ru, s_en, a_ru, a_en, open_=False):
    def part(q, g, s, a, lab_g, lab_a):
        return '<p>%s</p><p class="given">%s %s</p><div class="sol"><p>%s</p><p><strong>%s</strong> %s</p></div>' % (q, lab_g, g, s, lab_a, a)
    return ('<details class="task"%s><summary>%s</summary><div data-l="ru">%s</div><div data-l="en">%s</div></details>' % (
        ' open' if open_ else '', bi('Задача %d. %s' % (n, t_ru), 'Problem %d. %s' % (n, t_en)),
        part(q_ru, g_ru, s_ru, a_ru, 'Дано:', 'Ответ:'), part(q_en, g_en, s_en, a_en, 'Given:', 'Answer:')))

COMMON_JS = r'''
const $=id=>document.getElementById(id);
let lang="ru";
try{const s=localStorage.getItem("atlas-lang");if(s==="en"||s==="ru")lang=s}catch(e){}
const UN={ru:{ms:" м/с",m:" м",km:" км",mm:" мм",s:" с",min:" мин",h:" ч",kg:" кг",g:" г",L:" л",J:" Дж",kJ:" кДж",MJ:" МДж",W:" Вт",kW:" кВт",N:" Н",C:" °C",K:" К"},
 en:{ms:" m/s",m:" m",km:" km",mm:" mm",s:" s",min:" min",h:" h",kg:" kg",g:" g",L:" L",J:" J",kJ:" kJ",MJ:" MJ",W:" W",kW:" kW",N:" N",C:" °C",K:" K"}};
function tt(){return Object.assign({},UN[lang],T[lang])}
function fmt(x,dp){let s=x.toFixed(dp);return lang==="ru"?s.replace(".",","):s}
function num(x){return lang==="ru"?String(x).replace(/\B(?=(\d{3})+(?!\d))/g," "):String(x).replace(/\B(?=(\d{3})+(?!\d))/g,",")}
function svgText(x,y,txt,col,anchor,size){return '<text x="'+x+'" y="'+y+'" text-anchor="'+(anchor||"start")+'" font-family="JetBrains Mono,monospace" font-size="'+(size||11)+'" fill="'+col+'">'+txt+'</text>'}
function arrow(x1,y1,x2,y2,col,w){const dx=x2-x1,dy=y2-y1,L=Math.hypot(dx,dy);if(L<3)return "";const ux=dx/L,uy=dy/L,bx=x2-ux*11,by=y2-uy*11;return '<line x1="'+x1+'" y1="'+y1+'" x2="'+bx+'" y2="'+by+'" stroke="'+col+'" stroke-width="'+w+'"/><path d="M'+x2+' '+y2+' L'+(bx-uy*6)+' '+(by+ux*6)+' L'+(bx+uy*6)+' '+(by-ux*6)+' Z" fill="'+col+'"/>'}
function axes(xmax,ymax,xs,ys,x0,x1,yb,yt,xd,yd){let s='';xd=xd||0;yd=yd||0;
 for(let k=0;k<=xs;k++){const x=x0+k/xs*(x1-x0);s+='<line x1="'+x+'" y1="'+yb+'" x2="'+x+'" y2="'+yt+'" stroke="#e3e1da"/>'+svgText(x,yb+14,fmt(k*xmax/xs,xd),"#66666b","middle",10)}
 for(let k=0;k<=ys;k++){const y=yb-k/ys*(yb-yt);s+='<line x1="'+x0+'" y1="'+y+'" x2="'+x1+'" y2="'+y+'" stroke="#e3e1da"/>'+svgText(x0-6,y+4,fmt(k*ymax/ys,yd),"#66666b","end",10)}
 s+='<line x1="'+x0+'" y1="'+yb+'" x2="'+x1+'" y2="'+yb+'" stroke="#18181a" stroke-width="1.5"/><line x1="'+x0+'" y1="'+yb+'" x2="'+x0+'" y2="'+yt+'" stroke="#18181a" stroke-width="1.5"/>';return s}
function fillSel(id,list,def){const sel=$(id),v=sel.value;sel.innerHTML="";list.forEach((s,i)=>{const o=document.createElement("option");o.value=i;o.textContent=s;sel.appendChild(o)});sel.value=(v!==""&&v!=null)?v:(def||0)}
const G=9.8;
'''

QUIZ_JS = r'''
let answers={};
function saveScore(){const score=Q.filter((x,i)=>answers[i]===x.a).length,r={score:score,total:Q.length,date:new Date().toISOString(),chapter:"@@N@@"};try{localStorage.setItem("atlas-math-quiz-v1",JSON.stringify(r));const k="atlas-math-quiz-v1-history-v1";let h=JSON.parse(localStorage.getItem(k)||"[]");if(!Array.isArray(h))h=[];h.push(r);localStorage.setItem(k,JSON.stringify(h.slice(-20)))}catch(e){}}
const QT={ru:{score:(s,n)=>"Результат: "+s+" из "+n,right:"Правильный ответ: "},en:{score:(s,n)=>"Score: "+s+" of "+n,right:"Right answer: "}};
function renderQuiz(){const box=$("quizBox");box.innerHTML="";Q.forEach((item,i)=>{const d=item[lang],div=document.createElement("div");div.className="q";const h=document.createElement("h3");h.textContent=(i+1)+". "+d.q;div.appendChild(h);
 ORD[i%ORD.length].forEach(j=>{const o=d.o[j],b=document.createElement("button");b.type="button";b.className="opt";b.textContent=o[0];if(answers[i]!==undefined){if(j===item.a)b.classList.add("right");if(j===answers[i]&&j!==item.a)b.classList.add("wrong");b.disabled=true}b.addEventListener("click",()=>{answers[i]=j;if(Object.keys(answers).length===Q.length)saveScore();renderQuiz()});div.appendChild(b)});
 if(answers[i]!==undefined){const w=document.createElement("p");w.className="why "+(answers[i]===item.a?"fb ok":"fb bad");w.textContent=d.o[answers[i]][1]+(answers[i]===item.a?"":" — "+QT[lang].right+d.o[item.a][0]+".");div.appendChild(w)}box.appendChild(div)});
 const n=Object.keys(answers).length;$("score").textContent=n===Q.length?QT[lang].score(Q.filter((x,i)=>answers[i]===x.a).length,Q.length):""}
$("resetQuiz").addEventListener("click",()=>{answers={};renderQuiz()});
function apply(){document.documentElement.lang=lang;$("lang").textContent=lang==="ru"?"EN":"RU";document.title=lang==="ru"?"@@TRU@@ — Атлас математики":"@@TEN@@ — Atlas of Mathematics";
 Object.keys(LAB.ru).forEach(id=>$(id).setAttribute("aria-label",LAB[lang][id]));
 drawAll();renderQuiz()}
$("lang").addEventListener("click",()=>{lang=lang==="ru"?"en":"ru";try{localStorage.setItem("atlas-lang",lang)}catch(e){}apply()});
apply();
'''

ORD = [[1, 0, 2], [0, 2, 1], [2, 1, 0], [0, 1, 2], [2, 0, 1], [1, 2, 0], [0, 2, 1], [2, 0, 1]]

def build(c):
    n = c['n']
    toc = ''.join('<a href="#%s">%02d %s</a>' % (a, i + 1, bi(r, e)) for i, (a, r, e) in enumerate(c['toc']))
    body = ('<header class="top"><a class="brand" href="../index.html"><span data-l="ru">Атлас математики</span><span data-l="en">Atlas of Mathematics</span></a>'
            '<div class="actions"><a class="btn" href="../../index.html"><span data-l="ru">Все предметы</span><span data-l="en">All subjects</span></a>'
            '<button type="button" class="btn" id="lang">EN</button></div></header>\n<main>\n')
    body += ('<section class="intro"><p class="eyebrow">%s</p><h1>%s</h1><p class="lead">%s</p><nav class="toc" aria-label="Contents">%s</nav></section>\n' % (
        bi('БЛОК %s · ГЛАВА %s · %s' % (c['block'], n, c['level_ru']), 'BLOCK %s · CHAPTER %s · %s' % (c['block'], n, c['level_en']),),
        bi(*c['title']), bi(*c['lead']), toc))
    body += ('<section class="section" id="riddle"><div class="riddle"><span class="tag">%s</span>%s%s</div>%s</section>\n' % (
        bi('ЗАГАДКА В НАЧАЛЕ', 'OPENING PUZZLE'), '<div data-l="ru">%s</div>' % c['riddle'][0], '<div data-l="en">%s</div>' % c['riddle'][1],
        callout(*c['hint'])))
    body += '\n'.join(c['sections']) + '\n'
    body += '<section class="section" id="tasks"><h2>%s</h2>\n%s\n</section>\n' % (bi('Разобранные задачи', 'Worked problems'), '\n'.join(c['tasks']))
    body += ('<section class="section" id="quiz"><h2>%s</h2><p>%s</p><div id="quizBox"></div><p class="score" id="score" aria-live="polite"></p>'
             '<button class="act ghost" type="button" id="resetQuiz">%s</button></section>\n' % (
                 bi('Проверьте себя', 'Check yourself'), bi('Выберите ответ — сразу появится объяснение.', 'Pick an answer — an explanation appears at once.'),
                 bi('Пройти заново', 'Start again')))
    body += '<section class="section" id="answer"><h2>%s</h2>%s</section>\n' % (bi(*c['answer_h']), bd(*c['answer']))
    src = ''
    for r, e, links in c['sources']:
        src += '<li>%s %s</li>' % (bi(r, e), links)
    body += ('<section class="section" id="sources"><h2>%s</h2><ul class="src">%s</ul>%s</section>\n' % (
        bi('Источники', 'Sources'), src, callout(*c['note'])))
    p = c['prev']; nx = c['next']
    nxt = ('<a href="%s"><span data-l="ru">%s</span><span data-l="en">%s</span> →</a>' % (nx[0], nx[1], nx[2])) if nx[0] else \
          '<span><span data-l="ru">%s</span><span data-l="en">%s</span></span>' % (nx[1], nx[2])
    body += ('<section class="section"><div class="nav"><a href="%s">← <span data-l="ru">%s</span><span data-l="en">%s</span></a>'
             '<a href="../index.html"><span data-l="ru">Содержание блока</span><span data-l="en">Block contents</span></a>%s</div></section>\n</main>\n' % (p[0], p[1], p[2], nxt))
    body += ('<footer><span>%s</span><span class="credit"><span data-l="ru">© 2026 Азамат Орозобеков · подготовлено с помощью ИИ · <a href="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/CONTENT_LICENSE.md" target="_blank" rel="noopener">CC BY 4.0</a></span>'
             '<span data-l="en">© 2026 Azamat Orozobekov · prepared with AI assistance · <a href="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/CONTENT_LICENSE.md" target="_blank" rel="noopener">CC BY 4.0</a></span></span></footer>\n' % bi('АТЛАС МАТЕМАТИКИ · ГЛАВА ' + n, 'ATLAS OF MATHEMATICS · CHAPTER ' + n))
    Q = []
    for qr, orr, qe, oen, a in c['quiz']:
        Q.append({'ru': {'q': qr, 'o': [list(x) for x in orr]}, 'en': {'q': qe, 'o': [list(x) for x in oen]}, 'a': a})
    assert len(Q) == 8 and all(len(x['ru']['o']) == 3 for x in Q)
    js = '<script>\n(function(){' + COMMON_JS + c['js'] + '\nconst Q=' + json.dumps(Q, ensure_ascii=False) + ';\nconst ORD=' + json.dumps(ORD) + ';' + \
         QUIZ_JS.replace('@@N@@', n).replace('@@TRU@@', c['title'][0]).replace('@@TEN@@', c['title'][1]) + '\n})();\n</script>\n</body></html>\n'
    head = HEAD
    head, k1 = re.subn(r'<title>.*?</title>', '<title>%s — Атлас математики</title>' % c['title'][0], head)
    head, k2 = re.subn(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + c['desc'] + m.group(2), head)
    assert k1 == 1 and k2 == 1, (k1, k2)
    open(BASE + c['slug'], 'w', encoding='utf-8').write(head.replace('</style>','h1{overflow-wrap:anywhere}.stats{grid-template-columns:repeat(3,minmax(0,1fr))}.stat strong{overflow-wrap:anywhere;hyphens:auto}@media(max-width:560px){.stat strong{font-size:15px;line-height:1.25}}</style>',1) + '\n' + body + js)
    print('built', c['slug'])
