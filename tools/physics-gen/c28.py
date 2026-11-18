# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'СЕЙСМОГРАММА', 'A SEISMOGRAM', 'smSvg', '0 0 600 250',
  slider('md', 'Расстояние до очага', 'Distance to the source', 20, 600, 10, 150),
  stats([('mP', 'Приход P-волны', 'Arrival of the P-wave'), ('mS', 'Приход S-волны', 'Arrival of the S-wave'), ('mD', 'Разница S−P', 'Difference S−P')]),
  'smFb', 'Схема условная: скорости в земной коре приняты v(P) = 6 км/с, v(S) = 3,5 км/с; запись упрощена.',
  'A schematic drawing: crustal speeds are taken as v(P) = 6 km/s, v(S) = 3.5 km/s; the record is simplified.')
s1 = section('waves', 'Сейсмические волны', 'Seismic waves',
 bd('<p>Землетрясение — это внезапный сдвиг блоков земной коры по разлому. Освободившаяся энергия расходится во все стороны <strong>сейсмическими волнами</strong>. Место сдвига под землёй — <strong>очаг</strong> (гипоцентр), точка над ним на поверхности — <strong>эпицентр</strong>.</p><p>Волны бывают разные. <strong>P-волны</strong> (первичные) — продольные: порода сжимается и растягивается вдоль направления волны, они идут быстрее всего (в коре около 6 км/с) и приходят первыми — как короткий удар. <strong>S-волны</strong> (вторичные) — поперечные, медленнее (около 3,5 км/с); они приходят вторыми и дают сильную качку. В жидкостях поперечные волны не идут, поэтому S-волны не проходят сквозь жидкое внешнее ядро Земли. Самые разрушительные — медленные <strong>поверхностные волны</strong>.</p>',
    '<p>An earthquake is a sudden slip of blocks of the Earth’s crust along a fault. The released energy spreads in all directions as <strong>seismic waves</strong>. The place of the slip underground is the <strong>focus</strong> (hypocentre), the point above it on the surface is the <strong>epicentre</strong>.</p><p>The waves are of different kinds. <strong>P-waves</strong> (primary) are longitudinal: the rock is compressed and stretched along the direction of the wave; they are the fastest (about 6 km/s in the crust) and arrive first — as a short jolt. <strong>S-waves</strong> (secondary) are transverse and slower (about 3.5 km/s); they arrive second and give strong shaking. Transverse waves do not travel in liquids, so S-waves do not pass through the liquid outer core of the Earth. The most destructive are the slow <strong>surface waves</strong>.</p>'),
 lab1)

lab2 = model(2, 'КАК НАЙТИ РАССТОЯНИЕ ДО ЭПИЦЕНТРА', 'HOW TO FIND THE DISTANCE TO THE EPICENTRE', 'epSvg', '0 0 600 250',
  slider('ed', 'Разница прихода S и P', 'Time between the S and P arrivals', 2, 80, 1, 25),
  stats([('eR', 'Расстояние d = Δt·vP·vS/(vP−vS)', 'Distance d = Δt·vP·vS/(vP−vS)'), ('eQ', 'Быстрое правило ≈ 8 км на 1 с', 'Quick rule ≈ 8 km per 1 s')]),
  'epFb', 'Схема условная: одна станция определяет только расстояние, а не направление; нужны три станции.',
  'A schematic drawing: one station gives only the distance, not the direction; three stations are needed.')
s2 = section('locate', 'Как найти эпицентр', 'How to find the epicentre',
 bd('<p>Волны P и S выходят из очага одновременно, но идут с разной скоростью. Чем дальше станция, тем больше отстаёт S-волна. Если разница прихода <em>Δt</em>, то <em>d/vS − d/vP = Δt</em>, откуда</p>',
    '<p>The P and S waves leave the source at the same time but travel at different speeds. The farther the station the more the S-wave lags. If the difference in arrival is <em>Δt</em> then <em>d/vS − d/vP = Δt</em>, whence</p>')
 + formula('d = Δt · vP · vS / (vP − vS)', 'для vP = 6, vS = 3,5 км/с: d ≈ 8,4 · Δt  (км, если Δt в секундах)', 'for vP = 6, vS = 3.5 km/s: d ≈ 8.4 · Δt  (km if Δt is in seconds)')
 + bd('<p>Одна станция даёт только расстояние: эпицентр лежит на окружности вокруг неё. Три станции дают три окружности — они пересекаются в эпицентре. Так сейсмологи находят эпицентр через считанные минуты.</p>',
      '<p>One station gives only the distance: the epicentre lies on a circle around it. Three stations give three circles — they intersect at the epicentre. That is how seismologists find an epicentre within minutes.</p>'),
 lab2)

lab3 = model(3, 'МАГНИТУДА И ЭНЕРГИЯ', 'MAGNITUDE AND ENERGY', 'mgSvg', '0 0 600 250',
  slider('mm', 'Магнитуда', 'Magnitude', 3, 8, 0.1, 5),
  stats([('mE', 'Энергия E = 10^(1,5·M + 4,8)', 'Energy E = 10^(1.5·M + 4.8)'), ('mR', 'Во сколько раз больше, чем при M = 5', 'How many times more than at M = 5'), ('mT', 'Эквивалент в тротиле', 'TNT equivalent')]),
  'mgFb', 'Схема условная: энергия сейсмических волн по формуле Гутенберга — Рихтера; 1 т тротила = 4,184·10⁹ Дж.',
  'A schematic drawing: the energy of the seismic waves by the Gutenberg–Richter formula; 1 t of TNT = 4.184·10⁹ J.')
s3 = section('mag', 'Магнитуда: почему шкала логарифмическая', 'Magnitude: why the scale is logarithmic',
 bd('<p><strong>Магнитуда</strong> — число, характеризующее размер землетрясения по записи волн. Шкала логарифмическая: рост магнитуды на 1 означает, что амплитуда волн в 10 раз больше, а энергия — примерно в 32 раза (10^1,5). Поэтому землетрясение магнитудой 7 высвобождает энергии почти в тысячу раз больше, чем магнитудой 5.</p>',
    '<p>The <strong>magnitude</strong> is a number characterising the size of an earthquake from a record of the waves. The scale is logarithmic: a rise of 1 in magnitude means the wave amplitude is 10 times greater and the energy about 32 times greater (10^1.5). So an earthquake of magnitude 7 releases nearly a thousand times more energy than one of magnitude 5.</p>')
 + formula('lg E = 1,5 · M + 4,8   (E в джоулях)', 'приближённая формула Гутенберга — Рихтера', 'the approximate Gutenberg–Richter formula')
 + bd('<p>Кыргызстан лежит в сейсмически активной зоне, где Индия медленно надвигается на Азию и поднимает Тянь-Шань. Крупнейшие события: Кеминское землетрясение 1911 года (магнитуда около 7,7–8,0 в разных оценках) и Суусамырское землетрясение 19 августа 1992 года магнитудой 7,3 (погибли 75 человек). От магнитуды зависит энергия, а от глубины, грунта и качества зданий — разрушения. Поэтому сейсмостойкое строительство спасает жизни.</p>',
      '<p>Kyrgyzstan lies in a seismically active zone where India slowly pushes into Asia and raises the Tien Shan. The largest events: the Kemin earthquake of 1911 (magnitude about 7.7–8.0 in different estimates) and the Suusamyr earthquake of 19 August 1992 of magnitude 7.3 (75 people died). The magnitude sets the energy while the damage depends on depth, ground and the quality of buildings. That is why earthquake-resistant construction saves lives.</p>'),
 lab3)

tasks = [
 task(1, 'Расстояние по S−P', 'Distance from S−P', 'Станция записала S-волну на 25 с позже P-волны. Найдите расстояние до очага при vP = 6 км/с, vS = 3,5 км/с.', 'A station recorded the S-wave 25 s after the P-wave. Find the distance to the source for vP = 6 km/s, vS = 3.5 km/s.',
  'Δt = 25 с, vP = 6 км/с, vS = 3,5 км/с', 'Δt = 25 s, vP = 6 km/s, vS = 3.5 km/s', 'd = Δt·vP·vS / (vP − vS) = 25 · 6 · 3,5 / 2,5 = 25 · 8,4 = 210 км.', 'd = Δt·vP·vS / (vP − vS) = 25 · 6 · 3.5 / 2.5 = 25 · 8.4 = 210 km.', '210 км.', '210 km.', True),
 task(2, 'Когда придут волны', 'When the waves arrive', 'До очага 120 км. Через какое время придут P- и S-волны и какова разница?', 'The source is 120 km away. When do the P and S waves arrive and what is the difference?',
  'd = 120 км', 'd = 120 km', 't(P) = 120 / 6 = 20 с.<br>t(S) = 120 / 3,5 ≈ 34,3 с.<br>Разница: 34,3 − 20 = 14,3 с.', 't(P) = 120 / 6 = 20 s.<br>t(S) = 120 / 3.5 ≈ 34.3 s.<br>Difference: 34.3 − 20 = 14.3 s.', '20 с, 34 с, разница 14 с.', '20 s, 34 s, difference 14 s.'),
 task(3, 'Быстрое правило', 'The quick rule', 'S−P = 10 с. Оцените расстояние по правилу «8 км на секунду» и точной формулой.', 'S−P = 10 s. Estimate the distance by the rule “8 km per second” and by the exact formula.',
  'Δt = 10 с', 'Δt = 10 s', 'Правило: 8 · 10 = 80 км.<br>Формула: 10 · 8,4 = 84 км.', 'The rule: 8 · 10 = 80 km.<br>The formula: 10 · 8.4 = 84 km.', '80 и 84 км — разница около 5%.', '80 and 84 km — a difference of about 5%.'),
 task(4, 'Энергия Суусамыра', 'The energy of Suusamyr', 'Найдите энергию землетрясения магнитудой 7,3 и сравните с тротилом (1 т = 4,184·10⁹ Дж).', 'Find the energy of an earthquake of magnitude 7.3 and compare it with TNT (1 t = 4.184·10⁹ J).',
  'M = 7,3', 'M = 7.3', 'lg E = 1,5 · 7,3 + 4,8 = 15,75.<br>E = 10^15,75 ≈ 5,6·10¹⁵ Дж.<br>В тротиле: 5,6·10¹⁵ / 4,184·10⁹ ≈ 1,3·10⁶ т.', 'lg E = 1.5 · 7.3 + 4.8 = 15.75.<br>E = 10^15.75 ≈ 5.6·10¹⁵ J.<br>In TNT: 5.6·10¹⁵ / 4.184·10⁹ ≈ 1.3·10⁶ t.', 'около 5,6·10¹⁵ Дж, то есть 1,3 млн тонн тротила.', 'about 5.6·10¹⁵ J, that is 1.3 million tonnes of TNT.'),
 task(5, 'Сравнение магнитуд', 'Comparing magnitudes', 'Во сколько раз энергия землетрясения магнитудой 7,3 больше, чем магнитудой 5,3?', 'By what factor is the energy of a magnitude 7.3 earthquake greater than that of magnitude 5.3?',
  'ΔM = 2', 'ΔM = 2', 'Отношение = 10^(1,5 · 2) = 10³ = 1000.', 'The ratio = 10^(1.5 · 2) = 10³ = 1,000.', 'в 1000 раз.', '1,000 times.'),
 task(6, 'Сколько работала бы ГЭС', 'How long a power plant would need', 'Энергия землетрясения магнитудой 5 — около 2,0·10¹² Дж. Сколько времени должна работать Токтогульская ГЭС мощностью 1200 МВт, чтобы выработать столько энергии?', 'The energy of a magnitude 5 earthquake is about 2.0·10¹² J. How long must the 1,200 MW Toktogul plant run to produce that much energy?',
  'E = 2,0·10¹² Дж, P = 1,2·10⁹ Вт', 'E = 2.0·10¹² J, P = 1.2·10⁹ W', 't = E / P = 2,0·10¹² / 1,2·10⁹ ≈ 1670 с ≈ 28 мин.', 't = E / P = 2.0·10¹² / 1.2·10⁹ ≈ 1,670 s ≈ 28 min.', 'около 28 минут.', 'about 28 minutes.'),
]

quiz = [
 qz('Что такое эпицентр?', 'Точка на поверхности над очагом', 'Точка очага под землёй', 'Самая высокая гора поблизости', 'Очаг (гипоцентр) под землёй, эпицентр — над ним.',
    'What is the epicentre?', 'The point on the surface above the source', 'The point of the source underground', 'The highest nearby mountain', 'The focus (hypocentre) is underground, the epicentre above it.'),
 qz('Какая волна приходит первой?', 'P-волна', 'S-волна', 'Поверхностная волна', 'P-волны быстрее всех.',
    'Which wave arrives first?', 'The P-wave', 'The S-wave', 'The surface wave', 'P-waves are the fastest.'),
 qz('Какие волны не проходят через жидкость?', 'S-волны', 'P-волны', 'Все проходят', 'В жидкости нет упругости сдвига, поэтому поперечные волны не идут.',
    'Which waves do not pass through a liquid?', 'S-waves', 'P-waves', 'All pass', 'A liquid has no shear elasticity so transverse waves do not travel.'),
 qz('Как определяют расстояние до эпицентра по одной станции?', 'По разнице прихода P и S волн', 'По цвету неба', 'По силе ветра', 'Чем дальше очаг, тем больше S отстаёт от P.',
    'How is the distance to the epicentre found from one station?', 'From the difference between the P and S arrivals', 'From the colour of the sky', 'From the strength of the wind', 'The farther the source, the more S lags behind P.'),
 qz('Сколько станций нужно, чтобы найти сам эпицентр (а не только расстояние)?', 'Не менее трёх', 'Одной достаточно', 'Тысяча', 'Три окружности пересекаются в одной точке.',
    'How many stations are needed to find the epicentre itself (not only the distance)?', 'At least three', 'One is enough', 'A thousand', 'Three circles intersect at one point.'),
 qz('Во сколько раз примерно растёт энергия при росте магнитуды на 1?', 'В 32 раза', 'В 2 раза', 'В 10 000 раз', '10^1,5 ≈ 32.',
    'By roughly what factor does energy grow when the magnitude rises by 1?', '32 times', '2 times', '10,000 times', '10^1.5 ≈ 32.'),
 qz('Какое землетрясение в Кыргызстане произошло 19 августа 1992 года?', 'Суусамырское, магнитуда 7,3', 'Токтогульское, магнитуда 2', 'Иссык-Кульское, магнитуда 9', 'Суусамырское землетрясение 1992 года: M 7,3, 75 погибших.',
    'Which earthquake in Kyrgyzstan occurred on 19 August 1992?', 'Suusamyr, magnitude 7.3', 'Toktogul, magnitude 2', 'Issyk-Kul, magnitude 9', 'The 1992 Suusamyr earthquake: M 7.3, 75 dead.'),
 qz('Что сильнее влияет на разрушения, кроме магнитуды?', 'Глубина очага, грунт и качество зданий', 'Время суток', 'Цвет зданий', 'Разрушения зависят не только от энергии, но и от условий на месте.',
    'Besides magnitude what affects the damage most?', 'The depth of the source, the ground and the quality of buildings', 'The time of day', 'The colour of buildings', 'Damage depends not only on energy but on local conditions.'),
]

js = r'''
const T={ru:{
 smLabel:"Сейсмограмма: приход P- и S-волн на станции",epLabel:"Станция и окружность возможных положений эпицентра",mgLabel:"Шкала магнитуды и энергия землетрясения",
 smFb:"Чем дальше очаг, тем больше разрыв между приходом P- и S-волн.",epFb:"Одна станция даёт только расстояние; эпицентр лежит на окружности.",mgFb:"Каждая единица магнитуды — энергия в 32 раза больше."},
 en:{
 smLabel:"A seismogram: arrival of the P- and S-waves at a station",epLabel:"A station and the circle of possible epicentre positions",mgLabel:"A magnitude scale and the energy of an earthquake",
 smFb:"The farther the source, the greater the gap between the P and S arrivals.",epFb:"One station gives only the distance; the epicentre lies on a circle.",mgFb:"Each unit of magnitude is 32 times more energy."}};
const VP=6,VS=3.5;
function drawSm(){const t=tt(),d=+$("md").value,tp=d/VP,ts=d/VS,X=s=>40+s/180*520;
 let g='<line x1="40" y1="125" x2="560" y2="125" stroke="#c9c2b0"/>';
 [0,30,60,90,120,150,180].forEach(s=>g+='<line x1="'+X(s)+'" y1="205" x2="'+X(s)+'" y2="212" stroke="#18181a"/>'+svgText(X(s),228,s,"#66666b","middle",10));
 const pts=[];for(let i=0;i<=520;i++){const s=i/520*180;let a=1.5*Math.sin(s*3.1);if(s>=tp)a=14*Math.sin(s*7)*Math.exp(-(s-tp)/60);if(s>=ts)a=48*Math.sin(s*5.3)*Math.exp(-(s-ts)/40);pts.push((40+i)+","+(125-a))}
 g+='<polyline fill="none" stroke="#18181a" stroke-width="1.5" points="'+pts.join(" ")+'"/>';
 g+='<line x1="'+X(tp)+'" y1="30" x2="'+X(tp)+'" y2="205" stroke="#3f5f8f" stroke-dasharray="4 3"/>'+svgText(X(tp)+4,40,"P","#3f5f8f","start",13);
 if(ts<=180)g+='<line x1="'+X(ts)+'" y1="30" x2="'+X(ts)+'" y2="205" stroke="#b6533f" stroke-dasharray="4 3"/>'+svgText(X(ts)+4,40,"S","#b6533f","start",13);
 g+=svgText(560,246,"t, "+(lang==="ru"?"с":"s"),"#66666b","end",10);
 $("smSvg").innerHTML=g;
 $("mdOut").textContent=d+UN[lang].km;
 $("mP").textContent=fmt(tp,1)+UN[lang].s;$("mS").textContent=fmt(ts,1)+UN[lang].s;$("mD").textContent=fmt(ts-tp,1)+UN[lang].s;$("smFb").textContent=t.smFb}
$("md").addEventListener("input",drawSm);
function drawEp(){const t=tt(),dt=+$("ed").value,d=dt*VP*VS/(VP-VS),R=Math.min(110,d/600*110*3.2);
 let g='<circle cx="300" cy="125" r="'+R+'" fill="none" stroke="#b6533f" stroke-width="2.5" stroke-dasharray="6 4"/><polygon points="300,112 312,134 288,134" fill="#18181a"/>'+svgText(300,150,"▲","#18181a","middle",1);
 g+=svgText(300,175,(lang==="ru"?"станция":"station"),"#18181a","middle",12)+svgText(300,20,"d = "+fmt(d,0)+UN[lang].km,"#b6533f","middle",15);
 $("epSvg").innerHTML=g;
 $("edOut").textContent=dt+UN[lang].s;$("eR").textContent=fmt(d,0)+UN[lang].km;$("eQ").textContent=fmt(8*dt,0)+UN[lang].km;$("epFb").textContent=t.epFb}
$("ed").addEventListener("input",drawEp);
function drawMg(){const t=tt(),M=+$("mm").value,E=Math.pow(10,1.5*M+4.8),R=E/Math.pow(10,1.5*5+4.8),tn=E/4.184e9;
 const X=m=>40+(m-3)/5*520;let g='<rect x="40" y="100" width="520" height="24" fill="#e3e1da"/><rect x="40" y="100" width="'+(X(M)-40)+'" height="24" fill="#b6533f"/>';
 for(let m=3;m<=8;m++)g+='<line x1="'+X(m)+'" y1="95" x2="'+X(m)+'" y2="130" stroke="#18181a"/>'+svgText(X(m),148,m,"#66666b","middle",11);
 g+='<line x1="'+X(7.3)+'" y1="80" x2="'+X(7.3)+'" y2="100" stroke="#2f6f5d" stroke-width="2"/>'+svgText(X(7.3),72,"1992","#2f6f5d","middle",11);
 g+=svgText(300,200,"M = "+fmt(M,1),"#18181a","middle",22);
 $("mgSvg").innerHTML=g;
 $("mmOut").textContent=fmt(M,1);
 const ex=Math.floor(Math.log10(E)),mant=E/Math.pow(10,ex);$("mE").textContent=fmt(mant,1)+"·10^"+ex+UN[lang].J;
 $("mR").textContent=R>=10?num(Math.round(R))+"×":fmt(R,2)+"×";
 $("mT").textContent=tn>=1e6?fmt(tn/1e6,1)+(lang==="ru"?" млн т":" Mt"):tn>=1000?num(Math.round(tn/1000))+(lang==="ru"?" тыс. т":" kt"):fmt(tn,1)+(lang==="ru"?" т":" t");$("mgFb").textContent=t.mgFb}
$("mm").addEventListener("input",drawMg);
const LAB={ru:{smSvg:T.ru.smLabel,epSvg:T.ru.epLabel,mgSvg:T.ru.mgLabel},en:{smSvg:T.en.smLabel,epSvg:T.en.epLabel,mgSvg:T.en.mgLabel}};
function drawAll(){drawSm();drawEp();drawMg()}
'''

c = dict(n='28', slug='28-earthquakes.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Землетрясения и сейсмические волны', 'Earthquakes and seismic waves'),
 desc='Глава 28 Атласа физики: P- и S-волны, как найти эпицентр, магнитуда и энергия; землетрясения Кыргызстана.',
 lead=('Тянь-Шань растёт, а земля временами дрожит. Сейсмические волны, поиск эпицентра, магнитуда и энергия.',
       'The Tien Shan is rising and the ground trembles at times. Seismic waves, locating the epicentre, magnitude and energy.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('waves', 'Сейсмические волны', 'Seismic waves'), ('locate', 'Эпицентр', 'Epicentre'), ('mag', 'Магнитуда', 'Magnitude'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Ночью в доме дрожит стол. Сначала короткий резкий удар снизу — стёкла звякнули. Через несколько секунд начинается сильная качка, от которой падает посуда. Те, кто знает об этом, говорят: «Первый удар — предупреждение, и у тебя есть несколько секунд».</p><p>Откуда берётся такая задержка между ударом и качкой?</p>',
         '<p>At night a table shakes in the house. First a short sharp jolt from below — the windows rattle. A few seconds later strong shaking begins and dishes fall. Those who know say: “The first jolt is a warning and you have a few seconds.”</p><p>Where does this delay between the jolt and the shaking come from?</p>'),
 hint=stdhint('Сейсмограмма', 'A seismogram'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: две волны с разной скоростью', 'The answer: two waves of different speeds'),
 answer=('<p>Из очага одновременно выходят быстрая продольная P-волна и более медленная поперечная S-волна. P-волна приходит первой и ощущается как короткий удар, а S-волна — позже и даёт сильную качку. Задержка растёт с расстоянием: примерно 1 секунда на каждые 8 км (модели 1 и 2). На расстоянии 80 км это около 10 секунд.</p><p>Так работают системы раннего оповещения: датчик ловит P-волну и сообщает об S-волне, которая ещё в пути. Если вы почувствовали удар, не ждите: сразу присядьте под прочный стол или к внутренней стене, прикройте голову и держитесь подальше от окон. Подробные правила смотрите у МЧС Кыргызстана.</p>',
         '<p>A fast longitudinal P-wave and a slower transverse S-wave leave the source at the same time. The P-wave arrives first and is felt as a short jolt while the S-wave comes later and gives strong shaking. The delay grows with distance: about 1 second for each 8 km (models 1 and 2). At 80 km that is about 10 seconds.</p><p>That is how early-warning systems work: a sensor catches the P-wave and warns of the S-wave still on its way. If you feel the jolt do not wait: crouch at once under a sturdy table or by an inside wall, cover your head and keep away from windows. See the detailed rules of the Kyrgyz Ministry of Emergency Situations.</p>'),
 sources=[
  ('P- и S-волны, скорости в земной коре, S-волны не проходят через жидкое ядро —', 'P- and S-waves, speeds in the crust, S-waves do not pass through the liquid core —', LINK('https://opentextbc.ca/geology/chapter/9-1-understanding-earth-through-seismology/', 'Physical Geology (BCcampus): Understanding Earth through Seismology') + ', ' + LINK('https://en.wikipedia.org/wiki/Seismic_wave', 'Wikipedia: Seismic wave')),
  ('Магнитуда и энергия землетрясения —', 'Magnitude and the energy of an earthquake —', LINK('https://en.wikipedia.org/wiki/Seismic_magnitude_scales', 'Wikipedia: Seismic magnitude scales')),
  ('Суусамырское землетрясение 19.08.1992: Ms 7,3, 75 погибших —', 'The Suusamyr earthquake of 19.08.1992: Ms 7.3, 75 dead —', LINK('https://en.wikipedia.org/wiki/1992_Suusamyr_earthquake', 'Wikipedia: 1992 Suusamyr earthquake') + ', ' + LINK('https://www.mdpi.com/2076-3263/9/6/271/htm', 'Grützner et al., Geosciences 2019')),
  ('Кеминское землетрясение 1911 года, оценки магнитуды 7,7–8,0 —', 'The 1911 Kemin earthquake, magnitude estimates 7.7–8.0 —', LINK('https://en.wikipedia.org/wiki/List_of_earthquakes_in_Kyrgyzstan', 'Wikipedia: List of earthquakes in Kyrgyzstan') + ', ' + LINK('https://earthquake.usgs.gov/earthquakes/eventpage/iscgem16958130', 'USGS: The 1911 Kemin Earthquake')),
  ('Рост Тянь-Шаня из-за столкновения Индии с Азией —', 'The rise of the Tien Shan from the collision of India with Asia —', LINK('https://en.wikipedia.org/wiki/Tian_Shan', 'Wikipedia: Tian Shan'))],
 note=stdnote('Скорости P- и S-волн (6 и 3,5 км/с) — типичные условные значения для земной коры; в разных породах они разные.', 'The P- and S-wave speeds (6 and 3.5 km/s) are typical assumed values for the crust; they differ in different rocks.'),
 prev=('27-sound.html', 'Глава 27 · Звук', 'Chapter 27 · Sound'),
 next=('29-light-and-shadows.html', 'Глава 29 · Свет и тени', 'Chapter 29 · Light and shadows'),
 js=js)
build(c)
