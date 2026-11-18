# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'МОМЕНТ СИЛЫ: КЛЮЧ И ГАЙКА', 'TORQUE: A WRENCH AND A NUT', 'tqSvg', '0 0 600 250',
  slider('tf', 'Сила на ключе', 'Force on the wrench', 10, 300, 5, 80) + slider('tr', 'Длина ключа (плечо)', 'Wrench length (arm)', 0.05, 0.6, 0.01, 0.25) + slider('ta', 'Угол между силой и ключом', 'Angle between the force and the wrench', 10, 90, 5, 90),
  stats([('tM', 'Момент силы M = F·r·sin θ', 'Torque M = F·r·sin θ'), ('tE', 'Во сколько раз больше, чем у ключа вдвое короче', 'How many times more than with a wrench half as long')]),
  'tqFb', 'Схема условная: ось вращения — центр гайки; сила приложена к концу ключа.',
  'A schematic drawing: the axis of rotation is the centre of the nut; the force is applied at the end of the wrench.')
s1 = section('torque', 'Момент силы', 'Torque',
 bd('<p>Сила может вращать тело вокруг оси. Вращательное действие зависит и от силы, и от того, как далеко от оси и под каким углом она приложена. <strong>Момент силы</strong> — произведение силы на плечо — кратчайшее расстояние от оси до линии действия силы (единица — Н·м):</p>',
    '<p>A force can turn a body about an axis. The turning effect depends both on the force and on how far from the axis and at what angle it is applied. The <strong>torque</strong> is the force times the arm — the shortest distance from the axis to the line of action of the force (unit — N·m):</p>')
 + formula('M = F · d = F · r · sin θ', 'тело не вращается, если суммы моментов по часовой и против часовой стрелки равны (правило моментов)', 'a body does not rotate if the sums of the torques clockwise and anticlockwise are equal (the rule of moments)')
 + bd('<p>Правило моментов — обобщение рычага (глава 6): груз 30 кг на расстоянии 2 м уравновесит груз 40 кг на расстоянии 1,5 м, потому что 30·2 = 40·1,5. Длинный ключ даёт большой момент при той же силе руки.</p>',
      '<p>The rule of moments generalises the lever (chapter 6): a 30 kg load at 2 m balances a 40 kg load at 1.5 m because 30·2 = 40·1.5. A long wrench gives a large torque for the same force of the hand.</p>'),
 lab1)

lab2 = model(2, 'ПОВОРОТ НА ДОРОГЕ', 'A BEND IN THE ROAD', 'cvSvg', '0 0 600 250',
  slider('cr', 'Радиус поворота', 'Radius of the bend', 10, 200, 5, 50) + select('cu', 'Дорога', 'Road') + slider('cv', 'Скорость автомобиля', 'Speed of the car', 5, 40, 1, 15),
  stats([('cA', 'Центростремительное ускорение v²/r', 'Centripetal acceleration v²/r'), ('cM', 'Наибольшая безопасная скорость √(μgr)', 'The greatest safe speed √(μgr)'), ('cS', 'Состояние', 'Status')]),
  'cvFb', 'Схема условная: ровная дорога; μ — коэффициент трения шин о дорогу (сухая 0,7; мокрая 0,4; лёд 0,1 — условные); g = 9,8 Н/кг.',
  'A schematic drawing: a level road; μ is the friction coefficient of the tyres on the road (dry 0.7; wet 0.4; ice 0.1 — assumed); g = 9.8 N/kg.')
s2 = section('circle', 'Движение по окружности', 'Motion along a circle',
 bd('<p>Вращение описывают <strong>угловой скоростью</strong> <em>ω = 2π·f</em> (рад/с; f — число оборотов в секунду). Линейная скорость точки на расстоянии <em>r</em> от оси <em>v = ω·r</em>. Скорость при вращении всё время меняет направление, поэтому у тела есть ускорение, направленное к центру, — <strong>центростремительное</strong>:</p>',
    '<p>Rotation is described by the <strong>angular velocity</strong> <em>ω = 2π·f</em> (rad/s; f is the number of revolutions per second). The linear speed of a point at distance <em>r</em> from the axis is <em>v = ω·r</em>. In rotation the velocity constantly changes direction so the body has an acceleration pointing toward the centre — the <strong>centripetal</strong> acceleration:</p>')
 + formula('a = v² / r = ω² · r', 'по второму закону Ньютона для этого нужна сила, направленная к центру', 'by Newton’s second law this needs a force pointing toward the centre')
 + bd('<p>На повороте такой силой служит сила трения шин. Максимум трения <em>μ·m·g</em>, поэтому <em>m·v²/r ≤ μ·m·g</em>, то есть <em>v ≤ √(μ·g·r)</em>. Масса сокращается: скорость на повороте зависит от радиуса и дороги, а не от тяжести машины. На мокрой дороге или льду безопасная скорость резко падает.</p>',
      '<p>In a bend this force is the friction of the tyres. The maximum friction is <em>μ·m·g</em> so <em>m·v²/r ≤ μ·m·g</em>, that is <em>v ≤ √(μ·g·r)</em>. The mass cancels: the speed in a bend depends on the radius and the road, not on the weight of the car. On a wet road or ice the safe speed drops sharply.</p>'),
 lab2)

lab3 = model(3, 'ФИГУРИСТ И МОМЕНТ ИМПУЛЬСА', 'A SKATER AND ANGULAR MOMENTUM', 'skSvg', '0 0 600 250',
  slider('s1', 'Руки разведены на', 'Arms spread out to', 0.2, 0.9, 0.05, 0.8) + slider('s2', 'Руки прижаты на', 'Arms pulled in to', 0.1, 0.9, 0.05, 0.2) + slider('sw', 'Начальная частота вращения', 'Initial rotation rate', 0.5, 2, 0.1, 1),
  stats([('sI', 'Момент инерции до и после', 'Moment of inertia before and after'), ('sF', 'Частота вращения после', 'Rotation rate after')]),
  'skFb', 'Схема условная: момент инерции тела без рук 1 кг·м², в каждой руке сосредоточена масса 5 кг на расстоянии r от оси; трения нет.',
  'A schematic drawing: the body’s moment of inertia without the arms is 1 kg·m², each hand holds a mass of 5 kg at a distance r from the axis; no friction.')
s3 = section('angmom', 'Момент импульса', 'Angular momentum',
 bd('<p>Для вращения есть своя «масса» — <strong>момент инерции</strong> <em>I</em>: чем дальше от оси масса, тем труднее раскрутить тело (для материальной точки <em>I = m·r²</em>). Вращательный аналог второго закона — <em>M = I·ε</em>, где <em>ε</em> — угловое ускорение. А вращательный аналог импульса — <strong>момент импульса</strong> <em>L = I·ω</em>.</p><p>Если момент внешних сил равен нулю, <strong>момент импульса сохраняется</strong>: <em>I₁·ω₁ = I₂·ω₂</em>. Фигурист, прижав руки, уменьшает <em>I</em> — и вращается быстрее; разведя руки, замедляется.</p>',
    '<p>Rotation has its own “mass” — the <strong>moment of inertia</strong> <em>I</em>: the farther the mass from the axis the harder it is to spin the body (for a point mass <em>I = m·r²</em>). The rotational analogue of the second law is <em>M = I·ε</em> where <em>ε</em> is the angular acceleration. And the rotational analogue of momentum is the <strong>angular momentum</strong> <em>L = I·ω</em>.</p><p>If the torque of external forces is zero the <strong>angular momentum is conserved</strong>: <em>I₁·ω₁ = I₂·ω₂</em>. A skater pulling in the arms reduces <em>I</em> — and spins faster; spreading the arms slows the spin.</p>')
 + formula('L = I · ω = const', 'так же устойчиво вращаются колёса велосипеда, волчок и планеты', 'that is also why bicycle wheels, a top and planets spin so steadily'),
 lab3)

tasks = [
 task(1, 'Момент на ключе', 'Torque on a wrench', 'Длина ключа 0,25 м, сила 80 Н приложена перпендикулярно ключу. Найдите момент силы.', 'The wrench is 0.25 m long and a force of 80 N is applied perpendicular to it. Find the torque.',
  'r = 0,25 м, F = 80 Н', 'r = 0.25 m, F = 80 N', 'M = F·r = 80 · 0,25 = 20 Н·м.', 'M = F·r = 80 · 0.25 = 20 N·m.', '20 Н·м.', '20 N·m.', True),
 task(2, 'Под углом', 'At an angle', 'Та же сила действует под углом 30° к ключу. Каков момент?', 'The same force acts at 30° to the wrench. What is the torque?',
  'θ = 30°', 'θ = 30°', 'M = F·r·sin θ = 80 · 0,25 · 0,5 = 10 Н·м.', 'M = F·r·sin θ = 80 · 0.25 · 0.5 = 10 N·m.', '10 Н·м — вдвое меньше.', '10 N·m — half as much.'),
 task(3, 'Качели-балансир', 'A see-saw', 'Мальчик массой 30 кг сидит в 2 м от опоры. На каком расстоянии должен сесть мальчик массой 40 кг, чтобы доска уравновесилась?', 'A boy of 30 kg sits 2 m from the pivot. At what distance must a 40 kg boy sit to balance the plank?',
  'm₁ = 30 кг, d₁ = 2 м, m₂ = 40 кг', 'm₁ = 30 kg, d₁ = 2 m, m₂ = 40 kg', 'm₁·g·d₁ = m₂·g·d₂, d₂ = 30 · 2 / 40 = 1,5 м.', 'm₁·g·d₁ = m₂·g·d₂, d₂ = 30 · 2 / 40 = 1.5 m.', '1,5 м.', '1.5 m.'),
 task(4, 'Колесо', 'A wheel', 'Колесо делает 3 оборота в секунду, радиус 0,35 м. Найдите угловую скорость, линейную скорость обода и центростремительное ускорение.', 'A wheel makes 3 revolutions per second, radius 0.35 m. Find the angular velocity, the linear speed of the rim and the centripetal acceleration.',
  'f = 3 Гц, r = 0,35 м', 'f = 3 Hz, r = 0.35 m', 'ω = 2πf = 18,85 рад/с.<br>v = ωr = 18,85 · 0,35 ≈ 6,6 м/с.<br>a = ω²r = 355 · 0,35 ≈ 124 м/с².', 'ω = 2πf = 18.85 rad/s.<br>v = ωr = 18.85 · 0.35 ≈ 6.6 m/s.<br>a = ω²r = 355 · 0.35 ≈ 124 m/s².', '18,9 рад/с; 6,6 м/с; 124 м/с² (около 13 g).', '18.9 rad/s; 6.6 m/s; 124 m/s² (about 13 g).'),
 task(5, 'Скорость на повороте', 'Speed in a bend', 'Поворот радиусом 50 м. Найдите наибольшую скорость без заноса для μ = 0,7 (сухо) и μ = 0,4 (мокро). g = 9,8 Н/кг.', 'A bend of radius 50 m. Find the greatest speed without skidding for μ = 0.7 (dry) and μ = 0.4 (wet). g = 9.8 N/kg.',
  'r = 50 м, μ = 0,7 и 0,4', 'r = 50 m, μ = 0.7 and 0.4', 'v = √(μ·g·r).<br>Сухо: √(0,7 · 9,8 · 50) = √343 ≈ 18,5 м/с ≈ 67 км/ч.<br>Мокро: √(0,4 · 9,8 · 50) = √196 = 14 м/с ≈ 50 км/ч.', 'v = √(μ·g·r).<br>Dry: √(0.7 · 9.8 · 50) = √343 ≈ 18.5 m/s ≈ 67 km/h.<br>Wet: √(0.4 · 9.8 · 50) = √196 = 14 m/s ≈ 50 km/h.', '67 км/ч и 50 км/ч.', '67 km/h and 50 km/h.'),
 task(6, 'Фигурист', 'A skater', 'Фигурист вращается с частотой 1 об/с с раскинутыми руками, момент инерции 7,4 кг·м². Прижав руки, он уменьшает его до 1,4 кг·м². Найдите новую частоту.', 'A skater spins at 1 rev/s with arms outstretched, a moment of inertia of 7.4 kg·m². Pulling the arms in he reduces it to 1.4 kg·m². Find the new rate.',
  'I₁ = 7,4, I₂ = 1,4 кг·м², f₁ = 1 об/с', 'I₁ = 7.4, I₂ = 1.4 kg·m², f₁ = 1 rev/s', 'I₁·f₁ = I₂·f₂, f₂ = 7,4 · 1 / 1,4 ≈ 5,3 об/с.', 'I₁·f₁ = I₂·f₂, f₂ = 7.4 · 1 / 1.4 ≈ 5.3 rev/s.', 'около 5,3 об/с — в 5 раз быстрее.', 'about 5.3 rev/s — 5 times faster.'),
]

quiz = [
 qz('Что такое момент силы?', 'Произведение силы на плечо', 'Сила, делённая на время', 'Скорость вращения', 'M = F·d, плечо — расстояние от оси до линии действия силы.',
    'What is torque?', 'Force times the arm', 'Force divided by time', 'The rate of rotation', 'M = F·d, the arm is the distance from the axis to the line of action of the force.'),
 qz('Как легче открутить гайку?', 'Длинным ключом', 'Коротким ключом', 'Нажимая ближе к гайке', 'При той же силе момент тем больше, чем длиннее плечо.',
    'How is it easier to unscrew a nut?', 'With a long wrench', 'With a short wrench', 'By pushing closer to the nut', 'For the same force the torque grows with the arm.'),
 qz('При каком условии тело не вращается (правило моментов)?', 'Моменты по и против часовой стрелки равны', 'Силы направлены вверх', 'Масса равна нулю', 'Суммарный момент равен нулю.',
    'On what condition does a body not rotate (the rule of moments)?', 'The clockwise and anticlockwise torques are equal', 'The forces point upward', 'The mass is zero', 'The net torque is zero.'),
 qz('Куда направлено центростремительное ускорение?', 'К центру окружности', 'От центра', 'Вдоль скорости', 'Скорость меняет направление, ускорение направлено к центру.',
    'Where does the centripetal acceleration point?', 'Toward the centre of the circle', 'Away from the centre', 'Along the velocity', 'The velocity changes direction; the acceleration points to the centre.'),
 qz('Что удерживает автомобиль на повороте?', 'Сила трения шин о дорогу', 'Сила тяжести', 'Центробежная сила', 'Трение даёт силу, направленную к центру поворота.',
    'What holds a car in a bend?', 'The friction of the tyres on the road', 'Gravity', 'Centrifugal force', 'Friction gives a force pointing toward the centre of the bend.'),
 qz('Как изменится безопасная скорость на повороте на мокрой дороге?', 'Уменьшится', 'Увеличится', 'Не изменится', 'μ меньше — √(μgr) меньше.',
    'How does the safe speed in a bend change on a wet road?', 'It decreases', 'It increases', 'It does not change', 'A smaller μ gives a smaller √(μgr).'),
 qz('Что сохраняется у вращающегося фигуриста без трения?', 'Момент импульса', 'Только скорость', 'Масса рук', 'L = Iω не меняется, если нет внешнего момента.',
    'What is conserved for a spinning skater without friction?', 'The angular momentum', 'Only the speed', 'The mass of the arms', 'L = Iω does not change without an external torque.'),
 qz('Фигурист прижал руки к телу. Что произойдёт?', 'Вращение ускорится', 'Вращение замедлится', 'Вращение не изменится', 'I уменьшился, значит ω выросла, чтобы L = Iω сохранился.',
    'A skater pulls the arms to the body. What happens?', 'The spin speeds up', 'The spin slows down', 'The spin does not change', 'I decreased so ω grows to keep L = Iω.'),
]

js = r'''
const T={ru:{
 tqLabel:"Гаечный ключ, сила и плечо",cvLabel:"Автомобиль на повороте, вид сверху",skLabel:"Фигурист с разными положениями рук",
 road:["Сухая (μ = 0,7)","Мокрая (μ = 0,4)","Лёд (μ = 0,1)"],ok:"проходит поворот",skid:"занос!",
 tqFb:"Длинное плечо и перпендикулярная сила дают наибольший момент.",cvFb:"Скорость на повороте ограничена трением и радиусом.",skFb:"Прижали руки — вращение быстрее."},
 en:{
 tqLabel:"A wrench, force and arm",cvLabel:"A car in a bend, seen from above",skLabel:"A skater with different arm positions",
 road:["Dry (μ = 0.7)","Wet (μ = 0.4)","Ice (μ = 0.1)"],ok:"takes the bend",skid:"skid!",
 tqFb:"A long arm and a perpendicular force give the greatest torque.",cvFb:"Speed in a bend is limited by friction and radius.",skFb:"Arms pulled in — a faster spin."}};
const MR=[0.7,0.4,0.1];
function drawTq(){const t=tt(),F=+$("tf").value,r=+$("tr").value,th=+$("ta").value,A=th*Math.PI/180,M=F*r*Math.sin(A);
 const cx=120,cy=125,L=r*620,ex=cx+L,ey=cy;
 let g='<circle cx="'+cx+'" cy="'+cy+'" r="22" fill="#9a9a9a" stroke="#18181a" stroke-width="2"/><line x1="'+cx+'" y1="'+cy+'" x2="'+ex+'" y2="'+ey+'" stroke="#b87333" stroke-width="10"/>';
 const fl=Math.min(110,20+F*0.4),fx=ex+Math.cos(A)*fl*0.0,fy=ey;
 g+=arrow(ex,ey,ex+Math.sin(A)*0+Math.cos(Math.PI-A)*(-fl),ey-Math.sin(A)*fl,"#2f6f5d",3)+svgText(ex+8,ey-fl*Math.sin(A)-6,"F","#2f6f5d","start",13)+svgText((cx+ex)/2,cy+30,"r = "+fmt(r,2)+UN[lang].m,"#66666b","middle",11);
 $("tqSvg").innerHTML=g;
 $("tfOut").textContent=F+UN[lang].N;$("trOut").textContent=fmt(r,2)+UN[lang].m;$("taOut").textContent=th+"°";
 $("tM").textContent=fmt(M,1)+(lang==="ru"?" Н·м":" N·m");$("tE").textContent="2×";$("tqFb").textContent=t.tqFb}
["tf","tr","ta"].forEach(id=>$(id).addEventListener("input",drawTq));
function drawCv(){const t=tt(),r=+$("cr").value,mu=MR[+$("cu").value],v=+$("cv").value,a=v*v/r,vm=Math.sqrt(mu*9.8*r),skid=v>vm;
 const R=40+r/200*90;let g='<path d="M60 220 A '+R*2.4+' '+R*2.4+' 0 0 1 '+(60+R*2.4)+' '+(220-R*2.4)+'" fill="none" stroke="#c9c2b0" stroke-width="26"/>';
 const cx=60+R*2.4,cy=220;const ang=skid?-0.5:-0.8;const px=cx-Math.cos(0.8)*R*2.4,py=cy-Math.sin(0.8)*R*2.4;
 g+='<rect x="'+(px-14)+'" y="'+(py-8)+'" width="28" height="16" fill="'+(skid?"#b6533f":"#3f5f8f")+'" stroke="#18181a" transform="rotate(-35 '+px+' '+py+')"/>'+arrow(px,py,px+Math.min(60,a*3),py+Math.min(60,a*3)*0.6,"#2f6f5d",3)+svgText(px+Math.min(60,a*3)+4,py+Math.min(60,a*3)*0.6,"a","#2f6f5d","start",12);
 if(skid)g+=arrow(px,py,px+50,py-40,"#b6533f",2);
 $("cvSvg").innerHTML=g;
 $("crOut").textContent=r+UN[lang].m;$("cvOut").textContent=v+UN[lang].ms+" ("+fmt(v*3.6,0)+(lang==="ru"?" км/ч":" km/h")+")";
 $("cA").textContent=fmt(a,1)+(lang==="ru"?" м/с²":" m/s²");$("cM").textContent=fmt(vm,1)+UN[lang].ms+" ("+fmt(vm*3.6,0)+(lang==="ru"?" км/ч":" km/h")+")";$("cS").textContent=skid?t.skid:t.ok;$("cvFb").textContent=t.cvFb}
["cr","cu","cv"].forEach(id=>$(id).addEventListener("input",drawCv));
function drawSk(){const t=tt(),r1=+$("s1").value,r2=+$("s2").value,f1=+$("sw").value,I0=1,m=5,I1=I0+2*m*r1*r1,I2=I0+2*m*r2*r2,f2=f1*I1/I2;
 let g='';[[150,r1,f1,t.ru],[450,r2,f2]].forEach((p,i)=>{const x=p[0],r=p[1];g+='<circle cx="'+x+'" cy="110" r="10" fill="#b87333"/><line x1="'+x+'" y1="120" x2="'+x+'" y2="190" stroke="#18181a" stroke-width="8"/><line x1="'+(x-r*120)+'" y1="140" x2="'+(x+r*120)+'" y2="140" stroke="#18181a" stroke-width="5"/><circle cx="'+(x-r*120)+'" cy="140" r="7" fill="#b6533f"/><circle cx="'+(x+r*120)+'" cy="140" r="7" fill="#b6533f"/>'+svgText(x,225,(i?(lang==="ru"?"после: ":"after: "):(lang==="ru"?"до: ":"before: "))+fmt(i?f2:f1,1)+(lang==="ru"?" об/с":" rev/s"),"#18181a","middle",12)});
 g+=arrow(250,110,350,110,"#2f6f5d",3);
 $("skSvg").innerHTML=g;
 $("s1Out").textContent=fmt(r1,2)+UN[lang].m;$("s2Out").textContent=fmt(r2,2)+UN[lang].m;$("swOut").textContent=fmt(f1,1)+(lang==="ru"?" об/с":" rev/s");
 $("sI").textContent=fmt(I1,1)+" → "+fmt(I2,1)+(lang==="ru"?" кг·м²":" kg·m²");$("sF").textContent=fmt(f2,1)+(lang==="ru"?" об/с":" rev/s");$("skFb").textContent=t.skFb}
["s1","s2","sw"].forEach(id=>$(id).addEventListener("input",drawSk));
const LAB={ru:{tqSvg:T.ru.tqLabel,cvSvg:T.ru.cvLabel,skSvg:T.ru.skLabel},en:{tqSvg:T.en.tqLabel,cvSvg:T.en.cvLabel,skSvg:T.en.skLabel}};
function drawAll(){fillSel("cu",T[lang].road,0);drawTq();drawCv();drawSk()}
'''

c = dict(n='35', slug='35-rotation-torque.html', block='VI', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Вращение и момент силы', 'Rotation and torque'),
 desc='Глава 35 Атласа физики: момент силы и правило моментов, движение по окружности, центростремительное ускорение, момент импульса и его сохранение.',
 lead=('Почему гайку откручивают длинным ключом, а фигурист вращается быстрее, прижав руки. Момент силы, вращение, момент импульса.',
       'Why a nut is undone with a long wrench and a skater spins faster with the arms pulled in. Torque, rotation, angular momentum.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('torque', 'Момент силы', 'Torque'), ('circle', 'Поворот', 'A bend'), ('angmom', 'Момент импульса', 'Angular momentum'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Фигуристка начинает вращение, раскинув руки, — медленно. Затем она быстро прижимает руки к груди, и вращение становится таким быстрым, что лицо расплывается. Никто её не раскручивал, и никакой толчок она в этот момент не получала.</p><p>Откуда берётся ускорение вращения?</p>',
         '<p>A skater begins to spin with arms out — slowly. Then she quickly pulls her arms to her chest and the spin becomes so fast that her face blurs. Nobody spun her up and she got no push at that moment.</p><p>Where does the speeding-up of the spin come from?</p>'),
 hint=stdhint('Фигурист и момент импульса', 'A skater and angular momentum'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: сохраняется момент импульса', 'The answer: angular momentum is conserved'),
 answer=('<p>Внешних моментов нет (трение льда мало), поэтому момент импульса <em>L = I·ω</em> сохраняется. Прижимая руки, фигуристка приближает массу рук к оси, момент инерции <em>I</em> уменьшается в несколько раз, и для сохранения <em>L</em> угловая скорость <em>ω</em> должна во столько же раз вырасти. В модели 3 это 5,3 раза; энергию на это даёт работа мышц, которыми она тянет руки против центробежного эффекта.</p><p>Ускорения «из ничего» нет: меняется распределение массы, а не вращательный импульс.</p>',
         '<p>There are no external torques (the friction of ice is small) so the angular momentum <em>L = I·ω</em> is conserved. By pulling in the arms the skater moves the mass of the arms closer to the axis, the moment of inertia <em>I</em> falls several times and to keep <em>L</em> the angular velocity <em>ω</em> must grow by the same factor. In model 3 it is 5.3 times; the energy comes from the work of the muscles pulling the arms in against the centrifugal effect.</p><p>There is no acceleration “from nothing”: the distribution of mass changes, not the rotational momentum.</p>'),
 sources=[
  ('Момент силы, правило моментов, вращение, центростремительное ускорение —', 'Torque, the rule of moments, rotation, centripetal acceleration —', LINK('https://openstax.org/books/university-physics-volume-1/pages/10-introduction', 'OpenStax University Physics, Vol. 1, гл. 10') + ', ' + LINK('https://openstax.org/books/university-physics-volume-1/pages/4-5-uniform-circular-motion', 'OpenStax University Physics, Vol. 1, § 4.5')),
  ('Момент импульса и его сохранение —', 'Angular momentum and its conservation —', LINK('https://openstax.org/books/university-physics-volume-1/pages/11-introduction', 'OpenStax University Physics, Vol. 1, гл. 11') + ', ' + LINK('https://en.wikipedia.org/wiki/Angular_momentum', 'Wikipedia: Angular momentum'))],
 note=stdnote('Коэффициенты трения шин (0,7; 0,4; 0,1), момент инерции тела фигуриста и массы рук — условные.', 'The tyre friction coefficients (0.7; 0.4; 0.1), the skater’s moment of inertia and the masses of the arms are assumed.'),
 prev=('34-momentum.html', 'Глава 34 · Импульс', 'Chapter 34 · Momentum'),
 next=('36-gravity-satellites.html', 'Глава 36 · Гравитация и спутники', 'Chapter 36 · Gravity and satellites'),
 js=js)
build(c)
