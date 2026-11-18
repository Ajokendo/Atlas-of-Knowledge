# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'СИЛА МЕЖДУ ЗАРЯДАМИ', 'THE FORCE BETWEEN CHARGES', 'coSvg', '0 0 600 230',
  slider('q1', 'Заряд 1', 'Charge 1', -10, 10, 1, 4) + slider('q2', 'Заряд 2', 'Charge 2', -10, 10, 1, -4) + slider('rr', 'Расстояние', 'Distance', 0.1, 2, 0.1, 0.5),
  stats([('cF', 'Сила взаимодействия', 'Force of interaction'), ('cK', 'Что происходит', 'What happens')]),
  'coFb', 'Схема условная: заряды в микрокулонах (мкКл), расстояние в метрах; k = 9·10⁹ Н·м²/Кл².',
  'A schematic drawing: charges in microcoulombs (µC), distance in metres; k = 9·10⁹ N·m²/C².')
s1 = section('coulomb', 'Электрический заряд и закон Кулона', 'Electric charge and Coulomb’s law',
 bd('<p>Многие тела можно <strong>наэлектризовать</strong>, потерев их друг о друга. Тогда они начинают притягивать лёгкие предметы. Причина — <strong>электрический заряд</strong>. Зарядов два вида: условно положительные и отрицательные. Одноимённые заряды отталкиваются, разноимённые притягиваются.</p><p>При трении с одного тела на другое переходят электроны, а новые заряды не возникают: суммарный заряд сохраняется. Тело, получившее лишние электроны, заряжается отрицательно, потерявшее — положительно. Заряд измеряют в <strong>кулонах</strong> (Кл). Наименьший заряд свободной частицы — элементарный заряд электрона <em>e</em> ≈ 1,6·10⁻¹⁹ Кл.</p><p>Силу взаимодействия двух маленьких заряженных тел описывает <strong>закон Кулона</strong>:</p>',
    '<p>Many bodies can be <strong>electrified</strong> by rubbing them against each other. They then begin to attract light objects. The cause is <strong>electric charge</strong>. There are two kinds: conventionally positive and negative. Like charges repel, unlike charges attract.</p><p>When bodies are rubbed, electrons pass from one to the other, and no new charge is created: the total charge is conserved. A body that gained extra electrons becomes negative, one that lost them becomes positive. Charge is measured in <strong>coulombs</strong> (C). The smallest charge of a free particle is the elementary charge of the electron <em>e</em> ≈ 1.6·10⁻¹⁹ C.</p><p>The force between two small charged bodies is described by <strong>Coulomb’s law</strong>:</p>')
 + formula('F = k · |q₁| · |q₂| / r²', 'k ≈ 9·10⁹ Н·м²/Кл²; сила обратно пропорциональна квадрату расстояния', 'k ≈ 9·10⁹ N·m²/C²; the force is inversely proportional to the square of the distance')
 + bd('<p>Заметьте: закон похож на закон всемирного тяготения, но заряды могут и отталкиваться. Если расстояние увеличить вдвое, сила станет в 4 раза меньше.</p>',
      '<p>Note that the law resembles the law of universal gravitation, but charges can also repel. If the distance doubles the force becomes 4 times smaller.</p>'),
 lab1)

lab2 = model(2, 'ПЕРЕХОД ЭЛЕКТРОНОВ ПРИ ТРЕНИИ', 'ELECTRON TRANSFER BY RUBBING', 'elSvg', '0 0 600 230',
  slider('en', 'Перешло электронов (в десятках миллиардов)', 'Electrons transferred (in tens of billions)', 1, 100, 1, 20),
  stats([('eN', 'Число электронов', 'Number of electrons'), ('eQ', 'Заряд расчёской', 'Charge on the comb'), ('eP', 'Заряд волос', 'Charge on the hair')]),
  'elFb', 'Схема условная: десять миллиардов электронов — это 10¹⁰ штук; заряд q = N·e. Реальное число зависит от материалов и влажности.',
  'A schematic drawing: ten billion electrons is 10¹⁰ pieces; the charge is q = N·e. The real number depends on the materials and humidity.')
s2 = section('transfer', 'Заряд — это избыток или недостаток электронов', 'Charge is an excess or shortage of electrons',
 bd('<p>Заряд тела всегда равен целому числу элементарных зарядов: <em>q = N·e</em>. Чтобы получить заряд в 1 Кл, нужно около 6,2·10¹⁸ электронов — это очень много. Поэтому на опытах с расчёской речь идёт о миллиардах электронов, то есть о нанокулонах (1 нКл = 10⁻⁹ Кл).</p><p>Металлы хорошо проводят заряд (проводники), а пластик, стекло, резина — плохо (диэлектрики). Поэтому пластмассовая расчёска хранит заряд, а металлическая в руке — нет, он уходит в тело.</p>',
    '<p>A body’s charge is always a whole number of elementary charges: <em>q = N·e</em>. To get a charge of 1 C about 6.2·10¹⁸ electrons are needed — a very large number. So in experiments with a comb we are talking about billions of electrons, that is, nanocoulombs (1 nC = 10⁻⁹ C).</p><p>Metals conduct charge well (conductors), while plastic, glass and rubber conduct poorly (insulators). That is why a plastic comb keeps its charge, while a metal one in the hand does not: the charge goes into the body.</p>'),
 lab2)

lab3 = model(3, 'ГРОЗА: КАК ДАЛЕКО УДАР', 'THUNDERSTORM: HOW FAR THE STRIKE IS', 'thSvg', '0 0 600 230',
  slider('tt', 'Секунд между вспышкой и громом', 'Seconds between flash and thunder', 1, 30, 1, 6),
  stats([('tD', 'Расстояние до удара', 'Distance to the strike'), ('tL', 'Время света', 'Light travel time')]),
  'thFb', 'Схема условная: скорость звука ≈ 340 м/с; свет считаем мгновенным (≈ 0,000003 с на километр).',
  'A schematic drawing: the speed of sound ≈ 340 m/s; light is treated as instantaneous (≈ 0.000003 s per kilometre).')
s3 = section('lightning', 'Молния — гигантская искра', 'Lightning — a giant spark',
 bd('<p>Молния — электрический разряд между облаком и землёй или между облаками. В грозовом облаке заряды разделяются, и между ним и землёй возникает огромное напряжение — порядка сотен миллионов вольт. Типичный ток молнии около 30 000 А, а канал разряда нагревается примерно до 30 000 °C. Воздух при этом мгновенно расширяется — мы слышим гром.</p><p>Свет доходит почти мгновенно, а звук идёт со скоростью около 340 м/с. Поэтому расстояние до удара можно оценить: примерно по 340 м на каждую секунду между вспышкой и громом, или 3 секунды на километр.</p>',
    '<p>Lightning is an electric discharge between a cloud and the ground or between clouds. In a thundercloud charges separate, and an enormous voltage — of the order of hundreds of millions of volts — arises between it and the ground. A typical lightning current is about 30,000 A, and the discharge channel heats to about 30,000 °C. The air expands instantly — we hear thunder.</p><p>Light arrives almost instantly, while sound travels at about 340 m/s. So the distance to the strike can be estimated: roughly 340 m for each second between flash and thunder, or 3 seconds per kilometre.</p>'),
 lab3)

tasks = [
 task(1, 'Сила Кулона', 'Coulomb force', 'Два заряда, 2 мкКл и 3 мкКл, находятся на расстоянии 0,3 м. С какой силой они действуют друг на друга? k = 9·10⁹ Н·м²/Кл².', 'Two charges, 2 µC and 3 µC, are 0.3 m apart. What force acts between them? k = 9·10⁹ N·m²/C².',
  'q₁ = 2·10⁻⁶ Кл, q₂ = 3·10⁻⁶ Кл, r = 0,3 м', 'q₁ = 2·10⁻⁶ C, q₂ = 3·10⁻⁶ C, r = 0.3 m', 'F = k·q₁·q₂ / r² = 9·10⁹ · 2·10⁻⁶ · 3·10⁻⁶ / 0,09 = 0,054 / 0,09 = 0,6 Н.', 'F = k·q₁·q₂ / r² = 9·10⁹ · 2·10⁻⁶ · 3·10⁻⁶ / 0.09 = 0.054 / 0.09 = 0.6 N.',
  '0,6 Н. Это сила примерно как вес груза в 60 г.', '0.6 N. That is roughly the weight of a 60 g load.', True),
 task(2, 'Вдвое дальше', 'Twice as far', 'Как изменится сила между двумя зарядами, если расстояние между ними увеличить в 2 раза? в 3 раза?', 'How does the force between two charges change if the distance between them is increased 2 times? 3 times?',
  'r₂ = 2r₁ и r₂ = 3r₁', 'r₂ = 2r₁ and r₂ = 3r₁', 'F ~ 1/r².<br>При 2r: F уменьшится в 2² = 4 раза.<br>При 3r: в 3² = 9 раз.', 'F ~ 1/r².<br>At 2r: F decreases 2² = 4 times.<br>At 3r: 9 times.',
  'в 4 раза и в 9 раз.', '4 times and 9 times.'),
 task(3, 'Заряд расчёски', 'The comb’s charge', 'Расчёска получила 5·10¹⁰ лишних электронов. Каков её заряд? e = 1,6·10⁻¹⁹ Кл.', 'A comb received 5·10¹⁰ extra electrons. What is its charge? e = 1.6·10⁻¹⁹ C.',
  'N = 5·10¹⁰, e = 1,6·10⁻¹⁹ Кл', 'N = 5·10¹⁰, e = 1.6·10⁻¹⁹ C', 'q = N·e = 5·10¹⁰ · 1,6·10⁻¹⁹ = 8·10⁻⁹ Кл.', 'q = N·e = 5·10¹⁰ · 1.6·10⁻¹⁹ = 8·10⁻⁹ C.',
  '8 нКл, заряд отрицательный.', '8 nC, the charge is negative.'),
 task(4, 'Электронов в кулоне', 'Electrons in a coulomb', 'Сколько электронов нужно, чтобы получить заряд 1 Кл?', 'How many electrons are needed to give a charge of 1 C?',
  'q = 1 Кл, e = 1,6·10⁻¹⁹ Кл', 'q = 1 C, e = 1.6·10⁻¹⁹ C', 'N = q / e = 1 / (1,6·10⁻¹⁹) ≈ 6,25·10¹⁸.', 'N = q / e = 1 / (1.6·10⁻¹⁹) ≈ 6.25·10¹⁸.',
  'около 6·10¹⁸ электронов.', 'about 6·10¹⁸ electrons.'),
 task(5, 'Гроза над перевалом', 'A storm over a pass', 'Гром послышался через 6 секунд после вспышки. Как далеко ударила молния? Скорость звука 340 м/с.', 'Thunder was heard 6 seconds after the flash. How far did the lightning strike? Speed of sound 340 m/s.',
  't = 6 с, v = 340 м/с', 't = 6 s, v = 340 m/s', 's = v·t = 340 · 6 = 2040 м.', 's = v·t = 340 · 6 = 2,040 m.',
  'около 2 км. Свет дошёл практически мгновенно.', 'about 2 km. The light arrived practically instantly.'),
 task(6, 'Два кулона', 'Two coulombs', 'Два заряда по 1 Кл находятся на расстоянии 1 км. Найдите силу взаимодействия. Сравните с весом груза (g = 9,8 Н/кг).', 'Two 1 C charges are 1 km apart. Find the force between them. Compare it with the weight of a load (g = 9.8 N/kg).',
  'q = 1 Кл, r = 1000 м', 'q = 1 C, r = 1,000 m', 'F = 9·10⁹ · 1 · 1 / 1000² = 9000 Н.<br>Масса груза: m = F / g ≈ 918 кг.', 'F = 9·10⁹ · 1 · 1 / 1,000² = 9,000 N.<br>Mass of the load: m = F / g ≈ 918 kg.',
  '9000 Н, как вес почти тонны груза, даже на расстоянии километра. Кулон — очень большой заряд.', '9,000 N, like the weight of nearly a tonne even at a kilometre. A coulomb is a very large charge.'),
]

quiz = [
 ('Как взаимодействуют одноимённые заряды?', [('Притягиваются', 'Притягиваются разноимённые.'), ('Отталкиваются', 'Верно.'), ('Не взаимодействуют', 'Взаимодействие есть всегда.')],
  'How do like charges interact?', [('They attract', 'It is unlike charges that attract.'), ('They repel', 'Correct.'), ('They do not interact', 'There is always an interaction.')], 1),
 ('Что переходит с одного тела на другое при электризации трением?', [('Протоны', 'Протоны не уходят из ядер.'), ('Электроны', 'Верно: электроны слабо связаны.'), ('Атомы целиком', 'Атомы не переходят целиком.')],
  'What passes from one body to another in electrification by friction?', [('Protons', 'Protons do not leave the nuclei.'), ('Electrons', 'Correct: electrons are loosely bound.'), ('Whole atoms', 'Whole atoms do not pass over.')], 1),
 ('В каких единицах измеряют заряд?', [('Вольтах', 'Вольт — единица напряжения.'), ('Кулонах', 'Верно.'), ('Омах', 'Ом — единица сопротивления.')],
  'In which units is charge measured?', [('Volts', 'The volt is a unit of voltage.'), ('Coulombs', 'Correct.'), ('Ohms', 'The ohm is a unit of resistance.')], 1),
 ('Как изменится сила между зарядами, если расстояние увеличить вдвое?', [('Уменьшится в 2 раза', 'Сила зависит от квадрата расстояния.'), ('Уменьшится в 4 раза', 'Верно: F ~ 1/r².'), ('Не изменится', 'Сила зависит от расстояния.')],
  'How does the force between charges change if the distance is doubled?', [('It decreases 2 times', 'The force depends on the square of the distance.'), ('It decreases 4 times', 'Correct: F ~ 1/r².'), ('It does not change', 'The force depends on the distance.')], 1),
 ('Что произойдёт с силой, если один из зарядов увеличить втрое?', [('Увеличится втрое', 'Верно: F пропорциональна каждому заряду.'), ('Увеличится в 9 раз', 'В 9 раз сила меняется при изменении расстояния втрое (в обратную сторону).'), ('Не изменится', 'Сила зависит от величины заряда.')],
  'What happens to the force if one of the charges is tripled?', [('It triples', 'Correct: F is proportional to each charge.'), ('It grows 9 times', 'Tripling the distance changes the force by 9 times (the other way).'), ('It stays the same', 'The force depends on the size of the charge.')], 0),
 ('Какой материал лучше проводит заряд?', [('Пластмасса', 'Пластмасса — диэлектрик.'), ('Медь', 'Верно: металлы — проводники.'), ('Стекло', 'Стекло — диэлектрик.')],
  'Which material conducts charge best?', [('Plastic', 'Plastic is an insulator.'), ('Copper', 'Correct: metals are conductors.'), ('Glass', 'Glass is an insulator.')], 1),
 ('Гром услышали через 3 секунды после вспышки. Какое примерно расстояние до молнии?', [('1 км', 'Верно: 340 · 3 ≈ 1 км.'), ('3 км', 'Это было бы через 9 секунд.'), ('300 м', 'Это было бы через 1 секунду.')],
  'Thunder was heard 3 seconds after the flash. About how far is the lightning?', [('1 km', 'Correct: 340 · 3 ≈ 1 km.'), ('3 km', 'That would be after 9 seconds.'), ('300 m', 'That would be after 1 second.')], 0),
 ('Почему мы видим молнию раньше, чем слышим гром?', [('Свет быстрее звука', 'Верно: свет почти мгновенный, звук идёт 340 м/с.'), ('Гром происходит позже молнии', 'Гром возникает одновременно.'), ('Молния ближе грома', 'Они возникают в одном месте.')],
  'Why do we see lightning before we hear thunder?', [('Light is faster than sound', 'Correct: light is almost instantaneous, sound travels 340 m/s.'), ('Thunder happens later than lightning', 'Thunder arises at the same time.'), ('Lightning is nearer than thunder', 'They arise in the same place.')], 0),
]

js = r'''
const T={ru:{
 coLabel:"Два заряженных шарика и стрелки сил",elLabel:"Расчёска и волосы: переход электронов",thLabel:"Гроза: вспышка и гром",
 uC:" мкКл",mN:" мН",N:" Н",
 rep:"отталкиваются",att:"притягиваются",none:"нет заряда — нет силы",
 coFb:"Одноимённые заряды отталкиваются, разноимённые притягиваются.",
 elFb:"Заряды расчёски и волос равны по модулю и противоположны по знаку: суммарный заряд сохраняется.",
 thFb:"Три секунды на километр: расстояние растёт вместе с задержкой грома.",
 comb:"расчёска",hair:"волосы"},
 en:{
 coLabel:"Two charged balls and force arrows",elLabel:"A comb and hair: electron transfer",thLabel:"A storm: flash and thunder",
 uC:" µC",mN:" mN",N:" N",
 rep:"repel",att:"attract",none:"no charge — no force",
 coFb:"Like charges repel, unlike charges attract.",
 elFb:"The charges of the comb and the hair are equal in size and opposite in sign: the total charge is conserved.",
 thFb:"Three seconds per kilometre: the distance grows with the delay of the thunder.",
 comb:"comb",hair:"hair"}};
const KC=9e9,EL=1.602e-19;
function sgn(v){return v>0?"+"+v:""+v}
function drawCo(){const t=tt(),a=+$("q1").value,b=+$("q2").value,r=+$("rr").value,F=KC*Math.abs(a)*Math.abs(b)*1e-12/(r*r);
 const x1=300-r*120,x2=300+r*120,col=v=>v>0?"#b6533f":v<0?"#3f5f8f":"#c9c2b0";
 let g='<line x1="30" y1="150" x2="570" y2="150" stroke="#e3e1da"/>';
 g+='<circle cx="'+x1+'" cy="110" r="'+(12+Math.abs(a)*1.8)+'" fill="'+col(a)+'" stroke="#18181a"/><circle cx="'+x2+'" cy="110" r="'+(12+Math.abs(b)*1.8)+'" fill="'+col(b)+'" stroke="#18181a"/>';
 g+=svgText(x1,115,a>0?"+":a<0?"−":"0","#fff","middle",16)+svgText(x2,115,b>0?"+":b<0?"−":"0","#fff","middle",16);
 if(a!==0&&b!==0){const L=Math.min(120,15+Math.log10(1+F*1000)*28),same=a*b>0;
  if(same){g+=arrow(x1-14,110,x1-14-L,110,"#18181a",3)+arrow(x2+14,110,x2+14+L,110,"#18181a",3)}
  else{g+=arrow(x1+16,110,x1+16+Math.min(L,(x2-x1)/2-20),110,"#18181a",3)+arrow(x2-16,110,x2-16-Math.min(L,(x2-x1)/2-20),110,"#18181a",3)}}
 g+=svgText(300,190,"r = "+fmt(r,1)+(lang==="ru"?" м":" m"),"#66666b","middle",12);
 $("coSvg").innerHTML=g;
 $("q1Out").textContent=sgn(a)+t.uC;$("q2Out").textContent=sgn(b)+t.uC;$("rrOut").textContent=fmt(r,1)+(lang==="ru"?" м":" m");
 $("cF").textContent=F>=1?fmt(F,2)+t.N:fmt(F*1000,1)+t.mN;
 $("cK").textContent=(a===0||b===0)?t.none:(a*b>0?t.rep:t.att);$("coFb").textContent=t.coFb}
["q1","q2","rr"].forEach(id=>$(id).addEventListener("input",drawCo));
function drawEl(){const t=tt(),n=+$("en").value,N=n*1e10,q=N*EL*1e9;
 let g='<rect x="60" y="60" width="180" height="90" rx="10" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/><rect x="360" y="60" width="180" height="90" rx="10" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/>';
 const dots=Math.max(1,Math.round(n/4));
 for(let i=0;i<dots;i++){const px=70+(i*37)%160,py=72+((i*53)%70);g+='<circle cx="'+(px+300*0)+'" cy="'+py+'" r="4" fill="#3f5f8f"/>'}
 g+=svgText(150,180,t.comb+" (−)","#3f5f8f","middle",13)+svgText(450,180,t.hair+" (+)","#b6533f","middle",13);
 g+=arrow(370,105,250,105,"#18181a",3);
 for(let i=0;i<3;i++)g+='<circle cx="'+(330-i*25)+'" cy="'+(96+i*8)+'" r="0"/>';
 $("elSvg").innerHTML=g;
 $("enOut").textContent=num(n*10)+(lang==="ru"?" млрд":" billion");
 $("eN").textContent=num(n*10)+(lang==="ru"?" млрд":" billion");$("eQ").textContent="−"+fmt(q,1)+(lang==="ru"?" нКл":" nC");$("eP").textContent="+"+fmt(q,1)+(lang==="ru"?" нКл":" nC");$("elFb").textContent=t.elFb}
$("en").addEventListener("input",drawEl);
function drawTh(){const t=tt(),s=+$("tt").value,d=340*s;
 const x=60+Math.min(1,d/10200)*480;
 let g='<line x1="40" y1="170" x2="560" y2="170" stroke="#18181a" stroke-width="2"/><circle cx="60" cy="150" r="9" fill="#2f6f5d"/>'+svgText(60,196,lang==="ru"?"вы":"you","#2f6f5d","middle",12);
 g+='<path d="M'+(x-18)+' 40 L'+(x+6)+' 40 L'+(x-6)+' 95 L'+(x+12)+' 95 L'+(x-14)+' 168 L'+(x-4)+' 108 L'+(x-18)+' 108 Z" fill="#e0b82f" stroke="#18181a"/>';
 g+=svgText(x,196,fmt(d/1000,2)+(lang==="ru"?" км":" km"),"#b6533f","middle",13);
 $("thSvg").innerHTML=g;
 $("ttOut").textContent=s+UN[lang].s;
 $("tD").textContent=fmt(d/1000,2)+(lang==="ru"?" км":" km");$("tL").textContent=fmt(d/3e8*1e6,1)+(lang==="ru"?" мкс":" µs");$("thFb").textContent=t.thFb}
$("tt").addEventListener("input",drawTh);
const LAB={ru:{coSvg:T.ru.coLabel,elSvg:T.ru.elLabel,thSvg:T.ru.thLabel},en:{coSvg:T.en.coLabel,elSvg:T.en.elLabel,thSvg:T.en.thLabel}};
function drawAll(){drawCo();drawEl();drawTh()}
'''

c = dict(n='14', slug='14-electric-charge.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Электрический заряд и закон Кулона', 'Electric charge and Coulomb’s law'),
 desc='Глава 14 Атласа физики: электризация, заряд, закон Кулона, проводники и диэлектрики, молния и гром.',
 lead=('Расчёской можно поднять клочки бумаги, а молния в горах — это огромная искра. Заряд, электроны, закон Кулона и гроза.',
       'A comb can lift bits of paper, and lightning in the mountains is a huge spark. Charge, electrons, Coulomb’s law and thunderstorms.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('coulomb', 'Заряд и закон Кулона', 'Charge and Coulomb’s law'), ('transfer', 'Электроны', 'Electrons'), ('lightning', 'Молния', 'Lightning'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Расчешите сухие чистые волосы пластмассовой расчёской, а потом поднесите её к мелким клочкам бумаги. Бумажки подпрыгнут и прилипнут к расчёске. Они не железные, не магнитные и не липкие, а расчёска ничего не касалась.</p><p>Что заставляет бумагу тянуться к расчёске?</p>',
         '<p>Comb dry clean hair with a plastic comb, then bring it near small scraps of paper. The scraps jump up and stick to the comb. They are not iron, not magnetic and not sticky, and the comb touched nothing.</p><p>What makes the paper reach for the comb?</p>'),
 hint=('Подсказку даст модель «Переход электронов при трении». Разгадка — в конце главы.', 'The “Electron transfer by rubbing” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему бумага тянется к расчёске', 'The answer: why paper reaches for the comb'),
 answer=('<p>При расчёсывании электроны переходят с волос на пластмассу, и расчёска получает отрицательный заряд (около нескольких нанокулонов, то есть миллиарды электронов). Её электрическое поле смещает заряды внутри кусочков бумаги: ближе к расчёске оказывается положительный заряд, дальше — отрицательный. Притяжение к ближайшей стороне сильнее, чем отталкивание от дальней (закон Кулона: чем ближе, тем сильнее), поэтому бумага притягивается.</p><p>Так же и гроза: в облаке разделяются огромные заряды, и разряд между облаком и землёй — молния.</p>',
         '<p>When combing, electrons pass from the hair to the plastic, and the comb becomes negatively charged (a few nanocoulombs, that is, billions of electrons). Its electric field shifts the charges inside the bits of paper: positive charge ends up nearer the comb and negative farther. The attraction to the nearer side is stronger than the repulsion from the farther one (Coulomb’s law: the closer, the stronger), so the paper is attracted.</p><p>A thunderstorm is similar: huge charges separate in the cloud, and the discharge between cloud and ground is lightning.</p>'),
 sources=[
  ('Элементарный заряд e ≈ 1,602·10⁻¹⁹ Кл —', 'The elementary charge e ≈ 1.602·10⁻¹⁹ C —', LINK('https://physics.nist.gov/cgi-bin/cuu/Value?e', 'NIST: elementary charge')),
  ('Закон Кулона, k ≈ 8,99·10⁹ Н·м²/Кл² —', 'Coulomb’s law, k ≈ 8.99·10⁹ N·m²/C² —', LINK('https://en.wikipedia.org/wiki/Coulomb%27s_law', 'Wikipedia: Coulomb’s law')),
  ('Молния: ток около 30 000 А, температура канала около 30 000 °C, напряжение сотни миллионов вольт —', 'Lightning: current about 30,000 A, channel temperature about 30,000 °C, voltage hundreds of millions of volts —', LINK('https://www.britannica.com/science/thunderstorm/Cloud-to-ground-lightning', 'Britannica: Cloud-to-ground lightning') + ', ' + LINK('https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh0102', 'UNDRR: Lightning')),
  ('Расстояние до грозы по задержке грома —', 'Distance to a storm from the thunder delay —', LINK('https://www.alloprof.qc.ca/en/students/vl/sciences/lightning-s1365', 'Alloprof: Lightning'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Число электронов в модели — условное.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The number of electrons in the model is assumed.'),
 prev=('13-weather-climate.html', 'Глава 13 · Погода и климат', 'Chapter 13 · Weather and climate'),
 next=('15-electric-field.html', 'Глава 15 · Электрическое поле', 'Chapter 15 · The electric field'),
 js=js)
build(c)
