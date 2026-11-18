# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ПАРАЛЛАКС: РАССТОЯНИЕ ДО ЗВЕЗДЫ', 'PARALLAX: THE DISTANCE TO A STAR', 'pxSvg', '0 0 600 250',
  slider('xp', 'Параллакс звезды', 'Parallax of the star', 0.01, 0.8, 0.01, 0.77),
  stats([('xD', 'Расстояние d = 1/p', 'Distance d = 1/p'), ('xL', 'В световых годах', 'In light-years'), ('xT', 'Свет идёт до нас', 'Light travels to us')]),
  'pxFb', 'Схема условная, без масштаба; параллакс p — в угловых секундах, расстояние d — в парсеках (1 пк = 3,26 светового года).',
  'A schematic drawing, not to scale; the parallax p in arcseconds, the distance d in parsecs (1 pc = 3.26 light-years).')
s1 = section('parallax', 'Как измерить расстояние до звезды', 'How to measure the distance to a star',
 bd('<p>Звёзды очень далеки. Расстояние до ближайших измеряют по <strong>параллаксу</strong>: за полгода Земля смещается по орбите на 2 а.е., и ближняя звезда слегка «качается» на фоне далёких. Угол смещения <em>p</em> (в угловых секундах) связан с расстоянием просто: <em>d = 1/p</em> (в парсеках). Самая близкая звезда после Солнца, Проксима Центавра, имеет параллакс 0,77″ — это 1,3 парсека, или 4,2 светового года.</p>',
    '<p>Stars are very far away. The distances to the nearest are measured by <strong>parallax</strong>: in half a year the Earth moves 2 AU along its orbit and a nearby star “shifts” slightly against the distant ones. The angle of shift <em>p</em> (in arcseconds) is related to the distance simply: <em>d = 1/p</em> (in parsecs). The nearest star after the Sun, Proxima Centauri, has a parallax of 0.77″ — that is 1.3 parsecs or 4.2 light-years.</p>')
 + formula('d [пк] = 1 / p [″],   1 пк ≈ 3,26 св. года', 'световой год — расстояние, которое свет проходит за год: 9,46·10¹² км', 'a light-year is the distance light covers in a year: 9.46·10¹² km'),
 lab1)

lab2 = model(2, 'ЦВЕТ И СВЕТИМОСТЬ ЗВЕЗДЫ', 'THE COLOUR AND LUMINOSITY OF A STAR', 'stSvg', '0 0 600 250',
  slider('st', 'Температура поверхности', 'Surface temperature', 2500, 30000, 1, 5772) + slider('sr', 'Радиус (в радиусах Солнца)', 'Radius (in solar radii)', 0.1, 100, 0.1, 1),
  stats([('tW', 'Длина волны максимума λ = b/T', 'Wavelength of the peak λ = b/T'), ('tC', 'Цвет', 'Colour'), ('tL', 'Светимость (Солнце = 1) L = R²·(T/5772)⁴', 'Luminosity (Sun = 1) L = R²·(T/5772)⁴')]),
  'stFb', 'Схема условная: звезда считается абсолютно чёрным телом; b = 2,898·10⁶ нм·К; температура Солнца 5772 К.',
  'A schematic drawing: the star is treated as a black body; b = 2.898·10⁶ nm·K; the Sun’s temperature is 5772 K.')
s2 = section('colour', 'Цвет звезды — её температура', 'The colour of a star is its temperature',
 bd('<p>Нагретое тело излучает свет всех цветов, но больше всего на одной длине волны, которая зависит от температуры (<strong>закон Вина</strong>): чем горячее, тем короче волна. Холодные звёзды красные, как Бетельгейзе; Солнце жёлтое; самые горячие — голубые. Полная мощность излучения растёт очень быстро: как <em>T⁴</em> и как площадь поверхности <em>R²</em> (закон Стефана–Больцмана).</p>',
    '<p>A heated body radiates light of all colours but most strongly at one wavelength that depends on the temperature (<strong>Wien’s law</strong>): the hotter the shorter the wavelength. Cool stars are red like Betelgeuse; the Sun is yellow; the hottest are blue. The total power of radiation rises very fast: as <em>T⁴</em> and as the surface area <em>R²</em> (the Stefan–Boltzmann law).</p>')
 + formula('λ_max = 2,898·10⁶ нм·К / T,   L ~ R² · T⁴', 'вдвое горячее — в 16 раз ярче при том же размере', 'twice as hot — 16 times brighter at the same size'),
 lab2)

lab3 = model(3, 'ТЕЛЕСКОП И АТМОСФЕРА', 'A TELESCOPE AND THE ATMOSPHERE', 'tlSvg', '0 0 600 250',
  slider('td', 'Диаметр объектива', 'Aperture diameter', 0.05, 2, 0.05, 1) + slider('ts', 'Размытие атмосферой (сиинг)', 'Atmospheric blur (seeing)', 0.3, 4, 0.1, 1),
  stats([('tG', 'Светосбор по сравнению с глазом (зрачок 7 мм)', 'Light gathering compared with the eye (7 mm pupil)'), ('tD', 'Предел дифракции 1,22·λ/D (λ = 550 нм)', 'Diffraction limit 1.22·λ/D (λ = 550 nm)'), ('tE', 'Реальная резкость', 'Real sharpness'), ('tM', 'Наименьшая деталь на Луне', 'The smallest detail on the Moon')]),
  'tlFb', 'Схема условная: сиинг — условное значение для ночи; реальная резкость — большее из дифракционного предела и сиинга.',
  'A schematic drawing: seeing is an assumed value for a night; the real sharpness is the larger of the diffraction limit and the seeing.')
s3 = section('telescope', 'Зачем телескопу большой объектив и высокая гора', 'Why a telescope needs a large aperture and a high mountain',
 bd('<p>Объектив собирает свет: площадь пропорциональна <em>D²</em>, и вдвое больший диаметр даёт вчетверо больше света — видны более слабые звёзды. Диаметр определяет и <strong>дифракционный предел резкости</strong> <em>1,22·λ/D</em>. Но воздух дрожит, и изображения «плывут» на секунду дуги и больше — это <strong>сиинг</strong>. Поэтому обсерватории строят высоко в горах, где воздуха над головой меньше и он спокойнее, сухой и тёмное небо.</p>',
    '<p>The aperture collects light: the area is proportional to <em>D²</em> and a twice larger diameter gives four times more light — fainter stars become visible. The diameter also sets the <strong>diffraction limit of sharpness</strong> <em>1.22·λ/D</em>. But the air shimmers and images “swim” by an arcsecond or more — this is <strong>seeing</strong>. That is why observatories are built high in the mountains where there is less air overhead, it is calmer and drier and the sky is dark.</p>')
 + formula('N = (D / 7 мм)²,   θ = 1,22 · λ / D', 'при большом D резкость ограничена не оптикой, а атмосферой', 'for a large D the sharpness is limited not by the optics but by the atmosphere')
 + bd('<p>Недалеко от нас, на хребтах Тянь-Шаня близ Алматы, на высоте около 2700–2800 м работает Тянь-Шаньская астрономическая обсерватория (основана в 1957 году; два телескопа диаметром 1 м). Это тот же горный хребет Тянь-Шань, что тянется и по Кыргызстану.</p>',
      '<p>Not far from us, in the Tien Shan ridges near Almaty at an altitude of about 2,700–2,800 m, works the Tien Shan Astronomical Observatory (founded in 1957; two telescopes of 1 m diameter). It is the same Tien Shan mountain range that stretches across Kyrgyzstan.</p>'),
 lab3)

tasks = [
 task(1, 'Параллакс 0,1″', 'A parallax of 0.1″', 'Параллакс звезды 0,1″. Найдите расстояние в парсеках и световых годах.', 'A star has a parallax of 0.1″. Find the distance in parsecs and light-years.',
  'p = 0,1″', 'p = 0.1″', 'd = 1/p = 1 / 0,1 = 10 пк.<br>10 · 3,26 = 32,6 светового года.', 'd = 1/p = 1 / 0.1 = 10 pc.<br>10 · 3.26 = 32.6 light-years.', '10 пк ≈ 32,6 св. года.', '10 pc ≈ 32.6 light-years.', True),
 task(2, 'К Проксиме Центавра', 'To Proxima Centauri', 'До Проксимы Центавра 4,24 светового года. Сколько лет летел бы к ней зонд со скоростью 17 км/с? (1 св. год = 9,46·10¹² км.)', 'Proxima Centauri is 4.24 light-years away. How many years would a probe at 17 km/s take to fly to it? (1 light-year = 9.46·10¹² km.)',
  'd = 4,24 св. года, v = 17 км/с', 'd = 4.24 ly, v = 17 km/s', 'd = 4,24 · 9,46·10¹² ≈ 4,01·10¹³ км.<br>t = d/v = 4,01·10¹³ / 17 ≈ 2,36·10¹² с.<br>В годах: 2,36·10¹² / 3,156·10⁷ ≈ 7,5·10⁴ лет.', 'd = 4.24 · 9.46·10¹² ≈ 4.01·10¹³ km.<br>t = d/v = 4.01·10¹³ / 17 ≈ 2.36·10¹² s.<br>In years: 2.36·10¹² / 3.156·10⁷ ≈ 7.5·10⁴ years.', 'около 75 тысяч лет.', 'about 75 thousand years.'),
 task(3, 'Закон Вина', 'Wien’s law', 'Найдите длину волны максимума излучения у Солнца (5772 К) и у красной звезды 3000 К.', 'Find the wavelength of peak radiation for the Sun (5772 K) and for a red star of 3000 K.',
  'b = 2,898·10⁶ нм·К', 'b = 2.898·10⁶ nm·K', 'Солнце: 2,898·10⁶ / 5772 ≈ 502 нм (зелёно-голубой, видимый).<br>Красная звезда: 2,898·10⁶ / 3000 ≈ 966 нм — инфракрасное; поэтому звезда выглядит красной (видимая часть — хвост).', 'Sun: 2.898·10⁶ / 5772 ≈ 502 nm (blue-green, visible).<br>Red star: 2.898·10⁶ / 3000 ≈ 966 nm — infrared; so the star looks red (the visible part is the tail).', '≈ 502 нм и ≈ 966 нм.', '≈ 502 nm and ≈ 966 nm.'),
 task(4, 'Светимость гиганта', 'The luminosity of a giant', 'Красный гигант: T = 3500 К, R = 800 радиусов Солнца. Найдите светимость в светимостях Солнца.', 'A red giant: T = 3,500 K, R = 800 solar radii. Find the luminosity in solar luminosities.',
  'T = 3500 К, R = 800 R☉', 'T = 3,500 K, R = 800 R☉', 'L = R²·(T/5772)⁴ = 640 000 · (0,6064)⁴ = 640 000 · 0,1352 ≈ 8,7·10⁴.', 'L = R²·(T/5772)⁴ = 640,000 · (0.6064)⁴ = 640,000 · 0.1352 ≈ 8.7·10⁴.', '≈ 87 000 светимостей Солнца, хотя звезда холоднее.', '≈ 87,000 solar luminosities though the star is cooler.'),
 task(5, 'Светосбор метрового телескопа', 'The light gathering of a 1 m telescope', 'Во сколько раз метровый объектив собирает больше света, чем зрачок глаза диаметром 7 мм?', 'How many times more light does a 1 m aperture collect than an eye pupil of 7 mm?',
  'D = 1 м, d = 0,007 м', 'D = 1 m, d = 0.007 m', 'N = (D/d)² = (1 / 0,007)² ≈ 143² ≈ 2,0·10⁴.', 'N = (D/d)² = (1 / 0.007)² ≈ 143² ≈ 2.0·10⁴.', 'примерно в 20 000 раз.', 'about 20,000 times.'),
 task(6, 'Резкость метрового телескопа', 'The sharpness of a 1 m telescope', 'Найдите дифракционный предел для D = 1 м и λ = 550 нм (в угловых секундах; 1 рад = 206 265″). Что ограничивает резкость, если сиинг 1″?', 'Find the diffraction limit for D = 1 m and λ = 550 nm (in arcseconds; 1 rad = 206,265″). What limits the sharpness if the seeing is 1″?',
  'λ = 5,5·10⁻⁷ м, D = 1 м', 'λ = 5.5·10⁻⁷ m, D = 1 m', 'θ = 1,22 · 5,5·10⁻⁷ / 1 = 6,7·10⁻⁷ рад = 6,7·10⁻⁷ · 206 265 ≈ 0,14″.<br>Сиинг 1″ больше, значит резкость ограничена атмосферой.', 'θ = 1.22 · 5.5·10⁻⁷ / 1 = 6.7·10⁻⁷ rad = 6.7·10⁻⁷ · 206,265 ≈ 0.14″.<br>Seeing of 1″ is larger so the sharpness is limited by the atmosphere.', '≈ 0,14″; реально ≈ 1″ из-за атмосферы.', '≈ 0.14″; in practice ≈ 1″ because of the atmosphere.'),
]

quiz = [
 qz('Как связаны параллакс p (″) и расстояние d (пк)?', 'd = 1/p', 'd = p', 'd = p²', 'Меньше параллакс — дальше звезда.',
    'How are parallax p (″) and distance d (pc) related?', 'd = 1/p', 'd = p', 'd = p²', 'A smaller parallax means a farther star.'),
 qz('Что такое световой год?', 'Расстояние, которое свет проходит за год', 'Время обращения Земли', 'Скорость света', 'Около 9,46·10¹² км.',
    'What is a light-year?', 'The distance light covers in a year', 'The time of the Earth’s revolution', 'The speed of light', 'About 9.46·10¹² km.'),
 qz('Какого цвета самые горячие звёзды?', 'Голубые', 'Красные', 'Жёлтые', 'Чем горячее, тем короче длина волны максимума.',
    'What colour are the hottest stars?', 'Blue', 'Red', 'Yellow', 'The hotter the shorter the peak wavelength.'),
 qz('Как светимость звезды зависит от температуры при том же размере?', 'Как T⁴', 'Как T', 'Не зависит', 'Закон Стефана–Больцмана.',
    'How does the luminosity of a star depend on temperature at the same size?', 'As T⁴', 'As T', 'It does not', 'The Stefan–Boltzmann law.'),
 qz('Красный гигант холоднее Солнца, но намного ярче. Почему?', 'У него огромная площадь поверхности', 'Он ближе', 'Он горячее', 'L ~ R²·T⁴.',
    'A red giant is cooler than the Sun but much brighter. Why?', 'It has a huge surface area', 'It is closer', 'It is hotter', 'L ~ R²·T⁴.'),
 qz('Во сколько раз вырастет светосбор при увеличении диаметра объектива вдвое?', 'В 4 раза', 'В 2 раза', 'В 8 раз', 'Площадь ~ D².',
    'How many times does light gathering grow when the aperture doubles?', '4 times', '2 times', '8 times', 'The area ~ D².'),
 qz('Почему обсерватории строят высоко в горах?', 'Меньше воздуха, он спокойнее, небо темнее', 'Там теплее', 'Чтобы быть ближе к Луне', 'Атмосфера размывает изображение.',
    'Why are observatories built high in the mountains?', 'Less air, it is calmer, the sky is darker', 'It is warmer there', 'To be closer to the Moon', 'The atmosphere blurs the image.'),
 qz('Что чаще ограничивает резкость большого наземного телескопа?', 'Дрожание атмосферы', 'Дифракция', 'Цвет звезды', 'Сиинг порядка 1″ против дифракции 0,14″.',
    'What most often limits the sharpness of a large ground telescope?', 'Atmospheric turbulence', 'Diffraction', 'The colour of the star', 'Seeing of about 1″ against diffraction of 0.14″.'),
]

js = JSL + r'''
const T={ru:{
 pxLabel:"Земля на двух сторонах орбиты и близкая звезда",stLabel:"Звезда: цвет и размер",tlLabel:"Объектив и атмосфера",
 cols:["красная","оранжевая","жёлтая","жёлто-белая","белая","голубовато-белая","голубая"],
 pxFb:"Чем меньше параллакс, тем дальше звезда.",stFb:"Холодные звёзды красные, горячие — голубые.",tlFb:"Большой объектив не поможет, если атмосфера размывает изображение."},
 en:{
 pxLabel:"The Earth on two sides of its orbit and a nearby star",stLabel:"A star: colour and size",tlLabel:"The aperture and the atmosphere",
 cols:["red","orange","yellow","yellow-white","white","bluish-white","blue"],
 pxFb:"The smaller the parallax the farther the star.",stFb:"Cool stars are red, hot ones are blue.",tlFb:"A large aperture does not help if the atmosphere blurs the image."}};
function drawPx(){const t=tt(),p=+$("xp").value,d=1/p,ly=d*3.2616;
 const sy=Math.max(40,200-Math.min(160,d*10));let g='<circle cx="300" cy="215" r="10" fill="#e8c14a"/><circle cx="220" cy="215" r="5" fill="#3f5f8f"/><circle cx="380" cy="215" r="5" fill="#3f5f8f"/><circle cx="300" cy="'+sy+'" r="8" fill="#b6533f"/><line x1="220" y1="215" x2="300" y2="'+sy+'" stroke="#c9c2b0"/><line x1="380" y1="215" x2="300" y2="'+sy+'" stroke="#c9c2b0"/>'+svgText(300,'240',U("Земля через полгода — другая точка орбиты","The Earth half a year later — the other side of the orbit"),"#66666b","middle",11);
 $("pxSvg").innerHTML=g;$("xpOut").textContent=fmt(p,2)+"″";
 $("xD").textContent=fmt(d,2)+" "+U("пк","pc");$("xL").textContent=fmt(ly,2)+" "+U("св. года","ly");$("xT").textContent=fmt(ly,2)+" "+U("лет","yr");$("pxFb").textContent=t.pxFb}
$("xp").addEventListener("input",drawPx);
function drawSt(){const t=tt(),Tm=+$("st").value,R=+$("sr").value,lam=2.898e6/Tm,L=R*R*Math.pow(Tm/5772,4);
 const ci=Tm<3700?0:Tm<5200?1:Tm<6000?2:Tm<7500?3:Tm<10000?4:Tm<20000?5:6;
 const col=["#c0392b","#e67e22","#f1c40f","#f7e9a0","#ffffff","#cfe2ff","#8fb4ff"][ci];
 const rr=10+Math.min(100,Math.sqrt(R)*10);let g='<circle cx="300" cy="125" r="'+rr+'" fill="'+col+'" stroke="#18181a" stroke-width="2"/><circle cx="520" cy="125" r="10" fill="#f1c40f" stroke="#18181a"/>'+svgText(520,160,U("Солнце","Sun"),"#66666b","middle",11);
 $("stSvg").innerHTML=g;$("stOut").textContent=num(Tm)+" "+U("К","K");$("srOut").textContent=fmt(R,1);
 $("tW").textContent=fmt(lam,0)+" "+U("нм","nm");$("tC").textContent=t.cols[ci];$("tL").textContent=L>=1000?sci(L,2):fmt(L,L<10?3:1);$("stFb").textContent=t.stFb}
["st","sr"].forEach(id=>$(id).addEventListener("input",drawSt));
function drawTl(){const t=tt(),D=+$("td").value,s=+$("ts").value,N=Math.pow(D/0.007,2),th=1.22*550e-9/D*206265,eff=Math.max(th,s),mn=eff/206265*384400;
 let g='<ellipse cx="200" cy="125" rx="'+(20+D*30)+'" ry="'+(30+D*40)+'" fill="#9a9a9a" stroke="#18181a"/>'+svgText(200,235,"D = "+fmt(D,2)+" "+U("м","m"),"#18181a","middle",12);
 for(let i=0;i<9;i++){g+='<circle cx="'+(380+(i%3)*50+ (i*7%5-2)*s*2)+'" cy="'+(70+Math.floor(i/3)*50+(i*3%5-2)*s*2)+'" r="'+(4+s*1.5)+'" fill="#e8c14a" opacity="0.8"/>'}
 $("tlSvg").innerHTML=g;$("tdOut").textContent=fmt(D,2)+" "+U("м","m");$("tsOut").textContent=fmt(s,1)+"″";
 $("tG").textContent=num(Math.round(N))+"×";$("tD").textContent=fmt(th,2)+"″";$("tE").textContent=fmt(eff,2)+"″"+(s>th?U(" (ограничивает атмосфера)"," (the atmosphere limits)"):U(" (ограничивает оптика)"," (the optics limit)"));$("tM").textContent=fmt(mn,1)+" "+U("км","km");$("tlFb").textContent=t.tlFb}
["td","ts"].forEach(id=>$(id).addEventListener("input",drawTl));
const LAB={ru:{pxSvg:T.ru.pxLabel,stSvg:T.ru.stLabel,tlSvg:T.ru.tlLabel},en:{pxSvg:T.en.pxLabel,stSvg:T.en.stLabel,tlSvg:T.en.tlLabel}};
function drawAll(){drawPx();drawSt();drawTl()}
'''

c = dict(n='43', slug='43-stars-telescopes.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Звёзды и обсерватории', 'Stars and observatories'),
 desc='Глава 43 Атласа физики: параллакс и расстояния до звёзд, закон Вина и светимость, телескоп, дифракция и сиинг, Тянь-Шаньская астрономическая обсерватория.',
 lead=('Как измеряют расстояния до звёзд, о чём говорит их цвет и зачем обсерватории строят высоко в горах.',
       'How distances to stars are measured, what their colour says and why observatories are built high in the mountains.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('parallax', 'Расстояния', 'Distances'), ('colour', 'Цвет и яркость', 'Colour and brightness'), ('telescope', 'Телескоп', 'The telescope'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Ночью в горах звёзд видно намного больше, чем в городе, и мерцают они слабее. Поэтому телескопы ставят на вершинах, а не у моря. На Тянь-Шане, на высоте около 2700 м, астрономы изучают переменные звёзды и ищут планеты у других звёзд.</p><p>Почему для телескопа важна не только величина объектива, но и высота места?</p>',
         '<p>At night in the mountains many more stars are visible than in a city and they twinkle less. That is why telescopes are placed on summits and not by the sea. In the Tien Shan, at an altitude of about 2,700 m, astronomers study variable stars and search for planets of other stars.</p><p>Why does a telescope need not only a large aperture but also a high site?</p>'),
 hint=stdhint('Звёзды и телескопы', 'Stars and telescopes'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: атмосфера — часть телескопа', 'The answer: the atmosphere is part of the telescope'),
 answer=('<p>Свет звезды проходит всю толщу воздуха, а воздух постоянно движется и неравномерно нагрет. Изображение дрожит и расплывается примерно на секунду дуги (сиинг). У метрового телескопа дифракционный предел — всего 0,14″, но реально приходится довольствоваться около 1″ (модель 3): атмосфера, а не стекло, ограничивает резкость.</p><p>На высоте 2700 м над головой примерно на четверть меньше воздуха, он суше и спокойнее, а небо темнее — поэтому звёзды чётче и видны более слабые. Оттого астрономы идут в горы, а наиболее точные наблюдения проводят и вовсе из космоса.</p>',
         '<p>The light of a star passes through the whole thickness of air and the air is constantly moving and unevenly heated. The image shimmers and spreads by about an arcsecond (seeing). A 1 m telescope has a diffraction limit of just 0.14″ but in practice one must settle for about 1″ (model 3): the atmosphere, not the glass, limits the sharpness.</p><p>At 2,700 m there is about a quarter less air overhead, it is drier and calmer and the sky is darker — so stars are sharper and fainter ones are visible. That is why astronomers go to the mountains and make the most precise observations from space.</p>'),
 sources=[
  ('Параллакс, закон Вина, светимость звёзд —', 'Parallax, Wien’s law, stellar luminosity —', LINK('https://en.wikipedia.org/wiki/Stellar_parallax', 'Wikipedia: Stellar parallax') + ', ' + LINK('https://en.wikipedia.org/wiki/Wien%27s_displacement_law', 'Wikipedia: Wien’s displacement law') + ', ' + LINK('https://openstax.org/books/astronomy-2e/pages/17-2-luminosity-and-apparent-brightness', 'OpenStax Astronomy 2e, § 17.2')),
  ('Дифракция и разрешающая способность телескопа, сиинг —', 'Diffraction and the resolving power of a telescope, seeing —', LINK('https://en.wikipedia.org/wiki/Angular_resolution', 'Wikipedia: Angular resolution') + ', ' + LINK('https://en.wikipedia.org/wiki/Astronomical_seeing', 'Wikipedia: Astronomical seeing')),
  ('Тянь-Шаньская астрономическая обсерватория (близ Алматы, около 2700–2800 м, основана 1957 г., два телескопа по 1 м) —', 'Tien Shan Astronomical Observatory (near Almaty, about 2,700–2,800 m, founded 1957, two 1 m telescopes) —', LINK('https://en.wikipedia.org/wiki/Tien_Shan_Astronomical_Observatory', 'Wikipedia: Tien Shan Astronomical Observatory') + ', ' + LINK('https://en.tengrinews.kz/science/Kazakhstan-steps-up-space-research-254980', 'Tengrinews, 2014'))],
 note=stdnote('Сиинг (0,3–4″) — условный диапазон; звёзды считаются чёрными телами; параллакс Проксимы Центавра — около 0,77″.', 'Seeing (0.3–4″) is an assumed range; stars are treated as black bodies; the parallax of Proxima Centauri is about 0.77″.'),
 prev=('42-solar-system.html', 'Глава 42 · Солнечная система', 'Chapter 42 · The Solar System'),
 next=('44-ideal-gas.html', 'Глава 44 · Идеальный газ', 'Chapter 44 · The ideal gas'),
 js=js)
build(c)
