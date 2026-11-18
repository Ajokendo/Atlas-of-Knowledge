# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Прямоугольник из квадратиков', 'A rectangle of squares'),
 [('r', 'a', 'Длина (клеток)', 'Length (squares)', 1, 12, 1, 8), ('r', 'b', 'Ширина (клеток)', 'Width (squares)', 1, 8, 1, 5)],
 [('Периметр P = 2(a + b)', 'Perimeter P = 2(a + b)'), ('Площадь S = a · b', 'Area S = a · b'), ('Квадратиков внутри', 'Squares inside')],
 'Периметр — длина границы (в клетках). Площадь — сколько квадратиков помещается внутри.', 'Perimeter is the length of the border (in squares). Area is how many squares fit inside.', ('Прямоугольник на клетчатой бумаге', 'A rectangle on squared paper'),
 r'''const a=v.a,b=v.b,s=Math.min(500/a,180/b),x0=300-a*s/2,y0=125-b*s/2;let g="";
 for(let i=0;i<a;i++)for(let j=0;j<b;j++)g+=R(x0+i*s,y0+j*s,s,s,"#f4dfd8",COL.line,1);
 g+=R(x0,y0,a*s,b*s,"none",COL.a,4)+TX(300,y0-6,String(a),COL.a,15,"middle",600)+TX(x0-12,125+5,String(b),COL.a,15,"middle",600);
 return {svg:g,st:[2*(a+b),a*b,a*b],fb:U("Забор вокруг: 2 · ("+a+" + "+b+") = "+2*(a+b)+". Земли внутри: "+a+" · "+b+" = "+a*b+" клеток.","Fence around: 2 · ("+a+" + "+b+") = "+2*(a+b)+". Ground inside: "+a+" · "+b+" = "+a*b+" squares.")}''')

m2 = M(('Участок с оградой 24 м', 'A plot with 24 m of fence'),
 [('r', 'w', 'Ширина участка (м)', 'Width of the plot (m)', 1, 11, 1, 3)],
 [('Ширина', 'Width'), ('Длина', 'Length'), ('Площадь', 'Area'), ('Наибольшая возможная площадь', 'Greatest possible area')],
 'Периметр всегда 24 м, поэтому сумма двух соседних сторон 12 м. Меняется только площадь.', 'The perimeter is always 24 m, so two neighbouring sides add up to 12 m. Only the area changes.', ('Прямоугольники с одним периметром и столбики площадей', 'Rectangles with one perimeter and bars of their areas'),
 r'''const w=v.w,h=12-w,S=w*h;let g=R(40,40,w*14,h*14,"#f4dfd8",COL.a,3)+TX(40+w*7,34,w+U(" м"," m"),COL.a,12,"middle",600)+TX(34,40+h*7+4,h+U(" м"," m"),COL.a,12,"end",600)+TX(40+w*7,40+h*7+5,S+U(" м²"," m²"),COL.ink,15,"middle",600);
 for(let i=1;i<=11;i++){const s=i*(12-i),x=270+(i-1)*29,hh=s/36*170;g+=R(x,215-hh,24,hh,i===w?COL.a:COL.b,"none",0,2)+TX(x+12,232,String(i),COL.mut,10)}
 g+=TX(430,36,U("площадь при ширине 1…11","area for widths 1…11"),COL.mut,11);
 return {svg:g,st:[w+U(" м"," m"),h+U(" м"," m"),S+U(" м²"," m²"),"36"+U(" м² (6 × 6)"," m² (6 × 6)")],fb:w===6?U("Квадрат: у него наибольшая площадь при данном периметре.","A square: it has the greatest area for a given perimeter."):U("Чем ближе участок к квадрату, тем больше его площадь.","The closer the plot is to a square, the greater its area.")}''')

m3 = M(('Одна площадь — разные периметры', 'One area — different perimeters'),
 [('s', 'A', 'Площадь', 'Area', ['12', '16', '24', '36'], ['12', '16', '24', '36'], 2), ('r', 'i', 'Вариант сторон', 'Choice of sides', 1, 5, 1, 1)],
 [('Стороны', 'Sides'), ('Периметр', 'Perimeter'), ('Наименьший периметр при этой площади', 'Smallest perimeter for this area')],
 'Прямоугольники с целыми сторонами и одной площадью. Выбирайте вариант и сравнивайте периметры.', 'Rectangles with whole-number sides and one area. Choose a variant and compare the perimeters.', ('Прямоугольник заданной площади', 'A rectangle of a given area'),
 r'''const A=[12,16,24,36][v.A],pairs=[];for(let d=1;d*d<=A;d++)if(A%d===0)pairs.push([d,A/d]);const i=Math.min(v.i,pairs.length)-1,[a,b]=pairs[i];
 const P=2*(a+b),best=Math.min(...pairs.map(p=>2*(p[0]+p[1])));const s=Math.min(520/b,180/a);
 let g=R(300-b*s/2,125-a*s/2,b*s,a*s,"#f4dfd8",COL.a,4)+TX(300,125+5,A+U(" м²"," m²"),COL.ink,22,"middle",600)+TX(300,125-a*s/2-8,String(b),COL.a,14,"middle",600)+TX(300-b*s/2-10,125+4,String(a),COL.a,14,"end",600);
 return {svg:g,st:[a+" × "+b,P,best],fb:P===best?U("Это самый «экономный» прямоугольник: у него наименьший периметр.","This is the most “economical” rectangle: it has the smallest perimeter."):U("Периметр "+P+" больше наименьшего ("+best+") — прямоугольник вытянут.","The perimeter "+P+" is more than the smallest ("+best+") — the rectangle is stretched out.")}''')

chapter('11', '11-perimeter-area.html', 'II', ('Периметр и площадь прямоугольника', 'Perimeter and area of a rectangle'),
 ('Сколько нужно забора и сколько получится земли — и почему это разные вопросы.', 'How much fence is needed and how much ground it gives — and why these are different questions.'),
 ('У Азата 24 метра сетки. Он хочет огородить прямоугольный участок так, чтобы внутри было как можно больше земли.\n\nКакие стороны выбрать?', 'Azat has 24 metres of netting. He wants to fence a rectangular plot with as much ground inside as possible.\n\nWhich sides should he choose?'),
 ('Разгадка: квадрат 6 × 6', 'The answer: a 6 × 6 square'),
 ('Две соседние стороны в сумме дают 12 м. Перебираем: 1 × 11 = 11 м², 2 × 10 = 20 м², 3 × 9 = 27, 4 × 8 = 32, 5 × 7 = 35 и 6 × 6 = 36 м². Наибольшая площадь — у квадрата 6 × 6. При одном и том же периметре «вытянутый» участок вмещает меньше земли.', 'Two neighbouring sides add up to 12 m. We try: 1 × 11 = 11 m², 2 × 10 = 20 m², 3 × 9 = 27, 4 × 8 = 32, 5 × 7 = 35 and 6 × 6 = 36 m². The greatest area belongs to the 6 × 6 square. For the same perimeter a “stretched” plot holds less ground.'),
 [S('pa', 'Периметр и площадь', 'Perimeter and area', ('<strong>Периметр</strong> — сумма длин всех сторон, то есть длина границы фигуры (забор, рамка, бордюр). Измеряется в см, м, км.\n\n<strong>Площадь</strong> — сколько единичных квадратов помещается внутри (земля, ковёр, пол). Измеряется в см², м², км².', 'The <strong>perimeter</strong> is the sum of the lengths of all sides, the length of the border of a figure (a fence, a frame, a kerb). It is measured in cm, m, km.\n\nThe <strong>area</strong> is how many unit squares fit inside (ground, a carpet, a floor). It is measured in cm², m², km².'),
    ('P = 2(a + b),   S = a · b', 'прямоугольник со сторонами a и b', 'a rectangle with sides a and b'), m1),
  S('fence', 'Один забор — разная площадь', 'One fence — different areas', ('Если длина забора одинакова, форма участка всё равно влияет на площадь. Из всех прямоугольников с данным периметром наибольшую площадь имеет <strong>квадрат</strong>. Вот почему огород делают не слишком вытянутым.', 'If the length of the fence is the same, the shape of the plot still affects the area. Of all rectangles with a given perimeter the <strong>square</strong> has the greatest area. That is why a garden is not made too stretched.'),
    ('a + b = 12 → S = a(12 − a)', 'наибольшая при a = 6', 'the greatest at a = 6'), m2),
  S('same', 'Одна площадь — разный забор', 'One area — different fences', ('Бывает и наоборот: прямоугольники одной площади могут иметь разные периметры. Участок 1 × 24 м ограждать надо 50 м сетки, а участок 4 × 6 м — только 20 м. Поэтому при одной площади выгоднее участок, близкий к квадрату.', 'It also happens the other way: rectangles of one area may have different perimeters. A 1 × 24 m plot needs 50 m of netting, while a 4 × 6 m plot needs only 20 m. So for one area a plot close to a square is cheaper to fence.'),
    ('4 · 6 = 24,  P = 20', '1 · 24 = 24,  P = 50', '1 · 24 = 24,  P = 50'), m3)],
 [TK(('Огород', 'A vegetable garden'), ('Огород 8 м на 5 м. Сколько нужно забора и какая площадь?', 'A garden is 8 m by 5 m. How much fence is needed and what is the area?'), 'a = 8 м, b = 5 м', 'P = 2 · (8 + 5) = 26 м. S = 8 · 5 = 40 м².', ('26 м забора, 40 м².', '26 m of fence, 40 m².')),
  TK(('Площадь по периметру', 'Area from perimeter'), ('Периметр прямоугольника 20 см, одна сторона 6 см. Найдите площадь.', 'A rectangle has perimeter 20 cm and one side 6 cm. Find the area.'), 'P = 20, a = 6', 'a + b = 20 : 2 = 10, значит b = 10 − 6 = 4. S = 6 · 4 = 24.', ('24 см².', '24 cm².')),
  TK(('Ковёр', 'A carpet'), ('Комната 4 м × 5 м. Сколько ковра нужно, чтобы покрыть пол, и сколько метров плинтуса вдоль стен?', 'A room is 4 m × 5 m. How much carpet covers the floor, and how many metres of skirting along the walls?'), '4 м × 5 м', 'Ковёр — это площадь: 4 · 5 = 20 м². Плинтус — это периметр: 2 · (4 + 5) = 18 м.', ('20 м² и 18 м.', '20 m² and 18 m.')),
  TK(('Квадрат', 'A square'), ('Сторона квадрата 7 см. Найдите периметр и площадь.', 'The side of a square is 7 cm. Find the perimeter and the area.'), 'a = 7 см', 'P = 4 · 7 = 28 см. S = 7 · 7 = 49 см².', ('28 см и 49 см².', '28 cm and 49 cm².')),
  TK(('Сколько квадратиков', 'How many tiles'), ('Пол 3 м на 4 м выложить плиткой 1 м на 1 м. Сколько плиток?', 'A floor 3 m by 4 m is to be tiled with 1 m by 1 m tiles. How many tiles?'), '3 м × 4 м', '3 · 4 = 12 плиток.', ('12.', '12.'))],
 [Q('Что такое периметр?', 'What is the perimeter?', ('Сумма длин всех сторон', 'The sum of the lengths of all sides'), ('Место внутри фигуры', 'The space inside the figure'), ('Длина диагонали', 'The length of a diagonal'), ('Периметр — длина границы.', 'The perimeter is the length of the border.')),
  Q('В каких единицах измеряют площадь?', 'In what units is area measured?', ('в квадратных (см², м²)', 'in square units (cm², m²)'), ('в метрах', 'in metres'), ('в килограммах', 'in kilograms'), ('Площадь — число квадратов.', 'Area is a number of squares.')),
  Q('Периметр прямоугольника 8 × 5', 'The perimeter of an 8 × 5 rectangle', '26', '40', '13', ('2 · (8 + 5) = 26.', '2 · (8 + 5) = 26.')),
  Q('Площадь прямоугольника 8 × 5', 'The area of an 8 × 5 rectangle', '40', '26', '13', ('8 · 5 = 40.', '8 · 5 = 40.')),
  Q('Какой прямоугольник с периметром 24 имеет наибольшую площадь?', 'Which rectangle with perimeter 24 has the greatest area?', ('Квадрат 6 × 6', 'The 6 × 6 square'), ('1 × 11', '1 × 11'), ('2 × 10', '2 × 10'), ('36 м² у квадрата против 11 и 20 у остальных.', '36 m² for the square versus 11 and 20.')),
  Q('Сторона квадрата 5. Его площадь?', 'The side of a square is 5. Its area?', '25', '20', '10', ('5 · 5 = 25.', '5 · 5 = 25.')),
  Q('Сколько плиток 1 × 1 нужно на пол 3 × 4?', 'How many 1 × 1 tiles are needed for a 3 × 4 floor?', '12', '14', '7', ('3 · 4 = 12.', '3 · 4 = 12.')),
  Q('Прямоугольник 4 × 6. Его периметр?', 'A 4 × 6 rectangle. Its perimeter?', '20', '24', '10', ('2 · (4 + 6) = 20.', '2 · (4 + 6) = 20.'))],
 src=[('Wikipedia: Perimeter', 'https://en.wikipedia.org/wiki/Perimeter'), ('Wikipedia: Area', 'https://en.wikipedia.org/wiki/Area')])
