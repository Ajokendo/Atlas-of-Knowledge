# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Теорема косинусов', 'The law of cosines'),
 [('r', 'a', 'Сторона a', 'Side a', 2, 12, 1, 7), ('r', 'b', 'Сторона b', 'Side b', 2, 12, 1, 5), ('r', 'C', 'Угол между ними, °', 'Included angle, °', 10, 170, 1, 60)],
 [('c² = a² + b² − 2ab·cos C', 'c² = a² + b² − 2ab·cos C'), ('Сторона c', 'Side c'), ('Вид угла C', 'Kind of angle C')],
 'Для угла 90° теорема косинусов превращается в теорему Пифагора. Для острого угла c короче, для тупого — длиннее.', 'For 90° the law of cosines becomes the Pythagorean theorem. For an acute angle c is shorter, for an obtuse one longer.', ('Треугольник по двум сторонам и углу', 'A triangle from two sides and an angle'),
 r'''const C0=deg(v.C),c2=v.a*v.a+v.b*v.b-2*v.a*v.b*Math.cos(C0),c=Math.sqrt(c2),T=[[0,0],[v.a,0],[v.b*Math.cos(C0),v.b*Math.sin(C0)]];const F=fitPts(T,110,15,380,180);
 let g=poly(F,"#f4dfd8",COL.ink,3)+arcA(F[0][0],F[0][1],34,0,C0,COL.a,5)+TX(F[0][0]+48,F[0][1]-10,v.C+"°",COL.a,14,"start",700)+TX((F[0][0]+F[1][0])/2,F[0][1]+17,"a = "+v.a,COL.b,13,"middle",600)+TX((F[0][0]+F[2][0])/2-10,(F[0][1]+F[2][1])/2,"b = "+v.b,COL.c,13,"end",600)+TX((F[1][0]+F[2][0])/2+10,(F[1][1]+F[2][1])/2-6,"c = "+fnum(c,2),COL.a,14,"start",700);
 return {svg:g,st:[fnum(c2,2)+" = "+v.a*v.a+" + "+v.b*v.b+" − "+fnum(2*v.a*v.b*Math.cos(C0),2),fnum(c,2),v.C<90?U("острый","acute"):v.C===90?U("прямой","right"):U("тупой","obtuse")],fb:v.C===90?U("При C = 90° получаем c² = a² + b².","At C = 90° we get c² = a² + b²."):U("Поправка −2ab·cos C "+(v.C<90?"уменьшает":"увеличивает")+" c².","The correction −2ab·cos C "+(v.C<90?"reduces":"increases")+" c².")}''', '0 0 600 215')

m2 = M(('Теорема синусов', 'The law of sines'),
 [('r', 'A', 'Угол A, °', 'Angle A, °', 20, 100, 1, 40), ('r', 'B', 'Угол B, °', 'Angle B, °', 20, 100, 1, 70), ('r', 'a', 'Сторона a (напротив A)', 'Side a (opposite A)', 3, 15, 1, 8)],
 [('Сторона b = a·sin B / sin A', 'Side b = a·sin B / sin A'), ('Угол C и сторона c', 'Angle C and side c'), ('Диаметр описанной окружности', 'Diameter of the circumscribed circle')],
 'Стороны треугольника пропорциональны синусам противолежащих углов: a/sin A = b/sin B = c/sin C = 2R.', 'The sides of a triangle are proportional to the sines of opposite angles: a/sin A = b/sin B = c/sin C = 2R.', ('Треугольник по стороне и двум углам', 'A triangle from a side and two angles'),
 r'''const B=Math.min(v.B,175-v.A),C0=180-v.A-B,k=v.a/Math.sin(deg(v.A)),b=k*Math.sin(deg(B)),c=k*Math.sin(deg(C0));const T=triSides(v.a,b,c);if(!T)return {svg:"",st:["—","—","—"],fb:""};const F=fitPts(T,110,32,380,160);
 let g=poly(F,"#f4dfd8",COL.ink,3);const nm=["A","B","C"],vals=[v.A,B,C0];
 // T: [0,0]=A? sides: c=AB, b=AC, a=BC ; angles by position
 const ang=[angAt(T,0),angAt(T,1),angAt(T,2)];ang.forEach((an,i)=>{g+=TX(F[i][0]+(i===0?-8:i===1?8:0),F[i][1]+(i===2?-12:18),nm[i]+" "+fnum(an,0)+"°",[COL.a,COL.b,COL.c][i],14,i===0?"end":i===1?"start":"middle",700)});
 return {svg:g,st:[fnum(b,2),C0+"°; "+fnum(c,2),fnum(k,2)],fb:U("Отношение сторона : синус одинаково для всех трёх сторон: "+fnum(k,2)+".","The ratio side : sine is the same for all three sides: "+fnum(k,2)+".")}''', '0 0 600 215')

m3 = M(('Два решения?', 'Two solutions?'),
 [('r', 'A', 'Угол A, °', 'Angle A, °', 15, 85, 1, 35), ('r', 'b', 'Сторона b', 'Side b', 4, 12, 1, 9), ('r', 'a', 'Сторона a', 'Side a', 2, 14, 1, 6)],
 [('Высота h = b·sin A', 'Altitude h = b·sin A'), ('Сколько треугольников', 'How many triangles'), ('Угол B', 'Angle B')],
 'Известны две стороны и угол, лежащий против одной из них. Окружность радиуса a с центром в C пересекает луч AB в 0, 1 или 2 точках.', 'Two sides and an angle opposite one of them are known. A circle of radius a centred at C meets the ray AB in 0, 1 or 2 points.', ('Окружность и луч', 'A circle and a ray'),
 r'''const A=deg(v.A),h=v.b*Math.sin(A),x0c=v.b*Math.cos(A),xmin=Math.min(0,x0c-v.a),xmax=Math.max(v.b*Math.cos(A)+v.a,v.b,0),ymin=Math.min(0,h-v.a),ymax=h+v.a,sc=Math.min(540/(xmax-xmin),190/(ymax-ymin)),ox=30-xmin*sc,oy=10+ymax*sc,P=(x,y)=>[ox+x*sc,oy-y*sc];const Cc=P(v.b*Math.cos(A),h);
 let g=L(10,oy,590,oy,COL.mut,2)+L(...P(0,0).concat(Cc),COL.ink,3)+C(P(0,0)[0],P(0,0)[1],5,COL.ink)+C(Cc[0],Cc[1],5,COL.ink)+'<circle cx="'+Cc[0]+'" cy="'+Cc[1]+'" r="'+v.a*sc+'" fill="none" stroke="'+COL.b+'" stroke-width="2" stroke-dasharray="6 5"/>';
 const d=v.a*v.a-h*h;let n=0,xs=[];const cx0=v.b*Math.cos(A);if(v.a>h+1e-9){const w=Math.sqrt(d);[cx0-w,cx0+w].forEach(x=>{if(x>1e-9)xs.push(x)})}else if(Math.abs(v.a-h)<1e-9)xs.push(cx0);
 xs.forEach((x,i)=>{const p=P(x,0);g+=C(p[0],p[1],7,[COL.a,COL.c][i])+L(Cc[0],Cc[1],p[0],p[1],[COL.a,COL.c][i],2.5)});
 n=xs.length;const Bs=xs.map(x=>{const B1=Math.atan2(h,cx0-x);return fnum(((B1<0?B1+Math.PI:B1)*180/Math.PI),1)+"°"});
 return {svg:g,st:[fnum(h,2),n+" "+(n===0?U("— не существует","— none"):n===1?U("треугольник","triangle"):U("треугольника","triangles")),n?Bs.join(U(" или "," or ")):"—"],fb:n===2?U("a больше высоты, но меньше b: оба решения подходят.","a is above the altitude but below b: both solutions fit."):n===1?U("Один треугольник.","One triangle."):U("Сторона a слишком мала: не достаёт до луча.","Side a is too short: it does not reach the ray.")}''', '0 0 600 215')

chapter('38', '38-sine-cosine-laws.html', 'V', ('Теоремы синусов и косинусов', 'The laws of sines and cosines'),
 ('Как решать любые треугольники — не только прямоугольные: найти расстояние через озеро, не пересекая его.', 'How to solve any triangle, not only right-angled: find the distance across a lake without crossing it.'),
 ('Нужно узнать ширину озера между точками A и B. Из точки C на берегу измерили расстояния: CA = 7 км, CB = 5 км, а угол ACB равен 60°.\n\nКакова ширина озера?', 'We need the width of a lake between points A and B. From a point C on the shore the distances CA = 7 km and CB = 5 km were measured and the angle ACB is 60°.\n\nWhat is the width of the lake?'),
 ('Разгадка: √39 ≈ 6,24 км', 'The answer: √39 ≈ 6.24 km'),
 ('Две стороны и угол между ними известны — подходит теорема косинусов: AB² = 7² + 5² − 2 · 7 · 5 · cos 60° = 49 + 25 − 35 = 39. Значит, AB = √39 ≈ 6,24 км. Мы нашли расстояние, которое нельзя измерить рулеткой: достаточно двух расстояний и угла.', 'Two sides and the included angle are known — the law of cosines fits: AB² = 7² + 5² − 2 · 7 · 5 · cos 60° = 49 + 25 − 35 = 39. So AB = √39 ≈ 6.24 km. We found a distance that cannot be measured with a tape: two distances and an angle are enough.'),
 [S('cos', 'Теорема косинусов', 'The law of cosines', ('В любом треугольнике <strong>c² = a² + b² − 2ab·cos C</strong>, где C — угол между сторонами a и b. При C = 90° получается теорема Пифагора. Теорема позволяет найти третью сторону по двум и углу между ними, а также угол по трём сторонам: cos C = (a² + b² − c²) / 2ab.', 'In any triangle <strong>c² = a² + b² − 2ab·cos C</strong> where C is the angle between sides a and b. At C = 90° it gives the Pythagorean theorem. It lets us find the third side from two sides and the included angle, and an angle from three sides: cos C = (a² + b² − c²) / 2ab.'),
    ('c² = a² + b² − 2ab·cos C', '', 'c² = a² + b² − 2ab·cos C'), m1),
  S('sin', 'Теорема синусов', 'The law of sines', ('<strong>a / sin A = b / sin B = c / sin C = 2R</strong>, где R — радиус описанной окружности. По стороне и двум углам находим остальные стороны. Сумма углов 180° даёт третий угол.', '<strong>a / sin A = b / sin B = c / sin C = 2R</strong> where R is the radius of the circumscribed circle. From a side and two angles we find the other sides. The angle sum 180° gives the third angle.'),
    ('a / sin A = b / sin B', '= 2R', '= 2R'), m2),
  S('amb', 'Неоднозначный случай', 'The ambiguous case', ('Если известны две стороны и угол <em>против одной из них</em>, треугольников может быть 0, 1 или 2. Высота h = b·sin A: если a &lt; h — решений нет, a = h — одно (прямой угол), h &lt; a &lt; b — два, a ≥ b — одно.', 'If two sides and an angle <em>opposite one of them</em> are known, there may be 0, 1 or 2 triangles. The altitude h = b·sin A: if a &lt; h — none, a = h — one (a right angle), h &lt; a &lt; b — two, a ≥ b — one.'),
    ('h = b·sin A', '', 'h = b·sin A'), m3)],
 [TK(('Косинусов', 'Cosines'), ('a = 3, b = 4, угол между ними 90°. Найдите c.', 'a = 3, b = 4, the included angle 90°. Find c.'), 'cos 90° = 0', 'c² = 9 + 16 = 25, c = 5.', '5.'),
  TK(('Косинусов 60°', 'Cosines at 60°'), ('a = 8, b = 3, C = 60°. Найдите c.', 'a = 8, b = 3, C = 60°. Find c.'), 'cos 60° = 0,5', 'c² = 64 + 9 − 24 = 49, c = 7.', '7.'),
  TK(('Синусов', 'Sines'), ('A = 30°, a = 5, B = 90°. Найдите b.', 'A = 30°, a = 5, B = 90°. Find b.'), 'sin 30° = 0,5, sin 90° = 1', 'b = 5 · 1 : 0,5 = 10.', '10.'),
  TK(('Угол по сторонам', 'An angle from sides'), ('Стороны 5, 5, 5. Найдите угол.', 'Sides 5, 5, 5. Find an angle.'), 'cos C = (25 + 25 − 25)/50', 'cos C = 0,5, C = 60°.', '60°.'),
  TK(('Сколько решений', 'How many solutions'), ('A = 30°, b = 10, a = 4. Сколько треугольников?', 'A = 30°, b = 10, a = 4. How many triangles?'), 'h = 10 · 0,5 = 5', 'a = 4 &lt; 5 = h — треугольников нет.', ('Нет.', 'None.'))],
 [Q('Теорема косинусов для угла 90° — это', 'The law of cosines at 90° is', ('теорема Пифагора', 'the Pythagorean theorem'), ('теорема синусов', 'the law of sines'), ('признак равенства', 'a congruence test'), ('cos 90° = 0.', 'cos 90° = 0.')),
  Q('По двум сторонам и углу между ними лучше', 'From two sides and the included angle it is best to use', ('теорему косинусов', 'the law of cosines'), ('теорему синусов', 'the law of sines'), ('теорему Фалеса', 'Thales’ theorem'), ('Находим третью сторону.', 'We find the third side.')),
  Q('a/sin A =', 'a/sin A =', 'b/sin B', 'b·sin B', 'sin A/a', ('Теорема синусов.', 'The law of sines.')),
  Q('Что такое R в 2R?', 'What is R in 2R?', ('радиус описанной окружности', 'the circumradius'), ('радиус вписанной окружности', 'the inradius'), ('периметр', 'the perimeter'), ('Расширенная теорема синусов.', 'The extended law of sines.')),
  Q('Для тупого угла C величина −2ab·cos C', 'For an obtuse angle C the term −2ab·cos C is', ('положительна', 'positive'), ('отрицательна', 'negative'), ('равна нулю', 'zero'), ('cos C &lt; 0.', 'cos C &lt; 0.')),
  Q('При неоднозначном случае решений может быть', 'In the ambiguous case the number of solutions can be', ('0, 1 или 2', '0, 1 or 2'), ('только 1', 'only 1'), ('3', '3'), ('Окружность и луч.', 'A circle and a ray.')),
  Q('Углы 50° и 60°. Третий', 'Angles 50° and 60°. The third', '70°', '80°', '110°', ('180° − 110°.', '180° − 110°.')),
  Q('cos C = (a² + b² − c²)/2ab нужна, чтобы найти', 'cos C = (a² + b² − c²)/2ab is used to find', ('угол по трём сторонам', 'an angle from three sides'), ('площадь', 'the area'), ('периметр', 'the perimeter'), ('Выражаем cos C.', 'We solve for cos C.'))],
 src=[('Wikipedia: Law of cosines', 'https://en.wikipedia.org/wiki/Law_of_cosines'), ('Wikipedia: Law of sines', 'https://en.wikipedia.org/wiki/Law_of_sines')],
 note=('Озеро и расстояния в загадке условные.', 'The lake and distances in the puzzle are illustrative.'))
