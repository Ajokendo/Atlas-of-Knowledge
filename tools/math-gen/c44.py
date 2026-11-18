# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Сокращение дроби: «дырка» в графике', 'Simplifying: a “hole” in the graph'),
 [('r', 'a', 'Число a', 'Number a', -5, 5, 1, 2)],
 [('Исходная дробь', 'The original fraction'), ('После сокращения', 'After simplifying'), ('Исключённое значение', 'Excluded value')],
 'Дробь (x² − a²)/(x − a) после сокращения превращается в x + a, но при x = a исходная дробь не определена — на графике «выколотая точка».', 'The fraction (x² − a²)/(x − a) becomes x + a after simplifying, but the original has no value at x = a — a “hole” on the graph.', ('График дроби и упрощённой функции', 'The graph of the fraction and of the simplified function'),
 r'''const a=v.a,G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:210});let g=G.grid(2,2)+G.fn(x=>Math.abs(x-a)<1e-9?NaN:(x*x-a*a)/(x-a),COL.a,3.5)+'<circle cx="'+G.X(a)+'" cy="'+G.Y(2*a)+'" r="6" fill="#fff" stroke="'+COL.a+'" stroke-width="2.5"/>';
 return {svg:g,st:["(x² − "+a*a+")/(x "+(a<0?"+ "+(-a):"− "+a)+")","x "+(a<0?"− "+(-a):"+ "+a),"x ≠ "+a],fb:U("Сокращать можно только на множитель, не равный нулю: x − "+a+" ≠ 0.","We may cancel only a factor that is not zero: x − "+a+" ≠ 0.")}''', '0 0 600 250')

m2 = M(('Сложение дробей с x', 'Adding fractions with x'),
 [('r', 'd', 'Сдвиг d', 'Shift d', 1, 5, 1, 2), ('r', 'x', 'x для проверки', 'x for the check', 1, 12, 1, 4)],
 [('1/x + 1/(x + d)', '1/x + 1/(x + d)'), ('Общий знаменатель', 'Common denominator'), ('Проверка при выбранном x', 'Check at the chosen x')],
 'Как и с числами: приводим к общему знаменателю x(x + d), складываем числители, при необходимости сокращаем.', 'As with numbers: bring to the common denominator x(x + d), add the numerators, simplify if possible.', ('Две величины 1/x и 1/(x + d)', 'Two quantities 1/x and 1/(x + d)'),
 r'''const x=v.x,d=v.d,A=1/x,B=1/(x+d),S0=A+B,F=(2*x+d)/(x*(x+d)),G=Gr({x0:0,x1:12,y0:0,y1:1.2,L:80,T:10,W:460,H:210});let g=G.grid(2,0.2)+G.fn(t=>1/t,COL.a,2.5,0.3,12)+G.fn(t=>1/(t+d),COL.b,2.5,0,12)+G.fn(t=>(2*t+d)/(t*(t+d)),COL.c,3.5,0.3,12)+G.pt(x,S0,COL.c,7);
 return {svg:g,st:["(2x + "+d+")/(x² + "+d+"x)","x(x + "+d+")",fnum(A,4)+" + "+fnum(B,4)+" = "+fnum(S0,4)+" = "+fnum(F,4)],fb:U("Складываем числители над общим знаменателем: x + (x + "+d+") = 2x + "+d+".","We add the numerators over the common denominator: x + (x + "+d+") = 2x + "+d+".")}''', '0 0 600 250')

m3 = M(('Дробное уравнение и посторонний корень', 'A fractional equation and an extraneous root'),
 [('r', 'm', 'Правая часть m', 'Right-hand side m', -2, 8, 1, 4)],
 [('Уравнение', 'The equation'), ('Решение после сокращения', 'Solution after simplifying'), ('Проверка по знаменателю', 'Denominator check')],
 'Решая дробное уравнение, обязательно проверяйте: корень, при котором знаменатель обращается в нуль, — посторонний.', 'When solving a fractional equation always check: a root making the denominator zero is extraneous.', ('Уравнение (x² − 4)/(x − 2) = m на графике', 'The equation (x² − 4)/(x − 2) = m on a graph'),
 r'''const G=Gr({x0:-6,x1:6,y0:-6,y1:10,L:100,T:10,W:400,H:210});let g=G.grid(2,2)+G.fn(x=>Math.abs(x-2)<1e-9?NaN:(x*x-4)/(x-2),COL.a,3.5)+'<circle cx="'+G.X(2)+'" cy="'+G.Y(4)+'" r="6" fill="#fff" stroke="'+COL.a+'" stroke-width="2.5"/>'+G.fn(x=>v.m,COL.b,2,-6,6,true);const x=v.m-2,bad=Math.abs(x-2)<1e-9;if(!bad)g+=G.pt(x,v.m,COL.c,7);
 return {svg:g,st:["(x² − 4)/(x − 2) = "+v.m,"x + 2 = "+v.m+" → x = "+x,bad?U("x = 2 — посторонний корень","x = 2 — an extraneous root"):U("x ≠ 2 — подходит","x ≠ 2 — valid")],fb:bad?U("Решений нет: единственный кандидат x = 2 обращает знаменатель в нуль.","No solutions: the only candidate x = 2 makes the denominator zero."):U("Корень x = "+x+" проверен.","The root x = "+x+" is checked.")}''', '0 0 600 250')

chapter('44', '44-rational-expressions.html', 'VI', ('Дробно-рациональные выражения', 'Rational expressions'),
 ('Алгебраические дроби: как сокращать, складывать и решать дробные уравнения без ошибок.', 'Algebraic fractions: how to simplify, add and solve fractional equations without errors.'),
 ('Два крана наполняют бассейн: первый за x часов, второй на 2 часа дольше. Вместе они наполняют его за 3 часа.\n\nСоставьте уравнение. Что в нём необычного?', 'Two taps fill a pool: the first in x hours, the second 2 hours longer. Together they fill it in 3 hours.\n\nWrite an equation. What is unusual about it?'),
 ('Разгадка: 1/x + 1/(x + 2) = 1/3', 'The answer: 1/x + 1/(x + 2) = 1/3'),
 ('Производительности складываются: 1/x + 1/(x + 2) = 1/3. Это дробное уравнение: неизвестное стоит в знаменателе. Умножим на 3x(x + 2): 3(x + 2) + 3x = x(x + 2), то есть x² − 4x − 6 = 0. Корни 2 ± √10: положительный x ≈ 5,16 ч подходит, отрицательный — нет. Дробные уравнения требуют двух проверок: знаменатель не нуль и корень имеет смысл.', 'The rates add: 1/x + 1/(x + 2) = 1/3. This is a fractional equation: the unknown is in the denominator. Multiplying by 3x(x + 2): 3(x + 2) + 3x = x(x + 2), i.e. x² − 4x − 6 = 0. The roots are 2 ± √10: the positive x ≈ 5.16 h fits, the negative one does not. Fractional equations need two checks: the denominator is not zero and the root makes sense.'),
 [S('simp', 'Сокращение дробей', 'Simplifying fractions', ('<strong>Алгебраическая дробь</strong> — отношение многочленов. Чтобы сократить, числитель и знаменатель раскладывают на множители и делят на общий: (x² − 9)/(x − 3) = (x − 3)(x + 3)/(x − 3) = x + 3, где x ≠ 3. <strong>Допустимые значения</strong> — те, при которых знаменатель не нуль.', 'An <strong>algebraic fraction</strong> is a ratio of polynomials. To simplify we factorise numerator and denominator and divide out the common factor: (x² − 9)/(x − 3) = (x − 3)(x + 3)/(x − 3) = x + 3, where x ≠ 3. The <strong>admissible values</strong> are those where the denominator is not zero.'),
    ('(x² − a²)/(x − a) = x + a  (x ≠ a)', '', '(x² − a²)/(x − a) = x + a  (x ≠ a)'), m1),
  S('ops', 'Действия с дробями', 'Operations on fractions', ('Правила те же, что для обыкновенных: сложение — общий знаменатель; умножение — числитель на числитель, знаменатель на знаменатель; деление — умножение на обратную. Общий знаменатель берут минимальный: произведение разных множителей в наибольших степенях.', 'The rules are the same as for common fractions: addition — a common denominator; multiplication — numerator by numerator, denominator by denominator; division — multiplication by the reciprocal. The common denominator is the least: the product of different factors to their highest powers.'),
    ('a/b + c/d = (ad + bc)/(bd)', '', 'a/b + c/d = (ad + bc)/(bd)'), m2),
  S('eq', 'Дробные уравнения', 'Fractional equations', ('План: 1) найти допустимые значения; 2) умножить обе части на общий знаменатель; 3) решить получившееся уравнение; 4) отбросить корни, не входящие в допустимые значения. Корень, обращающий знаменатель в нуль, называют <strong>посторонним</strong>.', 'The plan: 1) find the admissible values; 2) multiply both sides by the common denominator; 3) solve the resulting equation; 4) discard roots outside the admissible values. A root that makes a denominator zero is called <strong>extraneous</strong>.'),
    ('знаменатель ≠ 0', '', 'denominator ≠ 0'), m3)],
 [TK(('Сократить', 'Simplify'), ('Сократите (x² − 16)/(x + 4).', 'Simplify (x² − 16)/(x + 4).'), '(x − 4)(x + 4)', 'x − 4, где x ≠ −4.', 'x − 4.'),
  TK(('Сложить', 'Add'), ('Найдите 1/x + 2/x².', 'Find 1/x + 2/x².'), 'Общий знаменатель x²', '(x + 2)/x².', '(x + 2)/x².'),
  TK(('Умножить', 'Multiply'), ('Найдите (x/2) · (6/x²).', 'Find (x/2) · (6/x²).'), '', '6x/(2x²) = 3/x.', '3/x.'),
  TK(('Уравнение', 'Equation'), ('Решите 6/x = 3.', 'Solve 6/x = 3.'), 'x ≠ 0', '6 = 3x, x = 2.', 'x = 2.'),
  TK(('Посторонний корень', 'Extraneous root'), ('Решите (x² − 9)/(x − 3) = 0.', 'Solve (x² − 9)/(x − 3) = 0.'), 'x ≠ 3', 'x² − 9 = 0: x = ±3. x = 3 запрещён, остаётся x = −3.', ('x = −3.', 'x = −3.'))],
 [Q('При каком x не определена 1/(x − 5)?', 'For which x is 1/(x − 5) undefined?', '5', '0', '−5', ('Знаменатель нуль.', 'The denominator is zero.')),
  Q('(x² − 1)/(x − 1) =', '(x² − 1)/(x − 1) =', 'x + 1', 'x − 1', 'x', ('Разность квадратов.', 'Difference of squares.')),
  Q('1/2 + 1/x =', '1/2 + 1/x =', '(x + 2)/(2x)', '2/(x + 2)', '1/(2 + x)', ('Общий знаменатель 2x.', 'Common denominator 2x.')),
  Q('Делить на дробь значит', 'Dividing by a fraction means', ('умножать на обратную', 'multiplying by the reciprocal'), ('складывать', 'adding'), ('вычитать', 'subtracting'), ('Правило.', 'The rule.')),
  Q('Посторонний корень — это', 'An extraneous root is one that', ('обращает знаменатель в нуль', 'makes a denominator zero'), ('равен нулю', 'is zero'), ('отрицательный', 'is negative'), ('Не входит в допустимые значения.', 'It is not among the admissible values.')),
  Q('2/x = 4. x =', '2/x = 4. x =', '1/2', '2', '8', ('2 = 4x.', '2 = 4x.')),
  Q('Сокращать дробь можно на', 'We may divide out a', ('общий множитель', 'common factor'), ('общее слагаемое', 'common term'), ('любое число', 'any number'), ('Слагаемые сокращать нельзя.', 'Terms cannot be cancelled.')),
  Q('x/x при x ≠ 0 равно', 'x/x for x ≠ 0 equals', '1', '0', 'x', ('Любое число, делённое на себя.', 'Any number divided by itself.'))],
 src=[('Wikipedia: Rational function', 'https://en.wikipedia.org/wiki/Rational_function'), ('Wikipedia: Extraneous and missing solutions', 'https://en.wikipedia.org/wiki/Extraneous_and_missing_solutions')],
 note=('Бассейн и краны — условный пример.', 'The pool and taps are an illustrative example.'))
