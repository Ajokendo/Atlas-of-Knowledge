# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ПРЕЛОМЛЕНИЕ СВЕТА', 'REFRACTION OF LIGHT', 'rfSvg', '0 0 600 250',
  select('r1', 'Первая среда', 'First medium') + select('r2', 'Вторая среда', 'Second medium') + slider('ra', 'Угол падения', 'Angle of incidence', 0, 89, 1, 40),
  stats([('rB', 'Угол преломления β', 'Angle of refraction β'), ('rN', 'Показатели преломления', 'Refractive indices')]),
  'rfFb', 'Схема условная: показатели преломления — для жёлтого света; воздух 1,00; вода 1,33; стекло 1,5; алмаз 2,42.',
  'A schematic drawing: the refractive indices are for yellow light; air 1.00, water 1.33, glass 1.5, diamond 2.42.')
s1 = section('snell', 'Преломление: закон Снеллиуса', 'Refraction: Snell’s law',
 bd('<p>Когда свет переходит из одной прозрачной среды в другую, он меняет направление — <strong>преломляется</strong>. Причина в том, что скорость света в разных средах разная: в вакууме <em>c</em>, а в среде с <strong>показателем преломления</strong> <em>n</em> скорость равна <em>c/n</em>. В воде <em>n</em> ≈ 1,33, в стекле около 1,5, в алмазе 2,42.</p><p>Угол падения α и угол преломления β (оба от перпендикуляра) связаны <strong>законом Снеллиуса</strong>:</p>',
    '<p>When light passes from one transparent medium into another it changes direction — it <strong>refracts</strong>. The reason is that the speed of light differs in different media: in a vacuum it is <em>c</em> and in a medium with <strong>refractive index</strong> <em>n</em> the speed is <em>c/n</em>. In water <em>n</em> ≈ 1.33, in glass about 1.5, in diamond 2.42.</p><p>The angle of incidence α and the angle of refraction β (both from the perpendicular) are related by <strong>Snell’s law</strong>:</p>')
 + formula('n₁ · sin α = n₂ · sin β', 'из менее плотной среды в более плотную луч приближается к перпендикуляру; из более плотной — удаляется', 'from a less dense medium into a denser one the ray bends toward the perpendicular; from a denser one — away from it')
 + bd('<p>Поэтому соломинка в стакане воды кажется переломленной, а дно водоёма — приподнятым: глубина кажется в <em>n</em> раз меньше настоящей (глядя сверху), то есть <em>h′ = h / n</em>. Озеро выглядит мельче, чем есть.</p>',
      '<p>That is why a straw in a glass of water seems broken and the bottom of a pond raised: the depth seems <em>n</em> times less than the real one (looking from above), that is <em>h′ = h / n</em>. A lake looks shallower than it is.</p>'),
 lab1)

lab2 = model(2, 'ПОЛНОЕ ВНУТРЕННЕЕ ОТРАЖЕНИЕ', 'TOTAL INTERNAL REFLECTION', 'tiSvg', '0 0 600 250',
  select('tm', 'Среда (граница с воздухом)', 'Medium (boundary with air)') + slider('tg', 'Угол падения внутри среды', 'Angle of incidence inside the medium', 0, 89, 1, 30),
  stats([('tC', 'Предельный угол arcsin(1/n)', 'Critical angle arcsin(1/n)'), ('tR', 'Что происходит', 'What happens')]),
  'tiFb', 'Схема условная: луч идёт изнутри среды к границе с воздухом.',
  'A schematic drawing: a ray travels from inside the medium to the boundary with air.')
s2 = section('tir', 'Полное внутреннее отражение', 'Total internal reflection',
 bd('<p>Если луч идёт из более плотной среды в менее плотную (например, из воды в воздух), то при некотором <strong>предельном угле</strong> преломлённый луч скользит вдоль границы, а при бо́льших углах преломления нет совсем — весь свет отражается обратно. Это <strong>полное внутреннее отражение</strong>. Предельный угол <em>arcsin(1/n)</em>: для воды около 49°, для стекла около 42°, для алмаза около 24°.</p><p>На этом основаны <strong>световоды</strong>: свет бежит по тонкому стеклянному волокну, раз за разом отражаясь от стенок и не выходя наружу. По оптоволокну идёт большая часть интернета; им же пользуются в медицинских эндоскопах. Блеск алмаза — тоже следствие малого предельного угла.</p>',
    '<p>If a ray goes from a denser medium into a less dense one (for example from water into air) then at a certain <strong>critical angle</strong> the refracted ray slides along the boundary and at greater angles there is no refraction at all — all the light is reflected back. This is <strong>total internal reflection</strong>. The critical angle is <em>arcsin(1/n)</em>: about 49° for water, about 42° for glass, about 24° for diamond.</p><p><strong>Light guides</strong> are based on it: light runs along a thin glass fibre reflecting again and again from the walls and not leaving. Most of the internet runs through optical fibre; medical endoscopes use it too. The sparkle of a diamond is also a consequence of its small critical angle.</p>'),
 lab2)

lab3 = model(3, 'ТОНКАЯ ЛИНЗА', 'A THIN LENS', 'lnSvg', '0 0 600 250',
  slider('nf', 'Фокусное расстояние (собирающая линза)', 'Focal length (converging lens)', 5, 50, 1, 20) + slider('nd', 'Расстояние до предмета', 'Distance to the object', 3, 100, 1, 60),
  stats([('nI', 'Расстояние до изображения d′', 'Image distance d′'), ('nM', 'Увеличение m = −d′/d', 'Magnification m = −d′/d'), ('nK', 'Изображение', 'The image')]),
  'lnFb', 'Схема условная: расстояния в сантиметрах (масштаб по горизонтали сжат); предмет — стрелка.',
  'A schematic drawing: distances in centimetres (the horizontal scale is compressed); the object is an arrow.')
s3 = section('lens', 'Линзы', 'Lenses',
 bd('<p><strong>Линза</strong> — прозрачное тело с изогнутыми поверхностями, которое преломляет свет. <strong>Собирающая</strong> (выпуклая) линза собирает параллельные лучи в одной точке — <strong>фокусе</strong>; расстояние от линзы до фокуса — <strong>фокусное расстояние</strong> <em>f</em>. Рассеивающая (вогнутая) линза, наоборот, расходится лучи.</p><p>Положение изображения даёт <strong>формула тонкой линзы</strong>:</p>',
    '<p>A <strong>lens</strong> is a transparent body with curved surfaces that refracts light. A <strong>converging</strong> (convex) lens gathers parallel rays at one point — the <strong>focus</strong>; the distance from the lens to the focus is the <strong>focal length</strong> <em>f</em>. A diverging (concave) lens, on the contrary, spreads rays.</p><p>The position of the image is given by the <strong>thin-lens formula</strong>:</p>')
 + formula('1/f = 1/d + 1/d′,   m = −d′ / d', 'если предмет дальше фокуса — изображение действительное и перевёрнутое; ближе фокуса — мнимое, прямое и увеличенное (лупа)', 'if the object is beyond the focus the image is real and inverted; inside the focus — virtual, upright and magnified (a magnifier)')
 + bd('<p>Оптическую силу линзы измеряют в <strong>диоптриях</strong>: <em>D = 1/f</em> (f в метрах). Линза с f = 0,5 м имеет силу 2 диоптрии. Очки записывают в диоптриях.</p>',
      '<p>The optical power of a lens is measured in <strong>dioptres</strong>: <em>D = 1/f</em> (f in metres). A lens with f = 0.5 m has a power of 2 dioptres. Spectacles are prescribed in dioptres.</p>'),
 lab3)

tasks = [
 task(1, 'Из воздуха в воду', 'From air into water', 'Луч падает из воздуха на воду под углом 40°. Найдите угол преломления. n(воды) = 1,33.', 'A ray falls from air on water at 40°. Find the angle of refraction. n(water) = 1.33.',
  'α = 40°, n₁ = 1, n₂ = 1,33', 'α = 40°, n₁ = 1, n₂ = 1.33', 'sin β = n₁·sin α / n₂ = 1 · 0,6428 / 1,33 = 0,4833.<br>β = arcsin 0,4833 ≈ 28,9°.', 'sin β = n₁·sin α / n₂ = 1 · 0.6428 / 1.33 = 0.4833.<br>β = arcsin 0.4833 ≈ 28.9°.', 'около 29° — луч приблизился к перпендикуляру.', 'about 29° — the ray bent toward the perpendicular.', True),
 task(2, 'Предельный угол', 'The critical angle', 'Найдите предельный угол полного внутреннего отражения для воды (n = 1,33) и для стекла (n = 1,5).', 'Find the critical angle of total internal reflection for water (n = 1.33) and glass (n = 1.5).',
  'n = 1,33 и 1,5', 'n = 1.33 and 1.5', 'Вода: arcsin(1/1,33) = arcsin 0,752 ≈ 48,8°.<br>Стекло: arcsin(1/1,5) = arcsin 0,667 ≈ 41,8°.', 'Water: arcsin(1/1.33) = arcsin 0.752 ≈ 48.8°.<br>Glass: arcsin(1/1.5) = arcsin 0.667 ≈ 41.8°.', 'около 49° и 42°.', 'about 49° and 42°.'),
 task(3, 'Глубина бассейна', 'The depth of a pool', 'Настоящая глубина бассейна 2 м. Какой она кажется, если смотреть сверху вниз? n = 1,33.', 'The real depth of a pool is 2 m. How deep does it seem looking straight down? n = 1.33.',
  'h = 2 м, n = 1,33', 'h = 2 m, n = 1.33', 'h′ = h / n = 2 / 1,33 ≈ 1,50 м.', 'h′ = h / n = 2 / 1.33 ≈ 1.50 m.', 'около 1,5 м — вода обманчиво мелкая.', 'about 1.5 m — water is deceptively shallow.'),
 task(4, 'Линза даёт изображение', 'The lens forms an image', 'Предмет на расстоянии 60 см от собирающей линзы с f = 20 см. Найдите положение изображения и увеличение.', 'An object 60 cm from a converging lens with f = 20 cm. Find the image position and magnification.',
  'd = 60 см, f = 20 см', 'd = 60 cm, f = 20 cm', '1/d′ = 1/f − 1/d = 1/20 − 1/60 = 2/60, d′ = 30 см.<br>m = −d′/d = −30/60 = −0,5.', '1/d′ = 1/f − 1/d = 1/20 − 1/60 = 2/60, d′ = 30 cm.<br>m = −d′/d = −30/60 = −0.5.', '30 см за линзой; изображение действительное, перевёрнутое, вдвое меньше.', '30 cm behind the lens; the image is real, inverted and half the size.'),
 task(5, 'Лупа', 'A magnifier', 'Предмет на расстоянии 10 см от линзы с f = 20 см. Где изображение и каково увеличение?', 'An object 10 cm from a lens with f = 20 cm. Where is the image and what is the magnification?',
  'd = 10 см, f = 20 см', 'd = 10 cm, f = 20 cm', '1/d′ = 1/20 − 1/10 = −1/20, d′ = −20 см (знак «−»: мнимое, с той же стороны, что предмет).<br>m = −d′/d = 20/10 = +2.', '1/d′ = 1/20 − 1/10 = −1/20, d′ = −20 cm (the sign “−”: virtual, on the same side as the object).<br>m = −d′/d = 20/10 = +2.', 'мнимое прямое изображение, увеличенное вдвое — так работает лупа.', 'a virtual upright image magnified twice — that is how a magnifier works.'),
 task(6, 'Диоптрии', 'Dioptres', 'Какова оптическая сила линзы с f = 25 см? Каково фокусное расстояние очковой линзы +2 дптр?', 'What is the optical power of a lens with f = 25 cm? What is the focal length of a +2 dioptre spectacle lens?',
  'f = 0,25 м; D = +2 дптр', 'f = 0.25 m; D = +2 dioptres', 'D = 1/f = 1/0,25 = 4 дптр.<br>f = 1/D = 1/2 = 0,5 м = 50 см.', 'D = 1/f = 1/0.25 = 4 dioptres.<br>f = 1/D = 1/2 = 0.5 m = 50 cm.', '4 дптр и 50 см.', '4 dioptres and 50 cm.'),
]

quiz = [
 qz('Почему свет преломляется на границе сред?', 'Скорость света в средах разная', 'Свет теряет энергию', 'Свет меняет цвет', 'v = c/n: в разных средах скорость различна.',
    'Why does light refract at the boundary of media?', 'The speed of light differs in the media', 'Light loses energy', 'Light changes colour', 'v = c/n: the speed differs in different media.'),
 qz('Как луч идёт при переходе из воздуха в воду?', 'Приближается к перпендикуляру', 'Удаляется от перпендикуляра', 'Не меняет направления', 'Вода оптически плотнее воздуха.',
    'How does a ray go when passing from air into water?', 'It bends toward the perpendicular', 'It bends away from the perpendicular', 'It does not change direction', 'Water is optically denser than air.'),
 qz('Что такое показатель преломления?', 'Отношение скорости света в вакууме к скорости в среде', 'Скорость света в среде', 'Угол падения', 'n = c / v.',
    'What is the refractive index?', 'The ratio of the speed of light in a vacuum to that in the medium', 'The speed of light in the medium', 'The angle of incidence', 'n = c / v.'),
 qz('Когда наступает полное внутреннее отражение?', 'При переходе в менее плотную среду под большим углом', 'При переходе в более плотную среду', 'При нормальном падении', 'Нужен угол больше предельного.',
    'When does total internal reflection occur?', 'Passing into a less dense medium at a large angle', 'Passing into a denser medium', 'At normal incidence', 'The angle must exceed the critical one.'),
 qz('Где используют полное внутреннее отражение?', 'В оптоволокне', 'В электрогенераторах', 'В пружинных весах', 'Свет бежит по волокну, отражаясь от стенок.',
    'Where is total internal reflection used?', 'In optical fibre', 'In electric generators', 'In spring balances', 'Light runs along the fibre reflecting from the walls.'),
 qz('Какое изображение даёт собирающая линза, если предмет за двойным фокусом?', 'Действительное, перевёрнутое, уменьшенное', 'Мнимое, прямое', 'Действительное, увеличенное', 'Для d > 2f изображение между f и 2f и меньше предмета.',
    'What image does a converging lens give if the object is beyond twice the focal length?', 'Real, inverted, reduced', 'Virtual, upright', 'Real, magnified', 'For d > 2f the image is between f and 2f and smaller than the object.'),
 qz('Когда линза работает как лупа?', 'Предмет ближе фокуса', 'Предмет дальше двойного фокуса', 'Предмет в бесконечности', 'При d < f получается мнимое увеличенное изображение.',
    'When does a lens work as a magnifier?', 'The object is nearer than the focus', 'The object is beyond twice the focus', 'The object is at infinity', 'For d < f a virtual magnified image results.'),
 qz('Чему равна оптическая сила линзы с f = 0,5 м?', '2 дптр', '0,5 дптр', '5 дптр', 'D = 1/f = 1/0,5 = 2.',
    'What is the optical power of a lens with f = 0.5 m?', '2 dioptres', '0.5 dioptres', '5 dioptres', 'D = 1/f = 1/0.5 = 2.'),
]

js = r'''
const T={ru:{
 rfLabel:"Луч, переходящий из одной среды в другую",tiLabel:"Луч внутри среды у границы с воздухом",lnLabel:"Собирающая линза, предмет и изображение",
 med:["Воздух (1,00)","Вода (1,33)","Стекло (1,5)","Алмаз (2,42)"],
 res:["луч выходит в воздух","луч скользит вдоль границы","полное внутреннее отражение"],
 real:"действительное, перевёрнутое",virt:"мнимое, прямое",inf:"в бесконечности",
 rfFb:"Из воздуха в воду луч идёт ближе к перпендикуляру.",tiFb:"За предельным углом весь свет отражается обратно.",lnFb:"Ближе фокуса линза работает как лупа."},
 en:{
 rfLabel:"A ray passing from one medium into another",tiLabel:"A ray inside a medium at the boundary with air",lnLabel:"A converging lens, an object and its image",
 med:["Air (1.00)","Water (1.33)","Glass (1.5)","Diamond (2.42)"],
 res:["the ray emerges into the air","the ray slides along the boundary","total internal reflection"],
 real:"real, inverted",virt:"virtual, upright",inf:"at infinity",
 rfFb:"From air into water the ray goes closer to the perpendicular.",tiFb:"Beyond the critical angle all the light is reflected back.",lnFb:"Nearer than the focus the lens works as a magnifier."}};
const NI=[1.0,1.33,1.5,2.42];
function drawRf(){const t=tt(),n1=NI[+$("r1").value],n2=NI[+$("r2").value],a=+$("ra").value,A=a*Math.PI/180,s=n1*Math.sin(A)/n2;
 const cx=300,cy=125;let g='<rect x="30" y="125" width="540" height="110" fill="#bcd4e6" opacity="0.55"/><line x1="30" y1="125" x2="570" y2="125" stroke="#18181a" stroke-width="2"/><line x1="300" y1="20" x2="300" y2="235" stroke="#9a9a9a" stroke-dasharray="4 3"/>';
 g+=arrow(cx-Math.sin(A)*100,cy-Math.cos(A)*100,cx,cy,"#f0a020",3);
 let bt;if(s<=1){const B=Math.asin(s);bt=Math.round(B*180/Math.PI)+"°";g+=arrow(cx,cy,cx+Math.sin(B)*100,cy+Math.cos(B)*100,"#b6533f",3)}else{bt=lang==="ru"?"полное отражение":"total reflection";g+=arrow(cx,cy,cx+Math.sin(A)*100,cy-Math.cos(A)*100,"#b6533f",3)}
 g+=svgText(40,40,"n₁ = "+fmt(n1,2),"#18181a","start",13)+svgText(40,230,"n₂ = "+fmt(n2,2),"#18181a","start",13);
 $("rfSvg").innerHTML=g;
 $("raOut").textContent=a+"°";$("rB").textContent=bt;$("rN").textContent=fmt(n1,2)+" → "+fmt(n2,2);$("rfFb").textContent=t.rfFb}
["r1","r2","ra"].forEach(id=>$(id).addEventListener("input",drawRf));
function drawTi(){const t=tt(),k0=+$("tm").value+1,n=NI[k0],a=+$("tg").value,A=a*Math.PI/180,cr=n>1?Math.asin(1/n):Math.PI/2,crd=cr*180/Math.PI;
 const cx=300,cy=125;let g='<rect x="30" y="125" width="540" height="110" fill="#bcd4e6" opacity="0.55"/><line x1="30" y1="125" x2="570" y2="125" stroke="#18181a" stroke-width="2"/><line x1="300" y1="20" x2="300" y2="235" stroke="#9a9a9a" stroke-dasharray="4 3"/>';
 g+=arrow(cx-Math.sin(A)*100,cy+Math.cos(A)*100,cx,cy,"#f0a020",3);
 let r;if(A<cr-1e-6){const s=Math.min(1,n*Math.sin(A)),B=Math.asin(s);g+=arrow(cx,cy,cx+Math.sin(B)*100,cy-Math.cos(B)*100,"#b6533f",3);r=0}else if(Math.abs(A-cr)<0.5*Math.PI/180){g+=arrow(cx,cy,cx+100,cy,"#b6533f",3);r=1}else{g+=arrow(cx,cy,cx+Math.sin(A)*100,cy+Math.cos(A)*100,"#b6533f",3);r=2}
 g+=svgText(40,40,(lang==="ru"?"воздух":"air"),"#18181a","start",13)+svgText(40,230,t.med[k0],"#18181a","start",13);
 $("tiSvg").innerHTML=g;
 $("tgOut").textContent=a+"°";$("tC").textContent=n>1?fmt(crd,1)+"°":"—";$("tR").textContent=n>1?t.res[r]:"—";$("tiFb").textContent=t.tiFb}
["tm","tg"].forEach(id=>$(id).addEventListener("input",drawTi));
function drawLn(){const t=tt(),f=+$("nf").value,d=+$("nd").value;
 let di,m,kind;if(Math.abs(d-f)<1e-9){di=null;m=null;kind=t.inf}else{di=f*d/(d-f);m=-di/d;kind=di>0?t.real:t.virt}
 const ho=45;let g='<line x1="20" y1="125" x2="580" y2="125" stroke="#c9c2b0"/><line x1="300" y1="25" x2="300" y2="225" stroke="#3f5f8f" stroke-width="4"/>';
 const sx=2.2,xo=300-Math.min(d*sx,270);g+='<line x1="'+xo+'" y1="125" x2="'+xo+'" y2="'+(125-ho)+'" stroke="#2f6f5d" stroke-width="5"/>';
 g+='<circle cx="'+(300-f*sx)+'" cy="125" r="4" fill="#18181a"/><circle cx="'+(300+f*sx)+'" cy="125" r="4" fill="#18181a"/>'+svgText(300-f*sx,145,"F","#18181a","middle",11)+svgText(300+f*sx,145,"F","#18181a","middle",11);
 if(di!==null){const xi=300+Math.max(-270,Math.min(270,di*sx)),ty=125-Math.max(-100,Math.min(100,m*ho));
  g+='<line x1="'+xi+'" y1="125" x2="'+xi+'" y2="'+ty+'" stroke="#b6533f" stroke-width="5" '+(di<0?'stroke-dasharray="5 4"':'')+'/>';
  g+='<line x1="'+xo+'" y1="'+(125-ho)+'" x2="300" y2="'+(125-ho)+'" stroke="#f0a020"/><line x1="300" y1="'+(125-ho)+'" x2="'+xi+'" y2="'+ty+'" stroke="#f0a020"/><line x1="'+xo+'" y1="'+(125-ho)+'" x2="'+xi+'" y2="'+ty+'" stroke="#f0a020" stroke-opacity="0.6"/>'}
 $("lnSvg").innerHTML=g;
 $("nfOut").textContent=f+(lang==="ru"?" см":" cm");$("ndOut").textContent=d+(lang==="ru"?" см":" cm");
 $("nI").textContent=di===null?"∞":fmt(di,1)+(lang==="ru"?" см":" cm");$("nM").textContent=m===null?"∞":fmt(m,2);$("nK").textContent=kind;$("lnFb").textContent=t.lnFb}
["nf","nd"].forEach(id=>$(id).addEventListener("input",drawLn));
const LAB={ru:{rfSvg:T.ru.rfLabel,tiSvg:T.ru.tiLabel,lnSvg:T.ru.lnLabel},en:{rfSvg:T.en.rfLabel,tiSvg:T.en.tiLabel,lnSvg:T.en.lnLabel}};
function drawAll(){fillSel("r1",T[lang].med,0);fillSel("r2",T[lang].med,1);fillSel("tm",T[lang].med.slice(1),1);drawRf();drawTi();drawLn()}
'''

c = dict(n='31', slug='31-refraction-lenses.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Преломление света и линзы', 'Refraction of light and lenses'),
 desc='Глава 31 Атласа физики: закон Снеллиуса, показатель преломления, полное внутреннее отражение и оптоволокно, формула тонкой линзы.',
 lead=('Почему ложка в стакане «ломается», а озеро кажется мельче. Закон преломления, оптоволокно, линзы.',
       'Why a spoon in a glass “breaks” and a lake looks shallower. The law of refraction, optical fibre, lenses.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('snell', 'Преломление', 'Refraction'), ('tir', 'Полное отражение', 'Total reflection'), ('lens', 'Линзы', 'Lenses'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вы стоите у берега прозрачной горной речки и видите на дне камень. Кажется, что до дна меньше метра — вы шагнули, а вода оказалась по пояс. Рыбак, наоборот, целится острогой не туда, где видит рыбу, а ниже.</p><p>Почему дно кажется ближе, чем оно на самом деле?</p>',
         '<p>You stand on the bank of a clear mountain river and see a stone on the bottom. The bottom seems less than a metre down — you step in and the water is waist-deep. A fisherman, on the contrary, aims his spear not where he sees the fish but lower.</p><p>Why does the bottom seem nearer than it really is?</p>'),
 hint=stdhint('Преломление света', 'Refraction of light'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: свет преломляется на поверхности воды', 'The answer: light refracts at the water surface'),
 answer=('<p>Лучи от камня, выходя из воды в воздух, преломляются и отклоняются от перпендикуляра. Глаз продолжает их назад по прямой и «видит» камень выше, чем он есть. Для взгляда сверху кажущаяся глубина <em>h′ = h / n</em>, то есть для воды в 1,33 раза меньше настоящей: бассейн глубиной 2 м кажется глубиной 1,5 м (задача 3).</p><p>Поэтому входить в незнакомую воду надо осторожно, а рыбаку целиться ниже видимого положения рыбы.</p>',
         '<p>The rays from the stone, leaving the water for the air, refract and bend away from the perpendicular. The eye continues them backward in a straight line and “sees” the stone higher than it is. Viewed from above the apparent depth is <em>h′ = h / n</em> — for water 1.33 times less than the real one: a 2 m pool seems 1.5 m deep (problem 3).</p><p>So one must enter unfamiliar water carefully and a fisherman must aim below the fish’s apparent position.</p>'),
 sources=[
  ('Преломление, закон Снеллиуса, показатели преломления воды, стекла и алмаза —', 'Refraction, Snell’s law, the refractive indices of water, glass and diamond —', LINK('https://openstax.org/books/university-physics-volume-3/pages/1-introduction-to-the-nature-of-light', 'OpenStax University Physics, Vol. 3, гл. 1') + ', ' + LINK('https://en.wikipedia.org/wiki/Refractive_index', 'Wikipedia: Refractive index')),
  ('Полное внутреннее отражение, оптоволокно —', 'Total internal reflection, optical fibre —', LINK('https://en.wikipedia.org/wiki/Total_internal_reflection', 'Wikipedia: Total internal reflection')),
  ('Линзы, формула тонкой линзы, оптическая сила —', 'Lenses, the thin-lens formula, optical power —', LINK('https://openstax.org/books/university-physics-volume-3/pages/2-introduction', 'OpenStax University Physics, Vol. 3, гл. 2') + ', ' + LINK('https://en.wikipedia.org/wiki/Lens', 'Wikipedia: Lens'))],
 note=stdnote('Значения ползунков и расстояния в модели линзы — условные; показатели преломления округлены.', 'The slider values and the distances in the lens model are assumed; the refractive indices are rounded.'),
 prev=('30-reflection.html', 'Глава 30 · Отражение света', 'Chapter 30 · Reflection of light'),
 next=('32-eye-and-instruments.html', 'Глава 32 · Глаз и оптические приборы', 'Chapter 32 · The eye and optical instruments'),
 js=js)
build(c)
