# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Площадь треугольника', 'The area of a triangle'),
 [('r', 'b', 'Основание', 'Base', 2, 12, 1, 8), ('r', 'h', 'Высота', 'Height', 1, 8, 1, 5), ('r', 'sh', 'Сдвиг вершины', 'Shift of the apex', -6, 6, 1, 2)],
 [('Площадь ½·b·h', 'Area ½·b·h'), ('Площадь параллелограмма b·h', 'Area of the parallelogram b·h'), ('Что не меняется при сдвиге', 'What does not change when shifting')],
 'Двигая вершину вдоль линии, параллельной основанию, мы не меняем высоту — а значит, и площадь.', 'Moving the apex along a line parallel to the base keeps the height — so the area stays.', ('Треугольник и достроенный параллелограмм', 'A triangle and its completed parallelogram'),
 r'''const b=v.b,h=v.h,sh=v.sh;const xs=[0,b,sh,sh-b],all=[[0,0],[b,0],[sh,h]],P=fitPts([[0,0],[b,0],[sh,h],[Math.min(0,sh),0],[Math.max(b,sh+b),0]],60,15,480,160),sc=P[1][0]-P[0][0];
 const k=Math.min(480/(Math.max(b,sh+b)-Math.min(0,sh)),160/h),ox=60+(480-(Math.max(b,sh+b)-Math.min(0,sh))*k)/2-Math.min(0,sh)*k,oy=175;
 const X=t=>ox+t*k,Y=t=>oy-t*k;let g=poly([[X(0),Y(0)],[X(b),Y(0)],[X(sh+b),Y(h)],[X(sh),Y(h)]],"#fdf0c8",COL.mut,1.5)+poly([[X(0),Y(0)],[X(b),Y(0)],[X(sh),Y(h)]],"#f4dfd8",COL.ink,3)+L(X(sh),Y(h),X(sh),Y(0),COL.b,2)+TX(X(sh)+8,Y(h/2),"h = "+h,COL.b,13,"start",600)+TX(X(b/2),Y(0)+17,"b = "+b,COL.a,13,"middle",600);
 return {svg:g,st:[fnum(0.5*b*h,1),b*h,U("высота и основание","the height and the base")],fb:U("Треугольник — ровно половина параллелограмма с тем же основанием и высотой.","A triangle is exactly half of a parallelogram with the same base and height.")}''', '0 0 600 200')

m2 = M(('Площадь трапеции', 'The area of a trapezoid'),
 [('r', 'a', 'Нижнее основание', 'Lower base', 4, 14, 1, 10), ('r', 'c', 'Верхнее основание', 'Upper base', 2, 12, 1, 5), ('r', 'h', 'Высота', 'Height', 2, 8, 1, 4)],
 [('Средняя линия', 'The midline'), ('Площадь ½(a + c)·h', 'Area ½(a + c)·h'), ('Две трапеции = параллелограмм', 'Two trapezoids = a parallelogram')],
 'Две одинаковые трапеции складываются в параллелограмм с основанием a + c. Площадь трапеции — половина его площади.', 'Two identical trapezoids make a parallelogram with base a + c. The trapezoid’s area is half of it.', ('Трапеция и её копия', 'A trapezoid and its copy'),
 r'''const a=v.a,c=Math.min(v.c,a-1),h=v.h,k=Math.min(500/(2*a),150/h/1.3),o=(a-c)/2,ox=50,oy=170;
 const X=t=>ox+t*k,Y=t=>oy-t*k;let g=poly([[X(0),Y(0)],[X(a),Y(0)],[X(a-o),Y(h)],[X(o),Y(h)]],"#f4dfd8",COL.ink,3)+poly([[X(2*a-o),Y(h)],[X(a-o),Y(h)],[X(a),Y(0)],[X(2*a-2*o),Y(0)]],"#dbe5f2",COL.ink,3);
 g+=TX(X(a/2),Y(0)+17,"a = "+a,COL.a,13,"middle",600)+TX(X(a/2),Y(h)-6,"c = "+c,COL.b,13,"middle",600)+L(X(o/2),Y(h/2),X(a-o/2),Y(h/2),COL.c,2.5);
 return {svg:g,st:[fnum((a+c)/2,1),fnum((a+c)*h/2,1),(a+c)+" × "+h+" = "+(a+c)*h],fb:U("S = средняя линия × высота.","S = midline × height.")}''', '0 0 600 205')

m3 = M(('Сектор круга', 'A circle sector'),
 [('r', 'r', 'Радиус', 'Radius', 2, 10, 1, 6), ('r', 'th', 'Угол сектора, °', 'Sector angle, °', 10, 360, 5, 90)],
 [('Площадь сектора', 'Sector area'), ('Длина дуги', 'Arc length'), ('Доля круга', 'Part of the disc')],
 'Сектор — часть круга. Его площадь и длина дуги составляют долю θ/360° от целого.', 'A sector is a part of a disc. Its area and arc length are the fraction θ/360° of the whole.', ('Сектор круга', 'A sector of a disc'),
 r'''const R0=90,cx=250,cy=105,a=deg(v.th),e=Math.min(deg(v.th),2*Math.PI-1e-4);let g=C(cx,cy,R0,COL.bg,COL.line,2);
 const x1=cx+R0,y1=cy,x2=cx+R0*Math.cos(e),y2=cy-R0*Math.sin(e);g+='<path d="M'+cx+" "+cy+" L"+x1+" "+y1+" A"+R0+" "+R0+" 0 "+(v.th>180?1:0)+" 0 "+x2.toFixed(1)+" "+y2.toFixed(1)+' Z" fill="#f4dfd8" stroke="'+COL.a+'" stroke-width="3"/>';
 g+=TX(cx+30,cy-8,v.th+"°",COL.a,15,"start",700)+TX(430,90,fnum(v.th/360*100,1)+" %",COL.a,26,"start",700)+TX(430,120,U("круга","of the disc"),COL.mut,14,"start");
 return {svg:g,st:[fnum(v.th/360*Math.PI*v.r*v.r,2),fnum(v.th/360*2*Math.PI*v.r,2),frStr(v.th,360)+" = "+fnum(v.th/360,3)],fb:U("При θ = 360° сектор — весь круг: πr².","At θ = 360° the sector is the whole disc: πr².")}''', '0 0 600 215')

chapter('34', '34-areas.html', 'V', ('Площади фигур', 'Areas of figures'),
 ('Как находить площади треугольника, параллелограмма, трапеции, круга и его сектора.', 'How to find the areas of a triangle, parallelogram, trapezoid, disc and its sector.'),
 ('Участок земли имеет форму трапеции: параллельные стороны 30 м и 50 м, расстояние между ними 20 м.\n\nСколько квадратных метров занимает участок?', 'A plot of land is shaped like a trapezoid: parallel sides 30 m and 50 m, 20 m between them.\n\nHow many square metres does the plot cover?'),
 ('Разгадка: 800 м²', 'The answer: 800 m²'),
 ('Площадь трапеции равна полусумме оснований, умноженной на высоту: (30 + 50) : 2 · 20 = 40 · 20 = 800 м². Почему так? Две такие трапеции, приставленные друг к другу, образуют параллелограмм с основанием 80 м и высотой 20 м, его площадь 1 600 м² — половина даёт 800.', 'The area of a trapezoid is half the sum of the bases times the height: (30 + 50) : 2 · 20 = 40 · 20 = 800 m². Why? Two such trapezoids joined make a parallelogram with base 80 m and height 20 m; its area is 1,600 m² — half is 800.'),
 [S('tri', 'Треугольник и параллелограмм', 'Triangle and parallelogram', ('Площадь прямоугольника S = a·b. Площадь параллелограмма S = a·h, где h — высота к стороне a (отрезок, перпендикулярный ей). Площадь треугольника S = ½·a·h. Треугольники с одинаковыми основанием и высотой имеют одинаковую площадь, как бы ни была сдвинута вершина.', 'The area of a rectangle S = a·b. The area of a parallelogram S = a·h where h is the height to side a (a segment perpendicular to it). The area of a triangle S = ½·a·h. Triangles with the same base and height have the same area however the apex is shifted.'),
    ('S = ½·a·h', '', 'S = ½·a·h'), m1),
  S('trap', 'Трапеция', 'Trapezoid', ('Площадь трапеции с основаниями a и c и высотой h: S = (a + c)/2 · h. То есть «средняя линия на высоту». Формула следует из площади параллелограмма, составленного из двух трапеций.', 'The area of a trapezoid with bases a and c and height h: S = (a + c)/2 · h, i.e. “midline times height”. The formula follows from the area of the parallelogram made of two trapezoids.'),
    ('S = (a + c)/2 · h', '', 'S = (a + c)/2 · h'), m2),
  S('circ', 'Круг и сектор', 'Disc and sector', ('Площадь круга S = πr². Сектор с центральным углом θ° составляет θ/360 круга: S = θ/360 · πr², длина дуги l = θ/360 · 2πr. Единицы площади — квадратные: м², см², км²; 1 га = 10 000 м².', 'The area of a disc S = πr². A sector with central angle θ° is θ/360 of the disc: S = θ/360 · πr², the arc length l = θ/360 · 2πr. Units of area are square: m², cm², km²; 1 hectare = 10,000 m².'),
    ('S = θ/360 · πr²', '', 'S = θ/360 · πr²'), m3)],
 [TK(('Треугольник', 'Triangle'), ('Основание 14, высота 6. Площадь?', 'Base 14, height 6. The area?'), '', '½ · 14 · 6 = 42.', '42.'),
  TK(('Параллелограмм', 'Parallelogram'), ('Сторона 9 и высота к ней 4. Площадь?', 'A side 9 and the height to it 4. The area?'), '', '9 · 4 = 36.', '36.'),
  TK(('Трапеция', 'Trapezoid'), ('Основания 7 и 13, высота 5. Площадь?', 'Bases 7 and 13, height 5. The area?'), '', '(7 + 13) : 2 · 5 = 50.', '50.'),
  TK(('Сектор', 'Sector'), ('Радиус 6, угол 60°. Площадь сектора (π ≈ 3,14)?', 'Radius 6, angle 60°. The sector area (π ≈ 3.14)?'), 'Доля 1/6', '3,14 · 36 : 6 = 18,84.', '18,84.'),
  TK(('Составная фигура', 'A composite figure'), ('Прямоугольник 10 × 6, из него вырезан квадрат со стороной 2. Площадь?', 'A 10 × 6 rectangle with a square of side 2 cut out. The area?'), '', '60 − 4 = 56.', '56.')],
 [Q('Площадь треугольника', 'The area of a triangle', '½·a·h', 'a·h', 'a + h', ('Половина параллелограмма.', 'Half a parallelogram.')),
  Q('Треугольник с основанием 10 и высотой 4', 'A triangle with base 10 and height 4', '20', '40', '14', ('½ · 10 · 4.', '½ · 10 · 4.')),
  Q('Площадь круга радиуса 3 (через π)', 'The area of a disc of radius 3 (in π)', '9π', '6π', '3π', ('π · 3².', 'π · 3².')),
  Q('Единицы площади', 'The units of area', ('м²', 'm²'), ('м', 'm'), ('кг', 'kg'), ('Квадратные единицы.', 'Square units.')),
  Q('Площадь трапеции с основаниями 4, 6 и высотой 3', 'A trapezoid with bases 4, 6 and height 3', '15', '30', '10', ('5 · 3.', '5 · 3.')),
  Q('Сектор 90° — это', 'A 90° sector is', ('четверть круга', 'a quarter of the disc'), ('половина круга', 'half the disc'), ('треть круга', 'a third of the disc'), ('90/360.', '90/360.')),
  Q('Как изменится площадь квадрата, если сторону удвоить?', 'How does the area of a square change if the side is doubled?', ('станет в 4 раза больше', 'it becomes 4 times greater'), ('в 2 раза', '2 times'), ('не изменится', 'it does not change'), ('Площадь пропорциональна квадрату длины.', 'Area is proportional to the square of length.')),
  Q('1 гектар =', '1 hectare =', ('10 000 м²', '10,000 m²'), ('100 м²', '100 m²'), ('1 000 м²', '1,000 m²'), ('100 м × 100 м.', '100 m × 100 m.'))],
 src=[('Wikipedia: Area', 'https://en.wikipedia.org/wiki/Area'), ('Wikipedia: Trapezoid', 'https://en.wikipedia.org/wiki/Trapezoid')],
 note=('Участок в загадке придуман.', 'The plot in the puzzle is made up.'))
