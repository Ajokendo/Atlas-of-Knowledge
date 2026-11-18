# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ГОРКА: ЭНЕРГИЯ СОХРАНЯЕТСЯ', 'A SLIDE: ENERGY IS CONSERVED', 'enSvg', '0 0 600 250',
  slider('eh', 'Высота горки', 'Height of the slide', 1, 20, 0.5, 5) + slider('el', 'Потери на трение', 'Loss to friction', 0, 50, 1, 0) + slider('em', 'Масса тела', 'Mass of the body', 1, 100, 1, 40),
  stats([('eE', 'Потенциальная энергия наверху m·g·h', 'Potential energy at the top m·g·h'), ('eV', 'Скорость внизу', 'Speed at the bottom'), ('eK', 'Кинетическая энергия внизу', 'Kinetic energy at the bottom')]),
  'enFb', 'Схема условная: тело скользит с покоя; доля потерь на трение — условная; g = 9,8 Н/кг.',
  'A schematic drawing: the body slides from rest; the share lost to friction is assumed; g = 9.8 N/kg.')
s1 = section('energy', 'Закон сохранения энергии', 'The law of conservation of energy',
 bd('<p>В замкнутой системе полная энергия не возникает и не исчезает, а переходит из одного вида в другой. Без трения сумма кинетической и потенциальной энергии постоянна: <em>m·g·h = m·v²/2</em>, откуда скорость внизу горки <em>v = √(2·g·h)</em> и не зависит ни от массы, ни от формы горки. Если часть энергии уходит на трение, она превращается в тепло.</p>',
    '<p>In a closed system total energy is neither created nor destroyed — it changes from one form to another. Without friction the sum of kinetic and potential energy is constant: <em>m·g·h = m·v²/2</em> so the speed at the bottom of the slide is <em>v = √(2·g·h)</em> and depends neither on the mass nor on the shape of the slide. If part of the energy goes into friction it becomes heat.</p>')
 + formula('E = E_к + E_п = const', 'v = √(2gh); с потерями v = √(2gh·(1 − k))', 'v = √(2gh); with losses v = √(2gh·(1 − k))'),
 lab1)

lab2 = model(2, 'БАЛЛИСТИЧЕСКИЙ МАЯТНИК', 'THE BALLISTIC PENDULUM', 'bpSvg', '0 0 600 250',
  slider('bm', 'Масса пули', 'Mass of the bullet', 5, 50, 1, 10) + slider('bM', 'Масса блока', 'Mass of the block', 1, 5, 0.1, 2) + slider('bv', 'Скорость пули', 'Speed of the bullet', 100, 500, 10, 200),
  stats([('bV', 'Скорость блока с пулей сразу после удара', 'Speed of block and bullet just after the impact'), ('bH', 'Высота подъёма', 'Height of the rise'), ('bL', 'Доля потерянной механической энергии', 'Share of mechanical energy lost')]),
  'bpFb', 'Схема условная: пуля застревает в блоке (удар неупругий), нить лёгкая; g = 9,8 Н/кг.',
  'A schematic drawing: the bullet lodges in the block (an inelastic impact), the string is light; g = 9.8 N/kg.')
s2 = section('pendulum', 'Импульс и энергия вместе', 'Momentum and energy together',
 bd('<p>Баллистический маятник измеряет скорость пули. В момент удара сохраняется <em>импульс</em> (энергия — нет: большая её часть уходит на нагрев и деформацию): <em>m·v = (m + M)·V</em>. После удара блок с пулей поднимается, и <em>энергия</em> сохраняется: <em>(m + M)·V²/2 = (m + M)·g·h</em>. Измерив высоту <em>h</em>, находят <em>V</em>, а затем скорость пули <em>v = (m + M)/m · √(2gh)</em>.</p>',
    '<p>The ballistic pendulum measures the speed of a bullet. At the impact <em>momentum</em> is conserved (energy is not: most of it goes into heat and deformation): <em>m·v = (m + M)·V</em>. After the impact the block with the bullet rises and <em>energy</em> is conserved: <em>(m + M)·V²/2 = (m + M)·g·h</em>. Measuring the height <em>h</em> gives <em>V</em> and then the speed of the bullet <em>v = (m + M)/m · √(2gh)</em>.</p>')
 + formula('m·v = (m + M)·V,   V²/2 = g·h', 'импульс — для удара, энергия — для подъёма', 'momentum for the impact, energy for the rise'),
 lab2)

lab3 = model(3, 'ЭЛЛИПТИЧЕСКАЯ ОРБИТА', 'AN ELLIPTICAL ORBIT', 'elSvg', '0 0 600 250',
  slider('lp', 'Расстояние в перигее', 'Perigee distance', 6800, 12000, 100, 7000) + slider('la', 'Расстояние в апогее', 'Apogee distance', 7000, 30000, 100, 14000) + slider('lv', 'Скорость в перигее', 'Speed at perigee', 5, 10, 0.1, 8),
  stats([('lA', 'Скорость в апогее v_p·r_p/r_a', 'Speed at apogee v_p·r_p/r_a'), ('lS', 'Площадь, заметаемая в секунду', 'Area swept per second'), ('lR', 'Во сколько раз медленнее в апогее', 'How many times slower at apogee')]),
  'elFb', 'Схема условная: расстояния от центра Земли, масштаб сжат; скорость в перигее — условная.',
  'A schematic drawing: distances from the Earth’s centre, the scale compressed; the perigee speed is assumed.')
s3 = section('kepler', 'Момент импульса и законы Кеплера', 'Angular momentum and Kepler’s laws',
 bd('<p>Сила тяготения направлена к центру, её момент равен нулю, поэтому <strong>момент импульса</strong> спутника <em>m·v·r</em> (в перигее и апогее) сохраняется: <em>v_p·r_p = v_a·r_a</em>. В дальней точке орбиты спутник движется медленнее, в ближней — быстрее. Это и есть второй закон Кеплера: радиус-вектор планеты за равные времена заметает равные площади (площадь в секунду <em>= ½·v·r</em>).</p>',
    '<p>Gravity points to the centre so its torque is zero and the <strong>angular momentum</strong> of the satellite <em>m·v·r</em> (at perigee and apogee) is conserved: <em>v_p·r_p = v_a·r_a</em>. At the far point of the orbit the satellite moves slower, at the near point faster. That is Kepler’s second law: the radius vector of a planet sweeps out equal areas in equal times (area per second <em>= ½·v·r</em>).</p>')
 + formula('v_p · r_p = v_a · r_a', 'то же — в любой точке орбиты: v·r·sin α = const', 'the same at any point of the orbit: v·r·sin α = const'),
 lab3)

tasks = [
 task(1, 'Скорость внизу горки', 'Speed at the bottom of a slide', 'Тело скользит без трения с высоты 5 м. Найдите скорость внизу. Затем — если 20% энергии уходит на трение.', 'A body slides without friction from a height of 5 m. Find the speed at the bottom. Then — if 20% of the energy goes to friction.',
  'h = 5 м, k = 0,2', 'h = 5 m, k = 0.2', 'v = √(2gh) = √(2 · 9,8 · 5) = √98 ≈ 9,9 м/с.<br>С потерями: v = √(98 · 0,8) = √78,4 ≈ 8,85 м/с.', 'v = √(2gh) = √(2 · 9.8 · 5) = √98 ≈ 9.9 m/s.<br>With losses: v = √(98 · 0.8) = √78.4 ≈ 8.85 m/s.', '9,9 м/с и 8,85 м/с.', '9.9 m/s and 8.85 m/s.', True),
 task(2, 'Мяч вверх', 'A ball thrown up', 'Мяч брошен вверх со скоростью 20 м/с. На какую высоту он поднимется? (g = 9,8, без сопротивления).', 'A ball is thrown up at 20 m/s. How high will it rise? (g = 9.8, no drag).',
  'v₀ = 20 м/с', 'v₀ = 20 m/s', 'm·v₀²/2 = m·g·h, h = v₀² / (2g) = 400 / 19,6 ≈ 20,4 м.', 'm·v₀²/2 = m·g·h, h = v₀² / (2g) = 400 / 19.6 ≈ 20.4 m.', '≈ 20,4 м.', '≈ 20.4 m.'),
 task(3, 'Скорость пули', 'The speed of a bullet', 'Пуля массой 10 г застряла в блоке массой 2 кг, подвешенном на нити, и блок поднялся на 5 см. Найдите скорость пули.', 'A bullet of 10 g lodged in a block of 2 kg hanging on a string and the block rose 5 cm. Find the speed of the bullet.',
  'm = 0,01 кг, M = 2 кг, h = 0,05 м', 'm = 0.01 kg, M = 2 kg, h = 0.05 m', 'V = √(2gh) = √(2 · 9,8 · 0,05) = √0,98 ≈ 0,99 м/с.<br>v = (m + M)/m · V = 2,01 / 0,01 · 0,99 ≈ 199 м/с.', 'V = √(2gh) = √(2 · 9.8 · 0.05) = √0.98 ≈ 0.99 m/s.<br>v = (m + M)/m · V = 2.01 / 0.01 · 0.99 ≈ 199 m/s.', '≈ 200 м/с.', '≈ 200 m/s.'),
 task(4, 'Потери энергии при ударе', 'Energy lost in the impact', 'Сколько процентов механической энергии потеряно при ударе пули в задаче 3?', 'What percentage of mechanical energy was lost in the impact in problem 3?',
  'v = 199 м/с, V = 0,99 м/с', 'v = 199 m/s, V = 0.99 m/s', 'До: E₁ = ½ · 0,01 · 199² ≈ 198 Дж.<br>После: E₂ = ½ · 2,01 · 0,99² ≈ 0,99 Дж.<br>Потеряно: (198 − 0,99) / 198 ≈ 99,5%.', 'Before: E₁ = ½ · 0.01 · 199² ≈ 198 J.<br>After: E₂ = ½ · 2.01 · 0.99² ≈ 0.99 J.<br>Lost: (198 − 0.99) / 198 ≈ 99.5%.', '≈ 99,5% ушло на тепло и деформацию.', '≈ 99.5% went into heat and deformation.'),
 task(5, 'Скорость в апогее', 'Speed at apogee', 'Спутник в перигее на расстоянии 7000 км от центра Земли летит со скоростью 8 км/с. Какова скорость в апогее на расстоянии 14 000 км?', 'A satellite at perigee, 7,000 km from the Earth’s centre, flies at 8 km/s. What is its speed at apogee at 14,000 km?',
  'r_p = 7000 км, v_p = 8 км/с, r_a = 14 000 км', 'r_p = 7,000 km, v_p = 8 km/s, r_a = 14,000 km', 'v_p·r_p = v_a·r_a, v_a = 8 · 7000 / 14 000 = 4 км/с.', 'v_p·r_p = v_a·r_a, v_a = 8 · 7,000 / 14,000 = 4 km/s.', '4 км/с — вдвое медленнее.', '4 km/s — half as fast.'),
 task(6, 'Закон Кеплера', 'Kepler’s law', 'Найдите площадь, которую радиус-вектор спутника из задачи 5 заметает за секунду в перигее и в апогее.', 'Find the area swept by the radius vector of the satellite in problem 5 in one second at perigee and at apogee.',
  'v_p·r_p, v_a·r_a', 'v_p·r_p, v_a·r_a', 'В перигее: ½ · 8 · 7000 = 28 000 км²/с.<br>В апогее: ½ · 4 · 14 000 = 28 000 км²/с.', 'At perigee: ½ · 8 · 7,000 = 28,000 km²/s.<br>At apogee: ½ · 4 · 14,000 = 28,000 km²/s.', 'одинаково — 28 000 км²/с.', 'the same — 28,000 km²/s.'),
]

quiz = [
 qz('Что утверждает закон сохранения энергии?', 'Энергия переходит из вида в вид, не пропадая', 'Энергия всегда уменьшается', 'Энергия исчезает при трении', 'При трении механическая энергия становится теплом.',
    'What does the law of conservation of energy state?', 'Energy changes form without disappearing', 'Energy always decreases', 'Energy vanishes in friction', 'In friction mechanical energy becomes heat.'),
 qz('От чего не зависит скорость внизу горки без трения?', 'От массы тела', 'От высоты горки', 'От g', 'v = √(2gh): масса сокращается.',
    'What does the speed at the bottom of a frictionless slide not depend on?', 'The mass of the body', 'The height of the slide', 'g', 'v = √(2gh): the mass cancels.'),
 qz('Во сколько раз вырастет скорость внизу горки при увеличении высоты в 4 раза?', 'В 2 раза', 'В 4 раза', 'В 16 раз', 'v ~ √h.',
    'How many times does the speed at the bottom grow when the height is 4 times greater?', '2 times', '4 times', '16 times', 'v ~ √h.'),
 qz('Что сохраняется при неупругом ударе пули в блок?', 'Импульс', 'Механическая энергия', 'Ничего', 'Энергия частично переходит в тепло.',
    'What is conserved in the inelastic impact of a bullet into a block?', 'Momentum', 'Mechanical energy', 'Nothing', 'Energy partly turns into heat.'),
 qz('Что сохраняется при подъёме блока с пулей после удара?', 'Механическая энергия', 'Импульс блока', 'Скорость', 'Сила натяжения нити меняет импульс.',
    'What is conserved while the block with the bullet rises after the impact?', 'Mechanical energy', 'The momentum of the block', 'The speed', 'The string tension changes the momentum.'),
 qz('Почему спутник в апогее движется медленнее, чем в перигее?', 'Сохраняется момент импульса v·r', 'Там нет тяготения', 'Спутник тормозит об воздух', 'v·r постоянно, значит больше r — меньше v.',
    'Why does a satellite move slower at apogee than at perigee?', 'The angular momentum v·r is conserved', 'There is no gravity there', 'The satellite brakes in the air', 'v·r is constant so greater r means smaller v.'),
 qz('О чём говорит второй закон Кеплера?', 'Радиус-вектор за равные времена заметает равные площади', 'Все орбиты — окружности', 'Период не зависит от орбиты', 'Площадь в секунду ½·v·r постоянна.',
    'What does Kepler’s second law state?', 'The radius vector sweeps equal areas in equal times', 'All orbits are circles', 'The period does not depend on the orbit', 'The area per second ½·v·r is constant.'),
 qz('Мяч брошен вверх со скоростью 20 м/с. Примерная высота подъёма (g = 9,8)?', '20 м', '2 м', '200 м', 'h = v²/(2g) ≈ 20,4 м.',
    'A ball is thrown up at 20 m/s. The approximate height (g = 9.8)?', '20 m', '2 m', '200 m', 'h = v²/(2g) ≈ 20.4 m.'),
]

js = r'''
const T={ru:{
 enLabel:"Тело скользит с горки",bpLabel:"Пуля попадает в подвешенный блок",elLabel:"Эллиптическая орбита вокруг Земли",
 enFb:"Чем выше горка, тем больше скорость внизу; трение превращает часть энергии в тепло.",bpFb:"Почти вся энергия пули уходит на тепло, но импульс сохраняется.",elFb:"Ближе к Земле — быстрее, дальше — медленнее; площадь за секунду постоянна.",
 perigee:"перигей",apogee:"апогей"},
 en:{
 enLabel:"A body slides down a slide",bpLabel:"A bullet hits a hanging block",elLabel:"An elliptical orbit around the Earth",
 enFb:"The higher the slide the greater the speed at the bottom; friction turns some energy into heat.",bpFb:"Almost all the bullet’s energy turns to heat but momentum is conserved.",elFb:"Closer to the Earth — faster, farther — slower; the area per second is constant.",
 perigee:"perigee",apogee:"apogee"}};
function drawEn(){const t=tt(),h=+$("eh").value,k=+$("el").value/100,m=+$("em").value,E=m*9.8*h,Ek=E*(1-k),v=Math.sqrt(2*Ek/m);
 const H=40+h/20*140;let g='<path d="M60 '+(220-H)+' Q 160 220 260 220 L 560 220" fill="none" stroke="#18181a" stroke-width="3"/><circle cx="68" cy="'+(212-H)+'" r="9" fill="#b87333"/>'+svgText(100,'30',"h = "+fmt(h,1)+UN[lang].m,"#66666b","start",12)+arrow(400,200,400+Math.min(150,v*9),200,"#2f6f5d",3)+svgText(400,190,"v = "+fmt(v,1)+UN[lang].ms,"#18181a","start",13);
 $("enSvg").innerHTML=g;
 $("ehOut").textContent=fmt(h,1)+UN[lang].m;$("elOut").textContent=Math.round(k*100)+"%";$("emOut").textContent=m+UN[lang].kg;
 $("eE").textContent=fmt(E/1000,2)+UN[lang].kJ;$("eV").textContent=fmt(v,1)+UN[lang].ms+" ("+fmt(v*3.6,0)+(lang==="ru"?" км/ч":" km/h")+")";$("eK").textContent=fmt(Ek/1000,2)+UN[lang].kJ;$("enFb").textContent=t.enFb}
["eh","el","em"].forEach(id=>$(id).addEventListener("input",drawEn));
function drawBp(){const t=tt(),m=+$("bm").value/1000,M=+$("bM").value,v=+$("bv").value,V=m*v/(m+M),h=V*V/(2*9.8),loss=M/(m+M);
 const dx=Math.min(120,h*600);let g='<line x1="200" y1="30" x2="400" y2="30" stroke="#18181a" stroke-width="4"/><line x1="300" y1="30" x2="'+(300+dx)+'" y2="'+(150-Math.min(40,h*100))+'" stroke="#66666b"/><rect x="'+(300+dx-20)+'" y="'+(150-Math.min(40,h*100))+'" width="40" height="30" fill="#b87333" stroke="#18181a"/>'+arrow(60,165,60+Math.min(110,v/4),165,"#b6533f",3)+svgText(60,190,"v = "+v+UN[lang].ms,"#18181a","start",12)+svgText(420,210,"h = "+fmt(h*100,1)+(lang==="ru"?" см":" cm"),"#18181a","start",13);
 $("bpSvg").innerHTML=g;
 $("bmOut").textContent=fmt(m*1000,0)+UN[lang].g;$("bMOut").textContent=fmt(M,1)+UN[lang].kg;$("bvOut").textContent=v+UN[lang].ms;
 $("bV").textContent=fmt(V,2)+UN[lang].ms;$("bH").textContent=fmt(h*100,1)+(lang==="ru"?" см":" cm");$("bL").textContent=fmt(loss*100,1)+"%";$("bpFb").textContent=t.bpFb}
["bm","bM","bv"].forEach(id=>$(id).addEventListener("input",drawBp));
function drawEl(){const t=tt(),rp=+$("lp").value,ra=Math.max(+$("la").value,rp),vp=+$("lv").value,va=vp*rp/ra,S=vp*rp/2,s=200/30000,cx=330,a=(rp+ra)/2,b=Math.sqrt(rp*ra);
 let g='<ellipse cx="'+(cx-(ra-rp)/2*s)+'" cy="125" rx="'+(a*s)+'" ry="'+(b*s)+'" fill="none" stroke="#c9c2b0" stroke-dasharray="5 4" stroke-width="2"/><circle cx="'+cx+'" cy="125" r="'+(6371*s)+'" fill="#3f5f8f" stroke="#18181a"/><circle cx="'+(cx+rp*s)+'" cy="125" r="6" fill="#b6533f"/><circle cx="'+(cx-ra*s)+'" cy="125" r="6" fill="#b6533f"/>'+arrow(cx+rp*s,125,cx+rp*s,125-Math.min(70,vp*8),"#2f6f5d",3)+arrow(cx-ra*s,125,cx-ra*s,125-Math.min(70,va*8),"#2f6f5d",3)+svgText(cx+rp*s+8,120,t.perigee,"#66666b","start",11)+svgText(cx-ra*s,150,t.apogee,"#66666b","middle",11);
 $("elSvg").innerHTML=g;
 $("lpOut").textContent=num(rp)+UN[lang].km;$("laOut").textContent=num(ra)+UN[lang].km;$("lvOut").textContent=fmt(vp,1)+(lang==="ru"?" км/с":" km/s");
 $("lA").textContent=fmt(va,2)+(lang==="ru"?" км/с":" km/s");$("lS").textContent=num(Math.round(S))+(lang==="ru"?" км²/с":" km²/s");$("lR").textContent=fmt(vp/va,2)+"×";$("elFb").textContent=t.elFb}
["lp","la","lv"].forEach(id=>$(id).addEventListener("input",drawEl));
const LAB={ru:{enSvg:T.ru.enLabel,bpSvg:T.ru.bpLabel,elSvg:T.ru.elLabel},en:{enSvg:T.en.enLabel,bpSvg:T.en.bpLabel,elSvg:T.en.elLabel}};
function drawAll(){drawEn();drawBp();drawEl()}
'''

c = dict(n='37', slug='37-conservation-laws.html', block='VI', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Законы сохранения', 'Conservation laws'),
 desc='Глава 37 Атласа физики: сохранение энергии, импульса и момента импульса вместе — горка, баллистический маятник, эллиптическая орбита и законы Кеплера.',
 lead=('Энергия, импульс и момент импульса не пропадают. Три закона сохранения решают задачи, где сами силы неизвестны.',
       'Energy, momentum and angular momentum do not vanish. Three conservation laws solve problems where the forces themselves are unknown.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('energy', 'Энергия', 'Energy'), ('pendulum', 'Маятник', 'Pendulum'), ('kepler', 'Орбита', 'Orbit'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Пуля массой 10 г летит так быстро, что пробивает доску, а подвешенный тяжёлый блок в 2 кг, в который она попала и застряла, только качнулся на 5 см. Как по такому слабому качанию узнать, с какой скоростью летела пуля, если силы удара никто не измерял?</p><p>Что помогает найти скорость, не зная сил?</p>',
         '<p>A 10 g bullet flies so fast that it pierces a plank, yet a heavy 2 kg block hanging on a string, in which it lodged, only swung 5 cm. How can such a feeble swing tell the speed of the bullet if nobody measured the force of the impact?</p><p>What helps find the speed without knowing the forces?</p>'),
 hint=stdhint('Баллистический маятник', 'The ballistic pendulum'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: два закона сохранения подряд', 'The answer: two conservation laws in a row'),
 answer=('<p>Удар короткий, и сохраняется импульс: <em>m·v = (m + M)·V</em>. Подъём блока — плавный, и сохраняется энергия: <em>V = √(2gh)</em>. Из высоты 5 см получаем <em>V ≈ 0,99 м/с</em>, а затем <em>v ≈ 199 м/с</em>. Силы внутри удара знать не нужно — это главное достоинство законов сохранения.</p><p>Почти вся энергия пули (около 99,5%) в таком ударе уходит на нагрев и деформацию, поэтому «слабое» качание не противоречит большой скорости.</p>',
         '<p>The impact is brief and momentum is conserved: <em>m·v = (m + M)·V</em>. The rise of the block is smooth and energy is conserved: <em>V = √(2gh)</em>. From a height of 5 cm we get <em>V ≈ 0.99 m/s</em> and then <em>v ≈ 199 m/s</em>. We do not need to know the forces inside the impact — that is the main virtue of conservation laws.</p><p>Almost all the bullet’s energy (about 99.5%) goes into heat and deformation in such an impact so the “weak” swing does not contradict the high speed.</p>'),
 sources=[
  ('Сохранение энергии, импульса и момента импульса —', 'Conservation of energy, momentum and angular momentum —', LINK('https://openstax.org/books/university-physics-volume-1/pages/8-introduction', 'OpenStax University Physics, Vol. 1, гл. 8') + ', ' + LINK('https://openstax.org/books/university-physics-volume-1/pages/9-introduction', 'гл. 9') + ', ' + LINK('https://openstax.org/books/university-physics-volume-1/pages/11-introduction', 'гл. 11')),
  ('Законы Кеплера и баллистический маятник —', 'Kepler’s laws and the ballistic pendulum —', LINK('https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion', 'Wikipedia: Kepler’s laws') + ', ' + LINK('https://en.wikipedia.org/wiki/Ballistic_pendulum', 'Wikipedia: Ballistic pendulum'))],
 note=stdnote('Скорости, массы и расстояния в моделях — условные.', 'The speeds, masses and distances in the models are assumed.'),
 prev=('36-gravity-satellites.html', 'Глава 36 · Гравитация и спутники', 'Chapter 36 · Gravity and satellites'),
 next=('38-photons-photoelectric.html', 'Глава 38 · Фотоны и фотоэффект', 'Chapter 38 · Photons and the photoelectric effect'),
 js=js)
build(c)
