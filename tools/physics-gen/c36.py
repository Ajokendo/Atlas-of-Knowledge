# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ТЯГОТЕНИЕ НА РАЗНЫХ ВЫСОТАХ', 'GRAVITY AT DIFFERENT HEIGHTS', 'gvSvg', '0 0 600 250',
  select('gb', 'Небесное тело', 'Celestial body') + slider('gh', 'Высота над поверхностью', 'Height above the surface', 0, 40000, 100, 400) + slider('gm', 'Масса тела', 'Mass of the body', 1, 100, 1, 70),
  stats([('gG', 'Ускорение свободного падения g = GM/r²', 'Free-fall acceleration g = GM/r²'), ('gF', 'Сила притяжения F = m·g', 'Force of attraction F = m·g'), ('gR', 'Во сколько раз меньше, чем на поверхности', 'How many times less than at the surface')]),
  'gvFb', 'Схема условная, без масштаба. G = 6,674·10⁻¹¹ Н·м²/кг²; массы и радиусы тел округлены; высота — в километрах.',
  'A schematic drawing, not to scale. G = 6.674·10⁻¹¹ N·m²/kg²; the masses and radii of the bodies are rounded; the height in kilometres.')
s1 = section('gravity', 'Закон всемирного тяготения', 'The law of universal gravitation',
 bd('<p>Любые два тела притягиваются друг к другу. <strong>Закон всемирного тяготения</strong> Ньютона: сила притяжения прямо пропорциональна произведению масс и обратно пропорциональна квадрату расстояния <em>между центрами</em>. Яблоко падает на Землю и Луна «падает» вокруг неё по одному и тому же закону.</p>',
    '<p>Any two bodies attract each other. Newton’s <strong>law of universal gravitation</strong>: the force of attraction is directly proportional to the product of the masses and inversely proportional to the square of the distance <em>between their centres</em>. An apple falls to the Earth and the Moon “falls” around it by the same law.</p>')
 + formula('F = G · M · m / r²,   g = G · M / r²', 'G = 6,674·10⁻¹¹ Н·м²/кг²; r — расстояние от центра тела', 'G = 6.674·10⁻¹¹ N·m²/kg²; r is the distance from the centre of the body')
 + bd('<p>У поверхности Земли <em>g ≈ 9,8 м/с²</em>, на Луне 1,6, на Марсе 3,7. С высотой тяготение слабеет, но очень медленно: на высоте 400 км (орбита Международной космической станции) оно всего на 12% меньше, чем у земной поверхности.</p>',
      '<p>At the Earth’s surface <em>g ≈ 9.8 m/s²</em>, on the Moon 1.6, on Mars 3.7. Gravity weakens with height but very slowly: at 400 km (the orbit of the International Space Station) it is only 12% weaker than at the Earth’s surface.</p>'),
 lab1)

lab2 = model(2, 'СПУТНИК НА ОРБИТЕ', 'A SATELLITE IN ORBIT', 'orSvg', '0 0 600 250',
  slider('oh', 'Высота орбиты над Землёй', 'Orbit height above the Earth', 200, 40000, 100, 400),
  stats([('oV', 'Скорость v = √(GM/r)', 'Speed v = √(GM/r)'), ('oT', 'Период обращения', 'Orbital period'), ('oN', 'Оборотов в сутки', 'Revolutions per day'), ('oK', 'Что это за орбита', 'What kind of orbit')]),
  'orFb', 'Схема условная: круговая орбита, масштаб сжат. Земля: M = 5,97·10²⁴ кг, R = 6371 км, GM = 3,986·10¹⁴ м³/с².',
  'A schematic drawing: a circular orbit, the scale compressed. Earth: M = 5.97·10²⁴ kg, R = 6,371 km, GM = 3.986·10¹⁴ m³/s².')
s2 = section('orbit', 'Спутники и космические скорости', 'Satellites and cosmic speeds',
 bd('<p>Спутник не «висит» в космосе — он падает. Брошенный камень падает по дуге, и чем сильнее бросок, тем дальше он улетит. При достаточно большой скорости (<strong>первая космическая скорость</strong>) Земля «уходит из-под ног» так же быстро, как камень падает, и тело летит вокруг планеты бесконечно. Для круговой орбиты радиуса <em>r</em> сила тяготения даёт центростремительное ускорение: <em>GM/r² = v²/r</em>, откуда</p>',
    '<p>A satellite does not “hang” in space — it falls. A thrown stone falls along an arc and the harder it is thrown the farther it lands. At a sufficiently high speed (the <strong>first cosmic speed</strong>) the Earth “falls away” beneath it as fast as the stone falls and the body flies round the planet for ever. For a circular orbit of radius <em>r</em> gravity gives the centripetal acceleration: <em>GM/r² = v²/r</em>, whence</p>')
 + formula('v = √(GM / r),   T = 2π · √(r³ / GM)', 'у поверхности Земли v ≈ 7,9 км/с; чем выше орбита, тем медленнее спутник и длиннее период', 'at the Earth’s surface v ≈ 7.9 km/s; the higher the orbit the slower the satellite and the longer the period')
 + bd('<p>На высоте около 36 000 км период равен суткам — спутник всё время «висит» над одной точкой экватора (<strong>геостационарная орбита</strong>); на ней работают телевидение и связь. Навигационные спутники (GPS) летают на высоте около 20 000 км, а Международная космическая станция — на 400 км и обходит Землю примерно за 92 минуты. Станция и космонавты в ней в невесомости, потому что находятся в свободном падении (глава 33).</p>',
      '<p>At a height of about 36,000 km the period equals a day — the satellite constantly “hangs” over one point of the equator (<strong>geostationary orbit</strong>); television and communications work there. Navigation satellites (GPS) fly at about 20,000 km and the International Space Station at 400 km goes round the Earth in about 92 minutes. The station and the astronauts in it are weightless because they are in free fall (chapter 33).</p>'),
 lab2)

lab3 = model(3, 'ПРЫЖОК НА РАЗНЫХ ПЛАНЕТАХ', 'A JUMP ON DIFFERENT PLANETS', 'jpSvg', '0 0 600 250',
  select('jb', 'Где прыгаем', 'Where we jump') + slider('jv', 'Скорость отрыва от земли', 'Take-off speed', 1, 5, 0.1, 2.8) + slider('jm', 'Ваша масса', 'Your mass', 30, 100, 1, 60),
  stats([('jH', 'Высота прыжка h = v²/(2g)', 'Jump height h = v²/(2g)'), ('jT', 'Время полёта 2v/g', 'Flight time 2v/g'), ('jW', 'Ваш вес', 'Your weight')]),
  'jpFb', 'Схема условная: тело подпрыгивает вертикально с одной и той же скоростью отрыва; сопротивление атмосферы не учитывается.',
  'A schematic drawing: the body jumps vertically at the same take-off speed; atmospheric drag is ignored.')
s3 = section('jump', 'Масса и вес на других планетах', 'Mass and weight on other planets',
 bd('<p>Масса — свойство тела, а вес — сила, с которой оно давит на опору. На Луне ваша масса та же, а вес в 6 раз меньше (там <em>g = 1,62 м/с²</em>). Поэтому тот же прыжок, который на Земле поднимает вас на 40 см, на Луне поднимет на 2,4 метра.</p><p>Высота прыжка при скорости отрыва <em>v</em> из закона сохранения энергии: <em>m·g·h = m·v²/2</em>, то есть <em>h = v² / (2g)</em>; время полёта — <em>2v / g</em>.</p>',
    '<p>Mass is a property of a body while weight is the force with which it presses on a support. On the Moon your mass is the same but your weight is 6 times less (there <em>g = 1.62 m/s²</em>). So the same jump that lifts you 40 cm on Earth lifts you 2.4 metres on the Moon.</p><p>The height of a jump at take-off speed <em>v</em> follows from conservation of energy: <em>m·g·h = m·v²/2</em>, that is <em>h = v² / (2g)</em>; the flight time is <em>2v / g</em>.</p>')
 + formula('h = v² / (2g),   P = m · g', 'масса не меняется, вес зависит от g места', 'the mass does not change; the weight depends on the local g'),
 lab3)

tasks = [
 task(1, 'Притяжение на поверхности', 'Attraction at the surface', 'Найдите силу, с которой Земля притягивает тело массой 1 кг на поверхности. G = 6,674·10⁻¹¹, M = 5,97·10²⁴ кг, R = 6,371·10⁶ м.', 'Find the force with which the Earth attracts a 1 kg body at the surface. G = 6.674·10⁻¹¹, M = 5.97·10²⁴ kg, R = 6.371·10⁶ m.',
  'm = 1 кг', 'm = 1 kg', 'F = G·M·m / R² = 6,674·10⁻¹¹ · 5,97·10²⁴ / (6,371·10⁶)² = 3,985·10¹⁴ / 4,059·10¹³ ≈ 9,8 Н.', 'F = G·M·m / R² = 6.674·10⁻¹¹ · 5.97·10²⁴ / (6.371·10⁶)² = 3.985·10¹⁴ / 4.059·10¹³ ≈ 9.8 N.', '≈ 9,8 Н, то есть g ≈ 9,8 м/с².', '≈ 9.8 N, that is g ≈ 9.8 m/s².', True),
 task(2, 'g на высоте станции', 'g at the height of the station', 'Найдите g на высоте 400 км (r = 6771 км). GM = 3,986·10¹⁴ м³/с².', 'Find g at a height of 400 km (r = 6,771 km). GM = 3.986·10¹⁴ m³/s².',
  'r = 6,771·10⁶ м', 'r = 6.771·10⁶ m', 'g = GM / r² = 3,986·10¹⁴ / (6,771·10⁶)² = 3,986·10¹⁴ / 4,584·10¹³ ≈ 8,7 м/с².', 'g = GM / r² = 3.986·10¹⁴ / (6.771·10⁶)² = 3.986·10¹⁴ / 4.584·10¹³ ≈ 8.7 m/s².', 'около 8,7 м/с² — на 12% меньше. Невесомость на станции не из-за отсутствия тяготения, а из-за свободного падения.', 'about 8.7 m/s² — 12% less. Weightlessness on the station is not from a lack of gravity but from free fall.'),
 task(3, 'Первая космическая', 'The first cosmic speed', 'Найдите скорость спутника на очень низкой круговой орбите (r ≈ R = 6371 км).', 'Find the speed of a satellite in a very low circular orbit (r ≈ R = 6,371 km).',
  'r = 6,371·10⁶ м', 'r = 6.371·10⁶ m', 'v = √(GM/r) = √(3,986·10¹⁴ / 6,371·10⁶) = √(6,257·10⁷) ≈ 7910 м/с.', 'v = √(GM/r) = √(3.986·10¹⁴ / 6.371·10⁶) = √(6.257·10⁷) ≈ 7,910 m/s.', '≈ 7,9 км/с.', '≈ 7.9 km/s.'),
 task(4, 'Период МКС', 'The period of the ISS', 'Найдите период обращения по круговой орбите на высоте 400 км (r = 6771 км) и число оборотов в сутки.', 'Find the orbital period on a circular orbit at a height of 400 km (r = 6,771 km) and the number of revolutions per day.',
  'r = 6,771·10⁶ м', 'r = 6.771·10⁶ m', 'T = 2π·√(r³/GM) = 6,283 · √(3,104·10²⁰ / 3,986·10¹⁴) = 6,283 · 882,4 ≈ 5544 с ≈ 92,4 мин.<br>Оборотов в сутки: 1440 / 92,4 ≈ 15,6.', 'T = 2π·√(r³/GM) = 6.283 · √(3.104·10²⁰ / 3.986·10¹⁴) = 6.283 · 882.4 ≈ 5,544 s ≈ 92.4 min.<br>Revolutions per day: 1440 / 92.4 ≈ 15.6.', 'около 92 минут и 15,6 оборота в сутки.', 'about 92 minutes and 15.6 revolutions per day.'),
 task(5, 'Геостационарная орбита', 'The geostationary orbit', 'На каком расстоянии от центра Земли период обращения равен звёздным суткам (86 164 с)? Найдите высоту над поверхностью.', 'At what distance from the Earth’s centre does the period equal a sidereal day (86,164 s)? Find the height above the surface.',
  'T = 86 164 с', 'T = 86,164 s', 'r³ = GM·T² / (4π²) = 3,986·10¹⁴ · 7,424·10⁹ / 39,48 = 7,496·10²².<br>r = 4,216·10⁷ м = 42 164 км.<br>Высота: 42 164 − 6371 ≈ 35 800 км.', 'r³ = GM·T² / (4π²) = 3.986·10¹⁴ · 7.424·10⁹ / 39.48 = 7.496·10²².<br>r = 4.216·10⁷ m = 42,164 km.<br>Height: 42,164 − 6,371 ≈ 35,800 km.', 'около 35 800 км над экватором.', 'about 35,800 km above the equator.'),
 task(6, 'Прыжок на Луне', 'A jump on the Moon', 'Вы отрываетесь от земли со скоростью 2,8 м/с. На какую высоту вы подпрыгнете на Земле (g = 9,8) и на Луне (g = 1,62)?', 'You leave the ground at 2.8 m/s. How high do you jump on Earth (g = 9.8) and on the Moon (g = 1.62)?',
  'v = 2,8 м/с', 'v = 2.8 m/s', 'h = v² / (2g).<br>Земля: 7,84 / 19,6 = 0,40 м.<br>Луна: 7,84 / 3,24 ≈ 2,42 м.', 'h = v² / (2g).<br>Earth: 7.84 / 19.6 = 0.40 m.<br>Moon: 7.84 / 3.24 ≈ 2.42 m.', '40 см и 2,4 м — в шесть раз выше.', '40 cm and 2.4 m — six times higher.'),
]

quiz = [
 qz('От чего зависит сила всемирного тяготения?', 'От масс тел и расстояния между их центрами', 'Только от массы одного тела', 'От цвета тел', 'F = G·M·m / r².',
    'What does the force of universal gravitation depend on?', 'The masses of the bodies and the distance between their centres', 'The mass of one body only', 'The colour of the bodies', 'F = G·M·m / r².'),
 qz('Как изменится сила притяжения при увеличении расстояния вдвое?', 'Уменьшится в 4 раза', 'Уменьшится в 2 раза', 'Не изменится', 'F ~ 1/r².',
    'How does the force of attraction change when the distance doubles?', 'It decreases 4 times', 'It decreases 2 times', 'It does not change', 'F ~ 1/r².'),
 qz('Почему космонавты на МКС в невесомости?', 'Станция и они находятся в свободном падении', 'На высоте 400 км нет тяготения', 'Там вакуум', 'Тяготение там почти такое же, как на Земле.',
    'Why are astronauts on the ISS weightless?', 'The station and they are in free fall', 'There is no gravity at 400 km', 'There is a vacuum there', 'Gravity there is almost as strong as on Earth.'),
 qz('Чему примерно равна первая космическая скорость у Земли?', '7,9 км/с', '0,79 км/с', '79 км/с', 'v = √(GM/R) ≈ 7,9 км/с.',
    'What is the first cosmic speed at the Earth approximately?', '7.9 km/s', '0.79 km/s', '79 km/s', 'v = √(GM/R) ≈ 7.9 km/s.'),
 qz('Как меняется период обращения спутника с ростом высоты орбиты?', 'Растёт', 'Уменьшается', 'Не меняется', 'T = 2π√(r³/GM).',
    'How does the orbital period change as the orbit gets higher?', 'It grows', 'It decreases', 'It does not change', 'T = 2π√(r³/GM).'),
 qz('Что такое геостационарная орбита?', 'Орбита с периодом в сутки над экватором', 'Орбита вокруг Луны', 'Орбита около полюсов', 'Спутник всё время над одной точкой экватора.',
    'What is a geostationary orbit?', 'An orbit with a period of a day above the equator', 'An orbit around the Moon', 'An orbit near the poles', 'The satellite stays above one point of the equator.'),
 qz('Что остаётся неизменным при переносе тела на Луну?', 'Масса', 'Вес', 'Ускорение свободного падения', 'Масса — свойство тела, вес зависит от g.',
    'What stays the same when a body is moved to the Moon?', 'The mass', 'The weight', 'The free-fall acceleration', 'Mass is a property of the body; weight depends on g.'),
 qz('Во сколько раз выше вы подпрыгнете на Луне (g = 1,62), чем на Земле (g = 9,8) при той же скорости отрыва?', 'Примерно в 6 раз', 'Примерно в 2 раза', 'Так же', 'h = v²/(2g): g в 6 раз меньше — h в 6 раз больше.',
    'How many times higher will you jump on the Moon (g = 1.62) than on Earth (g = 9.8) at the same take-off speed?', 'About 6 times', 'About 2 times', 'The same', 'h = v²/(2g): g is 6 times smaller so h is 6 times greater.'),
]

js = r'''
const T={ru:{
 gvLabel:"Тело на разных высотах над небесным телом",orLabel:"Земля и круговая орбита спутника",jpLabel:"Прыжок на разных телах Солнечной системы",
 bodies:["Земля","Луна","Марс"],kinds:["очень низкая орбита","низкая околоземная (как МКС)","средняя (как навигационные спутники)","геостационарная (≈ 36 000 км)","высокая"],
 gvFb:"Тяготение слабеет как квадрат расстояния от центра.",orFb:"Чем выше орбита, тем медленнее летит спутник и длиннее период.",jpFb:"На Луне тот же прыжок выше в 6 раз."},
 en:{
 gvLabel:"A body at different heights above a celestial body",orLabel:"The Earth and a circular satellite orbit",jpLabel:"A jump on different bodies of the Solar System",
 bodies:["Earth","Moon","Mars"],kinds:["a very low orbit","a low Earth orbit (like the ISS)","a medium orbit (like navigation satellites)","geostationary (≈ 36,000 km)","a high orbit"],
 gvFb:"Gravity weakens as the square of the distance from the centre.",orFb:"The higher the orbit the slower the satellite and the longer the period.",jpFb:"On the Moon the same jump is 6 times higher."}};
const GM=[3.986e14,4.9028e12,4.2828e13],RB=[6371e3,1737.4e3,3389.5e3];
function drawGv(){const t=tt(),k=+$("gb").value,h=+$("gh").value*1000,m=+$("gm").value,r=RB[k]+h,g=GM[k]/(r*r),g0=GM[k]/(RB[k]*RB[k]);
 const R0=Math.min(80,30+k*0),sc=R0/RB[k],rr=Math.min(105,r*sc);let gg='<circle cx="150" cy="125" r="'+R0+'" fill="'+(k===0?"#3f5f8f":k===1?"#9a9a9a":"#b6533f")+'" stroke="#18181a"/>';
 const px=150+Math.min(rr,115)+0;gg+='<circle cx="'+(150+Math.min(rr,115))+'" cy="125" r="7" fill="#18181a"/>'+arrow(150+Math.min(rr,115)-8,125,150+Math.min(rr,115)-8-Math.min(70,g*7),125,"#2f6f5d",3);
 gg+=svgText(400,110,"g = "+fmt(g,2),"#18181a","start",18)+svgText(400,140,"h = "+num(h/1000)+UN[lang].km,"#66666b","start",13);
 $("gvSvg").innerHTML=gg;
 $("ghOut").textContent=num(h/1000)+UN[lang].km;$("gmOut").textContent=m+UN[lang].kg;
 $("gG").textContent=fmt(g,2)+(lang==="ru"?" м/с²":" m/s²");$("gF").textContent=fmt(m*g,0)+UN[lang].N;$("gR").textContent=fmt(g0/g,2)+"×";$("gvFb").textContent=t.gvFb}
["gb","gh","gm"].forEach(id=>$(id).addEventListener("input",drawGv));
function drawOr(){const t=tt(),h=+$("oh").value*1000,r=6371e3+h,v=Math.sqrt(3.986e14/r),T0=2*Math.PI*Math.sqrt(r*r*r/3.986e14);
 const R0=40,Ro=Math.min(110,R0+8+(h/40000)*85);let g='<circle cx="300" cy="125" r="'+R0+'" fill="#3f5f8f" stroke="#18181a"/><circle cx="300" cy="125" r="'+Ro+'" fill="none" stroke="#c9c2b0" stroke-dasharray="5 4" stroke-width="2"/><rect x="'+(300+Ro-7)+'" y="118" width="14" height="14" fill="#b6533f" stroke="#18181a"/>';
 g+=arrow(300+Ro,118,300+Ro,118-Math.min(60,v/150),"#2f6f5d",3);
 $("orSvg").innerHTML=g;
 $("ohOut").textContent=num(h/1000)+UN[lang].km;
 const hk=h/1000,k=hk<300?0:hk<1500?1:hk<30000?2:hk<40000?3:4;
 $("oV").textContent=fmt(v/1000,2)+(lang==="ru"?" км/с":" km/s");$("oT").textContent=T0<7200?fmt(T0/60,1)+UN[lang].min:fmt(T0/3600,2)+UN[lang].h;$("oN").textContent=fmt(86400/T0,1);$("oK").textContent=Math.abs(hk-35786)<500?t.kinds[3]:(hk>=35000?t.kinds[4]:(hk>=18000&&hk<=22000?t.kinds[2]:(hk<300?t.kinds[0]:(hk<1500?t.kinds[1]:"—"))));$("orFb").textContent=t.orFb}
$("oh").addEventListener("input",drawOr);
function drawJp(){const t=tt(),k=+$("jb").value,v=+$("jv").value,m=+$("jm").value,g=GM[k]/(RB[k]*RB[k]),h=v*v/(2*g),Tf=2*v/g;
 const y=Math.min(190,h*70);let gg='<line x1="30" y1="215" x2="570" y2="215" stroke="#18181a" stroke-width="2"/><circle cx="300" cy="'+(205-y)+'" r="10" fill="#b87333"/><line x1="300" y1="'+(215-y)+'" x2="300" y2="215" stroke="#c9c2b0" stroke-dasharray="3 3"/>'+svgText(320,'110',"h = "+fmt(h,2)+UN[lang].m,"#18181a","start",14);
 $("jpSvg").innerHTML=gg;
 $("jvOut").textContent=fmt(v,1)+UN[lang].ms;$("jmOut").textContent=m+UN[lang].kg;
 $("jH").textContent=fmt(h,2)+UN[lang].m;$("jT").textContent=fmt(Tf,2)+UN[lang].s;$("jW").textContent=fmt(m*g,0)+UN[lang].N+" ("+fmt(m*g/9.8,0)+UN[lang].kg+")";$("jpFb").textContent=t.jpFb}
["jb","jv","jm"].forEach(id=>$(id).addEventListener("input",drawJp));
const LAB={ru:{gvSvg:T.ru.gvLabel,orSvg:T.ru.orLabel,jpSvg:T.ru.jpLabel},en:{gvSvg:T.en.gvLabel,orSvg:T.en.orLabel,jpSvg:T.en.jpLabel}};
function drawAll(){fillSel("gb",T[lang].bodies,0);fillSel("jb",T[lang].bodies,1);drawGv();drawOr();drawJp()}
'''

c = dict(n='36', slug='36-gravity-satellites.html', block='VI', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Гравитация и спутники', 'Gravity and satellites'),
 desc='Глава 36 Атласа физики: закон всемирного тяготения, орбиты и космические скорости, геостационарная орбита, первый кыргызский спутник, вес на Луне.',
 lead=('Спутник не висит в космосе — он падает. Всемирное тяготение, орбиты, невесомость и первый спутник Кыргызстана.',
       'A satellite does not hang in space — it falls. Universal gravitation, orbits, weightlessness and Kyrgyzstan’s first satellite.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('gravity', 'Тяготение', 'Gravitation'), ('orbit', 'Орбиты', 'Orbits'), ('jump', 'Вес на других телах', 'Weight on other bodies'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>1 октября 2026 года Кыргызстан запустил в космос первый национальный спутник: небольшой (около 5 кг) аппарат вывела ракета Falcon 9 с космодрома в Калифорнии, а управляют им из центра в Бишкеке. На орбите спутник летит со скоростью около 7,5 км/с. Но почему он не падает на Землю, если его притягивает Земля? И почему космонавты на борту подобных станций «парят», хотя тяготение на высоте орбиты почти такое же, как у земной поверхности?</p><p>Что удерживает спутник на орбите?</p>',
         '<p>On 1 October 2026 Kyrgyzstan launched its first national satellite into space: a small (about 5 kg) craft put up by a Falcon 9 rocket from a spaceport in California and controlled from a centre in Bishkek. In orbit a satellite flies at about 7.5 km/s. But why does it not fall to the Earth if the Earth attracts it? And why do astronauts aboard similar stations “float” though gravity at orbital height is almost as strong as at the surface?</p><p>What keeps a satellite in orbit?</p>'),
 hint=stdhint('Спутник на орбите', 'A satellite in orbit'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: спутник непрерывно падает', 'The answer: a satellite falls continuously'),
 answer=('<p>Спутник падает на Землю — но так быстро летит вбок, что поверхность Земли за время падения «уходит» вниз, и он всё время промахивается мимо. Сила тяготения не уравновешена: она и есть центростремительная сила, которая изгибает путь спутника в окружность. Для высоты 400 км нужна скорость около 7,7 км/с (модель 2); медленнее — и спутник войдёт в атмосферу и упадёт.</p><p>Космонавты невесомы потому, что и станция, и они падают с одним ускорением — давить друг на друга им нечем. Тяготения на высоте 400 км достаточно: оно всего на 12% слабее, чем на поверхности (задача 2).</p>',
         '<p>A satellite does fall to the Earth — but moves sideways so fast that the Earth’s surface “drops away” during the fall and it keeps missing. The gravitational force is not balanced: it is the centripetal force that bends the satellite’s path into a circle. For a height of 400 km a speed of about 7.7 km/s is needed (model 2); slower and the satellite would enter the atmosphere and fall.</p><p>Astronauts are weightless because the station and they fall with the same acceleration — they have nothing to press on each other. Gravity at 400 km is plenty: it is only 12% weaker than at the surface (problem 2).</p>'),
 sources=[
  ('Закон всемирного тяготения, орбиты, первая космическая скорость —', 'The law of universal gravitation, orbits, the first cosmic speed —', LINK('https://openstax.org/books/university-physics-volume-1/pages/13-introduction', 'OpenStax University Physics, Vol. 1, гл. 13') + ', ' + LINK('https://en.wikipedia.org/wiki/Orbital_speed', 'Wikipedia: Orbital speed')),
  ('Массы, радиусы и g Земли, Луны и Марса —', 'The masses, radii and g of the Earth, Moon and Mars —', LINK('https://nssdc.gsfc.nasa.gov/planetary/factsheet/', 'NASA Planetary Fact Sheets')),
  ('Геостационарная орбита —', 'The geostationary orbit —', LINK('https://en.wikipedia.org/wiki/Geostationary_orbit', 'Wikipedia: Geostationary orbit')),
  ('Запуск первого национального спутника Кыргызстана 1 октября 2026 года (Falcon 9, Ванденберг; управление из Бишкека; около 5 кг) —', 'The launch of Kyrgyzstan’s first national satellite on 1 October 2026 (Falcon 9, Vandenberg; operated from Bishkek; about 5 kg) —', LINK('https://www.interfax.com/newsroom/top-stories/119376/', 'Interfax, 2 Oct 2026') + ', ' + LINK('https://timesca.com/first-kyrgyzstan-satellite-spacex-falcon-9/', 'The Times of Central Asia, 1 Oct 2026'))],
 note=stdnote('Скорость спутника в загадке (около 7,5 км/с) — оценка для низкой орбиты; высота орбиты кыргызского спутника в источниках не указана. Значения ползунков — условные.', 'The satellite speed in the puzzle (about 7.5 km/s) is an estimate for a low orbit; the sources do not state the orbit height of the Kyrgyz satellite. The slider values are assumed.'),
 prev=('35-rotation-torque.html', 'Глава 35 · Вращение и момент силы', 'Chapter 35 · Rotation and torque'),
 next=('37-conservation-laws.html', 'Глава 37 · Законы сохранения', 'Chapter 37 · Conservation laws'),
 js=js)
build(c)
