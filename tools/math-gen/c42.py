# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Дискриминант и корни', 'The discriminant and roots'),
 [('r', 'a', 'a', 'a', -3, 3, 1, 1), ('r', 'b', 'b', 'b', -8, 8, 1, -2), ('r', 'c', 'c', 'c', -8, 8, 1, -3)],
 [('Уравнение', 'Equation'), ('Дискриминант D = b² − 4ac', 'Discriminant D = b² − 4ac'), ('Корни', 'Roots')],
 'Знак дискриминанта определяет число корней: D &gt; 0 — два, D = 0 — один, D &lt; 0 — ни одного вещественного.', 'The sign of the discriminant decides the number of roots: D &gt; 0 — two, D = 0 — one, D &lt; 0 — no real roots.', ('Парабола и её пересечения с осью x', 'A parabola and its crossings with the x-axis'),
 r'''const a=v.a===0?1:v.a,b=v.b,c=v.c,D=b*b-4*a*c,ps=n=>n<0?"− "+(-n):"+ "+n;const G=Gr({x0:-8,x1:8,y0:-12,y1:12,L:100,T:10,W:400,H:210});let g=G.grid(2,4)+G.fn(x=>a*x*x+b*x+c,COL.a,3.5);let r=[];if(D>=0){r=D===0?[-b/(2*a)]:[(-b-Math.sqrt(D))/(2*a),(-b+Math.sqrt(D))/(2*a)];r.forEach(x=>g+=G.pt(x,0,COL.c,7))}
 return {svg:g,st:[(a===1?"":a===-1?"−":a)+"x² "+ps(b)+"x "+ps(c)+" = 0","D = "+b*b+" − 4·"+a+"·("+c+") = "+D,D<0?U("действительных корней нет","no real roots"):r.map(x=>fnum(x,3)).join("; ")],fb:D>0?U("D > 0: парабола пересекает ось x в двух точках.","D > 0: the parabola crosses the x-axis at two points."):D===0?U("D = 0: парабола касается оси x.","D = 0: the parabola touches the x-axis."):U("D < 0: парабола не достаёт до оси x.","D < 0: the parabola does not reach the x-axis.")}''', '0 0 600 250')

m2 = M(('Теорема Виета', 'Vieta’s theorem'),
 [('r', 'p', 'Корень x₁', 'Root x₁', -8, 8, 1, 2), ('r', 'q', 'Корень x₂', 'Root x₂', -8, 8, 1, 5)],
 [('Сумма корней', 'Sum of roots'), ('Произведение корней', 'Product of roots'), ('Уравнение x² + bx + c = 0', 'Equation x² + bx + c = 0')],
 'Если x₁ и x₂ — корни x² + bx + c = 0, то x₁ + x₂ = −b и x₁·x₂ = c. Можно сразу «собрать» уравнение по корням.', 'If x₁ and x₂ are the roots of x² + bx + c = 0 then x₁ + x₂ = −b and x₁·x₂ = c. We can “assemble” the equation from the roots at once.', ('Парабола с заданными корнями', 'A parabola with given roots'),
 r'''const s=v.p+v.q,pr=v.p*v.q,ps=n=>n<0?"− "+(-n):"+ "+n;const G=Gr({x0:-10,x1:10,y0:-25,y1:25,L:100,T:10,W:400,H:210});let g=G.grid(2,10)+G.fn(x=>(x-v.p)*(x-v.q),COL.a,3.5)+G.pt(v.p,0,COL.c,7)+G.pt(v.q,0,COL.c,7);
 return {svg:g,st:[v.p+" + "+v.q+" = "+s,v.p+" · "+v.q+" = "+pr,"x² "+ps(-s)+"x "+ps(pr)+" = 0"],fb:U("Проверка: "+v.p+"² "+ps(-s)+"·"+v.p+" "+ps(pr)+" = "+(v.p*v.p-s*v.p+pr)+".","Check: "+v.p+"² "+ps(-s)+"·"+v.p+" "+ps(pr)+" = "+(v.p*v.p-s*v.p+pr)+".")}''', '0 0 600 250')

m3 = M(('Квадратное уравнение из жизни', 'A quadratic equation from life'),
 [('r', 'v0', 'Начальная скорость, м/с', 'Initial speed, m/s', 5, 30, 1, 20), ('r', 'h0', 'Высота броска, м', 'Launch height, m', 0, 10, 1, 2), ('r', 't', 'Время t, с', 'Time t, s', 0, 6, 0.1, 2)],
 [('Высота h(t)', 'Height h(t)'), ('Время падения (h = 0)', 'Fall time (h = 0)'), ('Наибольшая высота', 'The greatest height')],
 'Мяч, брошенный вверх: h(t) = h₀ + v₀t − 5t² (g округлено до 10 м/с²). Когда он упадёт? Решаем квадратное уравнение h(t) = 0.', 'A ball thrown up: h(t) = h₀ + v₀t − 5t² (g rounded to 10 m/s²). When will it land? We solve the quadratic equation h(t) = 0.', ('Высота мяча от времени', 'Height of the ball against time'),
 r'''const h=t=>v.h0+v.v0*t-5*t*t,tf=(v.v0+Math.sqrt(v.v0*v.v0+20*v.h0))/10,tm=v.v0/10,hm=h(tm);const G=Gr({x0:0,x1:7,y0:0,y1:60,L:80,T:10,W:460,H:210});let g=G.grid(1,10)+G.fn(h,COL.a,3,0,tf)+G.pt(tf,0,COL.c,7)+G.pt(tm,hm,COL.b,6);const y=h(v.t);if(v.t<=tf)g+=G.pt(v.t,y,COL.ink,6);
 return {svg:g,st:[v.t<=tf?fnum(y,2)+" м":U("уже на земле","already landed"),fnum(tf,2)+" с",fnum(hm,2)+" м ("+fnum(tm,1)+" с)"],fb:U("Положительный корень уравнения "+v.h0+" + "+v.v0+"t − 5t² = 0: t = "+fnum(tf,2)+" с.","The positive root of "+v.h0+" + "+v.v0+"t − 5t² = 0: t = "+fnum(tf,2)+" s.")}''', '0 0 600 250')

chapter('42', '42-quadratic-equations.html', 'VI', ('Квадратные уравнения', 'Quadratic equations'),
 ('Как решать уравнения вида ax² + bx + c = 0 и что такое дискриминант.', 'How to solve equations of the form ax² + bx + c = 0 and what the discriminant is.'),
 ('Мяч бросили вверх с высоты 2 м со скоростью 20 м/с. Высота (в метрах) через t секунд: h = 2 + 20t − 5t².\n\nЧерез сколько секунд мяч упадёт на землю?', 'A ball is thrown up from a height of 2 m at 20 m/s. The height (in metres) after t seconds: h = 2 + 20t − 5t².\n\nAfter how many seconds does the ball hit the ground?'),
 ('Разгадка: примерно через 4,1 секунды', 'The answer: after about 4.1 seconds'),
 ('Мяч упадёт, когда h = 0: 2 + 20t − 5t² = 0, то есть 5t² − 20t − 2 = 0. D = 400 + 40 = 440, t = (20 ± √440)/10. Положительный корень t = (20 + 20,98)/10 ≈ 4,1 с. Второй корень отрицателен — по смыслу задачи не подходит. Квадратное уравнение даёт два корня, но нужно проверять, какой из них имеет смысл.', 'The ball lands when h = 0: 2 + 20t − 5t² = 0, i.e. 5t² − 20t − 2 = 0. D = 400 + 40 = 440, t = (20 ± √440)/10. The positive root t = (20 + 20.98)/10 ≈ 4.1 s. The second root is negative — it does not fit the problem. A quadratic equation gives two roots but we must check which makes sense.'),
 [S('disc', 'Формула корней', 'The root formula', ('Уравнение <strong>ax² + bx + c = 0</strong> (a ≠ 0). Дискриминант <strong>D = b² − 4ac</strong>. Если D &gt; 0, два корня x = (−b ± √D)/(2a); если D = 0, один корень x = −b/(2a); если D &lt; 0, действительных корней нет. Неполные уравнения (b = 0 или c = 0) решают проще: x² = 9, x(x − 4) = 0.', 'The equation <strong>ax² + bx + c = 0</strong> (a ≠ 0). The discriminant <strong>D = b² − 4ac</strong>. If D &gt; 0 there are two roots x = (−b ± √D)/(2a); if D = 0 one root x = −b/(2a); if D &lt; 0 there are no real roots. Incomplete equations (b = 0 or c = 0) are easier: x² = 9, x(x − 4) = 0.'),
    ('x = (−b ± √D) / 2a', '', 'x = (−b ± √D) / 2a'), m1),
  S('viet', 'Теорема Виета', 'Vieta’s theorem', ('Для приведённого уравнения x² + bx + c = 0 корни связаны с коэффициентами: <strong>x₁ + x₂ = −b</strong>, <strong>x₁ · x₂ = c</strong>. Отсюда быстро подбирают целые корни: ищут два числа с суммой −b и произведением c. Квадратный трёхчлен раскладывают: ax² + bx + c = a(x − x₁)(x − x₂).', 'For the reduced equation x² + bx + c = 0 the roots are tied to the coefficients: <strong>x₁ + x₂ = −b</strong>, <strong>x₁ · x₂ = c</strong>. So integer roots are quickly guessed: look for two numbers with sum −b and product c. A quadratic trinomial factorises: ax² + bx + c = a(x − x₁)(x − x₂).'),
    ('x₁ + x₂ = −b;  x₁x₂ = c', '', 'x₁ + x₂ = −b;  x₁x₂ = c'), m2),
  S('life', 'Задачи с квадратным уравнением', 'Problems with a quadratic equation', ('Квадратные уравнения встречаются в задачах о движении под действием силы тяжести, площадях, прибыли. Решив, <strong>проверяют корни по смыслу</strong>: время и длина не бывают отрицательными.', 'Quadratic equations appear in problems of motion under gravity, areas, profit. After solving, <strong>the roots are checked against the meaning</strong>: time and length are not negative.'),
    ('h(t) = h₀ + v₀t − 5t²', '', 'h(t) = h₀ + v₀t − 5t²'), m3)],
 [TK(('Дискриминант', 'Discriminant'), ('Решите x² − 5x + 6 = 0.', 'Solve x² − 5x + 6 = 0.'), 'D = 25 − 24 = 1', 'x = (5 ± 1)/2 → 3 и 2. По Виету: 3 + 2 = 5, 3 · 2 = 6.', ('2 и 3.', '2 and 3.')),
  TK(('Один корень', 'One root'), ('Решите x² − 6x + 9 = 0.', 'Solve x² − 6x + 9 = 0.'), 'D = 36 − 36 = 0', 'x = 3 (уравнение (x − 3)² = 0).', 'x = 3.'),
  TK(('Нет корней', 'No roots'), ('Сколько корней у x² + x + 5 = 0?', 'How many roots has x² + x + 5 = 0?'), 'D = 1 − 20 < 0', 'D < 0 — действительных корней нет.', ('Ни одного.', 'None.')),
  TK(('Неполное', 'Incomplete'), ('Решите 3x² − 12x = 0.', 'Solve 3x² − 12x = 0.'), '3x(x − 4) = 0', 'x = 0 или x = 4.', ('0 и 4.', '0 and 4.')),
  TK(('Задача', 'A problem'), ('Длина прямоугольника на 3 м больше ширины, площадь 40 м². Найдите стороны.', 'The length of a rectangle is 3 m more than the width, the area is 40 m². Find the sides.'), 'x(x + 3) = 40', 'x² + 3x − 40 = 0, D = 169, x = 5 (или −8 — не подходит). Стороны 5 и 8.', ('5 м и 8 м.', '5 m and 8 m.'))],
 [Q('D = b² − 4ac. Если D < 0,', 'D = b² − 4ac. If D < 0,', ('корней нет', 'there are no roots'), ('два корня', 'two roots'), ('один корень', 'one root'), ('√ из отрицательного.', 'The root of a negative number.')),
  Q('x² = 16. Корни', 'x² = 16. The roots', '4 и −4', 'только 4', '8', ('Два корня ±4.', 'Two roots ±4.')),
  Q('x² − 7x + 12 = 0. Сумма корней', 'x² − 7x + 12 = 0. The sum of the roots', '7', '12', '−7', ('x₁ + x₂ = −b.', 'x₁ + x₂ = −b.')),
  Q('Произведение корней x² − 7x + 12', 'The product of the roots of x² − 7x + 12', '12', '7', '−12', ('x₁x₂ = c.', 'x₁x₂ = c.')),
  Q('При D = 0 корней', 'For D = 0 the number of roots is', ('один', 'one'), ('два', 'two'), ('нет', 'none'), ('Парабола касается оси.', 'The parabola touches the axis.')),
  Q('x(x − 5) = 0. Корни', 'x(x − 5) = 0. The roots', '0 и 5', '5', '0', ('Произведение равно нулю, если один из множителей нуль.', 'A product is zero if one of the factors is zero.')),
  Q('Корни по смыслу задачи', 'Roots according to the problem’s meaning', ('нужно проверить', 'must be checked'), ('брать оба всегда', 'always take both'), ('брать меньший', 'take the smaller'), ('Длина не бывает отрицательной.', 'Length is not negative.')),
  Q('Разложение x² − 9', 'Factorisation of x² − 9', '(x − 3)(x + 3)', '(x − 9)(x + 1)', '(x − 3)²', ('Разность квадратов.', 'Difference of squares.'))],
 src=[('Wikipedia: Quadratic equation', 'https://en.wikipedia.org/wiki/Quadratic_equation'), ('Wikipedia: Vieta’s formulas', 'https://en.wikipedia.org/wiki/Vieta%27s_formulas')],
 note=('Бросок мяча — условный пример, g округлено до 10 м/с².', 'The ball throw is an illustrative example, g rounded to 10 m/s².'))
