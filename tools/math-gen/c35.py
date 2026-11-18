# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Подобные треугольники', 'Similar triangles'),
 [('r', 'k', 'Коэффициент подобия ×10', 'Similarity ratio ×10', 5, 30, 1, 20), ('r', 'a', 'Сторона a', 'Side a', 3, 8, 1, 4), ('r', 'b', 'Сторона b', 'Side b', 3, 8, 1, 5)],
 [('Стороны большего', 'Sides of the larger'), ('Отношение периметров', 'Ratio of perimeters'), ('Отношение площадей', 'Ratio of areas')],
 'У подобных треугольников углы равны, а стороны пропорциональны. Площади относятся как квадрат коэффициента.', 'Similar triangles have equal angles and proportional sides. Areas are in the ratio of the square of the scale factor.', ('Два подобных треугольника', 'Two similar triangles'),
 r'''const k=v.k/10,a=v.a,b=v.b,c=Math.min(a+b-1,7),T=triSides(a,b,c)||triSides(4,5,6);const s=Math.max(1,k);const P1=fitPts(T,20,15,250,170,0.5/Math.max(1,k)*1.0>0?1:1);
 const sc=Math.min(250/(Math.max(...T.map(p=>p[0]))-Math.min(...T.map(p=>p[0]))),160/(Math.max(...T.map(p=>p[1]))))/Math.max(1,k)*0.95;
 const mk=(ox,oy,kk)=>T.map(p=>[ox+p[0]*sc*kk,oy-p[1]*sc*kk]);let g=poly(mk(30,180,1),"#f4dfd8",COL.ink,3)+poly(mk(300,180,k),"#dbe5f2",COL.ink,3);
 return {svg:g,st:[fnum(a*k,2)+"; "+fnum(b*k,2)+"; "+fnum(c*k,2),fnum(k,2),fnum(k*k,2)],fb:k===1?U("Коэффициент 1: треугольники равны.","Ratio 1: the triangles are congruent."):U("Все стороны растянули в "+fnum(k,2)+" раза, углы не изменились.","All sides were scaled by "+fnum(k,2)+"; the angles did not change.")}''', '0 0 600 200')

m2 = M(('Высота по тени', 'Height from a shadow'),
 [('r', 'h', 'Рост человека, см', "Person's height, cm", 100, 200, 5, 170), ('r', 's', 'Тень человека, см', "Person's shadow, cm", 50, 300, 5, 120), ('r', 'S', 'Тень дерева, м', "Tree's shadow, m", 2, 30, 1, 14)],
 [('Отношение рост : тень', 'Ratio height : shadow'), ('Высота дерева', 'Height of the tree'), ('Угол солнца', 'Sun elevation')],
 'Солнечные лучи параллельны, поэтому треугольники «предмет — тень» подобны, и отношение высоты к тени одинаково.', 'The Sun’s rays are parallel, so the “object – shadow” triangles are similar and the ratio of height to shadow is the same.', ('Человек и дерево с тенями', 'A person and a tree with shadows'),
 r'''const r=v.h/v.s,H=r*v.S,ang=Math.atan(r)*180/Math.PI,sc=Math.min(14,520/(v.S+2)),vsc=Math.min(sc,150/Math.max(H,2));
 const X0=40,Y0=180;let g=L(X0,Y0,570,Y0,COL.ink,3);
 const tree=X0+10,tt=tree+v.S*sc;g+=L(tree,Y0,tree,Y0-H*vsc,COL.c,6)+C(tree,Y0-H*vsc-8,12,COL.c)+L(tree,Y0-H*vsc,tt,Y0,COL.mut,2)+L(tree,Y0,tt,Y0,"#bfbdb5",5);
 const px=tt+30,ps=v.s/100;g+=L(px,Y0,px,Y0-v.h/100*vsc,COL.a,6)+C(px,Y0-v.h/100*vsc-6,6,COL.a)+L(px,Y0-v.h/100*vsc,px+ps*sc,Y0,COL.mut,2)+L(px,Y0,px+ps*sc,Y0,"#bfbdb5",5);
 g+=TX(tree-4,Y0-H*vsc/2,fnum(H,1)+" м",COL.c,14,"end",700)+TX(tree+v.S*sc/2,Y0+20,fnum(v.S,0)+" м",COL.mut,13)+TX(px,Y0-v.h/100*vsc-24,v.h/100+" м",COL.a,13,"middle",600);
 return {svg:g,st:[fnum(r,2),fnum(H,1)+" м",fnum(ang,1)+"°"],fb:U("Высота дерева = "+fnum(r,2)+" · "+v.S+" = "+fnum(H,1)+" м.","Tree height = "+fnum(r,2)+" · "+v.S+" = "+fnum(H,1)+" m.")}''', '0 0 600 215')

m3 = M(('Длины, площади, объёмы', 'Lengths, areas, volumes'),
 [('r', 'k', 'Увеличение ×', 'Scale ×', 1, 6, 1, 3)],
 [('Длины', 'Lengths'), ('Площади', 'Areas'), ('Объёмы', 'Volumes')],
 'Если все размеры увеличить в k раз, длины растут в k раз, площади — в k², объёмы — в k³.', 'If all dimensions grow k times, lengths grow k times, areas k², volumes k³.', ('Рост длины, площади и объёма', 'Growth of length, area and volume'),
 r'''const k=v.k,vals=[k,k*k,k*k*k],mx=216,cols=[COL.a,COL.b,COL.c];let g="";
 vals.forEach((x,i)=>{const w=Math.max(4,x/mx*400);g+=R(130,25+i*55,w,38,cols[i],COL.ink,1.5,3)+TX(120,50+i*55,["×"+k,"×"+k+"²","×"+k+"³"][i],COL.ink,15,"end",700)+TX(140+w,50+i*55,x,COL.ink,15,"start",700)});
 return {svg:g,st:["×"+k,"×"+k*k,"×"+k*k*k],fb:U("Мышь ростом ×"+k+" весила бы в "+k*k*k+" раз больше, а её кости выдержали бы лишь в "+k*k+" раз больше.","A mouse scaled ×"+k+" would weigh "+k*k*k+" times more, while its bones could bear only "+k*k+" times more.")}''', '0 0 600 200')

chapter('35', '35-similarity.html', 'V', ('Подобие фигур', 'Similar figures'),
 ('Что такое подобие, как измерить высоту предмета по тени и почему при увеличении площадь растёт быстрее длины.', 'What similarity is, how to measure the height of an object by its shadow and why area grows faster than length under scaling.'),
 ('Как узнать высоту большого дерева, не залезая на него? Рядом стоит человек ростом 170 см, его тень 120 см, а тень дерева 14 м.\n\nЧему равна высота дерева?', 'How can we find the height of a big tree without climbing it? A person 170 cm tall stands next to it, his shadow is 120 cm and the tree’s shadow is 14 m.\n\nWhat is the height of the tree?'),
 ('Разгадка: примерно 19,8 м', 'The answer: about 19.8 m'),
 ('Солнечные лучи параллельны, поэтому треугольники «предмет — тень» подобны: 170 : 120 = H : 1400, откуда H = 170 · 1400 : 120 ≈ 1983 см ≈ 19,8 м. Подобие позволяет измерять недоступное: высоту горы, ширину реки, расстояние до лодки.', 'The Sun’s rays are parallel, so the “object – shadow” triangles are similar: 170 : 120 = H : 1400, hence H = 170 · 1400 : 120 ≈ 1983 cm ≈ 19.8 m. Similarity lets us measure the inaccessible: a mountain’s height, a river’s width, the distance to a boat.'),
 [S('sim', 'Подобные фигуры', 'Similar figures', ('Фигуры <strong>подобны</strong>, если одна получается из другой увеличением или уменьшением в k раз (и, возможно, поворотом). Число k — <strong>коэффициент подобия</strong>. У подобных фигур соответственные углы равны, а длины пропорциональны. Подобные треугольники: равны два угла (признак УУ), или пропорциональны три стороны, или две стороны и угол между ними.', 'Figures are <strong>similar</strong> if one is obtained from the other by enlarging or reducing by a factor k (and possibly turning). The number k is the <strong>similarity ratio</strong>. In similar figures corresponding angles are equal and lengths are proportional. Similar triangles: two angles equal (AA), or three sides proportional, or two sides proportional with the included angle equal.'),
    ('a₁/a = b₁/b = c₁/c = k', '', 'a₁/a = b₁/b = c₁/c = k'), m1),
  S('shadow', 'Измерение по тени', 'Measuring by a shadow', ('Если Солнце одинаково освещает человека и дерево, то высота : тень одинаково для обоих. Получаем пропорцию H : S = h : s, откуда H = h · S : s. Так Фалес (по преданию) измерил высоту пирамиды.', 'If the Sun lights a person and a tree the same way, then height : shadow is the same for both. This gives the proportion H : S = h : s, hence H = h · S : s. Thales (according to tradition) measured the height of a pyramid this way.'),
    ('H : S = h : s', '', 'H : S = h : s'), m2),
  S('area', 'Площади и объёмы подобных фигур', 'Areas and volumes of similar figures', ('При подобии с коэффициентом k длины умножаются на k, площади — на k², объёмы — на k³. Квадрат со стороной в 3 раза больше имеет площадь в 9 раз больше, а куб — объём в 27 раз больше.', 'Under similarity with ratio k lengths multiply by k, areas by k², volumes by k³. A square with a side 3 times larger has an area 9 times larger and a cube a volume 27 times larger.'),
    ('S₁/S = k²,  V₁/V = k³', '', 'S₁/S = k²,  V₁/V = k³'), m3)],
 [TK(('Стороны', 'Sides'), ('Треугольники подобны с k = 3. Сторона меньшего 4. Сторона большего?', 'Triangles are similar with k = 3. A side of the smaller is 4. The larger one?'), '', '4 · 3 = 12.', '12.'),
  TK(('Площади', 'Areas'), ('Стороны подобных фигур 2 и 6. Во сколько раз различаются площади?', 'The sides of similar figures are 2 and 6. How many times do the areas differ?'), 'k = 3', 'k² = 9.', ('В 9 раз.', '9 times.')),
  TK(('Тень', 'Shadow'), ('Шест 2 м даёт тень 3 м. Тень дерева 18 м. Высота дерева?', 'A 2 m pole casts a 3 m shadow. The tree’s shadow is 18 m. The tree’s height?'), '2 : 3 = H : 18', 'H = 2 · 18 : 3 = 12.', '12 м.'),
  TK(('Признак УУ', 'AA test'), ('В треугольниках по два угла 50° и 60°. Подобны ли они?', 'Two triangles have angles 50° and 60° each. Are they similar?'), '', 'Третьи углы тоже равны (70°) — подобны.', ('Да.', 'Yes.')),
  TK(('Объёмы', 'Volumes'), ('Ребро куба увеличили в 2 раза. Как изменился объём?', 'The edge of a cube was doubled. How did the volume change?'), '', '2³ = 8.', ('В 8 раз.', '8 times.'))],
 [Q('У подобных фигур углы', 'In similar figures the angles', ('равны', 'are equal'), ('пропорциональны', 'are proportional'), ('различны', 'differ'), ('Соответственные углы равны.', 'Corresponding angles are equal.')),
  Q('k = 2. Площади отличаются в', 'k = 2. The areas differ by', '4', '2', '8', ('k².', 'k².')),
  Q('k = 3. Объёмы отличаются в', 'k = 3. The volumes differ by', '27', '9', '3', ('k³.', 'k³.')),
  Q('Для подобия треугольников достаточно', 'For similar triangles it is enough', ('двух равных углов', 'two equal angles'), ('одного угла', 'one angle'), ('равных площадей', 'equal areas'), ('Признак УУ.', 'The AA test.')),
  Q('Тень 5 м у шеста 1 м. Тень здания 50 м. Здание', 'A 1 m pole has a 5 m shadow. A building’s shadow is 50 m. The building is', '10 м', '250 м', '55 м', ('50 : 5.', '50 : 5.')),
  Q('Равные треугольники подобны с k =', 'Congruent triangles are similar with k =', '1', '0', '2', ('Размеры те же.', 'Same sizes.')),
  Q('Отношение периметров подобных фигур', 'The ratio of perimeters of similar figures', ('k', 'k'), ('k²', 'k²'), ('k³', 'k³'), ('Периметр — длина.', 'Perimeter is a length.')),
  Q('Карта — это', 'A map is', ('подобное изображение местности', 'a similar image of the terrain'), ('равное изображение', 'a congruent image'), ('случайный рисунок', 'a random drawing'), ('Масштаб — коэффициент подобия.', 'The scale is the similarity ratio.'))],
 src=[('Wikipedia: Similarity (geometry)', 'https://en.wikipedia.org/wiki/Similarity_(geometry)'), ('Wikipedia: Thales of Miletus', 'https://en.wikipedia.org/wiki/Thales_of_Miletus')],
 note=('Рост человека и длины теней в загадке придуманы.', 'The person’s height and shadow lengths in the puzzle are made up.'))
