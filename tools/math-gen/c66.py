# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Подобные тела: длина, площадь, объём', 'Similar solids: length, area, volume'),
 [('r', 'k', 'Коэффициент подобия k', 'Similarity ratio k', 0.5, 4, 0.5, 2)],
 [('Длины × k', 'Lengths × k'), ('Площади × k²', 'Areas × k²'), ('Объёмы × k³', 'Volumes × k³')],
 'Если все размеры тела увеличить в k раз, длины вырастут в k раз, площади в k², объёмы в k³. Поэтому большие тела «тяжелее для своей поверхности».', 'If all dimensions of a solid are multiplied by k, lengths grow k times, areas k², volumes k³. So bigger bodies are “heavier for their surface”.', ('Во сколько раз растут величины', 'How many times the quantities grow'),
 r'''const vals=[v.k,v.k*v.k,v.k*v.k*v.k],nm=[U("длина","length"),U("площадь","area"),U("объём","volume")],cl=[COL.a,COL.b,COL.c],mx=64;let g=L(50,200,560,200,COL.ink,2);vals.forEach((t,i)=>{const h=Math.min(170,170*t/Math.max(mx,t)*(t>mx?1:1)),x=90+i*160;const hh=170*Math.min(t,64)/64;g+=R(x,200-hh,90,hh,cl[i],COL.ink,1.5,3)+TX(x+45,192-hh,fnum(t,2)+"×",COL.ink,16,"middle",700)+TX(x+45,224,nm[i],COL.ink,14,"middle",700)});
 return {svg:g,st:[fnum(vals[0],2)+"×",fnum(vals[1],2)+"×",fnum(vals[2],2)+"×"],fb:U("Вдвое больше по размерам — вчетверо больше площадь и в 8 раз больше объём (и масса).","Twice the size means four times the area and eight times the volume (and mass).")}''', '0 0 600 240')

m2 = M(('Цилиндр, шар и конус Архимеда', 'The cylinder, sphere and cone of Archimedes'),
 [('r', 'R', 'Радиус R', 'Radius R', 1, 6, 1, 3)],
 [('Цилиндр (высота 2R)', 'Cylinder (height 2R)'), ('Шар', 'Sphere'), ('Конус (r = R, h = 2R)', 'Cone (r = R, h = 2R)')],
 'Цилиндр, шар и конус с одинаковым радиусом и высотой 2R имеют объёмы в отношении 3 : 2 : 1.', 'The cylinder, sphere and cone with the same radius and height 2R have volumes in the ratio 3 : 2 : 1.', ('Объёмы в отношении 3 : 2 : 1', 'Volumes in the ratio 3 : 2 : 1'),
 r'''const R0=v.R,V=[2*Math.PI*Math.pow(R0,3),4*Math.PI*Math.pow(R0,3)/3,2*Math.PI*Math.pow(R0,3)/3],mx=V[0],nm=[U("цилиндр","cylinder"),U("шар","sphere"),U("конус","cone")],cl=[COL.a,COL.b,COL.c];let g=L(50,200,560,200,COL.ink,2);V.forEach((t,i)=>{const h=170*t/mx,x=90+i*160;g+=R(x,200-h,90,h,cl[i],COL.ink,1.5,3)+TX(x+45,192-h,fnum(t,1),COL.ink,15,"middle",700)+TX(x+45,224,nm[i],COL.ink,14,"middle",700)});
 return {svg:g,st:[fnum(V[0],1),fnum(V[1],1),fnum(V[2],1)],fb:U("Отношение "+fnum(V[0]/V[2],1)+" : "+fnum(V[1]/V[2],1)+" : 1 не зависит от R.","The ratio "+fnum(V[0]/V[2],1)+" : "+fnum(V[1]/V[2],1)+" : 1 does not depend on R.")}''', '0 0 600 240')

m3 = M(('Юрта: объём и поверхность', 'A yurt: volume and surface'),
 [('r', 'r', 'Радиус юрты r, м', 'Yurt radius r, m', 3, 6, 0.5, 4), ('r', 'h1', 'Высота стен h₁, м', 'Wall height h₁, m', 1, 2.5, 0.1, 1.5), ('r', 'h2', 'Высота крыши h₂, м', 'Roof height h₂, m', 0.5, 3, 0.1, 1.5)],
 [('Объём (цилиндр + конус)', 'Volume (cylinder + cone)'), ('Поверхность стен и крыши', 'Surface of walls and roof'), ('Образующая крыши l', 'Roof slant l')],
 'Приближённая модель юрты — цилиндр (стены) с конусом (крыша). Размеры условные, реальные юрты отличаются.', 'A rough model of a yurt is a cylinder (walls) with a cone (roof). The dimensions are illustrative; real yurts differ.', ('Юрта сбоку', 'A yurt from the side'),
 r'''const k=Math.min(40,190/(v.h1+v.h2),240/v.r),cx=300,y0=230,w=v.r*k,H1=v.h1*k,H2=v.h2*k;let g=R(cx-w,y0-H1,2*w,H1,COL.a+"33",COL.ink,2.5,0)+poly([[cx-w*1.04,y0-H1],[cx+w*1.04,y0-H1],[cx,y0-H1-H2]],COL.b+"44",COL.ink,2.5)+L(cx-w,y0,cx+w,y0,COL.ink,3);
 const l=Math.hypot(v.r,v.h2),V=Math.PI*v.r*v.r*v.h1+Math.PI*v.r*v.r*v.h2/3,S=2*Math.PI*v.r*v.h1+Math.PI*v.r*l;
 return {svg:g,st:[fnum(V,1)+" м³",fnum(S,1)+" м²",fnum(l,2)+" м"],fb:U("Больший объём при меньшей поверхности — тёплее: меньше потерь тепла.","A larger volume with a smaller surface is warmer: less heat loss.")}''', '0 0 600 250')

chapter('66', '66-areas-volumes.html', 'IX', ('Площади поверхностей и объёмы', 'Surface areas and volumes'),
 ('Сводка формул, подобие тел и задачи на составные тела.', 'A summary of formulas, similar solids and problems with composite solids.'),
 ('Почему слон не может быть просто «увеличенной в 10 раз мышью»: у него ноги бы не выдержали вес?', 'Why can an elephant not be simply a “mouse enlarged 10 times”: would its legs not hold the weight?'),
 ('Разгадка: масса растёт как k³, а сечение костей как k²', 'The answer: mass grows as k³ while bone cross-section as k²'),
 ('При увеличении всех размеров в k раз масса растёт как объём — в k³, а прочность костей зависит от площади сечения — она растёт только в k². Нагрузка на единицу площади выросла бы в k раз. Поэтому у крупных животных ноги относительно толще. Тот же закон объясняет, почему капля воды круглая, а юрта с меньшей поверхностью при том же объёме теплее.', 'When all dimensions are scaled k times, mass grows like volume — k³ — while bone strength depends on the cross-section area, which grows only k². The load per unit area would grow k times. That is why large animals have relatively thicker legs. The same law explains why a drop of water is round and why a yurt with smaller surface for the same volume is warmer.'),
 [S('sim', 'Подобие тел', 'Similar solids', ('Если тела подобны с коэффициентом k, то <strong>длины ×k, площади ×k², объёмы ×k³</strong>. Пример: шар радиуса 2 по сравнению с шаром радиуса 1 имеет в 4 раза большую поверхность и в 8 раз больший объём.', 'If solids are similar with ratio k then <strong>lengths ×k, areas ×k², volumes ×k³</strong>. For example a sphere of radius 2 compared to a sphere of radius 1 has 4 times the surface and 8 times the volume.'),
    ('V₂/V₁ = k³,  S₂/S₁ = k²', '', 'V₂/V₁ = k³,  S₂/S₁ = k²'), m1),
  S('arch', 'Таблица формул', 'The table of formulas', ('Призма: V = S·h. Пирамида: V = S·h/3. Цилиндр: V = πr²h, S_бок = 2πrh. Конус: V = πr²h/3, S_бок = πrl. Шар: V = 4πR³/3, S = 4πR². Усечённые тела разбивают на разность двух подобных. Архимед доказал: цилиндр, шар и конус (при высоте 2R) относятся по объёму как 3 : 2 : 1.', 'Prism: V = S·h. Pyramid: V = S·h/3. Cylinder: V = πr²h, S_lat = 2πrh. Cone: V = πr²h/3, S_lat = πrl. Sphere: V = 4πR³/3, S = 4πR². Truncated solids are treated as a difference of two similar ones. Archimedes proved: the cylinder, sphere and cone (of height 2R) relate in volume as 3 : 2 : 1.'),
    ('3 : 2 : 1', '', '3 : 2 : 1'), m2),
  S('comp', 'Составные тела', 'Composite solids', ('Составное тело разбивают на простые: объёмы складывают, а поверхности считают без внутренних стыков. Модель юрты — цилиндр с конусом: V = πr²h₁ + πr²h₂/3; S = 2πrh₁ + πrl (без дна и общего сечения).', 'A composite solid is split into simple ones: volumes add, surfaces are counted without internal joints. The yurt model is a cylinder with a cone: V = πr²h₁ + πr²h₂/3; S = 2πrh₁ + πrl (without the floor and the shared section).'),
    ('V = V₁ + V₂', '', 'V = V₁ + V₂'), m3)],
 [TK(('Подобие', 'Similarity'), ('Ребро куба увеличили втрое. Во сколько раз выросли площадь и объём?', 'A cube edge was tripled. How many times did area and volume grow?'), '', 'Площадь ×9, объём ×27.', ('×9 и ×27.', '×9 and ×27.')),
  TK(('Модель', 'Model'), ('Модель здания в 1:50. Площадь окна модели 4 см². Реальная?', 'A model of a building at 1:50. The model window area is 4 cm². The real one?'), '', '4 · 50² = 10 000 см² = 1 м².', '1 м².'),
  TK(('Шар', 'Sphere'), ('Радиус шара увеличили вдвое. Объём?', 'The radius of a sphere was doubled. The volume?'), '', 'В 8 раз.', ('В 8 раз.', '8 times.')),
  TK(('Составное', 'Composite'), ('Цилиндр r = 1, h = 3 и сверху полушар r = 1. Объём?', 'A cylinder r = 1, h = 3 with a hemisphere r = 1 on top. The volume?'), '', 'π · 3 + (2/3)π = 11π/3.', '11π/3.'),
  TK(('Архимед', 'Archimedes'), ('Цилиндр вокруг шара имеет V = 54π. Объём шара?', 'The cylinder around a sphere has V = 54π. The sphere’s volume?'), '', 'Шар — 2/3 цилиндра: 36π.', '36π.')],
 [Q('Длины ×k, площади ×', 'Lengths ×k, areas ×', 'k²', 'k', 'k³', ('Площадь — два измерения.', 'Area is two-dimensional.')),
  Q('Длины ×k, объёмы ×', 'Lengths ×k, volumes ×', 'k³', 'k²', '2k', ('Три измерения.', 'Three dimensions.')),
  Q('Ребро куба вдвое длиннее. Объём больше в', 'A cube edge is twice as long. The volume is larger by', ('8 раз', '8 times'), ('4 раза', '4 times'), ('2 раза', '2 times'), ('2³.', '2³.')),
  Q('Цилиндр : шар : конус (Архимед)', 'Cylinder : sphere : cone (Archimedes)', '3 : 2 : 1', '1 : 2 : 3', '2 : 1 : 3', ('Отношение объёмов.', 'The ratio of volumes.')),
  Q('Масштаб 1:10: объём модели составляет от оригинала', 'At scale 1:10 the volume of a model is of the original', '1/1000', '1/100', '1/10', ('(1/10)³.', '(1/10)³.')),
  Q('Объём составного тела', 'The volume of a composite solid is', ('сумма объёмов частей', 'the sum of the volumes of its parts'), ('произведение', 'the product'), ('разность', 'the difference'), ('Складывают.', 'They add.')),
  Q('Нагрузка на кости растёт с размером, потому что масса растёт как', 'The load on bones grows with size because mass grows as', ('k³', 'k³'), ('k', 'k'), ('k²', 'k²'), ('Как объём.', 'Like volume.')),
  Q('Меньше потерь тепла у тела с', 'Less heat is lost by a body with', ('меньшей поверхностью при том же объёме', 'smaller surface for the same volume'), ('большей поверхностью', 'a larger surface'), ('меньшим объёмом', 'a smaller volume'), ('Тепло уходит через поверхность.', 'Heat escapes through the surface.'))],
 src=[('Wikipedia: Square–cube law', 'https://en.wikipedia.org/wiki/Square%E2%80%93cube_law'), ('Wikipedia: On the Sphere and Cylinder', 'https://en.wikipedia.org/wiki/On_the_Sphere_and_Cylinder'), ('Wikipedia: Yurt', 'https://en.wikipedia.org/wiki/Yurt')],
 note=('Размеры юрты в модели условные.', 'The yurt dimensions in the model are illustrative.'))
