# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Правильная призма', 'A regular prism'),
 [('r', 'n', 'Углов в основании n', 'Corners n of the base', 3, 8, 1, 6), ('r', 'a', 'Сторона основания a, см', 'Base side a, cm', 1, 8, 1, 4), ('r', 'h', 'Высота h, см', 'Height h, cm', 1, 12, 1, 6), ('r', 'yaw', 'Поворот', 'Rotation', -1, 1, 0.1, 0.3)],
 [('Площадь основания S', 'Base area S'), ('Объём V = S·h', 'Volume V = S·h'), ('Площадь поверхности', 'Surface area')],
 'Объём призмы — площадь основания на высоту. Площадь поверхности — боковая n·a·h плюс два основания.', 'The volume of a prism is the base area times the height. The surface area is the lateral n·a·h plus two bases.', ('Правильная n-угольная призма', 'A regular n-gonal prism'),
 r'''const n=v.n,Rr=v.a/(2*Math.sin(Math.PI/n)),s=Math.min(30,150/Math.max(2*Rr,v.h)),P=P3(v.yaw,0.5,s,300,230),A=[],B=[];for(let i=0;i<n;i++){const t=2*Math.PI*i/n;A.push([Rr*Math.cos(t),Rr*Math.sin(t),0]);B.push([Rr*Math.cos(t),Rr*Math.sin(t),v.h])}
 let g="";const E=(a,b,c,w)=>{const p=P(...a),q2=P(...b);g+=L(p[0],p[1],q2[0],q2[1],c||COL.ink,w||2)};for(let i=0;i<n;i++){const j=(i+1)%n;E(A[i],A[j]);E(B[i],B[j]);E(A[i],B[i],COL.mut,1.5)}
 const S=n*v.a*v.a/(4*Math.tan(Math.PI/n));
 return {svg:g,st:[fnum(S,2)+" см²",fnum(S*v.h,1)+" см³",fnum(2*S+n*v.a*v.h,1)+" см²"],fb:U("Боковая поверхность: n·a·h = "+fnum(n*v.a*v.h,1)+" см².","Lateral surface: n·a·h = "+fnum(n*v.a*v.h,1)+" cm².")}''', '0 0 600 290')

m2 = M(('Правильная четырёхугольная пирамида', 'A regular quadrangular pyramid'),
 [('r', 'a', 'Сторона основания a', 'Base side a', 2, 10, 1, 6), ('r', 'h', 'Высота h', 'Height h', 2, 10, 1, 4), ('r', 'yaw', 'Поворот', 'Rotation', -1, 1, 0.1, 0.5)],
 [('Апофема l', 'Slant height l'), ('Объём V = S·h/3', 'Volume V = S·h/3'), ('Площадь поверхности', 'Surface area')],
 'Апофема (высота боковой грани) l = √(h² + (a/2)²). Боковая поверхность — четыре треугольника: 2·a·l. Объём — треть произведения.', 'The slant height (the height of a lateral face) is l = √(h² + (a/2)²). The lateral surface is four triangles: 2·a·l. The volume is one third of the product.', ('Высота и апофема', 'Height and slant height'),
 r'''const a=v.a,h=v.h,s=Math.min(40,270/Math.max(a*1.4,h*1.3)),P=P3(v.yaw,0.35,s,300,225),B=[[-a/2,-a/2,0],[a/2,-a/2,0],[a/2,a/2,0],[-a/2,a/2,0]],T=[0,0,h];let g="";const E=(p0,p1,c,w,d)=>{const p=P(...p0),q2=P(...p1);g+=L(p[0],p[1],q2[0],q2[1],c||COL.ink,w||2)};
 for(let i=0;i<4;i++){E(B[i],B[(i+1)%4]);E(B[i],T,COL.mut,1.5)}E([0,0,0],T,COL.b,3);E([0,0,0],[0,-a/2,0],COL.c,3);E([0,-a/2,0],T,COL.a,3);
 const l=Math.sqrt(h*h+a*a/4);
 return {svg:g,st:[fnum(l,3),fnum(a*a*h/3,2),fnum(a*a+2*a*l,2)],fb:U("Синяя — высота h, зелёная — a/2, красная — апофема l: прямоугольный треугольник.","Blue — height h, green — a/2, red — slant height l: a right triangle.")}''', '0 0 600 280')

m3 = M(('Почему в пирамиде множитель 1/3', 'Why the pyramid has a factor 1/3'),
 [('r', 'z', 'Уровень сечения z, % высоты', 'Section level z, % of height', 0, 95, 5, 40)],
 [('Сторона сечения', 'Side of the section'), ('Площадь сечения / площадь основания', 'Section area / base area'), ('Объём пирамиды к призме', 'Pyramid to prism volume')],
 'Сечение, параллельное основанию, подобно основанию с коэффициентом (h − z)/h, а его площадь — с коэффициентом в квадрате. Складывая такие сечения, получают V = S·h/3.', 'A section parallel to the base is similar to the base with ratio (h − z)/h, and its area with that ratio squared. Adding up such sections gives V = S·h/3.', ('Сечение пирамиды на уровне z', 'A section of the pyramid at level z'),
 r'''const k=1-v.z/100,y0=200,hh=150;let g=poly([[60,y0],[300,y0],[180,y0-hh]],COL.a+"33",COL.ink,2.5);const yz=y0-hh*v.z/100,xl=60+120*v.z/100,xr=300-120*v.z/100;g+=L(xl,yz,xr,yz,COL.b,4);
 const side=200*k;g+=R(340+(200-side)/2,60+(200-side)/2,side,side,COL.b+"88",COL.ink,2,0)+R(340,60,200,200,"none",COL.mut,1.5,0)+TX(440,280,U("сечение и основание","section and base"),COL.mut,12,"middle");
 return {svg:g,st:[fnum(k,3)+" a",fnum(k*k,3),"1/3 ≈ 0,333"],fb:U("Площадь сечения убывает как квадрат: поэтому суммарно получается треть призмы, а не половина.","The section area falls as a square, so in total we get a third of the prism, not a half.")}''', '0 0 600 290')

chapter('64', '64-prism-pyramid.html', 'IX', ('Призма и пирамида', 'Prism and pyramid'),
 ('Объём и площадь поверхности призмы и пирамиды, апофема, почему в пирамиде множитель 1/3.', 'Volume and surface area of prism and pyramid, the slant height and why the pyramid carries the factor 1/3.'),
 ('Пирамида и призма стоят на одинаковом основании и имеют одинаковую высоту. Какая часть объёма призмы приходится на пирамиду: половина, треть или четверть?', 'A pyramid and a prism stand on the same base and have the same height. What part of the prism’s volume does the pyramid take: a half, a third or a quarter?'),
 ('Разгадка: ровно треть', 'The answer: exactly a third'),
 ('Объём пирамиды — треть объёма призмы с тем же основанием и высотой. Это видно по сечениям: на высоте z сечение подобно основанию, а его площадь составляет ((h − z)/h)² от площади основания; сумма таких квадратов, складываемых по высоте, даёт 1/3. Куб можно разрезать на три равные пирамиды с общей вершиной — это нагляднее всего. Знаменитые египетские пирамиды — правильные четырёхугольные.', 'The volume of a pyramid is a third of the volume of the prism with the same base and height. Sections show it: at height z the section is similar to the base and its area is ((h − z)/h)² of the base area; adding such squares along the height gives 1/3. A cube can be cut into three equal pyramids with a common apex — the most visual proof. The famous Egyptian pyramids are regular quadrangular ones.'),
 [S('prism', 'Призма', 'The prism', ('Прямая призма: боковые рёбра перпендикулярны основанию. <strong>V = S · h</strong>, боковая поверхность <strong>S_бок = P · h</strong> (P — периметр основания), полная <strong>S = S_бок + 2S_осн</strong>. Для правильной n-угольной призмы S_осн = n·a²/(4 tan(180°/n)).', 'A right prism: lateral edges are perpendicular to the base. <strong>V = S · h</strong>, lateral surface <strong>S_lat = P · h</strong> (P is the base perimeter), total <strong>S = S_lat + 2S_base</strong>. For a regular n-gonal prism S_base = n·a²/(4 tan(180°/n)).'),
    ('V = S·h', '', 'V = S·h'), m1),
  S('pyr', 'Пирамида', 'The pyramid', ('Правильная пирамида: в основании правильный многоугольник, вершина проектируется в его центр. Высота h, апофема l = √(h² + r²), где r — радиус вписанной окружности основания. <strong>V = S_осн · h / 3</strong>; <strong>S_бок = P · l / 2</strong>.', 'A regular pyramid: the base is a regular polygon and the apex projects onto its centre. Height h, slant height l = √(h² + r²) where r is the inradius of the base. <strong>V = S_base · h / 3</strong>; <strong>S_lat = P · l / 2</strong>.'),
    ('V = S·h/3', '', 'V = S·h/3'), m2),
  S('why', 'Почему 1/3', 'Why 1/3', ('Сечение пирамиды плоскостью, параллельной основанию, подобно основанию. При коэффициенте k площади относятся как k². Суммируя тонкие слои (это интеграл ∫₀¹ k² dk = 1/3), получаем треть призмы.', 'A section of a pyramid by a plane parallel to the base is similar to the base. With ratio k areas relate as k². Summing thin layers (this is the integral ∫₀¹ k² dk = 1/3) we get a third of the prism.'),
    ('∫₀¹ k² dk = 1/3', '', '∫₀¹ k² dk = 1/3'), m3)],
 [TK(('Призма', 'Prism'), ('Основание — квадрат со стороной 3, высота 5. Найдите V и S.', 'A square base of side 3, height 5. Find V and S.'), '', 'V = 9 · 5 = 45; S = 2 · 9 + 12 · 5 = 78.', 'V = 45; S = 78.'),
  TK(('Пирамида', 'Pyramid'), ('Правильная четырёхугольная пирамида: a = 6, h = 4. Найдите V.', 'A regular quadrangular pyramid: a = 6, h = 4. Find V.'), '', '36 · 4 / 3 = 48.', '48.'),
  TK(('Апофема', 'Slant height'), ('Для той же пирамиды найдите апофему.', 'For the same pyramid find the slant height.'), 'r = a/2 = 3', 'l = √(16 + 9) = 5.', '5.'),
  TK(('Боковая', 'Lateral'), ('Боковая поверхность той же пирамиды.', 'The lateral surface of the same pyramid.'), '', 'P · l / 2 = 24 · 5 / 2 = 60.', '60.'),
  TK(('Отношение', 'Ratio'), ('Во сколько раз объём куба больше объёма пирамиды с тем же основанием и высотой?', 'How many times is a cube’s volume larger than that of a pyramid on the same base with the same height?'), '', 'В 3 раза.', ('В 3 раза.', '3 times.'))],
 [Q('V призмы =', 'V of a prism =', 'S · h', 'S · h / 3', 'P · h', ('Основание на высоту.', 'Base times height.')),
  Q('V пирамиды =', 'V of a pyramid =', 'S · h / 3', 'S · h', 'S · h / 2', ('Треть призмы.', 'A third of a prism.')),
  Q('Апофема — это', 'The slant height is', ('высота боковой грани', 'the height of a lateral face'), ('высота пирамиды', 'the height of the pyramid'), ('ребро основания', 'a base edge'), ('Определение.', 'The definition.')),
  Q('Боковая поверхность правильной пирамиды', 'The lateral surface of a regular pyramid', ('P·l/2', 'P·l/2'), ('P·h', 'P·h'), ('S·h/3', 'S·h/3'), ('Сумма треугольников.', 'A sum of triangles.')),
  Q('Куб можно разрезать на столько равных пирамид с общей вершиной:', 'A cube can be cut into how many equal pyramids with a common apex:', '3', '2', '4', ('Три пирамиды по 1/3.', 'Three pyramids of 1/3.')),
  Q('Сечение пирамиды, параллельное основанию, подобно', 'A section of a pyramid parallel to the base is similar to', ('основанию', 'the base'), ('боковой грани', 'a lateral face'), ('высоте', 'the height'), ('Подобие.', 'Similarity.')),
  Q('Площадь поверхности куба с ребром 2', 'The surface area of a cube with edge 2', '24', '8', '12', ('6 · 4.', '6 · 4.')),
  Q('Основание правильной пирамиды — правильный', 'The base of a regular pyramid is a regular', ('многоугольник', 'polygon'), ('круг', 'circle'), ('отрезок', 'segment'), ('Определение.', 'The definition.'))],
 src=[('Wikipedia: Prism (geometry)', 'https://en.wikipedia.org/wiki/Prism_(geometry)'), ('Wikipedia: Pyramid (geometry)', 'https://en.wikipedia.org/wiki/Pyramid_(geometry)'), ('Wikipedia: Cavalieri’s principle', 'https://en.wikipedia.org/wiki/Cavalieri%27s_principle')])
