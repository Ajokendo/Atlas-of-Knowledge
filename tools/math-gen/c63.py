# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Считаем вершины, рёбра, грани', 'Counting vertices, edges, faces'),
 [('s', 't', 'Тело', 'Solid', ['призма', 'пирамида'], ['prism', 'pyramid'], 0), ('r', 'n', 'Сторон в основании n', 'Sides n of the base', 3, 8, 1, 5), ('r', 'yaw', 'Поворот', 'Rotation', -1, 1, 0.1, 0.3)],
 [('Вершины V', 'Vertices V'), ('Рёбра E', 'Edges E'), ('Грани F', 'Faces F')],
 'У n-угольной призмы V = 2n, E = 3n, F = n + 2; у n-угольной пирамиды V = n + 1, E = 2n, F = n + 1. Проверьте для разных n.', 'An n-gonal prism has V = 2n, E = 3n, F = n + 2; an n-gonal pyramid has V = n + 1, E = 2n, F = n + 1. Check for different n.', ('Каркас многогранника', 'The wireframe of the polyhedron'),
 r'''const n=v.n,P=P3(v.yaw,0.5,95,300,195),base=[],top=[];for(let i=0;i<n;i++){const a=2*Math.PI*i/n;base.push([Math.cos(a),Math.sin(a),0]);top.push([Math.cos(a),Math.sin(a),1.5])}
 let g="";const S2=p=>P(...p);const edge=(a,b,c,w)=>{const A=S2(a),B=S2(b);g+=L(A[0],A[1],B[0],B[1],c||COL.ink,w||2)};
 for(let i=0;i<n;i++){const j=(i+1)%n;edge(base[i],base[j]);if(v.t===0){edge(top[i],top[j]);edge(base[i],top[i])}else edge(base[i],[0,0,1.8],COL.a)}
 for(let i=0;i<n;i++){const A=S2(base[i]);g+=C(A[0],A[1],3.5,COL.ink);if(v.t===0){const B=S2(top[i]);g+=C(B[0],B[1],3.5,COL.ink)}}
 if(v.t===1){const T=S2([0,0,1.8]);g+=C(T[0],T[1],5,COL.b)}
 const V=v.t===0?2*n:n+1,E=v.t===0?3*n:2*n,F=v.t===0?n+2:n+1;
 return {svg:g,st:[V,E,F],fb:U("V − E + F = "+(V-E+F)+" — для любого выпуклого многогранника результат один и тот же.","V − E + F = "+(V-E+F)+" — for any convex polyhedron the result is the same.")}''', '0 0 600 280')

m2 = M(('Пять правильных многогранников', 'The five regular polyhedra'),
 [('s', 'p', 'Многогранник', 'Polyhedron', ['тетраэдр', 'куб', 'октаэдр', 'додекаэдр', 'икосаэдр'], ['tetrahedron', 'cube', 'octahedron', 'dodecahedron', 'icosahedron'], 1)],
 [('Вершины / рёбра / грани', 'Vertices / edges / faces'), ('V − E + F', 'V − E + F'), ('Грань; граней у вершины', 'Face; faces at a vertex')],
 'Правильных выпуклых многогранников ровно пять. У всех V − E + F = 2 (формула Эйлера).', 'There are exactly five regular convex polyhedra. For all of them V − E + F = 2 (Euler’s formula).', ('Диаграмма V, E, F', 'Diagram of V, E, F'),
 r'''const D=[[4,6,4,3,3],[8,12,6,4,3],[6,12,8,3,4],[20,30,12,5,3],[12,30,20,3,5]][v.p],nm=["V","E","F"],cl=[COL.a,COL.b,COL.c];let g=L(60,190,560,190,COL.ink,2);for(let i=0;i<3;i++){const h=D[i]*5.2,x=110+i*160;g+=R(x,190-h,90,h,cl[i],COL.ink,1.5,3)+TX(x+45,182-h,String(D[i]),COL.ink,18,"middle",700)+TX(x+45,214,nm[i],COL.ink,16,"middle",700)}
 
 return {svg:g,st:[D[0]+" / "+D[1]+" / "+D[2],D[0]+" − "+D[1]+" + "+D[2]+" = "+(D[0]-D[1]+D[2]),D[3]+U("-угольная; ","-gon; ")+D[4]],fb:U("Куб и октаэдр «двойственны»: V и F меняются местами, E остаётся.","The cube and the octahedron are “dual”: V and F swap, E stays.")}''', '0 0 600 235')

m3 = M(('Почему именно пять', 'Why exactly five'),
 [('r', 'k', 'Углов в грани k', 'Corners k of a face', 3, 6, 1, 3), ('r', 'm', 'Граней у вершины m', 'Faces m at a vertex', 3, 6, 1, 4)],
 [('Угол грани', 'Face angle'), ('Сумма у вершины', 'Angle sum at a vertex'), ('Можно построить?', 'Can it be built?')],
 'У вершины выпуклого многогранника сумма плоских углов должна быть меньше 360°. Из этого условия остаются только пять вариантов.', 'At a vertex of a convex polyhedron the sum of the face angles must be less than 360°. Only five variants satisfy this condition.', ('Сумма углов у вершины', 'The angle sum at a vertex'),
 r'''const al=180-360/v.k,sum=al*v.m,sc=1.5,x0=50;let g="";for(let i=0;i<v.m;i++)g+=R(x0+i*al*sc,60,al*sc,40,i%2?COL.a:COL.b,COL.bg,2,0);g+=L(x0+360*sc,40,x0+360*sc,120,COL.c,3,0)+TX(x0+360*sc,34,"360°",COL.c,14,"middle",700)+TX(x0+sum*sc/2,128,fnum(sum,0)+"°",COL.ink,16,"middle",700);const ok=sum<360-1e-9;
 return {svg:g,st:[fnum(al,0)+"°",fnum(sum,0)+"°",ok?U("да (< 360°)","yes (< 360°)"):U("нет (≥ 360°)","no (≥ 360°)")],fb:ok?U("Многогранник существует — это "+({"3,3":"тетраэдр","3,4":"октаэдр","3,5":"икосаэдр","4,3":"куб","5,3":"додекаэдр"}[v.k+","+v.m]||"многогранник")+".","The polyhedron exists — "+({"3,3":"the tetrahedron","3,4":"the octahedron","3,5":"the icosahedron","4,3":"the cube","5,3":"the dodecahedron"}[v.k+","+v.m]||"a polyhedron")+"."):U("Сумма 360° и больше — грани лягут в плоскость или не сойдутся.","A sum of 360° or more — the faces would lie flat or not meet.")}''', '0 0 600 150')

chapter('63', '63-polyhedra.html', 'IX', ('Многогранники', 'Polyhedra'),
 ('Вершины, рёбра, грани, формула Эйлера и пять правильных многогранников.', 'Vertices, edges, faces, Euler’s formula and the five regular polyhedra.'),
 ('Игральная кость — куб: 8 вершин, 12 рёбер, 6 граней. А у футбольного мяча из 12 пятиугольников и 20 шестиугольников: 60 вершин, 90 рёбер, 32 грани. Есть ли что-то общее в этих числах?', 'A die is a cube: 8 vertices, 12 edges, 6 faces. A football made of 12 pentagons and 20 hexagons has 60 vertices, 90 edges, 32 faces. Is there anything common in these numbers?'),
 ('Разгадка: V − E + F = 2', 'The answer: V − E + F = 2'),
 ('Для куба 8 − 12 + 6 = 2, для мяча 60 − 90 + 32 = 2. Леонард Эйлер заметил, что для любого выпуклого многогранника разность «вершины − рёбра + грани» равна 2. Это один из первых результатов топологии — науки о свойствах фигур, не меняющихся при растяжении.', 'For the cube 8 − 12 + 6 = 2, for the ball 60 − 90 + 32 = 2. Leonhard Euler noticed that for any convex polyhedron the difference “vertices − edges + faces” equals 2. This is one of the first results of topology — the science of properties of shapes that do not change under stretching.'),
 [S('el', 'Элементы многогранника', 'Elements of a polyhedron', ('<strong>Многогранник</strong> — тело, ограниченное плоскими многоугольниками — гранями; их стороны — рёбра, углы — вершины. Многогранник выпуклый, если он лежит по одну сторону от плоскости каждой своей грани. Призма: два равных параллельных основания и боковые грани-параллелограммы. Пирамида: основание и боковые треугольники с общей вершиной.', 'A <strong>polyhedron</strong> is a solid bounded by flat polygons — faces; their sides are edges, their corners are vertices. A polyhedron is convex if it lies on one side of the plane of each of its faces. A prism: two equal parallel bases and parallelogram side faces. A pyramid: a base and side triangles with a common apex.'),
    ('V, E, F', '', 'V, E, F'), m1),
  S('euler', 'Формула Эйлера', "Euler's formula", ('Для выпуклого многогранника <strong>V − E + F = 2</strong>. Формула позволяет проверять подсчёты: если у призмы получилось V − E + F ≠ 2, где-то ошибка. Для «бубликов» (с отверстием) число другое — 0.', 'For a convex polyhedron <strong>V − E + F = 2</strong>. The formula helps to check counts: if a prism gave V − E + F ≠ 2 there is a mistake somewhere. For “doughnuts” (with a hole) the number is different — 0.'),
    ('V − E + F = 2', '', 'V − E + F = 2'), m2),
  S('reg', 'Правильные многогранники', 'Regular polyhedra', ('Правильный многогранник: все грани — одинаковые правильные многоугольники и в каждой вершине сходится одинаковое число граней. Их ровно пять: тетраэдр, куб, октаэдр, додекаэдр, икосаэдр. Причина — в сумме углов у вершины: она должна быть меньше 360°.', 'A regular polyhedron: all faces are equal regular polygons and the same number of faces meet at each vertex. There are exactly five: tetrahedron, cube, octahedron, dodecahedron, icosahedron. The reason is the angle sum at a vertex: it must be less than 360°.'),
    ('сумма углов у вершины < 360°', '', 'angle sum at a vertex < 360°'), m3)],
 [TK(('Куб', 'Cube'), ('Проверьте формулу Эйлера для куба.', 'Check Euler’s formula for the cube.'), '', '8 − 12 + 6 = 2.', '2.'),
  TK(('Призма', 'Prism'), ('Сколько рёбер у шестиугольной призмы?', 'How many edges does a hexagonal prism have?'), '', '3 · 6 = 18.', '18.'),
  TK(('Пирамида', 'Pyramid'), ('Сколько граней у пятиугольной пирамиды?', 'How many faces does a pentagonal pyramid have?'), '', '5 + 1 = 6.', '6.'),
  TK(('Найти F', 'Find F'), ('У многогранника V = 10, E = 16. Сколько граней?', 'A polyhedron has V = 10, E = 16. How many faces?'), 'V − E + F = 2', 'F = 2 − 10 + 16 = 8.', '8.'),
  TK(('Углы', 'Angles'), ('Можно ли собрать вершину из 4 правильных пятиугольников?', 'Can a vertex be built from 4 regular pentagons?'), 'Угол пятиугольника 108°', '4 · 108° = 432° > 360° — нельзя.', ('Нельзя.', 'No.'))],
 [Q('V − E + F для выпуклого многогранника', 'V − E + F for a convex polyhedron', '2', '0', '1', ('Формула Эйлера.', 'Euler’s formula.')),
  Q('Граней у куба', 'Faces of a cube', '6', '8', '12', ('Шесть квадратов.', 'Six squares.')),
  Q('Рёбер у куба', 'Edges of a cube', '12', '8', '6', ('Двенадцать.', 'Twelve.')),
  Q('Правильных многогранников', 'Regular polyhedra', ('пять', 'five'), ('четыре', 'four'), ('шесть', 'six'), ('Платоновы тела.', 'The Platonic solids.')),
  Q('Вершин у четырёхугольной пирамиды', 'Vertices of a quadrangular pyramid', '5', '4', '8', ('4 + 1.', '4 + 1.')),
  Q('Сумма плоских углов у вершины выпуклого многогранника', 'The sum of face angles at a vertex of a convex polyhedron is', ('меньше 360°', 'less than 360°'), ('равна 360°', 'equal to 360°'), ('больше 360°', 'more than 360°'), ('Иначе грани лягут в плоскость.', 'Otherwise the faces would lie flat.')),
  Q('Призма имеет оснований', 'A prism has how many bases', '2', '1', '3', ('Два равных.', 'Two equal ones.')),
  Q('Октаэдр имеет граней', 'An octahedron has faces', '8', '6', '12', ('Название — «восьмигранник».', 'The name means “eight faces”.'))],
 src=[('Wikipedia: Euler characteristic', 'https://en.wikipedia.org/wiki/Euler_characteristic'), ('Wikipedia: Platonic solid', 'https://en.wikipedia.org/wiki/Platonic_solid'), ('Wikipedia: Truncated icosahedron', 'https://en.wikipedia.org/wiki/Truncated_icosahedron')])
