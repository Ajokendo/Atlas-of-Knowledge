# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Площадь прямоугольниками', 'Area by rectangles'),
 [('r', 'n', 'Число прямоугольников', 'Number of rectangles', 1, 60, 1, 6)],
 [('Сумма прямоугольников', 'Rectangle sum'), ('Точная площадь', 'Exact area'), ('Ошибка', 'Error')],
 'Площадь под графиком f(x) = x² на [0; 3] приближают суммой узких прямоугольников. Чем их больше, тем точнее; предел суммы — определённый интеграл.', 'The area under f(x) = x² on [0; 3] is approximated by a sum of thin rectangles. The more of them, the better; the limit of the sum is the definite integral.', ('Приближение площади', 'Approximating an area'),
 r'''const f=x=>x*x,n=v.n,w=3/n;const G=Gr({x0:0,x1:3.2,y0:0,y1:10,L:80,T:10,W:470,H:210});let g=G.grid(0.5,2),s=0;for(let i=0;i<n;i++){const xm=(i+0.5)*w,h=f(xm);s+=h*w;g+=R(G.X(i*w),G.Y(h),G.X(w)-G.X(0),G.Y(0)-G.Y(h),COL.a,COL.bg,0.5,0)}g+=G.fn(f,COL.ink,3,0,3);
 return {svg:g,st:[fnum(s,4),"9",fnum(Math.abs(9-s),4)],fb:U("Ошибка быстро падает при росте числа прямоугольников.","The error drops quickly as the number of rectangles grows.")}''', '0 0 600 250')

m2 = M(('Формула Ньютона — Лейбница', 'The Newton–Leibniz formula'),
 [('r', 'a', 'Нижний предел a', 'Lower limit a', 0, 3, 0.5, 0.5), ('r', 'b', 'Верхний предел b', 'Upper limit b', 0.5, 4, 0.5, 2.5)],
 [('F(b) − F(a)', 'F(b) − F(a)'), ('Площадь прямоугольниками (500)', 'Area by 500 rectangles'), ('Формула', 'Formula')],
 'Для f(x) = x² первообразная F(x) = x³/3. Определённый интеграл ∫ₐᵇ f dx = F(b) − F(a) — площадь под графиком между a и b, без суммирования.', 'For f(x) = x² the antiderivative is F(x) = x³/3. The definite integral ∫ₐᵇ f dx = F(b) − F(a) is the area under the graph between a and b, without summation.', ('Заштрихованная площадь', 'The shaded area'),
 r'''const a=Math.min(v.a,v.b),b=Math.max(v.a,v.b),f=x=>x*x,F=x=>x*x*x/3;const G=Gr({x0:0,x1:4,y0:0,y1:16,L:80,T:10,W:470,H:210});let g=G.grid(1,4),N=500,s=0,w=(b-a)/N;for(let i=0;i<N;i++){const x=a+(i+0.5)*w;s+=f(x)*w}
 const pts=[[a,0]];for(let i=0;i<=40;i++){const x=a+(b-a)*i/40;pts.push([x,f(x)])}pts.push([b,0]);g+='<polygon points="'+pts.map(p=>G.X(p[0])+","+G.Y(p[1])).join(" ")+'" fill="'+COL.a+'" opacity="0.45"/>'+G.fn(f,COL.ink,3,0,4);
 return {svg:g,st:[fnum(F(b)-F(a),4),fnum(s,4),"["+fnum(b,1)+"³ − "+fnum(a,1)+"³]/3"],fb:U("Площадь, найденная суммой прямоугольников, совпадает с F(b) − F(a).","The area found by summing rectangles equals F(b) − F(a).")}''', '0 0 600 250')

m3 = M(('Площадь между кривыми', 'Area between curves'),
 [('r', 'k', 'Коэффициент k у прямой y = kx', 'Slope k of the line y = kx', 1, 4, 0.5, 2)],
 [('Точки пересечения', 'Intersections'), ('Интеграл разности', 'Integral of the difference'), ('Формула', 'Formula')],
 'Площадь фигуры между параболой y = x² и прямой y = kx — интеграл от верхней функции минус нижней: ∫₀ᵏ (kx − x²) dx = k³/6.', 'The area of the figure between the parabola y = x² and the line y = kx is the integral of the upper function minus the lower: ∫₀ᵏ (kx − x²) dx = k³/6.', ('Область между параболой и прямой', 'The region between a parabola and a line'),
 r'''const G=Gr({x0:-0.5,x1:4.5,y0:-1,y1:17,L:80,T:10,W:470,H:210});let g=G.grid(1,4);const pts=[];for(let i=0;i<=40;i++){const x=v.k*i/40;pts.push([x,v.k*x])}for(let i=40;i>=0;i--){const x=v.k*i/40;pts.push([x,x*x])}
 g+='<polygon points="'+pts.map(p=>G.X(p[0])+","+G.Y(p[1])).join(" ")+'" fill="'+COL.a+'" opacity="0.45"/>'+G.fn(x=>x*x,COL.ink,3,-0.5,4.5)+G.fn(x=>v.k*x,COL.b,3,-0.5,4.5);
 return {svg:g,st:["x = 0 и x = "+v.k,fnum(Math.pow(v.k,3)/6,4),"k³/6"],fb:U("Верхняя функция минус нижняя: kx − x² ≥ 0 на [0; k].","Upper function minus lower: kx − x² ≥ 0 on [0; k].")}''', '0 0 600 250')

chapter('61', '61-definite-integral.html', 'VIII', ('Определённый интеграл', 'The definite integral'),
 ('Площадь под графиком как предел суммы и формула Ньютона — Лейбница.', 'The area under a graph as the limit of a sum and the Newton–Leibniz formula.'),
 ('Как найти площадь участка с криволинейной границей, если у вас только линейка и формулы для прямоугольников?', 'How can we find the area of a plot with a curved boundary if we have only a ruler and formulas for rectangles?'),
 ('Разгадка: нарезать на узкие полоски', 'The answer: cut into thin strips'),
 ('Нарежем участок на узкие вертикальные полоски и каждую заменим прямоугольником. Чем уже полоски, тем меньше ошибка; предел суммы их площадей и есть площадь участка — определённый интеграл. Удивительный факт: считать суммы не нужно — достаточно первообразной, потому что площадь = F(b) − F(a). Так связаны два мира: накопление (интеграл) и скорость изменения (производная).', 'Cut the plot into thin vertical strips and replace each by a rectangle. The thinner the strips, the smaller the error; the limit of the sum of their areas is the area of the plot — the definite integral. A surprising fact: no sums need to be computed — an antiderivative is enough, because area = F(b) − F(a). This connects two worlds: accumulation (the integral) and the rate of change (the derivative).'),
 [S('sum', 'Интеграл как предел суммы', 'The integral as a limit of sums', ('Разобьём [a; b] на n частей шириной Δx и составим сумму f(xᵢ)·Δx. Предел этой суммы при n → ∞ — <strong>определённый интеграл ∫ₐᵇ f(x) dx</strong>. Для f ≥ 0 он равен площади под графиком. Для f &lt; 0 вклад отрицателен.', 'Split [a; b] into n parts of width Δx and form the sum f(xᵢ)·Δx. The limit of this sum as n → ∞ is the <strong>definite integral ∫ₐᵇ f(x) dx</strong>. For f ≥ 0 it equals the area under the graph. For f &lt; 0 the contribution is negative.'),
    ('∫ₐᵇ f dx = lim Σ f(xᵢ)Δx', '', '∫ₐᵇ f dx = lim Σ f(xᵢ)Δx'), m1),
  S('nl', 'Формула Ньютона — Лейбница', 'The Newton–Leibniz formula', ('Если F — первообразная f на [a; b], то <strong>∫ₐᵇ f(x) dx = F(b) − F(a)</strong>. Пример: ∫₀³ x² dx = 3³/3 − 0 = 9. Свойства: ∫ₐᵇ = −∫ᵦₐ; ∫ₐᵇ + ∫ᵦᶜ = ∫ₐᶜ; ∫ (f + g) = ∫ f + ∫ g.', 'If F is an antiderivative of f on [a; b] then <strong>∫ₐᵇ f(x) dx = F(b) − F(a)</strong>. Example: ∫₀³ x² dx = 3³/3 − 0 = 9. Properties: ∫ₐᵇ = −∫ᵦₐ; ∫ₐᵇ + ∫ᵦᶜ = ∫ₐᶜ; ∫ (f + g) = ∫ f + ∫ g.'),
    ('∫ₐᵇ f dx = F(b) − F(a)', '', '∫ₐᵇ f dx = F(b) − F(a)'), m2),
  S('app', 'Площади и приложения', 'Areas and applications', ('Площадь между кривыми: S = ∫ₐᵇ (верхняя − нижняя) dx. Интеграл скорости даёт пройденный путь, интеграл мощности — работу, интеграл плотности — массу. Если подынтегральная функция меняет знак, площадь считают по частям.', 'The area between curves: S = ∫ₐᵇ (upper − lower) dx. The integral of speed gives the distance travelled, of power the work, of density the mass. If the integrand changes sign the area is computed in pieces.'),
    ('S = ∫ (верх − низ) dx', '', 'S = ∫ (upper − lower) dx'), m3)],
 [TK(('Простой интеграл', 'A simple integral'), ('Вычислите ∫₀² 3x² dx.', 'Compute ∫₀² 3x² dx.'), 'F = x³', '8 − 0 = 8.', '8.'),
  TK(('Площадь', 'Area'), ('Площадь под y = x на [0; 4].', 'Area under y = x on [0; 4].'), 'F = x²/2', '16/2 = 8.', '8.'),
  TK(('Между кривыми', 'Between curves'), ('Площадь между y = x и y = x² на [0; 1].', 'Area between y = x and y = x² on [0; 1].'), '', '∫(x − x²)dx = 1/2 − 1/3 = 1/6.', '1/6.'),
  TK(('Путь', 'Distance'), ('v(t) = 2t м/с. Путь за первые 5 с.', 'v(t) = 2t m/s. Distance in the first 5 s.'), '', '∫₀⁵ 2t dt = 25 м.', '25 м.'),
  TK(('Знак', 'Sign'), ('Вычислите ∫₀^(2π) sin x dx.', 'Compute ∫₀^(2π) sin x dx.'), 'F = −cos x', '−cos 2π + cos 0 = 0: верхняя и нижняя половины сокращаются.', '0.')],
 [Q('∫ₐᵇ f dx = ', '∫ₐᵇ f dx = ', 'F(b) − F(a)', 'F(a) − F(b)', 'F(b) + F(a)', ('Ньютон — Лейбниц.', 'Newton–Leibniz.')),
  Q('∫₀³ x² dx =', '∫₀³ x² dx =', '9', '27', '3', ('27/3.', '27/3.')),
  Q('Для f ≥ 0 интеграл равен', 'For f ≥ 0 the integral equals', ('площади под графиком', 'the area under the graph'), ('наклону', 'the slope'), ('значению f(a)', 'the value f(a)'), ('Геометрический смысл.', 'The geometric meaning.')),
  Q('Интеграл скорости по времени даёт', 'The integral of speed over time gives', ('путь', 'distance'), ('ускорение', 'acceleration'), ('массу', 'mass'), ('Накопление.', 'Accumulation.')),
  Q('∫ₐᵃ f dx =', '∫ₐᵃ f dx =', '0', '1', 'f(a)', ('Нулевая ширина.', 'Zero width.')),
  Q('При перестановке пределов интеграл', 'When the limits are swapped the integral', ('меняет знак', 'changes sign'), ('не меняется', 'does not change'), ('удваивается', 'doubles'), ('∫ₐᵇ = −∫ᵦₐ.', '∫ₐᵇ = −∫ᵦₐ.')),
  Q('Площадь между кривыми — это интеграл', 'The area between curves is the integral of', ('верхняя − нижняя', 'upper − lower'), ('нижняя − верхняя', 'lower − upper'), ('сумма', 'the sum'), ('Должно быть неотрицательно.', 'It must be non-negative.')),
  Q('Предел сумм прямоугольников при n → ∞ — это', 'The limit of rectangle sums as n → ∞ is', ('определённый интеграл', 'the definite integral'), ('производная', 'the derivative'), ('константа C', 'the constant C'), ('Определение.', 'The definition.'))],
 src=[('Wikipedia: Integral', 'https://en.wikipedia.org/wiki/Integral'), ('Wikipedia: Fundamental theorem of calculus', 'https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus'), ('OpenStax: Calculus Volume 1', 'https://openstax.org/details/books/calculus-volume-1')])
