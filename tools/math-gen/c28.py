# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Графический способ', 'The graphical method'),
 [('r', 'x0', 'x решения', 'x of the solution', -5, 5, 1, 2), ('r', 'y0', 'y решения', 'y of the solution', -5, 5, 1, 1), ('r', 'k1', 'Наклон первой прямой', 'Slope of the first line', -3, 3, 1, 1), ('r', 'k2', 'Наклон второй прямой', 'Slope of the second line', -3, 3, 1, -1)],
 [('Первое уравнение', 'First equation'), ('Второе уравнение', 'Second equation'), ('Решение', 'Solution')],
 'Каждое уравнение с двумя неизвестными задаёт прямую. Решение системы — точка, где прямые пересекаются.', 'Each equation with two unknowns defines a line. The solution of the system is the point where the lines meet.', ('Две прямые на плоскости', 'Two lines on the plane'),
 r'''const G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:220});const b1=v.y0-v.k1*v.x0,b2=v.y0-v.k2*v.x0,ps=n=>n<0?"− "+(-n):"+ "+n;
 let g=G.grid(2,2)+G.fn(t=>v.k1*t+b1,COL.a,3)+G.fn(t=>v.k2*t+b2,COL.b,3);if(v.k1!==v.k2)g+=G.pt(v.x0,v.y0,COL.c,8)+G.txt(v.x0+1.5,v.y0+0.8,"("+v.x0+"; "+v.y0+")",COL.c,14);
 return {svg:g,st:["y = "+v.k1+"x "+ps(b1),"y = "+v.k2+"x "+ps(b2),v.k1===v.k2?U("прямые параллельны — решений нет","the lines are parallel — no solution"):"x = "+v.x0+",  y = "+v.y0],fb:v.k1===v.k2?U("Одинаковый наклон — прямые не пересекаются.","Equal slopes — the lines do not meet."):U("Подставьте пару ("+v.x0+"; "+v.y0+") в оба уравнения — оба верны.","Substitute the pair ("+v.x0+"; "+v.y0+") into both equations — both hold.")}''', '0 0 600 250')

m2 = M(('Способ сложения', 'The addition method'),
 [('r', 'p', 'p', 'p', 1, 5, 1, 2), ('r', 'q', 'q', 'q', 1, 5, 1, 3), ('r', 'x0', 'x решения', 'x of the solution', -5, 5, 1, 2), ('r', 'y0', 'y решения', 'y of the solution', -5, 5, 1, 1)],
 [('Система', 'The system'), ('Складываем уравнения', 'Adding the equations'), ('Решение', 'Solution')],
 'В одном уравнении +y, в другом −y: при сложении y исчезает, остаётся уравнение с одним неизвестным.', 'One equation has +y, the other −y: adding makes y vanish and leaves an equation with one unknown.', ('Решение по шагам', 'The solution step by step'),
 r'''const C1=v.p*v.x0+v.y0,C2=v.q*v.x0-v.y0,s=v.p+v.q,ps=n=>n<0?"− "+(-n):"+ "+n;const st=[v.p+"x + y = "+C1+",   "+v.q+"x − y = "+C2,s+"x = "+(C1+C2)+"  →  x = "+v.x0,"y = "+C1+" − "+v.p+"·"+v.x0+" = "+v.y0];let g="";
 st.forEach((t,i)=>{g+=R(30,15+i*65,540,50,i===2?"#e1f0e8":COL.bg,i===2?COL.c:COL.line,2,6)+TX(300,48+i*65,t,COL.ink,20,"middle",600)});
 return {svg:g,st:[v.p+"x + y = "+C1+";  "+v.q+"x − y = "+C2,"("+v.p+" + "+v.q+")x = "+C1+" + "+C2+" = "+(C1+C2),"("+v.x0+"; "+v.y0+")"],fb:U("Проверка во втором уравнении: "+v.q+" · "+v.x0+" − "+v.y0+" = "+C2+" ✓.","Check in the second equation: "+v.q+" · "+v.x0+" − "+v.y0+" = "+C2+" ✓.")}''', '0 0 600 215')

m3 = M(('Сколько решений', 'How many solutions'),
 [('r', 'k', 'Наклон первой прямой', 'Slope of the first line', -3, 3, 1, 1), ('r', 'b1', 'Сдвиг первой прямой', 'Shift of the first line', -5, 5, 1, 1), ('r', 'b2', 'Сдвиг второй прямой', 'Shift of the second line', -5, 5, 1, 1), ('r', 'k2', 'Наклон второй прямой', 'Slope of the second line', -3, 3, 1, 1)],
 [('Первая прямая', 'First line'), ('Вторая прямая', 'Second line'), ('Вывод', 'Conclusion')],
 'Разные наклоны — одно решение. Равные наклоны и разный сдвиг — решений нет. Совпадающие прямые — бесконечно много решений.', 'Different slopes — one solution. Equal slopes and different shifts — no solution. Coinciding lines — infinitely many solutions.', ('Взаимное расположение прямых', 'The relative position of lines'),
 r'''const G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:220});const same=v.k===v.k2&&v.b1===v.b2,par=v.k===v.k2&&v.b1!==v.b2;
 let g=G.grid(2,2)+G.fn(t=>v.k*t+v.b1,COL.a,5)+G.fn(t=>v.k2*t+v.b2,COL.b,2.5,undefined,undefined,same);if(!par&&!same){const x=(v.b2-v.b1)/(v.k-v.k2);g+=G.pt(x,v.k*x+v.b1,COL.c,8)}
 return {svg:g,st:["y = "+v.k+"x + "+v.b1,"y = "+v.k2+"x + "+v.b2,same?U("бесконечно много решений","infinitely many solutions"):par?U("решений нет","no solutions"):U("одно решение","one solution")],fb:U("Сравните коэффициенты: наклон и сдвиг.","Compare the coefficients: slope and shift.")}''', '0 0 600 250')

chapter('28', '28-linear-systems.html', 'IV', ('Системы линейных уравнений', 'Systems of linear equations'),
 ('Как решить сразу два уравнения с двумя неизвестными: графиком, подстановкой и сложением.', 'How to solve two equations with two unknowns at once: by a graph, by substitution and by addition.'),
 ('В юрте-лавке продают войлочные коврики и шапки. 2 коврика и 1 шапка стоят 700 сомов, а 1 коврик и 1 шапка — 500 сомов.\n\nСколько стоит коврик и сколько шапка?', 'A felt-shop sells rugs and hats. 2 rugs and 1 hat cost 700 som, while 1 rug and 1 hat cost 500 som.\n\nHow much does a rug cost and how much a hat?'),
 ('Разгадка: коврик 200, шапка 300', 'The answer: rug 200, hat 300'),
 ('Пусть коврик x, шапка y: 2x + y = 700 и x + y = 500. Вычтем второе из первого: x = 200. Тогда y = 500 − 200 = 300. Проверка: 2 · 200 + 300 = 700 ✓. Два условия определяют две неизвестные — вместе они дают одну пару чисел.', 'Let a rug be x and a hat y: 2x + y = 700 and x + y = 500. Subtract the second from the first: x = 200. Then y = 500 − 200 = 300. Check: 2 · 200 + 300 = 700 ✓. Two conditions determine two unknowns — together they give one pair of numbers.'),
 [S('graph', 'Графический способ', 'The graphical method', ('Уравнение ax + by = c задаёт на плоскости прямую. Решение системы двух уравнений — общая точка двух прямых. Три случая: прямые пересекаются (одно решение), параллельны (решений нет), совпадают (бесконечно много).', 'An equation ax + by = c defines a line on the plane. The solution of a system of two equations is the common point of two lines. Three cases: the lines intersect (one solution), are parallel (no solution), or coincide (infinitely many).'),
    ('ax + by = c', '', 'ax + by = c'), m1),
  S('add', 'Подстановка и сложение', 'Substitution and addition', ('<strong>Подстановка</strong>: выражаем одно неизвестное из одного уравнения и подставляем в другое. <strong>Сложение</strong>: умножаем уравнения так, чтобы при сложении или вычитании одно неизвестное исчезло. Затем находим второе неизвестное и обязательно проверяем пару в обоих уравнениях.', '<strong>Substitution</strong>: express one unknown from one equation and substitute into the other. <strong>Addition</strong>: multiply the equations so that one unknown vanishes on adding or subtracting. Then find the second unknown and always check the pair in both equations.'),
    ('x + y = 500,  2x + y = 700', 'x = 200,  y = 300', 'x = 200,  y = 300'), m2),
  S('cases', 'Сколько решений', 'How many solutions', ('Прямые y = k₁x + b₁ и y = k₂x + b₂: при k₁ ≠ k₂ — одна точка пересечения; при k₁ = k₂ и b₁ ≠ b₂ — параллельны, решений нет; при k₁ = k₂ и b₁ = b₂ — одна и та же прямая. Системы без решений называют <em>несовместными</em>.', 'Lines y = k₁x + b₁ and y = k₂x + b₂: if k₁ ≠ k₂ — one intersection point; if k₁ = k₂ and b₁ ≠ b₂ — parallel, no solutions; if k₁ = k₂ and b₁ = b₂ — the same line. Systems without solutions are called <em>inconsistent</em>.'),
    ('k₁ ≠ k₂ — одно решение', '', 'k₁ ≠ k₂ — one solution'), m3)],
 [TK(('Сложение', 'Addition'), ('Решите: x + y = 10, x − y = 2.', 'Solve: x + y = 10, x − y = 2.'), '', 'Складываем: 2x = 12, x = 6; y = 4.', '(6; 4).'),
  TK(('Подстановка', 'Substitution'), ('Решите: y = 2x, x + y = 9.', 'Solve: y = 2x, x + y = 9.'), '', 'x + 2x = 9, x = 3, y = 6.', '(3; 6).'),
  TK(('Умножение уравнения', 'Multiplying an equation'), ('Решите: 2x + 3y = 13, x + y = 5.', 'Solve: 2x + 3y = 13, x + y = 5.'), '2·(x + y) = 10', 'Вычтем: (2x + 3y) − (2x + 2y) = 13 − 10, y = 3, x = 2.', '(2; 3).'),
  TK(('Задача', 'A problem'), ('Сумма двух чисел 35, а разность 9. Найдите числа.', 'The sum of two numbers is 35 and the difference is 9. Find the numbers.'), 'x + y = 35, x − y = 9', '2x = 44, x = 22, y = 13.', '22 и 13.'),
  TK(('Нет решений', 'No solutions'), ('Сколько решений у системы x + y = 3, x + y = 5?', 'How many solutions has the system x + y = 3, x + y = 5?'), '', 'Одно и то же выражение равно и 3, и 5 — так не бывает.', ('Нет решений.', 'No solutions.'))],
 [Q('Решение системы — это', 'The solution of a system is', ('пара чисел, удовлетворяющая обоим уравнениям', 'a pair of numbers satisfying both equations'), ('любое число', 'any number'), ('сумма уравнений', 'the sum of the equations'), ('Обоим сразу.', 'Both at once.')),
  Q('x + y = 7, x − y = 1. x =', 'x + y = 7, x − y = 1. x =', '4', '3', '6', ('2x = 8.', '2x = 8.')),
  Q('Прямые параллельны, значит', 'The lines are parallel, so', ('решений нет', 'no solutions'), ('одно решение', 'one solution'), ('бесконечно много', 'infinitely many'), ('Общих точек нет.', 'No common points.')),
  Q('Совпадающие прямые дают', 'Coinciding lines give', ('бесконечно много решений', 'infinitely many solutions'), ('одно', 'one'), ('ни одного', 'none'), ('Все точки общие.', 'All points are common.')),
  Q('Решение y = x, x + y = 8', 'The solution of y = x, x + y = 8', '(4; 4)', '(8; 0)', '(2; 6)', ('2x = 8.', '2x = 8.')),
  Q('Что обязательно делать в конце?', 'What must be done at the end?', ('проверить пару в обоих уравнениях', 'check the pair in both equations'), ('удвоить ответ', 'double the answer'), ('ничего', 'nothing'), ('Проверка — гарантия.', 'The check is a guarantee.')),
  Q('Коэффициенты при y противоположны. Лучше', 'The coefficients of y are opposites. Better to', ('сложить уравнения', 'add the equations'), ('вычесть уравнения', 'subtract the equations'), ('поделить', 'divide'), ('y исчезнет.', 'y vanishes.')),
  Q('Сколько решений у x + y = 1, 2x + 2y = 2?', 'How many solutions has x + y = 1, 2x + 2y = 2?', ('бесконечно много', 'infinitely many'), ('ни одного', 'none'), ('одно', 'one'), ('Второе уравнение — удвоенное первое.', 'The second is double the first.'))],
 src=[('Wikipedia: System of linear equations', 'https://en.wikipedia.org/wiki/System_of_linear_equations'), ('OpenStax: Elementary Algebra 2e', 'https://openstax.org/details/books/elementary-algebra-2e')],
 note=('Цены и сюжет про лавку придуманы для атласа.', 'The prices and the shop story are invented for the atlas.'))
