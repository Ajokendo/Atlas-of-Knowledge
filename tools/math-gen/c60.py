# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Восстанавливаем функцию по скорости', 'Recovering a function from its rate'),
 [('r', 'C', 'Постоянная C', 'Constant C', -3, 3, 0.5, 0)],
 [('F(x) = x² + C', 'F(x) = x² + C'), ('F′(x)', 'F′(x)'), ('Вывод', 'Conclusion')],
 'Первообразная F для f — функция, у которой F′ = f. Для f(x) = 2x подходит x², но и x² + 1, и x² − 3: все они отличаются на постоянную C.', 'An antiderivative F of f is a function with F′ = f. For f(x) = 2x the function x² works, and so do x² + 1 and x² − 3: they differ by a constant C.', ('Семейство первообразных', 'A family of antiderivatives'),
 r'''const G=Gr({x0:-3,x1:3,y0:-5,y1:12,L:80,T:10,W:470,H:210});let g=G.grid(1,2);for(const c of [-3,-2,-1,0,1,2,3])g+=G.fn(x=>x*x+c,COL.mut,1.5,-3,3);g+=G.fn(x=>x*x+v.C,COL.a,4,-3,3)+G.fn(x=>2*x,COL.b,2.5,-3,3,true);
 return {svg:g,st:["x² "+(v.C>=0?"+ ":"− ")+Math.abs(v.C),"2x",U("при любом C производная одна и та же","for any C the derivative is the same")],fb:U("Кривые сдвинуты вверх-вниз, но их наклон в каждом x одинаков.","The curves are shifted up and down but their slope at each x is the same.")}''', '0 0 600 250')

m2 = M(('Таблица первообразных', 'Table of antiderivatives'),
 [('s', 'f', 'Функция f', 'Function f', ['xⁿ (n = 3)', 'cos x', 'eˣ', '1/x'], ['xⁿ (n = 3)', 'cos x', 'eˣ', '1/x'], 0), ('r', 'x', 'Точка x', 'Point x', 0.5, 3, 0.1, 1.5)],
 [('f(x)', 'f(x)'), ('Первообразная F(x) (C = 0)', 'Antiderivative F(x) (C = 0)'), ('Проверка: F′ численно', 'Check: F′ numerically')],
 'Чтобы найти первообразную, обращают таблицу производных: если (x⁴/4)′ = x³, то первообразная x³ равна x⁴/4 + C.', 'To find an antiderivative we reverse the table of derivatives: if (x⁴/4)′ = x³ then the antiderivative of x³ is x⁴/4 + C.', ('f и её первообразная F', 'f and its antiderivative F'),
 r'''const f=[x=>x*x*x,Math.cos,Math.exp,x=>1/x][v.f],F=[x=>x**4/4,Math.sin,Math.exp,Math.log][v.f],nm=["x⁴/4","sin x","eˣ","ln x"][v.f];const G=Gr({x0:0.2,x1:3,y0:-2,y1:Math.max(10,F(3)),L:80,T:10,W:470,H:210});let g=G.grid(0.5,2)+G.fn(f,COL.a,3,0.2,3)+G.fn(F,COL.b,3.5,0.2,3)+G.pt(v.x,f(v.x),COL.a,6)+G.pt(v.x,F(v.x),COL.b,6);const h=1e-6,nd=(F(v.x+h)-F(v.x))/h;
 return {svg:g,st:[fnum(f(v.x),4),nm+" + C",fnum(nd,4)],fb:U("Численный наклон F совпадает со значением f — это и есть смысл первообразной.","The numerical slope of F equals the value of f — this is the meaning of an antiderivative.")}''', '0 0 600 250')

m3 = M(('Путь по скорости', 'Distance from speed'),
 [('r', 'a', 'Ускорение a, м/с²', 'Acceleration a, m/s²', 1, 5, 1, 2), ('r', 'v0', 'Начальная скорость, м/с', 'Initial speed, m/s', 0, 10, 1, 3), ('r', 't', 'Время t, с', 'Time t, s', 0, 6, 0.5, 4)],
 [('Скорость v(t) = v₀ + at', 'Speed v(t) = v₀ + at'), ('Путь s(t) = v₀t + at²/2', 'Distance s(t) = v₀t + at²/2'), ('Проверка s′ = v', 'Check s′ = v')],
 'Скорость — производная пути, значит путь — первообразная скорости: s = v₀t + at²/2 (при s(0) = 0). Так получают формулы равноускоренного движения.', 'Speed is the derivative of distance, so distance is an antiderivative of speed: s = v₀t + at²/2 (with s(0) = 0). This is how the uniform-acceleration formulas arise.', ('Скорость и путь', 'Speed and distance'),
 r'''const V=t=>v.v0+v.a*t,S=t=>v.v0*t+v.a*t*t/2;const G=Gr({x0:0,x1:6,y0:0,y1:Math.max(S(6),V(6))*1.1+1,L:80,T:10,W:470,H:210});let g=G.grid(1,Math.max(5,Math.round(S(6)/5)))+G.fn(V,COL.a,3,0,6)+G.fn(S,COL.b,3.5,0,6)+G.pt(v.t,V(v.t),COL.a,6)+G.pt(v.t,S(v.t),COL.b,7);const h=1e-6;
 return {svg:g,st:[fnum(V(v.t),3)+" м/с",fnum(S(v.t),3)+" м",fnum((S(v.t+h)-S(v.t))/h,3)],fb:U("Скорость — наклон кривой пути; путь — «накопленная» скорость.","Speed is the slope of the distance curve; distance is “accumulated” speed.")}''', '0 0 600 250')

chapter('60', '60-antiderivative.html', 'VIII', ('Первообразная', 'The antiderivative'),
 ('Обратная к дифференцированию операция: по скорости изменения найти саму величину.', 'The operation inverse to differentiation: from a rate of change find the quantity itself.'),
 ('Вы знаете скорость автобуса в каждый момент, но не видели дороги. Можно ли узнать, где он находится?', 'You know the bus’s speed at every moment but did not see the road. Can you find where it is?'),
 ('Разгадка: почти, нужна начальная точка', 'The answer: almost — a starting point is needed'),
 ('Скорость — производная положения, значит положение — первообразная скорости. Но первообразная определена с точностью до постоянной C: по скорости не узнать, откуда автобус выехал. Если известна начальная точка (s(0) = s₀), постоянная находится однозначно. Поэтому в ответе на «найдите первообразную» всегда пишут «+ C».', 'Speed is the derivative of position, so position is an antiderivative of speed. But an antiderivative is defined up to a constant C: from speed alone we cannot know where the bus started. If the initial point is known (s(0) = s₀) the constant is found uniquely. That is why the answer to “find the antiderivative” always has “+ C”.'),
 [S('def', 'Определение', 'Definition', ('Функция F — первообразная f на промежутке, если F′(x) = f(x). Все первообразные одной f отличаются на константу: F(x) + C. Множество всех первообразных называют <strong>неопределённым интегралом</strong>: ∫ f(x) dx = F(x) + C.', 'A function F is an antiderivative of f on an interval if F′(x) = f(x). All antiderivatives of one f differ by a constant: F(x) + C. The set of all antiderivatives is called the <strong>indefinite integral</strong>: ∫ f(x) dx = F(x) + C.'),
    ('F′ = f  ⇒  ∫ f dx = F + C', '', "F′ = f  ⇒  ∫ f dx = F + C"), m1),
  S('table', 'Таблица и правила', 'Table and rules', ('∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C (n ≠ −1); ∫ 1/x dx = ln|x| + C; ∫ eˣ dx = eˣ + C; ∫ cos x dx = sin x + C; ∫ sin x dx = −cos x + C. Правила: ∫ (f + g) = ∫ f + ∫ g; ∫ k·f = k·∫ f. Проверка любого ответа — дифференцированием.', '∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C (n ≠ −1); ∫ 1/x dx = ln|x| + C; ∫ eˣ dx = eˣ + C; ∫ cos x dx = sin x + C; ∫ sin x dx = −cos x + C. Rules: ∫ (f + g) = ∫ f + ∫ g; ∫ k·f = k·∫ f. Any answer is checked by differentiation.'),
    ('∫ xⁿ dx = xⁿ⁺¹/(n+1) + C', '', '∫ xⁿ dx = xⁿ⁺¹/(n+1) + C'), m2),
  S('mot', 'Задача о движении', 'A motion problem', ('По ускорению a находят скорость v = ∫ a dt = v₀ + at, затем путь s = ∫ v dt = v₀t + at²/2. Постоянные находят по начальным условиям.', 'From acceleration a we find speed v = ∫ a dt = v₀ + at, then distance s = ∫ v dt = v₀t + at²/2. The constants are found from initial conditions.'),
    ('v = v₀ + at;  s = v₀t + at²/2', '', 'v = v₀ + at;  s = v₀t + at²/2'), m3)],
 [TK(('Степень', 'Power'), ('Найдите ∫ x² dx.', 'Find ∫ x² dx.'), '', 'x³/3 + C.', 'x³/3 + C.'),
  TK(('Сумма', 'Sum'), ('Найдите ∫ (3x² + 4x) dx.', 'Find ∫ (3x² + 4x) dx.'), '', 'x³ + 2x² + C.', 'x³ + 2x² + C.'),
  TK(('Начальное условие', 'Initial condition'), ('F′ = 2x, F(1) = 5. Найдите F.', 'F′ = 2x, F(1) = 5. Find F.'), 'F = x² + C', '1 + C = 5, C = 4; F = x² + 4.', 'F = x² + 4.'),
  TK(('Тригонометрия', 'Trigonometry'), ('Найдите ∫ cos x dx и проверьте.', 'Find ∫ cos x dx and check.'), '', 'sin x + C; (sin x)′ = cos x ✓.', 'sin x + C.'),
  TK(('Движение', 'Motion'), ('v = 4t м/с, s(0) = 0. Найдите s(3).', 'v = 4t m/s, s(0) = 0. Find s(3).'), '', 's = 2t²; s(3) = 18 м.', '18 м.')],
 [Q('Первообразная F функции f — это', 'An antiderivative F of f is', ('F′ = f', 'F′ = f'), ('F = f′', 'F = f′'), ('F = f', 'F = f'), ('Определение.', 'The definition.')),
  Q('Первообразные одной функции различаются', 'Antiderivatives of one function differ by', ('на постоянную', 'a constant'), ('на x', 'x'), ('множителем', 'a factor'), ('Производная константы 0.', 'The derivative of a constant is 0.')),
  Q('∫ x dx =', '∫ x dx =', 'x²/2 + C', 'x² + C', '1 + C', ('Правило степени.', 'The power rule.')),
  Q('∫ eˣ dx =', '∫ eˣ dx =', 'eˣ + C', 'xeˣ + C', 'eˣ⁺¹', ('(eˣ)′ = eˣ.', '(eˣ)′ = eˣ.')),
  Q('∫ cos x dx =', '∫ cos x dx =', 'sin x + C', '−sin x + C', 'cos x + C', ('(sin x)′ = cos x.', '(sin x)′ = cos x.')),
  Q('Как проверить первообразную?', 'How to check an antiderivative?', ('продифференцировать', 'differentiate it'), ('возвести в квадрат', 'square it'), ('умножить на x', 'multiply by x'), ('F′ должна быть f.', 'F′ must be f.')),
  Q('Путь — первообразная', 'Distance is an antiderivative of', ('скорости', 'speed'), ('времени', 'time'), ('ускорения-квадрата', 'squared acceleration'), ('s′ = v.', 's′ = v.')),
  Q('Зачем в ответе «+ C»?', 'Why “+ C” in the answer?', ('первообразных бесконечно много', 'there are infinitely many antiderivatives'), ('для красоты', 'for decoration'), ('это ошибка', 'it is a mistake'), ('Все они отличаются на C.', 'They all differ by C.'))],
 src=[('Wikipedia: Antiderivative', 'https://en.wikipedia.org/wiki/Antiderivative'), ('Wikipedia: Integral', 'https://en.wikipedia.org/wiki/Integral'), ('OpenStax: Calculus Volume 1', 'https://openstax.org/details/books/calculus-volume-1')])
