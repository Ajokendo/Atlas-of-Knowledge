# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Производная степени', 'Derivative of a power'),
 [('r', 'n', 'Показатель n', 'Exponent n', -2, 5, 1, 3), ('r', 'x', 'Точка x', 'Point x', 0.5, 2.5, 0.1, 1.5)],
 [('f(x) = xⁿ', 'f(x) = xⁿ'), ('f′(x) = n·xⁿ⁻¹', 'f′(x) = n·xⁿ⁻¹'), ('Численная проверка', 'Numerical check')],
 'Правило степени: (xⁿ)′ = n·xⁿ⁻¹. Проверка: наклон секущей на очень малом интервале почти равен значению по формуле.', 'The power rule: (xⁿ)′ = n·xⁿ⁻¹. A check: the slope of a secant on a very small interval almost equals the formula value.', ('График xⁿ и касательная', 'The graph of xⁿ and the tangent'),
 r'''const F=t=>Math.pow(t,v.n),k=v.n*Math.pow(v.x,v.n-1),h=1e-5,num=(F(v.x+h)-F(v.x))/h;const G=Gr({x0:0,x1:3,y0:-1,y1:10,L:80,T:10,W:470,H:210});let g=G.grid(0.5,2)+G.fn(F,COL.a,3.5,0.05,3)+G.fn(t=>F(v.x)+k*(t-v.x),COL.b,2.5,0,3)+G.pt(v.x,F(v.x),COL.c,7);
 return {svg:g,st:[fnum(F(v.x),4),fnum(k,4),fnum(num,4)],fb:U("Показатель «спускается» вперёд, а в степени остаётся на единицу меньше.","The exponent comes down in front and the power drops by one.")}''', '0 0 600 250')

m2 = M(('Сумма и произведение', 'Sum and product'),
 [('r', 'x', 'Точка x', 'Point x', 0.2, 3, 0.1, 1)],
 [('f·g с f = x², g = sin x', 'f·g with f = x², g = sin x'), ('По правилу f′g + fg′', 'By the rule f′g + fg′'), ('Ошибочно f′·g′', 'Wrong f′·g′')],
 'Производная произведения — не произведение производных: (fg)′ = f′g + fg′. Сравните с численной проверкой.', 'The derivative of a product is not the product of derivatives: (fg)′ = f′g + fg′. Compare with the numerical check.', ('Верная и неверная формулы', 'The right and the wrong formula'),
 r'''const f=x=>x*x,g0=Math.sin,P=t=>f(t)*g0(t),good=t=>2*t*g0(t)+f(t)*Math.cos(t),bad=t=>2*t*Math.cos(t);const h=1e-5,num=(P(v.x+h)-P(v.x))/h;const G=Gr({x0:0,x1:3,y0:-6,y1:8,L:80,T:10,W:470,H:210});let g=G.grid(0.5,2)+G.fn(good,COL.a,3.5,0,3)+G.fn(bad,COL.c,2.5,0,3,true)+G.pt(v.x,num,COL.b,8);
 return {svg:g,st:[fnum(num,4),fnum(good(v.x),4),fnum(bad(v.x),4)],fb:U("Точка (численная производная) лежит на сплошной кривой — формуле f′g + fg′.","The point (numerical derivative) lies on the solid curve — the formula f′g + fg′.")}''', '0 0 600 250')

m3 = M(('Сложная функция', 'The chain rule'),
 [('r', 'k', 'Коэффициент k', 'Coefficient k', 1, 5, 1, 2), ('r', 'x', 'Точка x', 'Point x', 0, 3, 0.1, 1)],
 [('f(x) = sin(kx)', 'f(x) = sin(kx)'), ('f′(x) = k·cos(kx)', 'f′(x) = k·cos(kx)'), ('Численно', 'Numerically')],
 'Для функции внутри функции: (f(g(x)))′ = f′(g(x))·g′(x). У sin(kx) внутренняя функция kx, её производная k — множитель.', 'For a function inside a function: (f(g(x)))′ = f′(g(x))·g′(x). For sin(kx) the inner function is kx with derivative k — the factor.', ('Чем больше k, тем круче волна', 'The larger k, the steeper the wave'),
 r'''const F=t=>Math.sin(v.k*t),D=t=>v.k*Math.cos(v.k*t),h=1e-6,num=(F(v.x+h)-F(v.x))/h;const G=Gr({x0:0,x1:3,y0:-5.5,y1:5.5,L:80,T:10,W:470,H:210});let g=G.grid(0.5,1)+G.fn(F,COL.a,3.5,0,3)+G.fn(D,COL.b,2.5,0,3,true)+G.pt(v.x,F(v.x),COL.a,7)+G.pt(v.x,D(v.x),COL.b,7);
 return {svg:g,st:[fnum(F(v.x),4),fnum(D(v.x),4),fnum(num,4)],fb:U("Множитель k — производная внутренней функции: он делает наклон в k раз больше.","The factor k is the derivative of the inner function: it makes the slope k times larger.")}''', '0 0 600 250')

chapter('58', '58-diff-rules.html', 'VIII', ('Правила дифференцирования', 'Differentiation rules'),
 ('Готовые правила, чтобы не считать предел каждый раз: степень, сумма, произведение, частное, сложная функция.', 'Ready-made rules so that we do not compute a limit each time: power, sum, product, quotient, composite function.'),
 ('Если f(x) = x² и g(x) = sin x, то производная f равна 2x, а производная g равна cos x. Чему равна производная произведения x²·sin x — просто 2x·cos x?', 'If f(x) = x² and g(x) = sin x then f′ = 2x and g′ = cos x. Is the derivative of the product x²·sin x simply 2x·cos x?'),
 ('Разгадка: нет, 2x·sin x + x²·cos x', 'The answer: no, 2x·sin x + x²·cos x'),
 ('Производная произведения не равна произведению производных. Верное правило: (fg)′ = f′g + fg′ — каждый множитель по очереди «дифференцируется», а другой остаётся. Для x²·sin x получаем 2x·sin x + x²·cos x. Это легко проверить на числах: в модели видно, что точка численного наклона лежит на правильной кривой, а не на «наивной».', 'The derivative of a product is not the product of derivatives. The right rule is (fg)′ = f′g + fg′ — each factor is differentiated in turn while the other stays. For x²·sin x we get 2x·sin x + x²·cos x. It is easy to check with numbers: in the model the point of the numerical slope lies on the right curve, not on the “naive” one.'),
 [S('pow', 'Степень, константа, сумма', 'Power, constant, sum', ('<strong>(xⁿ)′ = n·xⁿ⁻¹</strong>; (C)′ = 0; (C·f)′ = C·f′; (f + g)′ = f′ + g′. Например, (3x⁴ − 5x + 7)′ = 12x³ − 5. Корень и дробь приводят к степени: √x = x^(1/2), (√x)′ = 1/(2√x); (1/x)′ = −1/x².', '<strong>(xⁿ)′ = n·xⁿ⁻¹</strong>; (C)′ = 0; (C·f)′ = C·f′; (f + g)′ = f′ + g′. For example (3x⁴ − 5x + 7)′ = 12x³ − 5. A root and a fraction reduce to a power: √x = x^(1/2), (√x)′ = 1/(2√x); (1/x)′ = −1/x².'),
    ('(xⁿ)′ = n·xⁿ⁻¹', '', '(xⁿ)′ = n·xⁿ⁻¹'), m1),
  S('prod', 'Произведение и частное', 'Product and quotient', ('<strong>(fg)′ = f′g + fg′</strong>; <strong>(f/g)′ = (f′g − fg′) / g²</strong>. Также запомните таблицу: (sin x)′ = cos x, (cos x)′ = −sin x, (eˣ)′ = eˣ, (ln x)′ = 1/x, (aˣ)′ = aˣ ln a.', '<strong>(fg)′ = f′g + fg′</strong>; <strong>(f/g)′ = (f′g − fg′) / g²</strong>. Also remember the table: (sin x)′ = cos x, (cos x)′ = −sin x, (eˣ)′ = eˣ, (ln x)′ = 1/x, (aˣ)′ = aˣ ln a.'),
    ('(fg)′ = f′g + fg′', '', '(fg)′ = f′g + fg′'), m2),
  S('chain', 'Сложная функция', 'The chain rule', ('<strong>(f(g(x)))′ = f′(g(x)) · g′(x)</strong>: производная внешней функции в точке g(x), умноженная на производную внутренней. Примеры: (sin 3x)′ = 3 cos 3x; ((2x + 1)⁵)′ = 5(2x + 1)⁴ · 2; (e^(x²))′ = 2x · e^(x²).', '<strong>(f(g(x)))′ = f′(g(x)) · g′(x)</strong>: the derivative of the outer function at g(x) times the derivative of the inner one. Examples: (sin 3x)′ = 3 cos 3x; ((2x + 1)⁵)′ = 5(2x + 1)⁴ · 2; (e^(x²))′ = 2x · e^(x²).'),
    ('(f(g(x)))′ = f′(g(x))·g′(x)', '', '(f(g(x)))′ = f′(g(x))·g′(x)'), m3)],
 [TK(('Многочлен', 'Polynomial'), ('Найдите (3x⁴ − 5x + 7)′.', 'Find (3x⁴ − 5x + 7)′.'), '', '12x³ − 5.', '12x³ − 5.'),
  TK(('Корень', 'Root'), ('Найдите (√x)′ при x = 4.', 'Find (√x)′ at x = 4.'), '√x = x^(1/2)', '1/(2√x) = 1/4.', '1/4.'),
  TK(('Произведение', 'Product'), ('Найдите (x·eˣ)′.', 'Find (x·eˣ)′.'), '', 'eˣ + x·eˣ = (1 + x)eˣ.', '(1 + x)eˣ.'),
  TK(('Частное', 'Quotient'), ('Найдите (x/(x + 1))′.', 'Find (x/(x + 1))′.'), '', '((x + 1) − x)/(x + 1)² = 1/(x + 1)².', '1/(x + 1)².'),
  TK(('Сложная', 'Composite'), ('Найдите ((2x + 1)⁵)′ при x = 0.', 'Find ((2x + 1)⁵)′ at x = 0.'), '', '5(2x + 1)⁴ · 2 = 10 при x = 0.', '10.')],
 [Q('(x⁵)′ =', '(x⁵)′ =', '5x⁴', 'x⁴', '5x⁵', ('Правило степени.', 'The power rule.')),
  Q('(7)′ =', '(7)′ =', '0', '7', '1', ('Производная константы.', 'The derivative of a constant.')),
  Q('(fg)′ =', '(fg)′ =', 'f′g + fg′', 'f′g′', 'f′ + g′', ('Правило произведения.', 'The product rule.')),
  Q('(sin x)′ =', '(sin x)′ =', 'cos x', '−cos x', 'sin x', ('Таблица.', 'The table.')),
  Q('(eˣ)′ =', '(eˣ)′ =', 'eˣ', 'x·eˣ⁻¹', '1', ('Особое свойство e.', 'The special property of e.')),
  Q('(sin 2x)′ =', '(sin 2x)′ =', '2 cos 2x', 'cos 2x', '2 sin 2x', ('Множитель внутренней функции.', 'The factor of the inner function.')),
  Q('(1/x)′ =', '(1/x)′ =', '−1/x²', '1/x²', 'ln x', ('(x⁻¹)′.', '(x⁻¹)′.')),
  Q('(ln x)′ =', '(ln x)′ =', '1/x', 'x', 'eˣ', ('Таблица.', 'The table.'))],
 src=[('Wikipedia: Differentiation rules', 'https://en.wikipedia.org/wiki/Differentiation_rules'), ('Wikipedia: Chain rule', 'https://en.wikipedia.org/wiki/Chain_rule'), ('OpenStax: Calculus Volume 1', 'https://openstax.org/details/books/calculus-volume-1')])
