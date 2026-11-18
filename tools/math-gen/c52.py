# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('sin x = a на окружности', 'sin x = a on the circle'),
 [('r', 'a', 'Значение a', 'Value a', -1, 1, 0.1, 0.5)],
 [('Первое решение arcsin a', 'First solution arcsin a'), ('Второе решение π − arcsin a', 'Second solution π − arcsin a'), ('Все решения', 'All solutions')],
 'На окружности две точки имеют одну и ту же ординату a. Каждую можно повернуть на полный оборот 2πk — получаем бесконечную серию.', 'On the circle two points have the same ordinate a. Each can be rotated by a full turn 2πk — we get an infinite family.', ('Две точки с ординатой a', 'Two points with ordinate a'),
 r'''const x1=Math.asin(v.a),x2=Math.PI-x1,R0=85,cx=300,cy=110;let g=L(cx-110,cy,cx+110,cy,COL.mut,1.5)+L(cx,cy-100,cx,cy+100,COL.mut,1.5)+C(cx,cy,R0,"none",COL.ink,2.5)+L(cx-100,cy-v.a*R0,cx+100,cy-v.a*R0,COL.c,2,0);
 [[x1,COL.a],[x2,COL.b]].forEach(p=>g+=L(cx,cy,cx+R0*Math.cos(p[0]),cy-R0*Math.sin(p[0]),p[1],3)+C(cx+R0*Math.cos(p[0]),cy-R0*Math.sin(p[0]),7,p[1]));
 return {svg:g,st:[fnum(x1,4)+" ≈ "+fnum(x1*180/Math.PI,1)+"°",fnum(x2,4)+" ≈ "+fnum(x2*180/Math.PI,1)+"°",Math.abs(v.a)===1?"x = "+(v.a>0?"π/2":"−π/2")+" + 2πk":"x = "+fnum(x1,3)+" + 2πk;  x = "+fnum(x2,3)+" + 2πk"],fb:U("При a = ±1 две точки сливаются в одну.","At a = ±1 the two points merge into one.")}''', '0 0 600 225')

m2 = M(('Сколько решений на отрезке', 'How many solutions on an interval'),
 [('s', 'f', 'Уравнение', 'Equation', ['sin x = a', 'cos x = a'], ['sin x = a', 'cos x = a'], 0), ('r', 'a', 'Значение a', 'Value a', -1.5, 1.5, 0.1, 0.5)],
 [('Решения на [−2π; 2π]', 'Solutions on [−2π; 2π]'), ('Число решений', 'Number of solutions'), ('Период', 'Period')],
 'Решения — точки пересечения графика с горизонтальной прямой y = a. На каждом периоде их обычно два.', 'The solutions are the intersection points of the graph with the horizontal line y = a. On each period there are usually two.', ('График и прямая y = a', 'The graph and the line y = a'),
 r'''const F=v.f===0?Math.sin:Math.cos,G=Gr({x0:-2*Math.PI,x1:2*Math.PI,y0:-1.7,y1:1.7,L:80,T:10,W:460,H:210});let g=G.grid(Math.PI/2,0.5,false)+G.fn(F,COL.a,3.5,-2*Math.PI,2*Math.PI)+G.fn(x=>v.a,COL.b,2,-2*Math.PI,2*Math.PI,true);const xs=[];
 if(Math.abs(v.a)<=1){const b=v.f===0?Math.asin(v.a):Math.acos(v.a);const base=v.f===0?[b,Math.PI-b]:[b,-b];for(let k=-2;k<=2;k++)base.forEach(x=>{const z=x+2*Math.PI*k;if(z>=-2*Math.PI-1e-9&&z<=2*Math.PI+1e-9&&!xs.some(t=>Math.abs(t-z)<1e-6))xs.push(z)})}
 xs.sort((p,q)=>p-q).forEach(x=>g+=G.pt(x,v.a,COL.c,7));
 return {svg:g,st:[xs.length?xs.map(x=>fnum(x,2)).join("; "):U("решений нет","no solutions"),xs.length,"2π ≈ 6,28"],fb:Math.abs(v.a)>1?U("|a| > 1: прямая выше (ниже) волны, решений нет.","|a| > 1: the line is above (below) the wave — no solutions."):U("Каждая точка пересечения — решение; их бесконечно много на всей оси.","Each intersection is a solution; there are infinitely many on the whole axis.")}''', '0 0 600 250')

m3 = M(('tan x = a и общее решение', 'tan x = a and the general solution'),
 [('r', 'a', 'Значение a', 'Value a', -5, 5, 0.5, 1)],
 [('Частное решение arctan a', 'Particular solution arctan a'), ('Решения на (−π; π)', 'Solutions on (−π; π)'), ('Общее решение', 'General solution')],
 'У тангенса период π, поэтому у уравнения tan x = a одна серия решений: x = arctan a + πk.', 'Tangent has period π, so the equation tan x = a has one family of solutions: x = arctan a + πk.', ('График тангенса и прямая y = a', 'The tangent graph and the line y = a'),
 r'''const G=Gr({x0:-Math.PI*1.5,x1:Math.PI*1.5,y0:-6,y1:6,L:80,T:10,W:460,H:210});const x0=Math.atan(v.a);let g=G.grid(Math.PI/2,2,false)+G.fn(Math.tan,COL.a,3.5,-Math.PI*1.5,Math.PI*1.5)+G.fn(x=>v.a,COL.b,2,-Math.PI*1.5,Math.PI*1.5,true);[x0-Math.PI,x0,x0+Math.PI].forEach(x=>{if(Math.abs(x)<=Math.PI*1.5)g+=G.pt(x,v.a,COL.c,7)});
 return {svg:g,st:[fnum(x0,4)+" ≈ "+fnum(x0*180/Math.PI,1)+"°",fnum(x0-Math.PI,3)+"; "+fnum(x0,3)+"; "+fnum(x0+Math.PI,3),"x = "+fnum(x0,3)+" + πk"],fb:U("Для любого a уравнение tan x = a имеет решение.","For any a the equation tan x = a has a solution.")}''', '0 0 600 250')

chapter('52', '52-trig-equations.html', 'VII', ('Тригонометрические уравнения', 'Trigonometric equations'),
 ('Как решать уравнения sin x = a, cos x = a, tan x = a и записывать бесконечные серии решений.', 'How to solve sin x = a, cos x = a, tan x = a and write infinite families of solutions.'),
 ('Высота прилива в порту описывается функцией h(t) = 2 + sin(t), где t — время в часах от начала отсчёта (условно). Корабль может зайти в порт при высоте воды не меньше 2,5 м.\n\nКогда это возможно?', 'The tide height in a port is described by h(t) = 2 + sin(t) where t is the time in hours from a starting point (illustratively). A ship can enter the port when the water is at least 2.5 m.\n\nWhen is this possible?'),
 ('Разгадка: sin t ≥ 0,5', 'The answer: sin t ≥ 0.5'),
 ('Нужно 2 + sin t ≥ 2,5, то есть sin t ≥ 0,5. Граничные значения находим из уравнения sin t = 0,5: t = π/6 и t = 5π/6 (плюс полные периоды 2πk). Между ними синус больше 0,5, то есть окно захода — π/6 ≤ t ≤ 5π/6, это около 2,1 ч за каждый период. Решения уравнения задают границы решения неравенства.', 'We need 2 + sin t ≥ 2.5, i.e. sin t ≥ 0.5. The boundary values come from the equation sin t = 0.5: t = π/6 and t = 5π/6 (plus full periods 2πk). Between them the sine exceeds 0.5, so the window is π/6 ≤ t ≤ 5π/6, about 2.1 h per period. The solutions of the equation give the boundaries of the inequality’s solution.'),
 [S('sin', 'Уравнение sin x = a', 'The equation sin x = a', ('При |a| ≤ 1 решения: <strong>x = arcsin a + 2πk</strong> и <strong>x = π − arcsin a + 2πk</strong>, k — любое целое. При |a| &gt; 1 решений нет. Частные случаи: sin x = 0 → x = πk; sin x = 1 → x = π/2 + 2πk. <em>arcsin a</em> — угол из [−π/2; π/2], синус которого равен a.', 'For |a| ≤ 1 the solutions are <strong>x = arcsin a + 2πk</strong> and <strong>x = π − arcsin a + 2πk</strong> with k any integer. For |a| &gt; 1 there are none. Special cases: sin x = 0 → x = πk; sin x = 1 → x = π/2 + 2πk. <em>arcsin a</em> is the angle in [−π/2; π/2] whose sine is a.'),
    ('x = (−1)ᵏ arcsin a + πk', '', 'x = (−1)ᵏ arcsin a + πk'), m1),
  S('cos', 'Уравнение cos x = a', 'The equation cos x = a', ('При |a| ≤ 1: <strong>x = ± arccos a + 2πk</strong>. Графически — точки пересечения косинусоиды с прямой y = a. Частные: cos x = 0 → x = π/2 + πk; cos x = 1 → x = 2πk; cos x = −1 → x = π + 2πk.', 'For |a| ≤ 1: <strong>x = ± arccos a + 2πk</strong>. Graphically — intersection points of the cosine curve with the line y = a. Special cases: cos x = 0 → x = π/2 + πk; cos x = 1 → x = 2πk; cos x = −1 → x = π + 2πk.'),
    ('x = ± arccos a + 2πk', '', 'x = ± arccos a + 2πk'), m2),
  S('tan', 'Уравнение tan x = a', 'The equation tan x = a', ('При любом a: <strong>x = arctan a + πk</strong>. Для сложных уравнений используют замену: 2 sin²x − sin x − 1 = 0 при t = sin x даёт квадратное 2t² − t − 1 = 0 с корнями 1 и −1/2.', 'For any a: <strong>x = arctan a + πk</strong>. For complex equations we use a substitution: 2 sin²x − sin x − 1 = 0 with t = sin x gives the quadratic 2t² − t − 1 = 0 with roots 1 and −1/2.'),
    ('x = arctan a + πk', '', 'x = arctan a + πk'), m3)],
 [TK(('Синус', 'Sine'), ('Решите sin x = 1/2.', 'Solve sin x = 1/2.'), '', 'x = π/6 + 2πk и x = 5π/6 + 2πk.', ('x = π/6 + 2πk; x = 5π/6 + 2πk.', 'x = π/6 + 2πk; x = 5π/6 + 2πk.')),
  TK(('Косинус', 'Cosine'), ('Решите cos x = 1/2.', 'Solve cos x = 1/2.'), '', 'x = ±π/3 + 2πk.', 'x = ±π/3 + 2πk.'),
  TK(('Нет решений', 'No solutions'), ('Решите sin x = 1,5.', 'Solve sin x = 1.5.'), '', '|1,5| > 1 — решений нет.', ('Нет решений.', 'No solutions.')),
  TK(('Тангенс', 'Tangent'), ('Решите tan x = 1.', 'Solve tan x = 1.'), 'arctan 1 = π/4', 'x = π/4 + πk.', 'x = π/4 + πk.'),
  TK(('Замена', 'Substitution'), ('Решите 2 sin²x − sin x − 1 = 0.', 'Solve 2 sin²x − sin x − 1 = 0.'), 't = sin x', '2t² − t − 1 = 0: t = 1 или t = −1/2. sin x = 1 → π/2 + 2πk; sin x = −1/2 → −π/6 + 2πk, 7π/6 + 2πk.', ('См. решение.', 'See the solution.'))],
 [Q('sin x = 0 при', 'sin x = 0 for', 'x = πk', 'x = 2πk', 'x = π/2 + πk', ('Синус нулевой при кратных π.', 'Sine is zero at multiples of π.')),
  Q('Решения sin x = 2', 'Solutions of sin x = 2', ('нет', 'none'), ('x = π/2', 'x = π/2'), ('два', 'two'), ('|a| > 1.', '|a| > 1.')),
  Q('Период решений tan x = a', 'The period of the solutions of tan x = a', 'π', '2π', 'π/2', ('Период тангенса.', 'The period of tangent.')),
  Q('cos x = 1. x =', 'cos x = 1. x =', '2πk', 'π + 2πk', 'πk', ('Точка (1; 0).', 'The point (1; 0).')),
  Q('Сколько решений sin x = 1/2 на [0; 2π]?', 'How many solutions has sin x = 1/2 on [0; 2π]?', '2', '1', '4', ('π/6 и 5π/6.', 'π/6 and 5π/6.')),
  Q('arcsin(1/2) =', 'arcsin(1/2) =', 'π/6', 'π/3', 'π/2', ('sin 30° = 1/2.', 'sin 30° = 1/2.')),
  Q('Подстановка t = sin x допустима при', 'Substituting t = sin x is valid for', ('|t| ≤ 1', '|t| ≤ 1'), ('любом t', 'any t'), ('t > 1', 't > 1'), ('Синус ограничен.', 'Sine is bounded.')),
  Q('k в серии решений — это', 'In a family of solutions k is', ('любое целое число', 'any integer'), ('только 0', 'only 0'), ('любое число', 'any number'), ('Целое число оборотов.', 'An integer number of turns.'))],
 src=[('Wikipedia: Inverse trigonometric functions', 'https://en.wikipedia.org/wiki/Inverse_trigonometric_functions'), ('Wikipedia: Trigonometric equation', 'https://en.wikipedia.org/wiki/Trigonometric_equation')],
 note=('Модель прилива в загадке условная.', 'The tide model in the puzzle is illustrative.'))
