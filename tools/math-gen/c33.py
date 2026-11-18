# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Круг, хорда, длина окружности', 'The circle, a chord, the circumference'),
 [('r', 'r', 'Радиус', 'Radius', 2, 10, 1, 6), ('r', 'd', 'Расстояние от центра до хорды', 'Distance from the centre to the chord', 0, 9, 1, 3)],
 [('Длина окружности 2πr', 'Circumference 2πr'), ('Площадь круга πr²', 'Area πr²'), ('Длина хорды', 'Chord length')],
 'Хорда соединяет две точки окружности. Чем она ближе к центру, тем длиннее; самая длинная хорда — диаметр.', 'A chord joins two points of the circle. The closer to the centre, the longer; the longest chord is the diameter.', ('Окружность с хордой', 'A circle with a chord'),
 r'''const r=v.r,d=Math.min(v.d,r-0.01),k=85/r*1.0,cx=300,cy=105,half=Math.sqrt(r*r-d*d);let g=C(cx,cy,r*k,"#f4dfd8",COL.ink,3)+C(cx,cy,3,COL.ink)+L(cx,cy,cx+r*k,cy,COL.b,2)+TX(cx+r*k/2,cy-8,"r = "+r,COL.b,13,"middle",600)+L(cx-half*k,cy-d*k,cx+half*k,cy-d*k,COL.a,3)+L(cx,cy,cx,cy-d*k,COL.mut,1.5);
 return {svg:g,st:[fnum(2*Math.PI*r,2),fnum(Math.PI*r*r,2),fnum(2*half,2)],fb:U("Хорда на расстоянии d: 2·√(r² − d²). При d = 0 получаем диаметр 2r.","A chord at distance d: 2·√(r² − d²). At d = 0 it is the diameter 2r.")}''', '0 0 600 215')

m2 = M(('Касательная', 'The tangent'),
 [('r', 'r', 'Радиус', 'Radius', 2, 8, 1, 4), ('r', 'D', 'Расстояние от центра до точки', 'Distance from the centre to the point', 5, 14, 1, 9)],
 [('Длина касательной √(D² − r²)', 'Tangent length √(D² − r²)'), ('Угол между касательными', 'Angle between the tangents'), ('Радиус ⟂ касательной', 'Radius ⟂ tangent')],
 'Касательная касается окружности в одной точке и перпендикулярна радиусу, проведённому в эту точку. Из внешней точки можно провести две равные касательные.', 'A tangent touches the circle at one point and is perpendicular to the radius to that point. From an outside point two equal tangents can be drawn.', ('Две касательные из точки', 'Two tangents from a point'),
 r'''const r=v.r,D=Math.max(v.D,r+1),k=Math.min(18,190/r/1.0),sc=Math.min(14,250/D),cx=120,cy=105,px=cx+D*sc,t=Math.sqrt(D*D-r*r),al=Math.asin(r/D),tx=cx+r*r/D*sc,ty=r*t/D*sc;
 let g=C(cx,cy,r*sc,"#f4dfd8",COL.ink,3)+C(cx,cy,3,COL.ink)+C(px,cy,5,COL.a)+L(px,cy,tx,cy-ty,COL.a,3)+L(px,cy,tx,cy+ty,COL.a,3)+L(cx,cy,tx,cy-ty,COL.b,2)+L(cx,cy,tx,cy+ty,COL.b,2)+L(cx,cy,px,cy,COL.mut,1.5);
 g+=TX(px+10,cy+5,"P",COL.a,15,"start",700)+TX(cx-12,cy+20,"O",COL.ink,14,"end",700)+TX((px+tx)/2+16,cy-ty/2-8,fnum(t,2),COL.a,14,"start",700);
 return {svg:g,st:[fnum(t,2),fnum(2*al*180/Math.PI,1)+"°","90°"],fb:U("Треугольник OTP прямоугольный: OT ⟂ TP, поэтому TP² = OP² − OT².","Triangle OTP is right-angled: OT ⟂ TP, so TP² = OP² − OT².")}''', '0 0 600 215')

m3 = M(('Вписанный и центральный углы', 'Inscribed and central angles'),
 [('r', 'arc', 'Дуга, °', 'Arc, °', 20, 340, 1, 100), ('r', 'pos', 'Положение вершины на окружности, °', 'Position of the vertex on the circle, °', 0, 359, 1, 200)],
 [('Центральный угол', 'Central angle'), ('Вписанный угол', 'Inscribed angle'), ('Связь', 'Relation')],
 'Вписанный угол, опирающийся на дугу, вдвое меньше центрального угла, опирающегося на ту же дугу.', 'An inscribed angle on an arc is half the central angle on the same arc.', ('Окружность с углами', 'A circle with angles'),
 r'''const R0=90,cx=300,cy=105,P=t=>[cx+R0*Math.cos(deg(t)),cy-R0*Math.sin(deg(t))],a0=270-v.arc/2,a1=270+v.arc/2,A=P(a0),B=P(a1);let pos=v.pos;const inArc=((pos-a0)%360+360)%360<=v.arc;if(inArc)pos=(a1+(360-v.arc)/2)%360;const M0=P(pos);
 let g=C(cx,cy,R0,"#f4dfd8",COL.ink,3)+arcA(cx,cy,R0,deg(a0),deg(a1),COL.a,6)+L(cx,cy,A[0],A[1],COL.a,2.5)+L(cx,cy,B[0],B[1],COL.a,2.5)+L(M0[0],M0[1],A[0],A[1],COL.b,2.5)+L(M0[0],M0[1],B[0],B[1],COL.b,2.5)+C(cx,cy,3,COL.ink)+C(M0[0],M0[1],5,COL.b)+TX(cx,cy-12,v.arc+"°",COL.a,14,"middle",700);
 const ins=v.arc>180?(360-v.arc)/2:v.arc/2;
 return {svg:g,st:[v.arc+"°",fnum(v.arc/2,1)+"°",U("вписанный = ½ дуги","inscribed = ½ arc")],fb:inArc?U("Точка попала на дугу — выбираем вершину на другой части окружности.","The point fell on the arc — choosing a vertex on the other part of the circle."):U("Где бы ни стояла вершина на большей части окружности, угол один и тот же.","Wherever the vertex stands on the other part of the circle, the angle is the same.")}''', '0 0 600 215')

chapter('33', '33-circle.html', 'V', ('Окружность и круг', 'The circle'),
 ('Элементы окружности, длина окружности и площадь круга, касательные и вписанные углы.', 'Elements of a circle, the circumference and the area of a disc, tangents and inscribed angles.'),
 ('Колесо арбы имеет диаметр 1 метр. Мастер хочет знать, сколько оборотов оно сделает на дороге в 314 метров.\n\nКак это посчитать?', 'A cart wheel has a diameter of 1 metre. A craftsman wants to know how many turns it makes on a road 314 metres long.\n\nHow can it be calculated?'),
 ('Разгадка: примерно 100 оборотов', 'The answer: about 100 turns'),
 ('За один оборот колесо проходит длину своей окружности: C = π · d ≈ 3,14 · 1 = 3,14 м. Значит, 314 : 3,14 = 100 оборотов. Число π — отношение длины любой окружности к её диаметру. Оно одинаково для колеса арбы и для орбиты Луны.', 'In one turn the wheel travels the length of its circumference: C = π · d ≈ 3.14 · 1 = 3.14 m. So 314 : 3.14 = 100 turns. The number π is the ratio of the circumference of any circle to its diameter. It is the same for a cart wheel and for the Moon’s orbit.'),
 [S('elem', 'Элементы окружности', 'Elements of a circle', ('<strong>Окружность</strong> — все точки плоскости на одном расстоянии r (радиусе) от центра. <strong>Хорда</strong> соединяет две точки окружности, <strong>диаметр</strong> — хорда через центр (d = 2r). Длина окружности C = 2πr, площадь круга S = πr². Перпендикуляр из центра к хорде делит хорду пополам.', 'A <strong>circle</strong> is all points of the plane at the same distance r (the radius) from the centre. A <strong>chord</strong> joins two points of the circle; a <strong>diameter</strong> is a chord through the centre (d = 2r). The circumference is C = 2πr, the area of the disc S = πr². The perpendicular from the centre to a chord bisects the chord.'),
    ('C = 2πr,  S = πr²', 'π ≈ 3,14', 'π ≈ 3.14'), m1),
  S('tan', 'Касательная', 'The tangent', ('<strong>Касательная</strong> имеет с окружностью одну общую точку и перпендикулярна радиусу в точке касания. Из точки P вне окружности проводят две касательные, их отрезки до точек касания равны: PT² = OP² − r² (теорема Пифагора).', 'A <strong>tangent</strong> has exactly one common point with the circle and is perpendicular to the radius at the point of contact. From a point P outside the circle two tangents are drawn; their segments to the points of contact are equal: PT² = OP² − r² (Pythagorean theorem).'),
    ('PT = √(OP² − r²)', '', 'PT = √(OP² − r²)'), m2),
  S('ins', 'Вписанные углы', 'Inscribed angles', ('<strong>Центральный угол</strong> имеет вершину в центре, <strong>вписанный</strong> — на окружности. Вписанный угол равен половине дуги, на которую опирается. Поэтому вписанные углы, опирающиеся на одну дугу, равны, а угол, опирающийся на диаметр, прямой (180° : 2 = 90°).', 'A <strong>central angle</strong> has its vertex at the centre, an <strong>inscribed</strong> one on the circle. An inscribed angle equals half the arc it stands on. So inscribed angles on the same arc are equal, and an angle on a diameter is right (180° : 2 = 90°).'),
    ('вписанный = ½ дуги', '', 'inscribed = ½ arc'), m3)],
 [TK(('Длина окружности', 'Circumference'), ('Найдите длину окружности радиуса 10 (π ≈ 3,14).', 'Find the circumference of a circle with radius 10 (π ≈ 3.14).'), '2πr', '2 · 3,14 · 10 = 62,8.', '62,8.'),
  TK(('Площадь круга', 'Area of a disc'), ('Радиус 5. Найдите площадь круга (π ≈ 3,14).', 'The radius is 5. Find the area of the disc (π ≈ 3.14).'), 'πr²', '3,14 · 25 = 78,5.', '78,5.'),
  TK(('Угол на диаметре', 'Angle on a diameter'), ('Точка C лежит на окружности с диаметром AB. Чему равен угол ACB?', 'A point C lies on a circle with diameter AB. What is angle ACB?'), '', 'Опирается на диаметр — дуга 180°, угол 90°.', '90°.'),
  TK(('Касательная', 'A tangent'), ('Центр O, радиус 3, OP = 5. Найдите касательную из P.', 'Centre O, radius 3, OP = 5. Find the tangent from P.'), '', '√(25 − 9) = 4.', '4.'),
  TK(('Вписанный угол', 'Inscribed angle'), ('Дуга 80°. Найдите вписанный угол, опирающийся на неё.', 'An arc is 80°. Find the inscribed angle on it.'), '', '80° : 2 = 40°.', '40°.')],
 [Q('Диаметр — это', 'A diameter is', ('наибольшая хорда', 'the longest chord'), ('касательная', 'a tangent'), ('дуга', 'an arc'), ('Проходит через центр.', 'It passes through the centre.')),
  Q('d = 12. Радиус', 'd = 12. The radius', '6', '24', '12', ('d : 2.', 'd : 2.')),
  Q('Формула длины окружности', 'The circumference formula', '2πr', 'πr²', 'πd²', ('C = 2πr.', 'C = 2πr.')),
  Q('Касательная ⟂ радиусу в точке', 'A tangent is perpendicular to the radius at the point of', ('касания', 'contact'), ('центра', 'the centre'), ('любой', 'any point'), ('Свойство.', 'The property.')),
  Q('Вписанный угол, опирающийся на дугу 100°', 'An inscribed angle on a 100° arc', '50°', '100°', '200°', ('Половина дуги.', 'Half the arc.')),
  Q('Число π', 'The number π', ('отношение окружности к диаметру', 'the ratio of circumference to diameter'), ('радиус', 'the radius'), ('ровно 3', 'exactly 3'), ('Определение.', 'The definition.')),
  Q('Площадь круга радиуса 1', 'The area of a disc of radius 1', 'π', '2π', '1', ('π · 1².', 'π · 1².')),
  Q('Две касательные из одной точки', 'Two tangents from one point', ('равны', 'are equal'), ('параллельны', 'are parallel'), ('перпендикулярны', 'are perpendicular'), ('Равные отрезки.', 'Equal segments.'))],
 src=[('Wikipedia: Circle', 'https://en.wikipedia.org/wiki/Circle'), ('Wikipedia: Pi', 'https://en.wikipedia.org/wiki/Pi'), ('Wikipedia: Inscribed angle', 'https://en.wikipedia.org/wiki/Inscribed_angle')])
