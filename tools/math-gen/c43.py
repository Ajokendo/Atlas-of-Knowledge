# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Парабола y = ax² + bx + c', 'The parabola y = ax² + bx + c'),
 [('r', 'a', 'a', 'a', -3, 3, 0.5, 1), ('r', 'b', 'b', 'b', -8, 8, 1, -4), ('r', 'c', 'c', 'c', -8, 8, 1, 1)],
 [('Вершина', 'The vertex'), ('Ось симметрии', 'Axis of symmetry'), ('Направление ветвей', 'Direction of the branches')],
 'Вершина параболы — в точке x₀ = −b/(2a). Если a &gt; 0, ветви вверх и вершина — наименьшее значение; если a &lt; 0 — вниз и наибольшее.', 'The vertex of the parabola is at x₀ = −b/(2a). If a &gt; 0 the branches go up and the vertex is the least value; if a &lt; 0 they go down and it is the greatest.', ('Парабола и её вершина', 'A parabola and its vertex'),
 r'''const a=v.a===0?0.5:v.a,x0=-v.b/(2*a),y0=a*x0*x0+v.b*x0+v.c;const G=Gr({x0:-8,x1:8,y0:-12,y1:12,L:100,T:10,W:400,H:210});let g=G.grid(2,4)+G.fn(x=>a*x*x+v.b*x+v.c,COL.a,3.5);g+=G.seg(x0,-12,x0,12,COL.mut,1.5)+G.pt(x0,y0,COL.b,8);
 return {svg:g,st:["("+fnum(x0,2)+"; "+fnum(y0,2)+")","x = "+fnum(x0,2),a>0?U("вверх (a > 0)","up (a > 0)"):U("вниз (a < 0)","down (a < 0)")],fb:a>0?U("Наименьшее значение y = "+fnum(y0,2)+".","The least value is y = "+fnum(y0,2)+"."):U("Наибольшее значение y = "+fnum(y0,2)+".","The greatest value is y = "+fnum(y0,2)+".")}''', '0 0 600 250')

m2 = M(('Вершинная форма', 'Vertex form'),
 [('r', 'a', 'a', 'a', -3, 3, 0.5, 1), ('r', 'h', 'Абсцисса вершины h', 'Vertex abscissa h', -5, 5, 1, 2), ('r', 'k', 'Ордината вершины k', 'Vertex ordinate k', -8, 8, 1, -3)],
 [('Вершинная форма', 'Vertex form'), ('Стандартная форма', 'Standard form'), ('Нули', 'Zeros')],
 'y = a(x − h)² + k: вершина в точке (h; k), всё видно сразу. Раскрыв скобки, получим стандартный вид ax² + bx + c.', 'y = a(x − h)² + k: the vertex is at (h; k), all is visible at once. Expanding the brackets we get the standard form ax² + bx + c.', ('Парабола с вершиной (h; k)', 'A parabola with vertex (h; k)'),
 r'''const a=v.a===0?0.5:v.a,b=-2*a*v.h,c=a*v.h*v.h+v.k,ps=n=>n<0?"− "+fnum(-n,2):"+ "+fnum(n,2);const G=Gr({x0:-8,x1:8,y0:-12,y1:12,L:100,T:10,W:400,H:210});let g=G.grid(2,4)+G.fn(x=>a*(x-v.h)*(x-v.h)+v.k,COL.a,3.5)+G.pt(v.h,v.k,COL.b,8)+G.txt(v.h+1.6,v.k-1,"("+v.h+"; "+v.k+")",COL.b,13);
 const D=b*b-4*a*c;return {svg:g,st:["y = "+a+"(x "+ps(-v.h)+")² "+ps(v.k),"y = "+fnum(a,2)+"x² "+ps(b)+"x "+ps(c),D<-1e-9?U("нет","none"):D<1e-9?fnum(-b/(2*a),2):fnum((-b-Math.sqrt(D))/(2*a),2)+"; "+fnum((-b+Math.sqrt(D))/(2*a),2)],fb:U("Параболу можно получить из y = x² сдвигом и растяжением.","The parabola is obtained from y = x² by shifting and stretching.")}''', '0 0 600 250')

m3 = M(('Наибольшая площадь', 'The greatest area'),
 [('r', 'P', 'Длина забора, м', 'Fence length, m', 20, 100, 2, 40), ('r', 'x', 'Ширина x, м', 'Width x, m', 1, 49, 1, 6)],
 [('Площадь S = x(P/2 − x)', 'Area S = x(P/2 − x)'), ('Наибольшая площадь', 'The greatest area'), ('При ширине', 'At a width of')],
 'Из забора длиной P огораживают прямоугольник. Площадь — квадратичная функция ширины; её наибольшее значение — в вершине параболы.', 'A fence of length P encloses a rectangle. The area is a quadratic function of the width; its greatest value is at the vertex of the parabola.', ('Площадь против ширины', 'Area against width'),
 r'''const hp=v.P/2,x=Math.min(v.x,hp-1),S=x*(hp-x),Sm=hp*hp/4;const G=Gr({x0:0,x1:hp,y0:0,y1:Sm*1.15,L:80,T:10,W:460,H:210});let g=G.grid(Math.max(1,Math.round(hp/10)),Math.round(Sm/4/10)*10||10)+G.fn(t=>t*(hp-t),COL.a,3.5,0,hp)+G.pt(hp/2,Sm,COL.b,8)+G.pt(x,S,COL.c,7);
 return {svg:g,st:[fnum(S,1)+" м²",fnum(Sm,1)+" м²",fnum(hp/2,1)+" м (квадрат)"],fb:U("При фиксированном периметре наибольшую площадь даёт квадрат.","For a fixed perimeter the square gives the greatest area.")}''', '0 0 600 250')

chapter('43', '43-parabola.html', 'VI', ('Квадратичная функция и парабола', 'The quadratic function and the parabola'),
 ('Парабола, её вершина и ось симметрии; как найти наибольшее или наименьшее значение.', 'The parabola, its vertex and axis of symmetry; how to find the greatest or least value.'),
 ('У фермера 40 метров ограды. Он хочет огородить прямоугольный загон для овец со всех четырёх сторон так, чтобы площадь была наибольшей.\n\nКакие размеры выбрать?', 'A farmer has 40 metres of fence. He wants a rectangular pen for sheep, fenced on all four sides, so that the area is as large as possible.\n\nWhich dimensions should he choose?'),
 ('Разгадка: квадрат 10 × 10 м, площадь 100 м²', 'The answer: a 10 × 10 m square, area 100 m²'),
 ('Пусть ширина x, тогда длина 20 − x (полупериметр 20), площадь S = x(20 − x) = −x² + 20x. Это парабола с ветвями вниз; наибольшее значение — в вершине x = −b/(2a) = 10. Тогда S = 10 · 10 = 100 м². Любое отклонение от квадрата уменьшает площадь: при 8 × 12 получится лишь 96 м².', 'Let the width be x, then the length is 20 − x (half the perimeter is 20) and the area is S = x(20 − x) = −x² + 20x. This is a parabola opening downwards; its greatest value is at the vertex x = −b/(2a) = 10. Then S = 10 · 10 = 100 m². Any deviation from the square reduces the area: with 8 × 12 we get only 96 m².'),
 [S('par', 'Парабола и вершина', 'The parabola and its vertex', ('График <strong>y = ax² + bx + c</strong> — парабола. Вершина имеет абсциссу <strong>x₀ = −b/(2a)</strong>, ось симметрии — прямая x = x₀. При a &gt; 0 ветви вверх, у вершины <em>наименьшее</em> значение, при a &lt; 0 — вниз, у вершины <em>наибольшее</em>. Нули функции — корни уравнения ax² + bx + c = 0.', 'The graph of <strong>y = ax² + bx + c</strong> is a parabola. The vertex has abscissa <strong>x₀ = −b/(2a)</strong>, the axis of symmetry is the line x = x₀. For a &gt; 0 the branches go up and the vertex gives the <em>least</em> value; for a &lt; 0 they go down and it gives the <em>greatest</em>. The zeros of the function are the roots of ax² + bx + c = 0.'),
    ('x₀ = −b/(2a)', '', 'x₀ = −b/(2a)'), m1),
  S('vf', 'Вершинная форма', 'Vertex form', ('Запись <strong>y = a(x − h)² + k</strong> сразу показывает вершину (h; k). К ней приводят выделением полного квадрата: x² − 4x + 1 = (x − 2)² − 3. Параболы y = ax² для разных a различаются «крутизной»: чем больше |a|, тем уже парабола.', 'The notation <strong>y = a(x − h)² + k</strong> shows the vertex (h; k) at once. We reach it by completing the square: x² − 4x + 1 = (x − 2)² − 3. Parabolas y = ax² for different a differ in “steepness”: the larger |a|, the narrower the parabola.'),
    ('y = a(x − h)² + k', '', 'y = a(x − h)² + k'), m2),
  S('opt', 'Задачи на наибольшее и наименьшее', 'Optimisation problems', ('Чтобы найти наибольшую площадь, наименьшие затраты или максимальную высоту, записывают величину как квадратичную функцию и находят её вершину. Парабола — также траектория брошенного предмета и форма отражателей.', 'To find the greatest area, least cost or maximum height we write the quantity as a quadratic function and find its vertex. A parabola is also the path of a thrown object and the shape of reflectors.'),
    ('S = x(p − x)', 'наибольшее при x = p/2', 'greatest at x = p/2'), m3)],
 [TK(('Вершина', 'Vertex'), ('Найдите вершину y = x² − 6x + 5.', 'Find the vertex of y = x² − 6x + 5.'), 'x₀ = 6/2 = 3', 'y₀ = 9 − 18 + 5 = −4. Вершина (3; −4).', '(3; −4).'),
  TK(('Наименьшее', 'Least value'), ('Найдите наименьшее значение y = 2x² − 8x + 3.', 'Find the least value of y = 2x² − 8x + 3.'), 'x₀ = 2', 'y(2) = 8 − 16 + 3 = −5.', '−5.'),
  TK(('Нули', 'Zeros'), ('Найдите нули y = x² − 4.', 'Find the zeros of y = x² − 4.'), '', 'x² = 4, x = ±2.', '±2.'),
  TK(('Вершинная форма', 'Vertex form'), ('Запишите x² + 4x + 7 в виде (x + h)² + k.', 'Write x² + 4x + 7 as (x + h)² + k.'), '', '(x + 2)² + 3.', '(x + 2)² + 3.'),
  TK(('Забор', 'The fence'), ('Забор 60 м. Какая наибольшая площадь прямоугольника?', 'A 60 m fence. What is the greatest rectangle area?'), 'S = x(30 − x)', 'Наибольшая при x = 15: 15 · 15 = 225.', ('225 м².', '225 m².'))],
 [Q('Ветви параболы y = −x² направлены', 'The branches of y = −x² point', ('вниз', 'down'), ('вверх', 'up'), ('вправо', 'right'), ('a < 0.', 'a < 0.')),
  Q('Вершина y = x² в точке', 'The vertex of y = x² is at', '(0; 0)', '(1; 1)', '(0; 1)', ('Начало координат.', 'The origin.')),
  Q('Ось симметрии y = x² − 4x', 'The axis of symmetry of y = x² − 4x', 'x = 2', 'x = 4', 'x = −2', ('−b/2a = 2.', '−b/2a = 2.')),
  Q('Парабола y = x² + 1 пересекает ось x', 'The parabola y = x² + 1 meets the x-axis', ('не пересекает', 'never'), ('в двух точках', 'at two points'), ('в одной точке', 'at one point'), ('y ≥ 1.', 'y ≥ 1.')),
  Q('Наибольшее y = −(x − 1)² + 5', 'The greatest value of y = −(x − 1)² + 5', '5', '1', '−5', ('Вершина (1; 5).', 'The vertex (1; 5).')),
  Q('При a > 0 вершина даёт', 'For a > 0 the vertex gives', ('наименьшее значение', 'the least value'), ('наибольшее значение', 'the greatest value'), ('нуль', 'zero'), ('Ветви вверх.', 'Branches up.')),
  Q('Форма y = a(x − h)² + k показывает', 'The form y = a(x − h)² + k shows', ('вершину', 'the vertex'), ('нули', 'the zeros'), ('периметр', 'the perimeter'), ('Вершина (h; k).', 'Vertex (h; k).')),
  Q('Прямоугольник с периметром 20: наибольшая площадь', 'A rectangle with perimeter 20: the greatest area', '25', '24', '20', ('5 × 5.', '5 × 5.'))],
 src=[('Wikipedia: Quadratic function', 'https://en.wikipedia.org/wiki/Quadratic_function'), ('Wikipedia: Parabola', 'https://en.wikipedia.org/wiki/Parabola')],
 note=('Загон и размеры — условный пример.', 'The pen and dimensions are an illustrative example.'))
