# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ПЛАНЕТЫ И ТРЕТИЙ ЗАКОН КЕПЛЕРА', 'THE PLANETS AND KEPLER’S THIRD LAW', 'plSvg', '0 0 600 250',
  slider('pt', 'Прошло времени', 'Time elapsed', 0, 30, 0.1, 0) + select('pp', 'Планета для расчёта', 'Planet for the calculation'),
  stats([('pA', 'Большая полуось a', 'Semi-major axis a'), ('pT', 'Период T = a^(3/2)', 'Period T = a^(3/2)'), ('pV', 'Скорость по орбите', 'Orbital speed')]),
  'plFb', 'Схема условная: орбиты считаются круговыми, радиусы нарисованы сжато (пропорционально √a); a — в астрономических единицах (1 а.е. — расстояние Земля–Солнце).',
  'A schematic drawing: the orbits are taken as circular, the radii compressed (proportional to √a); a is in astronomical units (1 AU is the Earth–Sun distance).')
s1 = section('kepler3', 'Год на разных планетах', 'A year on different planets',
 bd('<p>Планеты обращаются вокруг Солнца под действием тяготения (глава 36). Чем дальше планета, тем слабее притяжение Солнца и длиннее путь, поэтому тем дольше её год. Третий закон Кеплера: если расстояние <em>a</em> измерять в астрономических единицах (1 а.е. ≈ 150 млн км), а период <em>T</em> — в земных годах, то</p>',
    '<p>The planets revolve around the Sun under gravity (chapter 36). The farther the planet the weaker the Sun’s pull and the longer the path so the longer its year. Kepler’s third law: if the distance <em>a</em> is measured in astronomical units (1 AU ≈ 150 million km) and the period <em>T</em> in Earth years then</p>')
 + formula('T² = a³', 'Марс: a = 1,52 а.е. → T = 1,88 года; Юпитер: 5,2 а.е. → 11,9 года', 'Mars: a = 1.52 AU → T = 1.88 years; Jupiter: 5.2 AU → 11.9 years')
 + bd('<p>Скорость по орбите уменьшается с расстоянием: Земля летит со скоростью около 30 км/с, Юпитер — 13 км/с.</p>',
      '<p>The orbital speed decreases with distance: the Earth moves at about 30 km/s, Jupiter at 13 km/s.</p>'),
 lab1)

lab2 = model(2, 'СВЕТ И РАССТОЯНИЯ', 'LIGHT AND DISTANCES', 'ltSvg', '0 0 600 250',
  select('lb', 'Планета', 'Planet') + slider('lv', 'Скорость зонда', 'Probe speed', 5, 70, 1, 17),
  stats([('lD', 'Расстояние от Солнца', 'Distance from the Sun'), ('lT', 'Свет идёт от Солнца', 'Light travels from the Sun'), ('lR', 'Сигнал туда и обратно', 'A signal there and back'), ('lP', 'Зонд долетит от Земли за (грубо, a − 1 а.е.)', 'A probe will arrive from Earth in (roughly, a − 1 AU)')]),
  'ltFb', 'Схема условная: 1 а.е. = 149,6 млн км; скорость света 299 792 км/с; для зонда принят прямой полёт с постоянной скоростью.',
  'A schematic drawing: 1 AU = 149.6 million km; the speed of light 299,792 km/s; the probe is assumed to fly straight at a constant speed.')
s2 = section('distances', 'Расстояния в Солнечной системе', 'Distances in the Solar System',
 bd('<p>Свет — самый быстрый «гонец»: за одну секунду он проходит 299 792 км. От Солнца до Земли он идёт около 8 минут 19 секунд — мы видим Солнце таким, каким оно было 8 минут назад. До Юпитера свет идёт около 43 минут, до Нептуна — около 4 часов. Поэтому команды на далёкие зонды идут часами, и они должны управлять собой сами.</p>',
    '<p>Light is the fastest “messenger”: in one second it covers 299,792 km. From the Sun to the Earth it takes about 8 minutes 19 seconds — we see the Sun as it was 8 minutes ago. To Jupiter light takes about 43 minutes, to Neptune about 4 hours. So commands to distant probes take hours and the probes must steer themselves.</p>')
 + formula('t = d / c,   1 а.е. ≈ 499 световых секунд', 'a·499 с — время света от Солнца до планеты', 'a·499 s is the light time from the Sun to the planet'),
 lab2)

lab3 = model(3, 'КАКАЯ ПЛАНЕТА ДЕРЖИТ ВОЗДУХ', 'WHICH PLANET HOLDS AN ATMOSPHERE', 'esSvg', '0 0 600 250',
  select('eb', 'Небесное тело', 'Celestial body') + select('eg', 'Газ', 'Gas') + slider('et', 'Температура', 'Temperature', 100, 1000, 10, 288),
  stats([('eG', 'g на поверхности', 'g at the surface'), ('eV', 'Вторая космическая скорость √(2GM/R)', 'Escape speed √(2GM/R)'), ('eM', 'Средняя скорость молекул газа', 'Typical speed of gas molecules'), ('eS', 'Удерживает газ?', 'Does it hold the gas?')]),
  'esFb', 'Схема условная: правило «газ удерживается миллиарды лет, если v_II больше примерно 6·v молекул» — грубое; v = √(3kT/m).',
  'A schematic drawing: the rule “a gas is held for billions of years if the escape speed exceeds about 6× the molecule speed” is rough; v = √(3kT/m).')
s3 = section('escape', 'Вторая космическая скорость и атмосфера', 'Escape speed and the atmosphere',
 bd('<p>Чтобы навсегда покинуть планету, нужна <strong>вторая космическая скорость</strong> <em>v = √(2GM/R)</em> — в √2 раз больше первой. У Земли она 11,2 км/с, у Луны 2,4 км/с. Молекулы газа тоже движутся быстро: чем легче газ и выше температура, тем выше скорость. Лёгкие газы (водород, гелий) уходят с Земли, а тяжёлые (азот, кислород) остаются. У Луны слабая тяжесть, и атмосферы у неё практически нет.</p>',
    '<p>To leave a planet for good a <strong>second cosmic (escape) speed</strong> <em>v = √(2GM/R)</em> is needed — √2 times the first. For the Earth it is 11.2 km/s, for the Moon 2.4 km/s. Gas molecules also move fast: the lighter the gas and the higher the temperature the higher the speed. Light gases (hydrogen, helium) escape from the Earth while heavy ones (nitrogen, oxygen) stay. The Moon’s gravity is weak and it has practically no atmosphere.</p>')
 + formula('v_II = √(2GM / R),   v ≈ √(3kT / m)', 'тело держит газ, если v_II заметно больше скорости молекул', 'a body holds a gas if the escape speed is well above the molecule speed'),
 lab3)

tasks = [
 task(1, 'Год на Марсе', 'A year on Mars', 'Большая полуось орбиты Марса 1,524 а.е. Найдите период обращения.', 'The semi-major axis of Mars’s orbit is 1.524 AU. Find the orbital period.',
  'a = 1,524 а.е.', 'a = 1.524 AU', 'T = a^(3/2) = 1,524 · √1,524 = 1,524 · 1,2345 ≈ 1,88 года.', 'T = a^(3/2) = 1.524 · √1.524 = 1.524 · 1.2345 ≈ 1.88 years.', '≈ 1,88 земных года (687 суток).', '≈ 1.88 Earth years (687 days).', True),
 task(2, 'Расстояние до Юпитера', 'The distance to Jupiter', 'Период Юпитера 11,86 года. Найдите большую полуось его орбиты.', 'Jupiter’s period is 11.86 years. Find the semi-major axis of its orbit.',
  'T = 11,86 года', 'T = 11.86 years', 'a³ = T² = 140,7, a = ∛140,7 ≈ 5,20 а.е.', 'a³ = T² = 140.7, a = ∛140.7 ≈ 5.20 AU.', '≈ 5,2 а.е. ≈ 780 млн км.', '≈ 5.2 AU ≈ 780 million km.'),
 task(3, 'Скорость Земли', 'The Earth’s speed', 'Найдите скорость Земли по орбите (r = 1,496·10¹¹ м, T = 3,156·10⁷ с).', 'Find the Earth’s orbital speed (r = 1.496·10¹¹ m, T = 3.156·10⁷ s).',
  'r, T', 'r, T', 'v = 2πr / T = 6,283 · 1,496·10¹¹ / 3,156·10⁷ ≈ 2,98·10⁴ м/с.', 'v = 2πr / T = 6.283 · 1.496·10¹¹ / 3.156·10⁷ ≈ 2.98·10⁴ m/s.', '≈ 29,8 км/с.', '≈ 29.8 km/s.'),
 task(4, 'Свет до Нептуна', 'Light to Neptune', 'Нептун — на расстоянии 30,07 а.е. Сколько идёт свет от Солнца до Нептуна? (1 а.е. = 499 световых секунд.)', 'Neptune is 30.07 AU away. How long does light take from the Sun to Neptune? (1 AU = 499 light-seconds.)',
  'a = 30,07 а.е.', 'a = 30.07 AU', 't = 30,07 · 499 ≈ 15 000 с ≈ 4,17 ч.', 't = 30.07 · 499 ≈ 15,000 s ≈ 4.17 h.', '≈ 4,2 часа.', '≈ 4.2 hours.'),
 task(5, 'Вторая космическая Луны', 'The Moon’s escape speed', 'Для Луны GM = 4,903·10¹² м³/с², R = 1,737·10⁶ м. Найдите вторую космическую скорость.', 'For the Moon GM = 4.903·10¹² m³/s², R = 1.737·10⁶ m. Find the escape speed.',
  'GM, R', 'GM, R', 'v = √(2GM/R) = √(2 · 4,903·10¹² / 1,737·10⁶) = √(5,645·10⁶) ≈ 2376 м/с.', 'v = √(2GM/R) = √(2 · 4.903·10¹² / 1.737·10⁶) = √(5.645·10⁶) ≈ 2,376 m/s.', '≈ 2,4 км/с.', '≈ 2.4 km/s.'),
 task(6, 'Полёт к Нептуну', 'A flight to Neptune', 'За какое время зонд со скоростью 17 км/с пролетит расстояние 29 а.е. (≈ 4,34·10⁹ км) от Земли до орбиты Нептуна?', 'How long will a probe at 17 km/s take to cover 29 AU (≈ 4.34·10⁹ km) from the Earth to Neptune’s orbit?',
  'v = 17 км/с', 'v = 17 km/s', 't = 4,34·10⁹ / 17 = 2,55·10⁸ с.<br>В годах: 2,55·10⁸ / 3,156·10⁷ ≈ 8,1 года.', 't = 4.34·10⁹ / 17 = 2.55·10⁸ s.<br>In years: 2.55·10⁸ / 3.156·10⁷ ≈ 8.1 years.', '≈ 8 лет.', '≈ 8 years.'),
]

quiz = [
 qz('Что утверждает третий закон Кеплера (T в годах, a в а.е.)?', 'T² = a³', 'T = a', 'T = a²', 'Чем дальше планета, тем дольше год.',
    'What does Kepler’s third law state (T in years, a in AU)?', 'T² = a³', 'T = a', 'T = a²', 'The farther the planet the longer the year.'),
 qz('Что такое астрономическая единица?', 'Среднее расстояние Земля–Солнце', 'Диаметр Земли', 'Скорость света', 'Около 150 млн км.',
    'What is an astronomical unit?', 'The mean Earth–Sun distance', 'The diameter of the Earth', 'The speed of light', 'About 150 million km.'),
 qz('Как меняется скорость планеты по орбите с ростом расстояния от Солнца?', 'Уменьшается', 'Растёт', 'Не меняется', 'Земля ≈ 30 км/с, Юпитер ≈ 13 км/с.',
    'How does a planet’s orbital speed change with distance from the Sun?', 'It decreases', 'It grows', 'It does not change', 'Earth ≈ 30 km/s, Jupiter ≈ 13 km/s.'),
 qz('За какое время свет идёт от Солнца до Земли?', 'Около 8 минут', 'Около 1 секунды', 'Около суток', '1 а.е. ≈ 499 световых секунд.',
    'How long does light take from the Sun to the Earth?', 'About 8 minutes', 'About 1 second', 'About a day', '1 AU ≈ 499 light-seconds.'),
 qz('Почему команды на далёкий зонд идут часами?', 'Расстояния огромны, а скорость света конечна', 'Зонд выключен', 'Нет связи в космосе', 'Радиоволны идут со скоростью света.',
    'Why do commands to a distant probe take hours?', 'The distances are huge and the speed of light is finite', 'The probe is switched off', 'There is no communication in space', 'Radio waves travel at the speed of light.'),
 qz('Во сколько раз вторая космическая скорость больше первой?', 'В √2 раз', 'В 2 раза', 'Они равны', 'v_II = √2 · v_I.',
    'How many times is the escape speed greater than the first cosmic speed?', '√2 times', '2 times', 'They are equal', 'v_II = √2 · v_I.'),
 qz('Почему у Луны почти нет атмосферы?', 'Слабая тяжесть не удерживает газ', 'Там слишком холодно', 'Атмосферу сдувает Земля', 'Вторая космическая скорость всего 2,4 км/с.',
    'Why does the Moon have almost no atmosphere?', 'Weak gravity does not hold the gas', 'It is too cold', 'The Earth blows it away', 'The escape speed is only 2.4 km/s.'),
 qz('Какие газы легче уходят из атмосферы планеты?', 'Лёгкие (водород, гелий)', 'Тяжёлые (CO₂)', 'Все одинаково', 'При той же температуре лёгкие молекулы быстрее.',
    'Which gases escape from a planet’s atmosphere more easily?', 'Light ones (hydrogen, helium)', 'Heavy ones (CO₂)', 'All equally', 'At the same temperature light molecules are faster.'),
]

js = JSL + r'''
const T={ru:{
 plLabel:"Орбиты планет (вид сверху, масштаб сжат)",ltLabel:"Расстояния до планет и время света",esLabel:"Вторая космическая скорость и скорость молекул",
 pl:["Меркурий","Венера","Земля","Марс","Юпитер","Сатурн"],plN:["Меркурий","Венера","Земля","Марс","Юпитер","Сатурн","Уран","Нептун"],
 bd:["Меркурий","Венера","Земля","Луна","Марс","Юпитер"],gas:["Водород H₂","Гелий He","Азот N₂","Углекислый газ CO₂"],yes:"да, надолго",no:"нет, уходит",
 plFb:"Дальше от Солнца — медленнее и дольше год.",ltFb:"Свет до Нептуна идёт около четырёх часов.",esFb:"Тяжёлая планета держит и лёгкие газы; лёгкая — только тяжёлые."},
 en:{
 plLabel:"The planets’ orbits (seen from above, the scale compressed)",ltLabel:"Distances to the planets and light time",esLabel:"Escape speed and molecule speed",
 pl:["Mercury","Venus","Earth","Mars","Jupiter","Saturn"],plN:["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"],
 bd:["Mercury","Venus","Earth","Moon","Mars","Jupiter"],gas:["Hydrogen H₂","Helium He","Nitrogen N₂","Carbon dioxide CO₂"],yes:"yes, for long",no:"no, it escapes",
 plFb:"Farther from the Sun — slower and a longer year.",ltFb:"Light takes about four hours to reach Neptune.",esFb:"A heavy planet holds even light gases; a light one only heavy ones."}};
const PA=[0.387,0.723,1,1.524,5.203,9.537,19.19,30.07];
const BM=[[3.301e23,2439.7e3],[4.867e24,6051.8e3],[5.972e24,6371e3],[7.342e22,1737.4e3],[6.417e23,3389.5e3],[1.898e27,69911e3]];
const GMOL=[2,4,28,44];
function drawPl(){const t=tt(),tm=+$("pt").value,k=+$("pp").value;
 let g='<circle cx="300" cy="125" r="9" fill="#e8c14a" stroke="#18181a"/>';
 for(let i=0;i<6;i++){const a=PA[i],r=37.2*Math.sqrt(a),T0=Math.pow(a,1.5),ang=2*Math.PI*tm/T0;g+='<circle cx="300" cy="125" r="'+r+'" fill="none" stroke="#c9c2b0"/><circle cx="'+(300+r*Math.cos(ang))+'" cy="'+(125-r*Math.sin(ang))+'" r="'+(i===k?6:4)+'" fill="'+(i===k?"#b6533f":"#3f5f8f")+'"/>'}
 $("plSvg").innerHTML=g;$("ptOut").textContent=fmt(tm,1)+" "+U("лет","yr");
 const a=PA[k],T0=Math.pow(a,1.5),v=2*Math.PI*a*149.6e6/(T0*3.156e7);
 $("pA").textContent=fmt(a,3)+" "+U("а.е.","AU");$("pT").textContent=fmt(T0,2)+" "+U("лет","yr");$("pV").textContent=fmt(v,1)+" "+U("км/с","km/s");$("plFb").textContent=t.plFb}
["pt","pp"].forEach(id=>$(id).addEventListener("input",drawPl));
function drawLt(){const t=tt(),k=+$("lb").value,v=+$("lv").value,a=PA[k],ts=a*499.0,d=a*149.6e6,rt=2*ts,tp=Math.max(0,a-1)*149.6e6/v/3.156e7;
 const fmtT=s=>s<120?fmt(s,0)+" "+U("с","s"):s<7200?fmt(s/60,1)+" "+U("мин","min"):fmt(s/3600,2)+" "+U("ч","h");
 let g='<circle cx="60" cy="125" r="14" fill="#e8c14a" stroke="#18181a"/><line x1="76" y1="125" x2="'+(76+Math.min(480,Math.sqrt(a)*85))+'" y2="125" stroke="#c9c2b0" stroke-width="3"/><circle cx="'+(76+Math.min(480,Math.sqrt(a)*85))+'" cy="125" r="7" fill="#3f5f8f"/>'+svgText(300,200,U("свет: ","light: ")+fmtT(ts),"#18181a","middle",16);
 $("ltSvg").innerHTML=g;$("lvOut").textContent=v+" "+U("км/с","km/s");
 $("lD").textContent=fmt(a,2)+" "+U("а.е.","AU")+" ("+num(Math.round(d/1e6))+" "+U("млн км","M km")+")";$("lT").textContent=fmtT(ts);$("lR").textContent=fmtT(rt);$("lP").textContent=a<=1?"—":fmt(tp,1)+" "+U("лет","yr");$("ltFb").textContent=t.ltFb}
["lb","lv"].forEach(id=>$(id).addEventListener("input",drawLt));
function drawEs(){const t=tt(),k=+$("eb").value,gi=+$("eg").value,T0=+$("et").value,GM=6.674e-11*BM[k][0],R=BM[k][1],g=GM/(R*R),ve=Math.sqrt(2*GM/R),m=GMOL[gi]*1.66054e-27,vm=Math.sqrt(3*1.380649e-23*T0/m),hold=ve>6*vm;
 const mx=Math.max(ve,vm*6,1)*1.1;let gg='<rect x="80" y="'+(210-ve/mx*170)+'" width="110" height="'+(ve/mx*170)+'" fill="#3f5f8f" stroke="#18181a"/><rect x="330" y="'+(210-6*vm/mx*170)+'" width="110" height="'+(6*vm/mx*170)+'" fill="'+(hold?"#2f6f5d":"#b6533f")+'" stroke="#18181a"/>'+svgText(135,228,U("v₂ планеты","escape speed"),"#18181a","middle",11)+svgText(385,228,U("6 × v молекул","6 × molecule speed"),"#18181a","middle",11);
 $("esSvg").innerHTML=gg;$("etOut").textContent=T0+" "+U("К","K");
 $("eG").textContent=fmt(g,2)+" "+U("м/с²","m/s²");$("eV").textContent=fmt(ve/1000,2)+" "+U("км/с","km/s");$("eM").textContent=fmt(vm/1000,2)+" "+U("км/с","km/s");$("eS").textContent=hold?t.yes:t.no;$("esFb").textContent=t.esFb}
["eb","eg","et"].forEach(id=>$(id).addEventListener("input",drawEs));
const LAB={ru:{plSvg:T.ru.plLabel,ltSvg:T.ru.ltLabel,esSvg:T.ru.esLabel},en:{plSvg:T.en.plLabel,ltSvg:T.en.ltLabel,esSvg:T.en.esLabel}};
function drawAll(){fillSel("pp",T[lang].pl,2);fillSel("lb",T[lang].plN,2);fillSel("eb",T[lang].bd,2);fillSel("eg",T[lang].gas,2);drawPl();drawLt();drawEs()}
'''

c = dict(n='42', slug='42-solar-system.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Солнечная система', 'The Solar System'),
 desc='Глава 42 Атласа физики: третий закон Кеплера, периоды и скорости планет, время света, вторая космическая скорость и атмосферы планет.',
 lead=('Почему год на Юпитере в 12 раз длиннее нашего, сколько света идёт до Нептуна и какая планета удерживает воздух.',
       'Why a year on Jupiter is 12 times longer than ours, how long light takes to reach Neptune and which planet holds air.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('kepler3', 'Законы Кеплера', 'Kepler’s laws'), ('distances', 'Расстояния', 'Distances'), ('escape', 'Атмосфера', 'Atmosphere'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Год Меркурия — 88 земных суток, год Земли — 365, а год Юпитера — почти 12 земных лет, Сатурна — почти 30. Все планеты притягиваются одним и тем же Солнцем, но обращаются с такой разной скоростью. А у Луны, в отличие от Земли, почти нет атмосферы</p><p>Что определяет, сколько длится год, и почему одни небесные тела держат воздух, а другие нет?</p>',
         '<p>Mercury’s year is 88 Earth days, the Earth’s is 365 and Jupiter’s is almost 12 Earth years, Saturn’s almost 30. All the planets are attracted by the same Sun yet revolve at such different speeds. And the Moon, unlike the Earth, has almost no atmosphere.</p><p>What determines the length of a year and why do some celestial bodies hold air while others do not?</p>'),
 hint=stdhint('Планеты', 'The planets'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: тяготение и расстояние', 'The answer: gravity and distance'),
 answer=('<p>Сила тяготения Солнца уменьшается как 1/r², поэтому дальняя планета и движется медленнее, и проходит более длинный путь: период растёт быстрее расстояния, как <em>T² = a³</em>. Для Юпитера a = 5,2 а.е., поэтому T ≈ 11,9 года.</p><p>Воздух удерживает тяготение: чтобы молекула навсегда покинула тело, её скорость должна превысить вторую космическую. У Земли она 11,2 км/с, у Луны 2,4 км/с. По грубому правилу газ удерживается миллиарды лет, если вторая космическая больше шести скоростей молекул. Для азота у Земли это выполнено с большим запасом (11,2 против 6·0,5 = 3 км/с), а у Луны — нет (2,4 против 2,8 км/с при 250 К); у лёгкого водорода условие не выполнено даже на Земле. На Луне к этому добавляются дневной нагрев и солнечный ветер.</p>',
         '<p>The Sun’s gravity falls as 1/r² so a distant planet both moves slower and travels a longer path: the period grows faster than the distance, as <em>T² = a³</em>. For Jupiter a = 5.2 AU so T ≈ 11.9 years.</p><p>Gravity holds air: for a molecule to leave a body for good its speed must exceed the escape speed. For the Earth it is 11.2 km/s, for the Moon 2.4 km/s. By a rough rule a gas is held for billions of years if the escape speed exceeds six molecule speeds. For nitrogen on the Earth this is met with a wide margin (11.2 against 6·0.5 = 3 km/s) but on the Moon it is not (2.4 against 2.8 km/s at 250 K); for light hydrogen it is not met even on the Earth. On the Moon daytime heating and the solar wind add to this.</p>'),
 sources=[
  ('Третий закон Кеплера, орбиты, космические скорости —', 'Kepler’s third law, orbits, cosmic speeds —', LINK('https://openstax.org/books/university-physics-volume-1/pages/13-5-keplers-laws-of-planetary-motion', 'OpenStax University Physics, Vol. 1, § 13.5') + ', ' + LINK('https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion', 'Wikipedia: Kepler’s laws')),
  ('Массы, радиусы, орбиты планет, астрономическая единица —', 'Masses, radii, orbits of the planets, the astronomical unit —', LINK('https://nssdc.gsfc.nasa.gov/planetary/factsheet/', 'NASA Planetary Fact Sheets') + ', ' + LINK('https://en.wikipedia.org/wiki/Astronomical_unit', 'Wikipedia: Astronomical unit')),
  ('Удержание атмосферы (скорость убегания и скорость молекул) —', 'Atmospheric retention (escape speed and molecule speed) —', LINK('https://en.wikipedia.org/wiki/Atmospheric_escape', 'Wikipedia: Atmospheric escape'))],
 note=stdnote('Орбиты приняты круговыми; правило удержания газа (v_II более 6 скоростей молекул) — приближённое; температура атмосферы задаётся ползунком условно.', 'The orbits are taken as circular; the rule of gas retention (escape speed above 6 molecule speeds) is approximate; the atmosphere temperature is set by the slider as an assumption.'),
 prev=('41-nuclear-energy.html', 'Глава 41 · Ядерная энергия', 'Chapter 41 · Nuclear energy'),
 next=('43-stars-telescopes.html', 'Глава 43 · Звёзды и обсерватории', 'Chapter 43 · Stars and observatories'),
 js=js)
build(c)
