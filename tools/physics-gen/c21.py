# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'КОМПАС РЯДОМ С МАГНИТОМ', 'A COMPASS NEAR A MAGNET', 'cpSvg', '0 0 600 250',
  slider('cd', 'Расстояние до магнита', 'Distance to the magnet', 2, 30, 1, 10),
  stats([('cB', 'Поле магнита у компаса', 'The magnet’s field at the compass'), ('cA', 'Стрелка отклонена от севера на', 'The needle is deflected from north by')]),
  'cpFb', 'Схема условная: поле Земли 50 мкТл; магнит — небольшой, его поле у компаса на 10 см принято 50 мкТл и убывает как 1/r³; магнит стоит к востоку от компаса.',
  'A schematic drawing: the Earth’s field is 50 µT; the magnet is small, its field at the compass at 10 cm is taken as 50 µT and falls as 1/r³; the magnet stands east of the compass.')
s1 = section('magnets', 'Магниты и магнитное поле', 'Magnets and the magnetic field',
 bd('<p>У каждого магнита есть два полюса — северный (N) и южный (S). Одноимённые полюса отталкиваются, разноимённые притягиваются. Магнит действует на железо, никель, кобальт и друг на друга через <strong>магнитное поле</strong>. Поле показывают линиями: они выходят из северного полюса и входят в южный, а чем гуще линии, тем поле сильнее. Силу поля характеризует <strong>магнитная индукция</strong> <em>B</em>, её единица — тесла (Тл).</p><p>Стрелка компаса — маленький магнит, она ставится вдоль линий поля. Земля сама — большой магнит: у её поверхности индукция от 25 до 65 мкТл. Рядом с сильным магнитом, например, в телефонной подставке, стрелка компаса «обманывается» и показывает уже не на север.</p>',
    '<p>Every magnet has two poles — north (N) and south (S). Like poles repel, unlike poles attract. A magnet acts on iron, nickel, cobalt and on other magnets through the <strong>magnetic field</strong>. The field is shown with lines: they leave the north pole and enter the south pole, and the denser the lines, the stronger the field. The strength of the field is characterized by the <strong>magnetic flux density</strong> <em>B</em>, whose unit is the tesla (T).</p><p>A compass needle is a tiny magnet and lines up along the field lines. The Earth itself is a large magnet: at its surface the flux density is 25 to 65 µT. Near a strong magnet, for example in a phone holder, the compass needle is “fooled” and no longer points north.</p>'),
 lab1)

lab2 = model(2, 'МАГНИТНОЕ ПОЛЕ ЗЕМЛИ', 'THE EARTH’S MAGNETIC FIELD', 'erSvg', '0 0 600 250',
  slider('el', 'Широта', 'Latitude', 0, 90, 1, 41),
  stats([('eB', 'Индукция поля Земли', 'Earth’s field flux density'), ('eI', 'Наклонение (угол к горизонту)', 'Inclination (angle to the horizon)')]),
  'erFb', 'Схема условная: простая дипольная модель, B = B₀·√(1 + 3 sin²φ), tg I = 2 tg φ, B₀ ≈ 31 мкТл. Реальное поле неоднородно.',
  'A schematic drawing: a simple dipole model, B = B₀·√(1 + 3 sin²φ), tan I = 2 tan φ, B₀ ≈ 31 µT. The real field is not uniform.')
s2 = section('earth', 'Земля — большой магнит', 'The Earth is a big magnet',
 bd('<p>Поле Земли возникает из-за движения расплавленного железа в её внешнем ядре. Грубо его можно представить полем магнита-диполя, наклонённого примерно на 11° к оси вращения. Южный магнитный полюс этого «магнита» находится у северного географического полюса — поэтому северный конец стрелки компаса и показывает на север.</p><p>У экватора поле почти горизонтально и слабее, у полюсов оно направлено почти вертикально и сильнее примерно вдвое. На широте Бишкека (≈ 42° с. ш.) оно наклонено к горизонту примерно на 60° по этой модели. Компас показывает направление горизонтальной составляющей.</p>',
    '<p>The Earth’s field arises from the motion of molten iron in its outer core. Roughly it can be represented by the field of a dipole magnet tilted about 11° to the rotation axis. The south magnetic pole of this “magnet” lies near the north geographic pole — so the north end of a compass needle points north.</p><p>At the equator the field is nearly horizontal and weaker; near the poles it is nearly vertical and about twice as strong. At the latitude of Bishkek (≈ 42° N) it is inclined to the horizon by about 60° in this model. A compass shows the direction of the horizontal component.</p>'),
 lab2)

lab3 = model(3, 'РАЗРЕЗАЕМ МАГНИТ', 'CUTTING A MAGNET', 'cuSvg', '0 0 600 200',
  slider('cn', 'На сколько частей разрезать', 'How many pieces to cut into', 1, 6, 1, 3),
  stats([('cP', 'Получилось магнитов', 'Magnets obtained'), ('cS', 'Полюсов у каждого', 'Poles on each'), ('cM', 'Отдельных «северных» полюсов', 'Isolated “north” poles')]),
  'cuFb', 'Схема условная: каждая часть магнита — снова магнит с двумя полюсами.', 'A schematic drawing: each piece of a magnet is again a magnet with two poles.')
s3 = section('cut', 'Магнитных «зарядов» нет', 'There are no magnetic “charges”',
 bd('<p>Электрические заряды бывают по отдельности: можно получить только положительный или только отрицательный. А с магнитом так не получится. Если разрезать магнит, у каждого куска снова появляются два полюса — северный и южный. Отдельных магнитных полюсов («магнитных зарядов») в природе до сих пор не обнаружено. Дело в том, что магнитное поле создают движущиеся электрические заряды: токи в атомах. Об этом — следующая глава.</p>',
    '<p>Electric charges occur separately: one can have only positive or only negative. With a magnet this is impossible. If a magnet is cut, each piece again has two poles — north and south. Isolated magnetic poles (“magnetic charges”) have so far not been found in nature. The point is that magnetic fields are created by moving electric charges: currents inside atoms. That is the subject of the next chapter.</p>'),
 lab3)

tasks = [
 task(1, 'Одноимённые полюса', 'Like poles', 'Два одинаковых магнита сближают северными полюсами. Что произойдёт? А если северным и южным?', 'Two identical magnets are brought together with their north poles facing. What happens? And with a north and a south?',
  'N–N и N–S', 'N–N and N–S', 'Одноимённые полюса отталкиваются, разноимённые притягиваются.', 'Like poles repel, unlike poles attract.',
  'N–N: отталкиваются; N–S: притягиваются.', 'N–N: they repel; N–S: they attract.', True),
 task(2, 'Магнит на ручке компаса', 'A magnet near a compass', 'Поле Земли 50 мкТл, а у компаса поле магнита направлено перпендикулярно и равно 50 мкТл. На какой угол отклонится стрелка от севера?', 'The Earth’s field is 50 µT, and at the compass the magnet’s field is perpendicular to it and equals 50 µT. By what angle does the needle deviate from north?',
  'B₁ = 50 мкТл, B₂ = 50 мкТл', 'B₁ = 50 µT, B₂ = 50 µT', 'Стрелка встаёт по сумме полей: tg α = B₂ / B₁ = 50 / 50 = 1.<br>α = 45°.', 'The needle aligns with the sum of the fields: tan α = B₂ / B₁ = 50 / 50 = 1.<br>α = 45°.',
  '45°.', '45°.'),
 task(3, 'Слабое поле', 'A weaker field', 'Поле магнита убывает как 1/r³. Как изменится оно при увеличении расстояния вдвое?', 'The field of a magnet falls as 1/r³. How does it change if the distance doubles?',
  'r₂ = 2r₁', 'r₂ = 2r₁', 'B ~ 1/r³, при 2r: B уменьшится в 2³ = 8 раз.', 'B ~ 1/r³, at 2r: B decreases 2³ = 8 times.',
  'в 8 раз.', '8 times.'),
 task(4, 'Поле на экваторе', 'Field at the equator', 'По дипольной модели B = B₀·√(1 + 3 sin²φ), B₀ = 31 мкТл. Найдите индукцию на экваторе и на полюсе.', 'In the dipole model B = B₀·√(1 + 3 sin²φ), B₀ = 31 µT. Find the flux density at the equator and at the pole.',
  'B₀ = 31 мкТл, φ = 0° и 90°', 'B₀ = 31 µT, φ = 0° and 90°', 'Экватор: sin 0 = 0, B = 31 мкТл.<br>Полюс: sin 90° = 1, B = 31 · √4 = 62 мкТл.', 'Equator: sin 0 = 0, B = 31 µT.<br>Pole: sin 90° = 1, B = 31 · √4 = 62 µT.',
  '31 мкТл на экваторе и 62 мкТл на полюсе: вдвое больше. Значения укладываются в 25–65 мкТл.', '31 µT at the equator and 62 µT at the pole: twice as much. The values fit within 25–65 µT.'),
 task(5, 'Наклонение в Бишкеке', 'Inclination at Bishkek', 'Найдите наклонение поля Земли на широте 42° по модели tg I = 2 tg φ.', 'Find the inclination of the Earth’s field at latitude 42° from tan I = 2 tan φ.',
  'φ = 42°', 'φ = 42°', 'tg 42° ≈ 0,90, значит tg I ≈ 1,80.<br>I = arctg 1,80 ≈ 61°.', 'tan 42° ≈ 0.90, so tan I ≈ 1.80.<br>I = arctan 1.80 ≈ 61°.',
  'около 61°: линии поля идут круто вниз.', 'about 61°: the field lines go steeply downward.'),
 task(6, 'Разрезали пополам', 'Cut in half', 'Стержневой магнит разрезали пополам, а потом каждую часть ещё раз пополам. Сколько получилось магнитов и сколько у них всего полюсов?', 'A bar magnet was cut in half, and then each part cut in half again. How many magnets are there and how many poles in all?',
  '2 разреза → 4 части', '2 cuts → 4 pieces', 'Частей: 2 · 2 = 4.<br>У каждой 2 полюса: 4 · 2 = 8 полюсов.', 'Pieces: 2 · 2 = 4.<br>Each has 2 poles: 4 · 2 = 8 poles.',
  '4 магнита и 8 полюсов; отдельных полюсов нет.', '4 magnets and 8 poles; there are no isolated poles.'),
]

quiz = [
 ('Как взаимодействуют одноимённые полюса магнитов?', [('Притягиваются', 'Притягиваются разноимённые.'), ('Отталкиваются', 'Верно.'), ('Не взаимодействуют', 'Взаимодействие есть всегда.')],
  'How do like poles of magnets interact?', [('They attract', 'It is unlike poles that attract.'), ('They repel', 'Correct.'), ('They do not interact', 'There is always an interaction.')], 1),
 ('Куда направлены линии магнитного поля вне магнита?', [('От южного полюса к северному', 'Вне магнита они идут от северного к южному.'), ('От северного полюса к южному', 'Верно.'), ('По кругу вокруг магнита, не касаясь полюсов', 'Они выходят и входят в полюса.')],
  'Where do the field lines point outside a magnet?', [('From the south pole to the north', 'Outside the magnet they go from north to south.'), ('From the north pole to the south', 'Correct.'), ('In circles around the magnet, not touching the poles', 'They leave and enter at the poles.')], 1),
 ('В каких единицах измеряют магнитную индукцию?', [('В теслах', 'Верно.'), ('В вольтах', 'Вольт — единица напряжения.'), ('В амперах', 'Ампер — единица силы тока.')],
  'In which units is magnetic flux density measured?', [('In teslas', 'Correct.'), ('In volts', 'The volt is a unit of voltage.'), ('In amperes', 'The ampere is a unit of current.')], 0),
 ('Что покажет стрелка компаса вдали от магнитов?', [('Направление на север (магнитный)', 'Верно: она ставится вдоль поля Земли.'), ('Направление на ближайший город', 'Стрелка реагирует на поле.'), ('Любое направление', 'Направление определено полем Земли.')],
  'What does a compass needle show far from magnets?', [('The direction to (magnetic) north', 'Correct: it lines up with the Earth’s field.'), ('The direction to the nearest city', 'The needle responds to the field.'), ('Any direction', 'The direction is set by the Earth’s field.')], 0),
 ('Какова индукция поля Земли у поверхности?', [('Около 25–65 мкТл', 'Верно.'), ('Около 25–65 Тл', 'Это в миллион раз больше.'), ('Около 25–65 мТл', 'Это в тысячу раз больше.')],
  'What is the Earth’s field flux density near the surface?', [('About 25–65 µT', 'Correct.'), ('About 25–65 T', 'That is a million times more.'), ('About 25–65 mT', 'That is a thousand times more.')], 0),
 ('Что получится, если разрезать магнит пополам?', [('Северный полюс отдельно, южный отдельно', 'Отдельных полюсов не бывает.'), ('Два магнита, у каждого два полюса', 'Верно.'), ('Два куска без магнитных свойств', 'Свойства сохраняются.')],
  'What happens if a magnet is cut in half?', [('One north pole, one south pole, separate', 'Isolated poles do not exist.'), ('Two magnets, each with two poles', 'Correct.'), ('Two pieces without magnetic properties', 'The properties remain.')], 1),
 ('Почему стрелка компаса показывает на север?', [('Земля — большой магнит, и стрелка ставится вдоль его поля', 'Верно.'), ('Её притягивает Полярная звезда', 'Звёзды тут ни при чём.'), ('Север тяжелее юга', 'Дело не в тяжести.')],
  'Why does a compass needle point north?', [('The Earth is a big magnet and the needle lines up with its field', 'Correct.'), ('It is attracted by the Pole Star', 'Stars have nothing to do with it.'), ('North is heavier than south', 'It is not a matter of weight.')], 0),
 ('Откуда берётся магнитное поле Земли?', [('От движения расплавленного железа во внешнем ядре', 'Верно.'), ('От океанов', 'Не от океанов.'), ('От Луны', 'Не от Луны.')],
  'Where does the Earth’s magnetic field come from?', [('From the motion of molten iron in the outer core', 'Correct.'), ('From the oceans', 'Not from the oceans.'), ('From the Moon', 'Not from the Moon.')], 0),
]

js = r'''
const T={ru:{
 cpLabel:"Компас с магнитом рядом",erLabel:"Линия поля Земли на выбранной широте",cuLabel:"Разрезанный на части магнит",
 cpFb:"Чем ближе магнит, тем сильнее он влияет на стрелку.",erFb:"К полюсам поле растёт и становится почти вертикальным.",cuFb:"Сколько ни режь, у каждого куска два полюса."},
 en:{
 cpLabel:"A compass with a magnet nearby",erLabel:"A field line of the Earth at the chosen latitude",cuLabel:"A magnet cut into pieces",
 cpFb:"The closer the magnet, the stronger its effect on the needle.",erFb:"Towards the poles the field grows and becomes almost vertical.",cuFb:"However many times you cut, each piece has two poles."}};
function drawCp(){const t=tt(),d=+$("cd").value,Bm=50*Math.pow(10/d,3),Be=50,ang=Math.atan2(Bm,Be)*180/Math.PI;
 const cx=250,cy=125,r=70,a=ang*Math.PI/180;
 let g='<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="#f1efe8" stroke="#18181a" stroke-width="2"/>';
 g+=svgText(cx,cy-r+14,"N","#66666b","middle",13);
 const nx=cx+Math.sin(a)*(r-12),ny=cy-Math.cos(a)*(r-12);
 g+='<line x1="'+(2*cx-nx)+'" y1="'+(2*cy-ny)+'" x2="'+nx+'" y2="'+ny+'" stroke="#18181a" stroke-width="4"/><circle cx="'+nx+'" cy="'+ny+'" r="6" fill="#b6533f"/>';
 const mx=cx+r+30+d*8;
 g+='<rect x="'+mx+'" y="'+(cy-16)+'" width="64" height="32" fill="#3f5f8f" stroke="#18181a"/><rect x="'+(mx+32)+'" y="'+(cy-16)+'" width="32" height="32" fill="#b6533f" stroke="#18181a"/>'+svgText(mx+16,cy+5,"S","#fff","middle",14)+svgText(mx+48,cy+5,"N","#fff","middle",14);
 g+=svgText(cx,cy+r+24,d+(lang==="ru"?" см":" cm"),"#66666b","middle",12);
 $("cpSvg").innerHTML=g;
 $("cdOut").textContent=d+(lang==="ru"?" см":" cm");
 $("cB").textContent=(Bm>=1000?fmt(Bm/1000,1)+(lang==="ru"?" мТл":" mT"):fmt(Bm,1)+(lang==="ru"?" мкТл":" µT"));$("cA").textContent=fmt(ang,0)+"°";$("cpFb").textContent=t.cpFb}
$("cd").addEventListener("input",drawCp);
function drawEr(){const t=tt(),ph=+$("el").value,p=ph*Math.PI/180,B=31*Math.sqrt(1+3*Math.sin(p)*Math.sin(p)),I=Math.atan(2*Math.tan(Math.min(p,1.5707)))*180/Math.PI;
 const cx=200,cy=125,R=95;
 let g='<circle cx="'+cx+'" cy="'+cy+'" r="'+R+'" fill="#e3ede6" stroke="#18181a" stroke-width="2"/><line x1="'+(cx-R-20)+'" y1="'+cy+'" x2="'+(cx+R+20)+'" y2="'+cy+'" stroke="#c9c2b0" stroke-dasharray="4 3"/>';
 const px=cx+R*Math.cos(p),py=cy-R*Math.sin(p),ia=I*Math.PI/180;
 const dx=Math.cos(ia)*(-Math.sin(p))+Math.sin(ia)*(-Math.cos(p)),dy=Math.cos(ia)*(-Math.cos(p))+Math.sin(ia)*(Math.sin(p));
 g+='<circle cx="'+px+'" cy="'+py+'" r="6" fill="#b6533f"/>'+arrow(px-dx*20,py-dy*20,px+dx*30,py+dy*30,"#2f6f5d",3);
 g+=svgText(cx,cy-R-10,lang==="ru"?"северный географический полюс":"north geographic pole","#66666b","middle",11);
 g+=svgText(420,110,"B = "+fmt(B,1)+(lang==="ru"?" мкТл":" µT"),"#18181a","start",16)+svgText(420,140,(lang==="ru"?"наклонение ":"inclination ")+fmt(I,0)+"°","#18181a","start",14);
 $("erSvg").innerHTML=g;
 $("elOut").textContent=ph+"°";
 $("eB").textContent=fmt(B,1)+(lang==="ru"?" мкТл":" µT");$("eI").textContent=fmt(I,0)+"°";$("erFb").textContent=t.erFb}
$("el").addEventListener("input",drawEr);
function drawCu(){const t=tt(),n=+$("cn").value,w=480/n;
 let g='';for(let i=0;i<n;i++){const x=60+i*w+4,ww=w-8;g+='<rect x="'+x+'" y="70" width="'+ww+'" height="50" fill="#3f5f8f" stroke="#18181a"/><rect x="'+(x+ww/2)+'" y="70" width="'+ww/2+'" height="50" fill="#b6533f" stroke="#18181a"/>'+svgText(x+ww/4,100,"S","#fff","middle",14)+svgText(x+ww*3/4,100,"N","#fff","middle",14)}
 $("cuSvg").innerHTML=g;
 $("cnOut").textContent=n;$("cP").textContent=n;$("cS").textContent="2";$("cM").textContent="0";$("cuFb").textContent=t.cuFb}
$("cn").addEventListener("input",drawCu);
const LAB={ru:{cpSvg:T.ru.cpLabel,erSvg:T.ru.erLabel,cuSvg:T.ru.cuLabel},en:{cpSvg:T.en.cpLabel,erSvg:T.en.erLabel,cuSvg:T.en.cuLabel}};
function drawAll(){drawCp();drawEr();drawCu()}
'''

c = dict(n='21', slug='21-magnets.html', block='IV', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Магниты и магнитное поле', 'Magnets and the magnetic field'),
 desc='Глава 21 Атласа физики: полюса магнитов, магнитное поле, магнитная индукция, поле Земли, компас.',
 lead=('Почему стрелка компаса показывает на север и почему рядом с магнитом она сбивается. Полюса, магнитное поле и Земля как огромный магнит.',
       'Why a compass needle points north and why it is thrown off near a magnet. Poles, the magnetic field and the Earth as a giant magnet.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('magnets', 'Магниты', 'Magnets'), ('earth', 'Земля', 'The Earth'), ('cut', 'Разрезаем магнит', 'Cutting a magnet'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Путешественник идёт по горной тропе с компасом: стрелка уверенно показывает на север. Но стоит ему положить компас на металлический ящик или рядом с телефоном в магнитном чехле — и стрелка начинает показывать куда-то в сторону.</p><p>Что заставляет стрелку «выбирать» направление и почему её можно сбить?</p>',
         '<p>A traveller walks along a mountain path with a compass: the needle points firmly north. But as soon as he puts the compass on a metal box or beside a phone in a magnetic case, the needle begins to point somewhere aside.</p><p>What makes the needle “choose” a direction and why can it be thrown off?</p>'),
 hint=('Подсказку даст модель «Компас рядом с магнитом». Разгадка — в конце главы.', 'The “A compass near a magnet” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему компас можно сбить', 'The answer: why a compass can be thrown off'),
 answer=('<p>Стрелка — маленький магнит, и она ставится вдоль полного магнитного поля в этом месте. Вдали от других источников это поле Земли (около 50 мкТл), и стрелка показывает на север. Но рядом с магнитом или большим железным предметом добавляется ещё одно поле, часто сильнее земного. Стрелка ставится вдоль суммы полей и отклоняется (модель 1: уже на расстоянии 10 см небольшой магнит отклоняет стрелку на 45°).</p><p>Поэтому при ориентировании компас держат подальше от телефона, ножа и других металлических предметов.</p>',
         '<p>The needle is a tiny magnet and lines up along the total magnetic field at that place. Far from other sources this is the Earth’s field (about 50 µT) and the needle points north. But near a magnet or a large iron object another field is added, often stronger than the Earth’s. The needle lines up with the sum of the fields and deflects (model 1: at 10 cm a small magnet already deflects the needle by 45°).</p><p>That is why a compass is held away from a phone, a knife and other metal objects.</p>'),
 sources=[
  ('Магнитное поле Земли: индукция 25–65 мкТл, наклон диполя ≈ 11° —', 'The Earth’s magnetic field: 25–65 µT, dipole tilt ≈ 11° —', LINK('https://en.wikipedia.org/wiki/Earth%27s_magnetic_field', 'Wikipedia: Earth’s magnetic field') + ', ' + LINK('https://worldatlas.com/articles/what-is-earth-s-magnetic-field.html', 'WorldAtlas: What is Earth’s magnetic field')),
  ('Дипольная модель поля Земли —', 'The dipole model of the Earth’s field —', LINK('https://en.wikipedia.org/wiki/Magnetic_dipole', 'Wikipedia: Magnetic dipole')),
  ('Магниты, полюса, магнитная индукция —', 'Magnets, poles, magnetic flux density —', LINK('https://openstax.org/books/university-physics-volume-2/pages/11-introduction', 'OpenStax University Physics, Vol. 2, гл. 11'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Поле магнита в модели компаса — условное; дипольная формула поля Земли — упрощение.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The magnet’s field in the compass model is assumed; the dipole formula for the Earth’s field is a simplification.'),
 prev=('20-electrical-safety.html', 'Глава 20 · Электробезопасность', 'Chapter 20 · Electrical safety'),
 next=('22-magnetic-field-of-current.html', 'Глава 22 · Магнитное поле тока', 'Chapter 22 · The magnetic field of a current'),
 js=js)
build(c)
