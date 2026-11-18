# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Отрезок, луч, прямая', 'Segment, ray, line'),
 [('s', 't', 'Что рисуем', 'What we draw', ['Отрезок', 'Луч', 'Прямая'], ['Segment', 'Ray', 'Line'], 0), ('r', 'b', 'Положение точки B (см)', 'Position of point B (cm)', 2, 9, 1, 6)],
 [('Есть ли начало', 'Is there a start'), ('Есть ли конец', 'Is there an end'), ('Длина', 'Length')],
 'Точка A стоит на отметке 1 см. Отрезок можно измерить, луч и прямая бесконечны.', 'Point A stands at the 1 cm mark. A segment can be measured; a ray and a line go on for ever.', ('Линейка с точками A и B', 'A ruler with points A and B'),
 r'''const t=v.t,A=1,B=v.b,X=i=>40+i*52,y=115;let g="";
 if(t===0)g+=L(X(A),y,X(B),y,COL.a,5);else if(t===1)g+=L(X(A),y,X(B),y,COL.a,5)+arrow(X(B),y,578,y,COL.a,5);else g+=L(X(A),y,X(B),y,COL.a,5)+arrow(X(B),y,578,y,COL.a,5)+arrow(X(A),y,22,y,COL.a,5);
 g+=L(40,170,560,170,COL.mut,1.5);for(let i=0;i<=10;i++)g+=L(X(i),165,X(i),177,COL.mut,1.5)+TX(X(i),196,i,COL.mut,11);
 g+=C(X(A),y,8,COL.ink)+TX(X(A),y-18,"A",COL.ink,18,"middle",600)+C(X(B),y,8,COL.ink)+TX(X(B),y-18,"B",COL.ink,18,"middle",600);
 const no=U("нет","no"),yes=U("есть: точка ","yes: point ");
 return {svg:g,st:[t===2?no:yes+"A",t===0?yes+"B":no,t===0?(B-A)+U(" см"," cm"):U("измерить нельзя","cannot be measured")],
 fb:t===0?U("Отрезок AB: у него два конца, длина "+(B-A)+" см.","Segment AB has two ends; its length is "+(B-A)+" cm."):t===1?U("Луч AB: начинается в точке A и уходит через B в бесконечность.","Ray AB starts at A and goes through B to infinity."):U("Прямая AB: нет ни начала, ни конца, она бесконечна в обе стороны.","Line AB has no start and no end; it is infinite in both directions.")}''')

m2 = M(('Угол', 'Angle'),
 [('r', 'a', 'Угол (градусы)', 'Angle (degrees)', 5, 180, 5, 60)],
 [('Величина', 'Size'), ('Вид угла', 'Kind of angle'), ('До прямого угла не хватает', 'Short of a right angle by'), ('До развёрнутого', 'Short of a straight angle by')],
 'Угол образуют два луча с общим началом. Мера угла — в градусах: прямой угол 90°, развёрнутый 180°.', 'An angle is made by two rays with a common start. Angles are measured in degrees: a right angle is 90°, a straight angle 180°.', ('Угол между двумя лучами', 'An angle between two rays'),
 r'''const a=v.a,cx=110,cy=200,R=150;const p=d=>[cx+R*Math.cos(deg(d)),cy-R*Math.sin(deg(d))],e=p(a);let g=L(cx,cy,cx+R,cy,COL.ink,4)+L(cx,cy,e[0],e[1],COL.ink,4);
 if(a===90)g+=poly([[cx,cy],[cx+28,cy],[cx+28,cy-28],[cx,cy-28]],"#f4dfd8",COL.a,2);else g+=arcA(cx,cy,55,0,deg(a),COL.a,4);
 g+=TX(cx+90*Math.cos(deg(a/2)),cy-90*Math.sin(deg(a/2))+5,a+"°",COL.a,20,"middle",600)+C(cx,cy,5,COL.ink);
 const k=a<90?U("острый","acute"):a===90?U("прямой","right"):a<180?U("тупой","obtuse"):U("развёрнутый","straight");
 return {svg:g,st:[a+"°",k,a<=90?(90-a)+"°":"—",(180-a)+"°"],fb:a<90?U("Острый угол меньше прямого.","An acute angle is smaller than a right angle."):a===90?U("Прямой угол — как угол листа бумаги.","A right angle is like the corner of a sheet of paper."):a<180?U("Тупой угол больше прямого, но меньше развёрнутого.","An obtuse angle is bigger than a right angle but smaller than a straight one."):U("Развёрнутый угол: лучи образуют прямую.","A straight angle: the rays form a line.")}''')

m3 = M(('Многоугольники', 'Polygons'),
 [('r', 'n', 'Число сторон', 'Number of sides', 3, 8, 1, 5)],
 [('Сторон = углов = вершин', 'Sides = angles = vertices'), ('Название', 'Name'), ('Диагоналей', 'Diagonals'), ('Сумма углов', 'Sum of angles')],
 'Диагональ соединяет две вершины, которые не соседние. Из одной вершины их выходит на 3 меньше, чем сторон.', 'A diagonal joins two vertices that are not neighbours. From one vertex there are 3 fewer diagonals than sides.', ('Правильный многоугольник с диагоналями из одной вершины', 'A regular polygon with the diagonals from one vertex'),
 r'''const n=v.n,cx=300,cy=128,R=100;const P=[];for(let i=0;i<n;i++){const a=Math.PI/2+i*2*Math.PI/n;P.push([cx+R*Math.cos(a),cy-R*Math.sin(a)])}
 let g=poly(P,"#f4dfd8",COL.ink,3);for(let i=2;i<n-1;i++)g+=L(P[0][0],P[0][1],P[i][0],P[i][1],COL.b,2);P.forEach((p,i)=>{g+=C(p[0],p[1],5,COL.a)});
 const names=U(["","","","треугольник","четырёхугольник","пятиугольник","шестиугольник","семиугольник","восьмиугольник"],["","","","triangle","quadrilateral","pentagon","hexagon","heptagon","octagon"]);
 return {svg:g,st:[n,names[n],n*(n-3)/2,(n-2)*180+"°"],fb:U("Из одной вершины выходит "+(n-3)+" диагонал"+(n-3===1?"ь":(n-3<5&&n>3?"и":"ей"))+" (показаны синим); всего "+(n*(n-3)/2)+".","From one vertex there are "+(n-3)+" diagonals (blue); "+(n*(n-3)/2)+" in all.")}''')

chapter('09', '09-points-lines-angles.html', 'II', ('Точки, линии, углы, фигуры', 'Points, lines, angles, shapes'),
 ('Сколько прямых проходит через две точки, какие бывают углы и как называют многоугольники.', 'How many lines pass through two points, what kinds of angles there are and how polygons are named.'),
 ('Чабан Эрлан вбил в землю колышек и натянул вдоль него верёвку. Потом вбил второй колышек.\n\nСколько разных прямых верёвок можно натянуть через один колышек? А через два?', 'The shepherd Erlan drove a peg into the ground and stretched a rope along it. Then he drove a second peg.\n\nHow many different straight ropes can be stretched through one peg? And through two?'),
 ('Разгадка: бесконечно много и ровно одна', 'The answer: infinitely many and exactly one'),
 ('Через одну точку можно провести бесконечно много прямых: верёвку можно повернуть как угодно. Через две точки проходит **ровно одна** прямая. Поэтому два колышка сразу задают направление ряда — так строители и садоводы выравнивают борозды и стены.'.replace('**', ''), 'Through one point you can draw infinitely many lines: the rope can be turned any way. Through two points there passes **exactly one** line. That is why two pegs fix the direction of a row at once — builders and gardeners use it to line up furrows and walls.'.replace('**', '')),
 [S('line', 'Точка, отрезок, луч, прямая', 'Point, segment, ray, line',
    ('<strong>Точка</strong> не имеет размеров. <strong>Прямая</strong> бесконечна в обе стороны. <strong>Луч</strong> имеет начало и бесконечен в одну сторону. <strong>Отрезок</strong> ограничен двумя точками — его можно измерить.\n\nЧерез две точки проходит ровно одна прямая; отрезок между ними — кратчайший путь.', 'A <strong>point</strong> has no size. A <strong>line</strong> is infinite in both directions. A <strong>ray</strong> has a start and is infinite one way. A <strong>segment</strong> is bounded by two points — it can be measured.\n\nThrough two points there passes exactly one line; the segment between them is the shortest path.'),
    ('отрезок AB', 'длина измеряется в см, м, км', 'segment AB: its length is measured in cm, m, km'), m1),
  S('angle', 'Угол', 'Angle',
    ('Два луча с общим началом образуют <strong>угол</strong>. Углы бывают <strong>острые</strong> (меньше 90°), <strong>прямые</strong> (90°), <strong>тупые</strong> (от 90° до 180°) и <strong>развёрнутые</strong> (180°). Измеряют угол транспортиром.', 'Two rays with a common start form an <strong>angle</strong>. Angles are <strong>acute</strong> (under 90°), <strong>right</strong> (90°), <strong>obtuse</strong> (between 90° and 180°) and <strong>straight</strong> (180°). We measure an angle with a protractor.'),
    ('90° + 90° = 180°', 'два прямых угла дают развёрнутый', 'two right angles make a straight angle'), m2),
  S('shapes', 'Многоугольники', 'Polygons',
    ('<strong>Многоугольник</strong> — замкнутая ломаная линия. У него столько же углов, сколько сторон. Название зависит от числа углов: три — треугольник, четыре — четырёхугольник, пять — пятиугольник и так далее.\n\nСумма углов многоугольника с <em>n</em> сторонами равна (n − 2) · 180°.', 'A <strong>polygon</strong> is a closed broken line. It has as many angles as sides. The name depends on the number of angles: three — a triangle, four — a quadrilateral, five — a pentagon and so on.\n\nThe angles of a polygon with <em>n</em> sides add up to (n − 2) · 180°.'),
    ('(n − 2) · 180°', 'сумма углов n-угольника', 'the sum of the angles of an n-gon'), m3)],
 [TK(('Измерить отрезок', 'Measure a segment'), ('Точка A на отметке 1 см, точка B на отметке 7 см. Найдите длину отрезка AB.', 'Point A is at 1 cm and point B at 7 cm. Find the length of segment AB.'), ('A = 1 см, B = 7 см', 'A = 1 cm, B = 7 cm'), '7 − 1 = 6.', ('6 см.', '6 cm.')),
  TK(('Вид угла', 'Kind of angle'), ('Какой это угол: 35°, 90°, 120°, 180°?', 'What kind of angle is it: 35°, 90°, 120°, 180°?'), '35°, 90°, 120°, 180°', ('35° &lt; 90° — острый; 90° — прямой; 90° &lt; 120° &lt; 180° — тупой; 180° — развёрнутый.', '35° &lt; 90° — acute; 90° — right; 90° &lt; 120° &lt; 180° — obtuse; 180° — straight.'), ('Острый, прямой, тупой, развёрнутый.', 'Acute, right, obtuse, straight.')),
  TK(('Дополнить до прямого', 'Complete to a right angle'), ('Один из двух углов, составляющих прямой угол, равен 65°. Чему равен второй?', 'One of two angles that make a right angle is 65°. What is the other?'), '65° + ? = 90°', '90° − 65° = 25°.', '25°.'),
  TK(('Диагонали шестиугольника', 'Diagonals of a hexagon'), ('Сколько всего диагоналей у шестиугольника?', 'How many diagonals does a hexagon have in all?'), 'n = 6', ('n(n − 3)/2 = 6 · 3 / 2 = 9. Проверка: из каждой вершины 3 диагонали, 6 · 3 = 18, но каждую посчитали дважды: 18 : 2 = 9.', 'n(n − 3)/2 = 6 · 3 / 2 = 9. Check: 3 diagonals from each vertex, 6 · 3 = 18, but each is counted twice: 18 : 2 = 9.'), ('9 диагоналей.', '9 diagonals.')),
  TK(('Сумма углов', 'Sum of angles'), ('Найдите сумму углов пятиугольника.', 'Find the sum of the angles of a pentagon.'), 'n = 5', '(5 − 2) · 180° = 3 · 180° = 540°.', '540°.')],
 [Q('Сколько прямых проходит через две разные точки?', 'How many lines pass through two different points?', 'Ровно одна', 'Две', 'Бесконечно много', ('Через две точки проходит единственная прямая.', 'Through two points passes a single line.')),
  Q('Что можно измерить: отрезок, луч или прямую?', 'What can be measured: a segment, a ray or a line?', ('Отрезок', 'A segment'), ('Луч', 'A ray'), ('Прямую', 'A line'), ('У отрезка два конца, и его длина конечна.', 'A segment has two ends and a finite length.')),
  Q('Какой угол равен 90°?', 'Which angle is 90°?', ('Прямой', 'Right'), ('Острый', 'Acute'), ('Тупой', 'Obtuse'), ('Прямой угол — 90°.', 'A right angle is 90°.')),
  Q('Какой угол 120°?', 'What kind of angle is 120°?', ('Тупой', 'Obtuse'), ('Острый', 'Acute'), ('Прямой', 'Right'), ('120° больше 90°, но меньше 180°.', '120° is more than 90° but less than 180°.')),
  Q('Сколько углов у шестиугольника?', 'How many angles does a hexagon have?', '6', '5', '8', ('Столько же, сколько сторон.', 'As many as sides.')),
  Q('Сумма углов четырёхугольника', 'The sum of the angles of a quadrilateral', '360°', '180°', '270°', ('(4 − 2) · 180° = 360°.', '(4 − 2) · 180° = 360°.')),
  Q('Сколько диагоналей у четырёхугольника?', 'How many diagonals does a quadrilateral have?', '2', '4', '1', ('4 · 1 / 2 = 2.', '4 · 1 / 2 = 2.')),
  Q('Два угла в сумме дают развёрнутый. Один 110°. Другой?', 'Two angles add up to a straight angle. One is 110°. The other?', '70°', '80°', '250°', ('180° − 110° = 70°.', '180° − 110° = 70°.'))],
 src=[('Wikipedia: Angle', 'https://en.wikipedia.org/wiki/Angle'), ('Wikipedia: Polygon', 'https://en.wikipedia.org/wiki/Polygon')])
