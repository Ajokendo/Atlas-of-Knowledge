# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Смежные и вертикальные углы', 'Adjacent and vertical angles'),
 [('r', 'a', 'Угол α, °', 'Angle α, °', 10, 170, 1, 55)],
 [('Смежный угол', 'Adjacent angle'), ('Вертикальный угол', 'Vertical angle'), ('Сумма смежных', 'Sum of adjacent')],
 'Две пересекающиеся прямые образуют четыре угла. Смежные в сумме дают 180°, вертикальные равны.', 'Two intersecting lines form four angles. Adjacent angles add to 180°; vertical angles are equal.', ('Две пересекающиеся прямые', 'Two intersecting lines'),
 r'''const cx=300,cy=110,a=deg(v.a);let g=L(cx-230,cy,cx+230,cy,COL.ink,3)+L(cx-200*Math.cos(a),cy+200*Math.sin(a)*0.55,cx+200*Math.cos(a),cy-200*Math.sin(a)*0.55,COL.ink,3);
 const r=36;g+=arcA(cx,cy,r,0,a*1,COL.a,6)+arcA(cx,cy,r,Math.PI,Math.PI+a,COL.a,6)+arcA(cx,cy,r+14,a,Math.PI,COL.b,6)+arcA(cx,cy,r+14,Math.PI+a,2*Math.PI,COL.b,6);
 g+=TX(cx+62*Math.cos(a/2),cy-62*Math.sin(a/2)+5,v.a+"°",COL.a,15,"middle",700)+TX(cx-62*Math.cos(a/2),cy+62*Math.sin(a/2)+5,v.a+"°",COL.a,15,"middle",700)+TX(cx+75*Math.cos((a+Math.PI)/2),cy-75*Math.sin((a+Math.PI)/2)+5,(180-v.a)+"°",COL.b,15,"middle",700)+TX(cx-75*Math.cos((a+Math.PI)/2),cy+75*Math.sin((a+Math.PI)/2)+5,(180-v.a)+"°",COL.b,15,"middle",700);
 return {svg:g,st:[180-v.a+"°",v.a+"°",v.a+"° + "+(180-v.a)+"° = 180°"],fb:U("Вертикальные углы всегда равны: у них общее смежное.","Vertical angles are always equal: they share the same adjacent angle.")}''', '0 0 600 220')

m2 = M(('Параллельные прямые и секущая', 'Parallel lines and a transversal'),
 [('r', 'a', 'Угол при секущей, °', 'Angle at the transversal, °', 20, 160, 1, 65), ('s', 'k', 'Подсветить пару', 'Highlight a pair', ['накрест лежащие', 'соответственные', 'односторонние'], ['alternate interior', 'corresponding', 'co-interior'], 0)],
 [('Первый угол', 'The first angle'), ('Второй угол', 'The second angle'), ('Связь', 'The relation')],
 'Если прямые параллельны, накрест лежащие и соответственные углы равны, а односторонние в сумме дают 180°.', 'If the lines are parallel, alternate and corresponding angles are equal; co-interior angles add up to 180°.', ('Две параллельные прямые и секущая', 'Two parallel lines and a transversal'),
 r'''const a=deg(v.a),y1=70,y2=170,dx=(y2-y1)/Math.tan(a),x1=250,x2=x1-dx;let g=L(60,y1,540,y1,COL.ink,3)+L(60,y2,540,y2,COL.ink,3)+L(x1+(y1-30)/Math.tan(a)*-1*-1,30,x2-(210-y2)/Math.tan(a)*-1,210,COL.mut,3);
 g+=C(x1,y1,4,COL.ink)+C(x2,y2,4,COL.ink);
 const ang=(x,y,a0,a1,c,t)=>arcA(x,y,28,a0,a1,c,6)+TX(x+46*Math.cos((a0+a1)/2),y-46*Math.sin((a0+a1)/2)+5,t,c,14,"middle",700);
 let tx;if(v.k===0){g+=ang(x1,y1,Math.PI,Math.PI+a,COL.a,v.a+"°")+ang(x2,y2,0,a,COL.b,v.a+"°");tx=[v.a+"°",v.a+"°",U("равны","equal")]}
 else if(v.k===1){g+=ang(x1,y1,0,a,COL.a,v.a+"°")+ang(x2,y2,0,a,COL.b,v.a+"°");tx=[v.a+"°",v.a+"°",U("равны","equal")]}
 else{g+=ang(x1,y1,Math.PI+a,2*Math.PI,COL.a,(180-v.a)+"°")+ang(x2,y2,0,a,COL.b,v.a+"°");tx=[(180-v.a)+"°",v.a+"°",U("в сумме 180°","sum is 180°")]}
 return {svg:g,st:tx,fb:U("Эти свойства верны только для параллельных прямых.","These properties hold only for parallel lines.")}''', '0 0 600 230')

m3 = M(('Найдите неизвестный угол', 'Find the unknown angle'),
 [('r', 'a', 'Угол A, °', 'Angle A, °', 20, 160, 1, 70), ('r', 'b', 'Угол B, °', 'Angle B, °', 10, 80, 1, 30)],
 [('Смежный с A', 'Adjacent to A'), ('Угол C = 180° − A − B?', 'Angle C = 180° − A − B?'), ('Развёрнутый угол', 'A straight angle')],
 'Развёрнутый угол равен 180°. Если известны два из трёх углов вдоль прямой, третий найти легко.', 'A straight angle is 180°. If two of three angles along a line are known, the third is easy to find.', ('Три угла вдоль прямой', 'Three angles along a line'),
 r'''const A=v.a,B=Math.min(v.b,179-A),C0=180-A-B;let g="";const cx=300,cy=170;g+=L(60,cy,540,cy,COL.ink,3);
 const rays=[A,A+B];rays.forEach(t=>{g+=L(cx,cy,cx+230*Math.cos(deg(180-t)),cy-230*Math.sin(deg(180-t)),COL.ink,3)});
 g+=arcA(cx,cy,60,deg(180-A),Math.PI,COL.a,7)+arcA(cx,cy,80,deg(180-A-B),deg(180-A),COL.b,7)+arcA(cx,cy,100,0,deg(180-A-B),COL.c,7);
 g+=TX(cx-100*Math.cos(deg(A/2)),cy-70*Math.sin(deg(A/2))-8,A+"°",COL.a,15,"middle",700)+TX(cx+14,cy-110,B+"°",COL.b,15,"middle",700)+TX(cx+120*Math.cos(deg(C0/2)),cy-120*Math.sin(deg(C0/2)),C0+"°",COL.c,15,"middle",700);
 return {svg:g,st:[180-A+"°",C0+"°",A+"° + "+B+"° + "+C0+"° = 180°"],fb:U("Сумма трёх углов вдоль прямой всегда 180°.","The sum of three angles along a line is always 180°.")}''', '0 0 600 200')

chapter('29', '29-angles-parallel.html', 'V', ('Углы и параллельные прямые', 'Angles and parallel lines'),
 ('Как связаны углы при пересечении прямых и почему рельсы остаются параллельными.', 'How angles are related when lines cross and why rails stay parallel.'),
 ('Две дороги пересекаются на перекрёстке. Один из углов между ними равен 55°.\n\nЧему равны остальные три угла?', 'Two roads cross at an intersection. One of the angles between them is 55°.\n\nWhat are the other three angles?'),
 ('Разгадка: 125°, 55°, 125°', 'The answer: 125°, 55°, 125°'),
 ('Углы, лежащие рядом (смежные), в сумме дают развёрнутый угол 180°: 180° − 55° = 125°. Угол напротив (вертикальный) равен самому углу: 55°. Третий — снова 125°. Знание одного угла определяет все четыре.', 'Neighbouring (adjacent) angles add up to a straight angle of 180°: 180° − 55° = 125°. The angle opposite (vertical) equals the angle itself: 55°. The third is again 125°. One angle fixes all four.'),
 [S('adj', 'Смежные и вертикальные углы', 'Adjacent and vertical angles', ('<strong>Смежные</strong> углы имеют общую сторону, а две другие стороны образуют прямую: их сумма 180°. <strong>Вертикальные</strong> углы — противоположные при пересечении двух прямых: они равны. Угол 90° — прямой; два угла по 90° — перпендикулярные прямые.', '<strong>Adjacent</strong> angles share a side and their other sides form a line: their sum is 180°. <strong>Vertical</strong> angles are opposite ones at the crossing of two lines: they are equal. A 90° angle is right; two 90° angles mean perpendicular lines.'),
    ('α + β = 180°', 'смежные', 'adjacent'), m1),
  S('par', 'Параллельные прямые и секущая', 'Parallel lines and a transversal', ('Прямая, пересекающая две другие, — <strong>секущая</strong>. Она образует 8 углов. Если прямые параллельны, то <strong>накрест лежащие</strong> и <strong>соответственные</strong> углы равны, а <strong>односторонние</strong> в сумме дают 180°. Верно и обратное: по равенству таких углов можно доказать параллельность.', 'A line crossing two others is a <strong>transversal</strong>. It forms 8 angles. If the lines are parallel, the <strong>alternate interior</strong> and <strong>corresponding</strong> angles are equal and the <strong>co-interior</strong> angles add to 180°. The converse also holds: equality of such angles proves parallelism.'),
    ('a ∥ b ⇒ накрест лежащие равны', '', 'a ∥ b ⇒ alternate angles equal'), m2),
  S('find', 'Нахождение углов', 'Finding angles', ('Задачи на углы решают цепочкой: находят угол через смежный, вертикальный или через параллельность, записывая каждый шаг с причиной. Сумма углов вдоль прямой и вокруг точки: 180° и 360°.', 'Angle problems are solved as a chain: find an angle via an adjacent, vertical or parallel relation, writing each step with its reason. The sums along a line and around a point: 180° and 360°.'),
    ('сумма вокруг точки = 360°', '', 'sum around a point = 360°'), m3)],
 [TK(('Смежные', 'Adjacent'), ('Один из смежных углов 40°. Найдите второй.', 'One of two adjacent angles is 40°. Find the other.'), '', '180° − 40° = 140°.', '140°.'),
  TK(('Вертикальные', 'Vertical'), ('Угол 72°. Чему равен вертикальный?', 'An angle is 72°. What is its vertical angle?'), '', 'Вертикальные углы равны: 72°.', '72°.'),
  TK(('Параллельные', 'Parallel'), ('Прямые a ∥ b, накрест лежащий угол 48°. Найдите соответственный ему угол при другой прямой и односторонний.', 'Lines a ∥ b, alternate angle 48°. Find the other alternate angle and a co-interior one.'), '', 'Накрест лежащий — 48°; односторонний 180° − 48° = 132°.', ('48° и 132°.', '48° and 132°.')),
  TK(('Вокруг точки', 'Around a point'), ('Вокруг точки четыре угла: 90°, 100°, 70° и x. Найдите x.', 'Around a point there are four angles: 90°, 100°, 70° and x. Find x.'), '360° − ...', '360° − 90° − 100° − 70° = 100°.', '100°.'),
  TK(('Биссектриса', 'A bisector'), ('Развёрнутый угол разделён биссектрисой пополам. Чему равны части?', 'A straight angle is bisected. What are the parts?'), '', '180° : 2 = 90°.', '90°.')],
 [Q('Смежные углы в сумме', 'Adjacent angles add up to', '180°', '90°', '360°', ('Развёрнутый угол.', 'A straight angle.')),
  Q('Вертикальные углы', 'Vertical angles are', ('равны', 'equal'), ('в сумме 180°', 'sum to 180°'), ('в сумме 90°', 'sum to 90°'), ('Свойство вертикальных углов.', 'The property of vertical angles.')),
  Q('Один из смежных 35°. Другой', 'One adjacent angle is 35°. The other is', '145°', '55°', '35°', ('180° − 35°.', '180° − 35°.')),
  Q('При a ∥ b накрест лежащие углы', 'For a ∥ b the alternate angles are', ('равны', 'equal'), ('в сумме 180°', 'sum to 180°'), ('в сумме 90°', 'sum to 90°'), ('Свойство параллельных.', 'The parallel-line property.')),
  Q('При a ∥ b односторонние углы', 'For a ∥ b the co-interior angles', ('в сумме 180°', 'sum to 180°'), ('равны', 'are equal'), ('в сумме 90°', 'sum to 90°'), ('Свойство параллельных.', 'The parallel-line property.')),
  Q('Сколько углов образует секущая с двумя прямыми?', 'How many angles does a transversal make with two lines?', '8', '4', '6', ('По четыре при каждой.', 'Four at each.')),
  Q('Сумма углов вокруг точки', 'The sum of angles around a point', '360°', '180°', '270°', ('Полный оборот.', 'A full turn.')),
  Q('Прямой угол', 'A right angle is', '90°', '180°', '45°', ('Угол между перпендикулярными.', 'The angle between perpendiculars.'))],
 src=[('Wikipedia: Angle', 'https://en.wikipedia.org/wiki/Angle'), ('Wikipedia: Transversal (geometry)', 'https://en.wikipedia.org/wiki/Transversal_(geometry)')])
