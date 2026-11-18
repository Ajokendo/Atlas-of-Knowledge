# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ЗАМЕДЛЕНИЕ ВРЕМЕНИ И СЖАТИЕ ДЛИНЫ', 'TIME DILATION AND LENGTH CONTRACTION', 'tdSvg', '0 0 600 250',
  slider('tb', 'Скорость корабля (доля скорости света)', 'Speed of the ship (fraction of the speed of light)', 0, 0.999, 0.001, 0.8) + slider('ty', 'Время в пути по часам Земли', 'Travel time by Earth clocks', 1, 20, 1, 10) + slider('tl', 'Длина корабля в покое', 'Length of the ship at rest', 10, 200, 5, 100),
  stats([('tG', 'Лоренц-фактор γ = 1/√(1 − v²/c²)', 'Lorentz factor γ = 1/√(1 − v²/c²)'), ('tP', 'Время по часам на корабле', 'Time by the clocks on the ship'), ('tK', 'Длина корабля для наблюдателя на Земле', 'Length of the ship for an observer on the Earth')]),
  'tdFb', 'Схема условная: равномерное прямолинейное движение; c — скорость света; стартовые часы показывают одно и то же.',
  'A schematic drawing: uniform straight-line motion; c is the speed of light; the clocks at the start show the same.')
s1 = section('sr', 'Скорость света — предел, время — не абсолютно', 'The speed of light is a limit and time is not absolute',
 bd('<p>Опыты показывают: скорость света в вакууме одинакова для всех наблюдателей, как бы они ни двигались. Эйнштейн в 1905 году принял это как закон (специальная теория относительности) и вывел следствия: у движущегося тела <em>время идёт медленнее</em> (замедление времени), а его <em>длина вдоль движения короче</em> (сжатие длины). Эффекты определяет лоренц-фактор <em>γ</em>; при скоростях в обычной жизни он неотличимо близок к 1, поэтому мы их не замечаем.</p>',
    '<p>Experiments show: the speed of light in a vacuum is the same for all observers however they move. In 1905 Einstein took this as a law (special relativity) and derived the consequences: in a moving body <em>time runs slower</em> (time dilation) and its <em>length along the motion is shorter</em> (length contraction). The effects are set by the Lorentz factor <em>γ</em>; at everyday speeds it is indistinguishably close to 1 so we do not notice them.</p>')
 + formula('γ = 1 / √(1 − v²/c²),   Δt′ = Δt / γ,   L = L₀ / γ', 'при v = 0,8c: γ = 1,67; при v = 0,99c: γ ≈ 7,1', 'at v = 0.8c: γ = 1.67; at v = 0.99c: γ ≈ 7.1'),
 lab1)

lab2 = model(2, 'ПОПРАВКА ДЛЯ ЧАСОВ GPS', 'THE CORRECTION FOR GPS CLOCKS', 'gpSvg', '0 0 600 250',
  slider('gh', 'Высота орбиты спутника', 'Orbit height of the satellite', 500, 36000, 100, 20200),
  stats([('gV', 'Скорость спутника v = √(GM/r)', 'Speed of the satellite v = √(GM/r)'), ('gS', 'Замедление из-за скорости, за сутки', 'Slowing due to speed, per day'), ('gG', 'Ускорение из-за слабее тяготения, за сутки', 'Speeding up due to weaker gravity, per day'), ('gN', 'Итог: часы спутника уходят вперёд на', 'Net: the satellite clock gains'), ('gE', 'Ошибка определения места без поправки', 'Position error without the correction')]),
  'gpFb', 'Схема условная: круговая орбита; вращение Земли и эллиптичность не учтены; GM = 3,986·10¹⁴ м³/с², радиус Земли 6371 км; приближение слабого поля.',
  'A schematic drawing: a circular orbit; the Earth’s rotation and ellipticity are ignored; GM = 3.986·10¹⁴ m³/s², the Earth’s radius 6,371 km; the weak-field approximation.')
s2 = section('gps', 'Навигация, которой нужна теория относительности', 'Navigation that needs relativity',
 bd('<p>Спутники GPS летят на высоте около 20 200 км со скоростью около 3,9 км/с. По специальной теории относительности их часы идут чуть <em>медленнее</em> земных: <em>Δt/t ≈ −v²/(2c²)</em>, это около −7 мкс в сутки. По общей теории относительности (глава 36) часы в более слабом тяготении идут <em>быстрее</em>: <em>Δt/t ≈ (GM/R − GM/r)/c²</em>, это около +46 мкс в сутки. В сумме часы на спутнике уходят вперёд примерно на 38 мкс в сутки. Радиосигнал за 38 мкс проходит около 11 км — без поправки навигатор «уезжал» бы за сутки на километры. Поэтому частоту часов на спутниках заранее подстраивают.</p>',
    '<p>GPS satellites fly at a height of about 20,200 km at about 3.9 km/s. By special relativity their clocks run slightly <em>slower</em> than Earth’s: <em>Δt/t ≈ −v²/(2c²)</em>, about −7 µs per day. By general relativity (chapter 36) clocks in a weaker gravity run <em>faster</em>: <em>Δt/t ≈ (GM/R − GM/r)/c²</em>, about +46 µs per day. In total the satellite clocks gain about 38 µs per day. In 38 µs a radio signal travels about 11 km — without the correction a navigator would “drift” by kilometres a day. So the frequency of the satellite clocks is adjusted in advance.</p>')
 + formula('δ ≈ −v²/(2c²) + (GM/R − GM/r)/c²', 'ошибка положения Δx = c·Δt', 'the position error Δx = c·Δt'),
 lab2)

lab3 = model(3, 'СЛОЖЕНИЕ СКОРОСТЕЙ', 'ADDITION OF VELOCITIES', 'vaSvg', '0 0 600 250',
  slider('vu', 'Скорость корабля относительно Земли', 'Speed of the ship relative to the Earth', 0, 0.99, 0.01, 0.9) + slider('vv', 'Скорость ракеты относительно корабля', 'Speed of the rocket relative to the ship', 0, 0.99, 0.01, 0.9),
  stats([('vC', 'Классический ответ u + v', 'Classical answer u + v'), ('vR', 'Релятивистский ответ (u + v)/(1 + u·v/c²)', 'Relativistic answer (u + v)/(1 + u·v/c²)'), ('vG', 'Разница', 'The difference')]),
  'vaFb', 'Схема условная: скорости — в долях скорости света c.',
  'A schematic drawing: the speeds are in fractions of the speed of light c.')
s3 = section('velocity', 'Почему нельзя обогнать свет', 'Why light cannot be overtaken',
 bd('<p>Если корабль летит с <em>0,9c</em>, а с него вперёд пускают ракету со скоростью <em>0,9c</em> относительно корабля, то по обычной арифметике скорость ракеты относительно Земли <em>1,8c</em>. По теории относительности скорости складываются иначе: <em>w = (u + v)/(1 + uv/c²) ≈ 0,994c</em>. Результат всегда меньше <em>c</em>. Чем ближе к скорости света, тем больше энергии нужно для небольшого прироста скорости — масса-энергия тела растёт как <em>γ·m·c²</em>, а на скорости света она стала бы бесконечной.</p>',
    '<p>If a ship flies at <em>0.9c</em> and a rocket is fired forward from it at <em>0.9c</em> relative to the ship then by ordinary arithmetic the speed of the rocket relative to the Earth is <em>1.8c</em>. In relativity velocities add differently: <em>w = (u + v)/(1 + uv/c²) ≈ 0.994c</em>. The result is always less than <em>c</em>. The closer to the speed of light the more energy is needed for a small gain in speed — the mass-energy of a body grows as <em>γ·m·c²</em> and at the speed of light it would become infinite.</p>')
 + formula('w = (u + v) / (1 + u·v / c²),   E = γ·m·c²', 'при малых скоростях формула даёт обычное u + v', 'at small speeds the formula gives the ordinary u + v'),
 lab3)

tasks = [
 task(1, 'Лоренц-фактор', 'The Lorentz factor', 'Найдите γ при скоростях 0,6c и 0,8c.', 'Find γ at speeds of 0.6c and 0.8c.',
  'β = 0,6 и 0,8', 'β = 0.6 and 0.8', 'γ = 1/√(1 − β²).<br>β = 0,6: 1/√0,64 = 1/0,8 = 1,25.<br>β = 0,8: 1/√0,36 = 1/0,6 ≈ 1,67.', 'γ = 1/√(1 − β²).<br>β = 0.6: 1/√0.64 = 1/0.8 = 1.25.<br>β = 0.8: 1/√0.36 = 1/0.6 ≈ 1.67.', '1,25 и 1,67.', '1.25 and 1.67.', True),
 task(2, 'Космонавт на 0,8c', 'An astronaut at 0.8c', 'Корабль летит 10 лет по часам Земли со скоростью 0,8c. Сколько времени прошло для космонавта?', 'A ship flies for 10 years by Earth clocks at 0.8c. How much time passed for the astronaut?',
  'Δt = 10 лет, γ = 1,67', 'Δt = 10 years, γ = 1.67', 'Δt′ = Δt/γ = 10 · 0,6 = 6 лет.', 'Δt′ = Δt/γ = 10 · 0.6 = 6 years.', '6 лет — космонавт стал на 4 года моложе «земных» ровесников.', '6 years — the astronaut aged 4 years less than his Earth peers.'),
 task(3, 'Сжатие длины', 'Length contraction', 'Корабль длиной 100 м в покое летит со скоростью 0,6c. Какова его длина для наблюдателя на Земле?', 'A ship of length 100 m at rest flies at 0.6c. What is its length for an observer on the Earth?',
  'L₀ = 100 м, γ = 1,25', 'L₀ = 100 m, γ = 1.25', 'L = L₀/γ = 100 / 1,25 = 80 м.', 'L = L₀/γ = 100 / 1.25 = 80 m.', '80 м.', '80 m.'),
 task(4, 'Сложение скоростей', 'Addition of velocities', 'Корабль летит с 0,9c, ракета вылетает вперёд со скоростью 0,9c относительно корабля. Найдите скорость ракеты относительно Земли.', 'A ship flies at 0.9c and a rocket leaves forward at 0.9c relative to the ship. Find the rocket’s speed relative to the Earth.',
  'u = v = 0,9c', 'u = v = 0.9c', 'w = (u + v)/(1 + uv/c²) = 1,8 / (1 + 0,81) = 1,8 / 1,81 ≈ 0,994c.', 'w = (u + v)/(1 + uv/c²) = 1.8 / (1 + 0.81) = 1.8 / 1.81 ≈ 0.994c.', '≈ 0,994c — меньше c.', '≈ 0.994c — less than c.'),
 task(5, 'GPS: скорость', 'GPS: speed', 'Спутник GPS летит со скоростью 3,87 км/с. Найдите относительное замедление его часов из-за скорости и выразите в мкс за сутки. (c² = 8,99·10¹⁶ м²/с².)', 'A GPS satellite flies at 3.87 km/s. Find the relative slowing of its clock due to speed and give it in µs per day. (c² = 8.99·10¹⁶ m²/s².)',
  'v = 3870 м/с', 'v = 3,870 m/s', 'v²/(2c²) = 1,498·10⁷ / (1,798·10¹⁷) ≈ 8,3·10⁻¹¹.<br>За сутки: 8,3·10⁻¹¹ · 86 400 с ≈ 7,2·10⁻⁶ с.', 'v²/(2c²) = 1.498·10⁷ / (1.798·10¹⁷) ≈ 8.3·10⁻¹¹.<br>Per day: 8.3·10⁻¹¹ · 86,400 s ≈ 7.2·10⁻⁶ s.', '≈ 7,2 мкс в сутки (часы отстают).', '≈ 7.2 µs per day (the clock lags).'),
 task(6, 'GPS: ошибка', 'GPS: the error', 'Итоговый уход часов GPS вперёд — 38 мкс в сутки. На какое расстояние «уедет» вычисленное положение за сутки без поправки?', 'The net gain of the GPS clocks is 38 µs per day. By what distance would the computed position “drift” in a day without the correction?',
  'Δt = 38·10⁻⁶ с', 'Δt = 38·10⁻⁶ s', 'Δx = c·Δt = 3·10⁸ · 38·10⁻⁶ = 1,14·10⁴ м.', 'Δx = c·Δt = 3·10⁸ · 38·10⁻⁶ = 1.14·10⁴ m.', '≈ 11 км за сутки.', '≈ 11 km per day.'),
]

quiz = [
 qz('Что остаётся одинаковым для всех наблюдателей по теории относительности?', 'Скорость света в вакууме', 'Время', 'Длина тела', 'Это основной постулат.',
    'What stays the same for all observers in relativity?', 'The speed of light in a vacuum', 'Time', 'The length of a body', 'This is the basic postulate.'),
 qz('Как идут часы в движущемся корабле, по часам Земли?', 'Медленнее', 'Быстрее', 'Так же', 'Δt′ = Δt/γ.',
    'How do clocks in a moving ship run, by Earth clocks?', 'Slower', 'Faster', 'The same', 'Δt′ = Δt/γ.'),
 qz('Чему равен γ при v = 0,6c?', '1,25', '0,8', '2', '1/√(1 − 0,36) = 1,25.',
    'What is γ at v = 0.6c?', '1.25', '0.8', '2', '1/√(1 − 0.36) = 1.25.'),
 qz('Как меняется длина тела вдоль движения?', 'Сокращается', 'Растёт', 'Не меняется', 'L = L₀/γ.',
    'How does the length of a body along its motion change?', 'It contracts', 'It grows', 'It does not change', 'L = L₀/γ.'),
 qz('Почему в быту мы не замечаем эффектов теории относительности?', 'Скорости много меньше скорости света, γ ≈ 1', 'Их нет', 'Они слишком большие', 'γ неотличимо близок к 1.',
    'Why do we not notice the effects of relativity in everyday life?', 'The speeds are far below the speed of light, γ ≈ 1', 'They do not exist', 'They are too large', 'γ is indistinguishably close to 1.'),
 qz('Может ли тело с массой достичь скорости света?', 'Нет — потребовалась бы бесконечная энергия', 'Да, с ракетой', 'Да, в вакууме', 'E = γmc² растёт без предела.',
    'Can a body with mass reach the speed of light?', 'No — infinite energy would be required', 'Yes, with a rocket', 'Yes, in a vacuum', 'E = γmc² grows without limit.'),
 qz('Зачем в GPS вводят поправки по теории относительности?', 'Иначе ошибка положения росла бы на километры в сутки', 'Для красоты', 'Чтобы спутники не падали', 'Часы спутника уходят на ≈ 38 мкс в сутки.',
    'Why are relativistic corrections introduced in GPS?', 'Otherwise the position error would grow by kilometres a day', 'For beauty', 'So that the satellites do not fall', 'The satellite clocks gain ≈ 38 µs per day.'),
 qz('Чему равно сложение 0,9c и 0,9c по теории относительности?', 'Около 0,994c', '1,8c', 'c', 'w = 1,8/1,81.',
    'What is the sum of 0.9c and 0.9c in relativity?', 'About 0.994c', '1.8c', 'c', 'w = 1.8/1.81.'),
]

js = JSL + r'''
const T={ru:{
 tdLabel:"Часы на Земле и на быстром корабле",gpLabel:"Спутник GPS и часы на Земле",vaLabel:"Корабль и ракета",
 tdFb:"Чем ближе к скорости света, тем медленнее идут часы на корабле.",gpFb:"Два эффекта действуют в разные стороны, итог — уход вперёд.",vaFb:"Сумма скоростей никогда не превысит c."},
 en:{
 tdLabel:"Clocks on the Earth and on a fast ship",gpLabel:"A GPS satellite and clocks on the Earth",vaLabel:"A ship and a rocket",
 tdFb:"The closer to the speed of light the slower the clocks on the ship run.",gpFb:"The two effects act in opposite directions; the net result is a gain.",vaFb:"The sum of speeds never exceeds c."}};
function drawTd(){const t=tt(),b=+$("tb").value,Y=+$("ty").value,L0=+$("tl").value,g=1/Math.sqrt(1-b*b),tp=Y/g,L=L0/g;
 let s='<rect x="40" y="80" width="'+(140)+'" height="40" fill="#cfe2ff" stroke="#18181a"/>'+svgText(110,70,U("корабль в покое: ","ship at rest: ")+L0+" "+U("м","m"),"#66666b","middle",11)+'<rect x="40" y="160" width="'+(140/g)+'" height="40" fill="#b87333" stroke="#18181a"/>'+svgText(110,150,U("для Земли: ","for the Earth: ")+fmt(L,1)+" "+U("м","m"),"#66666b","middle",11)+arrow(220,180,220+Math.min(300,b*300),180,"#2f6f5d",4)
 +'<circle cx="480" cy="100" r="40" fill="#f4f1e8" stroke="#18181a"/>'+svgText(480,105,Y+" "+U("лет","yr"),"#18181a","middle",14)+svgText(480,160,U("Земля","Earth"),"#66666b","middle",11)+'<circle cx="480" cy="200" r="30" fill="#f4f1e8" stroke="#18181a"/>'+svgText(480,205,fmt(tp,1)+" "+U("лет","yr"),"#18181a","middle",13);
 $("tdSvg").innerHTML=s;$("tbOut").textContent=fmt(b,3)+" c";$("tyOut").textContent=Y+" "+U("лет","yr");$("tlOut").textContent=L0+" "+U("м","m");
 $("tG").textContent=fmt(g,3);$("tP").textContent=fmt(tp,2)+" "+U("лет","yr");$("tK").textContent=fmt(L,1)+" "+U("м","m");$("tdFb").textContent=t.tdFb}
["tb","ty","tl"].forEach(id=>$(id).addEventListener("input",drawTd));
function drawGp(){const t=tt(),h=+$("gh").value*1000,R=6371e3,GM=3.986e14,c=299792458,r=R+h,v=Math.sqrt(GM/r),sr=-v*v/(2*c*c)*86400,gr=(GM/R-GM/r)/(c*c)*86400,net=sr+gr,err=Math.abs(net)*c;
 let g='<circle cx="150" cy="125" r="50" fill="#3f5f8f" stroke="#18181a"/><circle cx="150" cy="125" r="'+(50+Math.min(100,h/1000/36000*160+10))+'" fill="none" stroke="#c9c2b0" stroke-dasharray="5 4"/>'+svgText(380,90,"SR: "+fmt(sr*1e6,1)+" "+U("мкс/сут","µs/day"),"#b6533f","start",15)+svgText(380,125,"GR: "+(gr>=0?"+":"")+fmt(gr*1e6,1)+" "+U("мкс/сут","µs/day"),"#2f6f5d","start",15)+svgText(380,165,U("итог: ","net: ")+(net>=0?"+":"")+fmt(net*1e6,1)+" "+U("мкс/сут","µs/day"),"#18181a","start",17);
 $("gpSvg").innerHTML=g;$("ghOut").textContent=num(h/1000)+" "+U("км","km");
 $("gV").textContent=fmt(v/1000,2)+" "+U("км/с","km/s");$("gS").textContent=fmt(sr*1e6,1)+" "+U("мкс","µs");$("gG").textContent="+"+fmt(gr*1e6,1)+" "+U("мкс","µs");$("gN").textContent=(net>=0?"+":"")+fmt(net*1e6,1)+" "+U("мкс/сутки","µs/day");$("gE").textContent=fmt(err/1000,1)+" "+U("км в сутки","km per day");$("gpFb").textContent=t.gpFb}
$("gh").addEventListener("input",drawGp);
function drawVa(){const t=tt(),u=+$("vu").value,v=+$("vv").value,cl=u+v,re=(u+v)/(1+u*v);
 let g='<rect x="40" y="120" width="'+(500)+'" height="4" fill="#c9c2b0"/><circle cx="'+(40+Math.min(1,cl/2)*500)+'" cy="122" r="9" fill="#b6533f"/><circle cx="'+(40+re*500/2)+'" cy="122" r="9" fill="#2f6f5d"/><line x1="'+(40+250)+'" y1="100" x2="'+(40+250)+'" y2="145" stroke="#18181a" stroke-dasharray="4 3"/>'+svgText(290,90,"c","#18181a","start",13)+svgText(40,185,U("красная — по обычной арифметике; зелёная — по теории относительности","red — ordinary arithmetic; green — relativity"),"#66666b","start",11);
 $("vaSvg").innerHTML=g;$("vuOut").textContent=fmt(u,2)+" c";$("vvOut").textContent=fmt(v,2)+" c";
 $("vC").textContent=fmt(cl,3)+" c";$("vR").textContent=fmt(re,4)+" c";$("vG").textContent=fmt(cl-re,4)+" c";$("vaFb").textContent=t.vaFb}
["vu","vv"].forEach(id=>$(id).addEventListener("input",drawVa));
const LAB={ru:{tdSvg:T.ru.tdLabel,gpSvg:T.ru.gpLabel,vaSvg:T.ru.vaLabel},en:{tdSvg:T.en.tdLabel,gpSvg:T.en.gpLabel,vaSvg:T.en.vaLabel}};
function drawAll(){drawTd();drawGp();drawVa()}
'''

c = dict(n='49', slug='49-relativity.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Относительность', 'Relativity'),
 desc='Глава 49 Атласа физики: постулаты специальной теории относительности, замедление времени, сжатие длины, сложение скоростей, поправки для часов GPS.',
 lead=('Скорость света — предел, а время зависит от движения. Лоренц-фактор, сложение скоростей и поправка, без которой навигатор врал бы на километры.',
       'The speed of light is a limit and time depends on motion. The Lorentz factor, addition of velocities and the correction without which a navigator would be wrong by kilometres.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('sr', 'Теория относительности', 'Relativity'), ('gps', 'GPS', 'GPS'), ('velocity', 'Сложение скоростей', 'Adding velocities'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Спутники навигации несут сверхточные атомные часы. Инженеры знают, что часы на спутнике нужно «подкрутить» заранее — иначе их показания расходятся с земными на десятки микросекунд в сутки. Микросекунда — одна миллионная секунды, ничтожное время. Но стоит оставить часы без поправки — и навигатор в телефоне через сутки ошибётся на километры.</p><p>Почему крошечная разница во времени даёт большую ошибку и откуда она берётся?</p>',
         '<p>Navigation satellites carry ultra-precise atomic clocks. Engineers know the clocks on a satellite must be “adjusted” in advance — otherwise their readings diverge from the Earth’s by tens of microseconds a day. A microsecond is one millionth of a second, a negligible time. But leave the clock without a correction and the navigator in a phone will be wrong by kilometres a day later.</p><p>Why does a tiny time difference give a large error and where does it come from?</p>'),
 hint=stdhint('Поправка для часов GPS', 'The correction for GPS clocks'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: радиосигнал — 300 000 км в секунду', 'The answer: a radio signal covers 300,000 km a second'),
 answer=('<p>Навигатор определяет расстояние до спутника по времени прохождения радиосигнала, а он идёт со скоростью света: за микросекунду — 300 метров. Ошибка часов в 38 мкс даёт ошибку расстояния <em>c·Δt ≈ 11 км</em> (задача 6).</p><p>Сами 38 мкс складываются из двух эффектов теории относительности: из-за скорости спутника его часы идут медленнее (−7 мкс в сутки), а из-за более слабого тяготения на высоте — быстрее (+46 мкс в сутки). Теория относительности — не абстракция: GPS каждый день проверяет её на практике.</p>',
         '<p>A navigator finds the distance to a satellite from the travel time of a radio signal and that travels at the speed of light: 300 metres in a microsecond. A clock error of 38 µs gives a distance error <em>c·Δt ≈ 11 km</em> (problem 6).</p><p>The 38 µs itself comes from two effects of relativity: due to the satellite’s speed its clock runs slower (−7 µs per day) and due to the weaker gravity at height it runs faster (+46 µs per day). Relativity is not an abstraction: GPS tests it in practice every day.</p>'),
 sources=[
  ('Специальная теория относительности, замедление времени, сложение скоростей —', 'Special relativity, time dilation, addition of velocities —', LINK('https://openstax.org/books/university-physics-volume-3/pages/5-introduction', 'OpenStax University Physics, Vol. 3, гл. 5') + ', ' + LINK('https://en.wikipedia.org/wiki/Special_relativity', 'Wikipedia: Special relativity')),
  ('Релятивистские поправки GPS (около −7 и +46 мкс в сутки; итог ≈ +38 мкс) —', 'Relativistic corrections in GPS (about −7 and +46 µs per day; net ≈ +38 µs) —', LINK('https://en.wikipedia.org/wiki/Error_analysis_for_the_Global_Positioning_System', 'Wikipedia: Error analysis for the GPS') + ', ' + LINK('https://www.livingreviews.org/lrr-2003-1', 'N. Ashby, Relativity in the Global Positioning System, Living Reviews in Relativity'))],
 note=stdnote('Модель GPS учитывает только скорость и высоту спутника по круговой орбите; вращение Земли и эллиптичность орбиты не учтены. Высота 20 200 км — типичное значение для спутников GPS.', 'The GPS model accounts only for the satellite’s speed and height on a circular orbit; the Earth’s rotation and the ellipticity of the orbit are ignored. A height of 20,200 km is typical for GPS satellites.'),
 prev=('48-electromagnetic-waves.html', 'Глава 48 · Электромагнитные волны', 'Chapter 48 · Electromagnetic waves'),
 next=('', 'Блок VIII пройден — программа физики 7–11 классов выполнена', 'Block VIII complete — the physics programme for grades 7–11 is done'),
 js=js)
build(c)
