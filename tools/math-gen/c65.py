# -*- coding: utf-8 -*-
from gen2 import *

EL = r'''function EL(cx,cy,rx,ry,fill,stroke,sw,dash){return '<ellipse cx="'+cx.toFixed(1)+'" cy="'+cy.toFixed(1)+'" rx="'+rx.toFixed(1)+'" ry="'+ry.toFixed(1)+'" fill="'+(fill||"none")+'" stroke="'+(stroke||"none")+'" stroke-width="'+(sw||1)+'"'+(dash?' stroke-dasharray="6 5"':"")+'/>'}
'''

m1 = M(('Цилиндр и его развёртка', 'A cylinder and its net'),
 [('r', 'r', 'Радиус r', 'Radius r', 1, 6, 1, 3), ('r', 'h', 'Высота h', 'Height h', 1, 10, 1, 6)],
 [('Объём V = πr²h', 'Volume V = πr²h'), ('Боковая поверхность 2πrh', 'Lateral surface 2πrh'), ('Полная поверхность', 'Total surface')],
 'Боковая поверхность цилиндра, развёрнутая на плоскость, — прямоугольник со сторонами 2πr (длина окружности) и h.', 'The lateral surface of a cylinder, unrolled onto a plane, is a rectangle with sides 2πr (the circumference) and h.', ('Цилиндр и боковая поверхность', 'The cylinder and its lateral surface'),
 EL + r'''const k=Math.min(30,480/(2*v.r+2*Math.PI*v.r),150/v.h),ry=0.3*v.r*k,cx=40+v.r*k,top=40+ry,bot=top+v.h*k;let g=EL(cx,bot,v.r*k,ry,COL.a+"22",COL.ink,2.5)+R(cx-v.r*k,top,2*v.r*k,v.h*k,COL.a+"22","none",0)+L(cx-v.r*k,top,cx-v.r*k,bot,COL.ink,2.5)+L(cx+v.r*k,top,cx+v.r*k,bot,COL.ink,2.5)+EL(cx,top,v.r*k,ry,COL.a+"44",COL.ink,2.5)+L(cx,top,cx+v.r*k,top,COL.b,3)+TX(cx+v.r*k/2,top-ry-6,"r",COL.b,14)+L(cx+v.r*k+14,top,cx+v.r*k+14,bot,COL.c,3)+TX(cx+v.r*k+28,(top+bot)/2,"h",COL.c,14);
 const x2=cx+v.r*k+80;g+=R(x2,top,2*Math.PI*v.r*k,v.h*k,COL.a+"33",COL.ink,2.5,0)+TX(x2+Math.PI*v.r*k,top+v.h*k+22,"2πr = "+fnum(2*Math.PI*v.r,2),COL.ink,14,"middle")+TX(x2+Math.PI*v.r*k,top+v.h*k/2,"S = "+fnum(2*Math.PI*v.r*v.h,1),COL.ink,15,"middle",700);
 return {svg:g,st:[fnum(Math.PI*v.r*v.r*v.h,2),fnum(2*Math.PI*v.r*v.h,2),fnum(2*Math.PI*v.r*(v.r+v.h),2)],fb:U("Две крышки добавляют 2πr² к боковой поверхности.","The two lids add 2πr² to the lateral surface.")}''', '0 0 600 250')

m2 = M(('Конус', 'A cone'),
 [('r', 'r', 'Радиус r', 'Radius r', 1, 8, 1, 3), ('r', 'h', 'Высота h', 'Height h', 1, 10, 1, 4)],
 [('Образующая l = √(r² + h²)', 'Slant l = √(r² + h²)'), ('Объём V = πr²h/3', 'Volume V = πr²h/3'), ('Развёртка — сектор', 'The net is a sector')],
 'Боковая поверхность конуса разворачивается в круговой сектор радиуса l с длиной дуги 2πr. Её площадь — πrl.', 'The lateral surface of a cone unrolls into a circular sector of radius l with arc length 2πr. Its area is πrl.', ('Конус и образующая', 'The cone and its slant'),
 EL + r'''const k=Math.min(28,190/Math.max(2*v.r,v.h)),ry=0.3*v.r*k,cx=170,bot=235-ry,apex=bot-v.h*k;let g=EL(cx,bot,v.r*k,ry,"none",COL.ink,2.5)+L(cx-v.r*k,bot,cx,apex,COL.ink,2.5)+L(cx+v.r*k,bot,cx,apex,COL.ink,2.5)+L(cx,apex,cx,bot,COL.c,3,0)+L(cx,bot,cx+v.r*k,bot,COL.b,3)+L(cx,apex,cx+v.r*k,bot,COL.a,3)+C(cx,apex,4,COL.ink);
 const l=Math.hypot(v.r,v.h),sec=360*v.r/l,ls=Math.min(l*k,170),sx=420,sy=60,a0=Math.PI/2+deg(sec)/2*-1;const a1=Math.PI/2-deg(sec)/2*-1;g+=L(sx,sy,sx+ls*Math.cos(Math.PI/2+deg(sec)/2),sy+ls*Math.sin(Math.PI/2+deg(sec)/2),COL.a,2.5)+L(sx,sy,sx+ls*Math.cos(Math.PI/2-deg(sec)/2),sy+ls*Math.sin(Math.PI/2-deg(sec)/2),COL.a,2.5);
 const pa=Math.PI/2-deg(sec)/2,pb=Math.PI/2+deg(sec)/2,big=sec>180?1:0;g+='<path d="M'+sx+" "+sy+" L"+(sx+ls*Math.cos(pa)).toFixed(1)+" "+(sy+ls*Math.sin(pa)).toFixed(1)+" A"+ls.toFixed(1)+" "+ls.toFixed(1)+" 0 "+big+" 1 "+(sx+ls*Math.cos(pb)).toFixed(1)+" "+(sy+ls*Math.sin(pb)).toFixed(1)+' Z" fill="'+COL.a+'33" stroke="'+COL.ink+'" stroke-width="2.5"/>'+TX(sx,sy+ls+22,fnum(sec,0)+"°",COL.ink,15,"middle",700);
 return {svg:g,st:[fnum(l,3),fnum(Math.PI*v.r*v.r*v.h/3,2),fnum(sec,1)+"°"],fb:U("Угол сектора = 360°·r/l: чем «острее» конус, тем уже сектор.","Sector angle = 360°·r/l: the sharper the cone, the narrower the sector.")}''', '0 0 600 260')

m3 = M(('Шар и сечение', 'A sphere and a section'),
 [('r', 'R', 'Радиус шара R', 'Radius R', 2, 10, 1, 8), ('r', 'd', 'Расстояние до плоскости d', 'Distance d to the plane', 0, 10, 1, 4)],
 [('Объём V = 4πR³/3', 'Volume V = 4πR³/3'), ('Площадь поверхности 4πR²', 'Surface area 4πR²'), ('Радиус сечения √(R² − d²)', 'Section radius √(R² − d²)')],
 'Сечение шара плоскостью — всегда круг. Его радиус r = √(R² − d²); при d = R плоскость касается шара, при d = 0 получаем большой круг.', 'A section of a sphere by a plane is always a circle. Its radius r = √(R² − d²); at d = R the plane touches the sphere, at d = 0 we get a great circle.', ('Шар и секущая плоскость', 'A sphere and a cutting plane'),
 EL + r'''const d=Math.min(v.d,v.R),k=100/v.R,cx=300,cy=130,rr=Math.sqrt(Math.max(0,v.R*v.R-d*d));let g=C(cx,cy,v.R*k,COL.a+"22",COL.ink,2.5)+EL(cx,cy,v.R*k,0.3*v.R*k,"none",COL.mut,1.5,true);const y=cy-d*k;g+=EL(cx,y,rr*k,0.3*rr*k,COL.b+"55",COL.b,3)+L(cx,cy,cx,y,COL.c,3)+L(cx,y,cx+rr*k,y,COL.b,3)+L(cx,cy,cx+rr*k,y,COL.ink,2)+C(cx,cy,3,COL.ink)+TX(cx+rr*k/2,y+(d>=v.R?-8:16),"r",COL.b,14)+TX(cx-12,(cy+y)/2,"d",COL.c,14);
 return {svg:g,st:[fnum(4*Math.PI*Math.pow(v.R,3)/3,1),fnum(4*Math.PI*v.R*v.R,1),fnum(rr,3)],fb:d>=v.R?U("d = R: плоскость касается шара в одной точке.","d = R: the plane touches the sphere at one point."):U("Прямоугольный треугольник: R — гипотенуза, d и r — катеты.","A right triangle: R is the hypotenuse, d and r are the legs.")}''', '0 0 600 265')

chapter('65', '65-round-solids.html', 'IX', ('Цилиндр, конус, шар', 'Cylinder, cone, sphere'),
 ('Тела вращения: объёмы, площади поверхностей, развёртки и сечения.', 'Solids of revolution: volumes, surface areas, nets and sections.'),
 ('Банка консервов — цилиндр. Почему её этикетка, снятая и разложенная, — прямоугольник, а этикетка на конусе-стаканчике мороженого — часть круга?', 'A tin can is a cylinder. Why is its label, taken off and laid flat, a rectangle, while the label on an ice-cream cone is part of a circle?'),
 ('Разгадка: цилиндр и конус развёртываются по-разному', 'The answer: a cylinder and a cone unroll differently'),
 ('Боковую поверхность цилиндра можно «разрезать по образующей» и выпрямить: получится прямоугольник 2πr × h. У конуса все образующие сходятся в вершине, поэтому развёртка — сектор круга радиуса l, длина дуги которого равна длине окружности основания 2πr. Шар же не развернуть на плоскость без растяжений — поэтому карты мира искажают размеры.', 'The lateral surface of a cylinder can be “cut along a generatrix” and straightened: a rectangle 2πr × h results. In a cone all generatrices meet at the apex, so the net is a sector of a circle of radius l whose arc length equals the base circumference 2πr. A sphere cannot be flattened without stretching — that is why world maps distort sizes.'),
 [S('cyl', 'Цилиндр', 'The cylinder', ('Прямой круговой цилиндр: радиус r, высота h. <strong>V = πr²h</strong>, <strong>S_бок = 2πrh</strong>, <strong>S = 2πr(r + h)</strong>. Осевое сечение — прямоугольник 2r × h.', 'A right circular cylinder: radius r, height h. <strong>V = πr²h</strong>, <strong>S_lat = 2πrh</strong>, <strong>S = 2πr(r + h)</strong>. The axial section is a rectangle 2r × h.'),
    ('V = πr²h', '', 'V = πr²h'), m1),
  S('cone', 'Конус', 'The cone', ('Образующая l = √(r² + h²). <strong>V = πr²h/3</strong>, <strong>S_бок = πrl</strong>, <strong>S = πr(r + l)</strong>. Осевое сечение — равнобедренный треугольник. Развёртка боковой поверхности — сектор с углом 360°·r/l.', 'The generatrix l = √(r² + h²). <strong>V = πr²h/3</strong>, <strong>S_lat = πrl</strong>, <strong>S = πr(r + l)</strong>. The axial section is an isosceles triangle. The net of the lateral surface is a sector with angle 360°·r/l.'),
    ('V = πr²h/3', '', 'V = πr²h/3'), m2),
  S('sph', 'Шар', 'The sphere', ('<strong>V = 4πR³/3</strong>, <strong>S = 4πR²</strong>. Любое сечение шара плоскостью — круг радиуса √(R² − d²). Шар, вписанный в цилиндр (высота 2R), занимает 2/3 его объёма — открытие Архимеда, которым он гордился.', '<strong>V = 4πR³/3</strong>, <strong>S = 4πR²</strong>. Any section of a sphere by a plane is a circle of radius √(R² − d²). A sphere inscribed in a cylinder (height 2R) takes 2/3 of its volume — a discovery of Archimedes of which he was proud.'),
    ('V = 4πR³/3', '', 'V = 4πR³/3'), m3)],
 [TK(('Цилиндр', 'Cylinder'), ('r = 2, h = 5. Найдите V (через π).', 'r = 2, h = 5. Find V (in terms of π).'), '', 'π · 4 · 5 = 20π.', '20π.'),
  TK(('Боковая', 'Lateral'), ('Боковая поверхность цилиндра r = 3, h = 4.', 'The lateral surface of a cylinder r = 3, h = 4.'), '', '2π · 3 · 4 = 24π.', '24π.'),
  TK(('Конус', 'Cone'), ('r = 3, h = 4. Найдите l и V.', 'r = 3, h = 4. Find l and V.'), '', 'l = 5; V = π · 9 · 4 / 3 = 12π.', 'l = 5; V = 12π.'),
  TK(('Шар', 'Sphere'), ('Объём шара R = 3.', 'The volume of a sphere R = 3.'), '', '4π · 27 / 3 = 36π.', '36π.'),
  TK(('Сечение', 'Section'), ('Радиус шара 5, плоскость на расстоянии 3. Радиус сечения?', 'A sphere of radius 5, a plane at distance 3. The section radius?'), '', '√(25 − 9) = 4.', '4.')],
 [Q('V цилиндра =', 'V of a cylinder =', 'πr²h', 'πrh', '2πrh', ('Основание на высоту.', 'Base times height.')),
  Q('Развёртка боковой поверхности цилиндра —', 'The net of a cylinder’s lateral surface is', ('прямоугольник', 'a rectangle'), ('круг', 'a circle'), ('сектор', 'a sector'), ('2πr × h.', '2πr × h.')),
  Q('V конуса =', 'V of a cone =', 'πr²h/3', 'πr²h', 'πrl', ('Треть цилиндра.', 'A third of the cylinder.')),
  Q('Развёртка конуса —', 'The net of a cone is', ('сектор', 'a sector'), ('прямоугольник', 'a rectangle'), ('треугольник', 'a triangle'), ('Радиус l.', 'Radius l.')),
  Q('S поверхности шара', 'The surface area of a sphere', '4πR²', 'πR²', '2πR²', ('Формула.', 'The formula.')),
  Q('Сечение шара плоскостью —', 'A section of a sphere by a plane is', ('круг', 'a circle'), ('эллипс', 'an ellipse'), ('квадрат', 'a square'), ('Всегда круг.', 'Always a circle.')),
  Q('Шар в цилиндре занимает объёма цилиндра', 'A sphere inscribed in a cylinder takes of its volume', '2/3', '1/2', '1/3', ('Открытие Архимеда.', 'Archimedes’ discovery.')),
  Q('l конуса при r = 6, h = 8', 'l of a cone at r = 6, h = 8', '10', '14', '7', ('√(36 + 64).', '√(36 + 64).'))],
 src=[('Wikipedia: Cylinder', 'https://en.wikipedia.org/wiki/Cylinder'), ('Wikipedia: Cone', 'https://en.wikipedia.org/wiki/Cone'), ('Wikipedia: Sphere', 'https://en.wikipedia.org/wiki/Sphere'), ('Wikipedia: On the Sphere and Cylinder', 'https://en.wikipedia.org/wiki/On_the_Sphere_and_Cylinder')])
