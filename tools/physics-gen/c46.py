# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ЗАРЯД В МАГНИТНОМ ПОЛЕ', 'A CHARGE IN A MAGNETIC FIELD', 'lrSvg', '0 0 600 250',
  select('lp', 'Частица', 'Particle') + slider('lv', 'Скорость частицы', 'Speed of the particle', 0.1, 30, 0.1, 1) + slider('lb', 'Индукция поля B', 'Field induction B', 0.1, 50, 0.1, 1),
  stats([('lF', 'Сила Лоренца F = q·v·B', 'Lorentz force F = q·v·B'), ('lR', 'Радиус окружности r = m·v/(q·B)', 'Radius of the circle r = m·v/(q·B)'), ('lT', 'Период обращения T = 2π·m/(q·B)', 'Period of revolution T = 2π·m/(q·B)')]),
  'lrFb', 'Схема условная: поле направлено «от нас» (⊗); скорость в Мм/с (10⁶ м/с), B — в миллитеслах; радиус нарисован сжато.',
  'A schematic drawing: the field points “away from us” (⊗); the speed in Mm/s (10⁶ m/s), B in millitesla; the radius is drawn compressed.')
s1 = section('lorentz', 'Сила Лоренца', 'The Lorentz force',
 bd('<p>На движущийся заряд в магнитном поле действует <strong>сила Лоренца</strong> <em>F = q·v·B·sin α</em>. Она направлена перпендикулярно и скорости, и полю (правило левой руки), поэтому <em>работы не совершает</em>: скорость частицы не меняется по модулю, а меняется только направление. Если частица влетает перпендикулярно полю, она движется по окружности: сила Лоренца — центростремительная, <em>q·v·B = m·v²/r</em>.</p>',
    '<p>On a moving charge in a magnetic field acts the <strong>Lorentz force</strong> <em>F = q·v·B·sin α</em>. It is perpendicular to both the velocity and the field (the left-hand rule) so it <em>does no work</em>: the speed of the particle does not change in magnitude, only its direction. If the particle enters perpendicular to the field it moves along a circle: the Lorentz force is the centripetal force, <em>q·v·B = m·v²/r</em>.</p>')
 + formula('r = m·v / (q·B),   T = 2π·m / (q·B)', 'период не зависит от скорости — это основа циклотрона', 'the period does not depend on the speed — the basis of the cyclotron'),
 lab1)

lab2 = model(2, 'ЦИКЛОТРОН', 'THE CYCLOTRON', 'cySvg', '0 0 600 250',
  slider('yb', 'Индукция магнитного поля', 'Magnetic field induction', 0.1, 2, 0.05, 1.5) + slider('yr', 'Радиус ускорителя', 'Radius of the accelerator', 0.1, 1, 0.05, 0.5),
  stats([('yF', 'Частота обращения протона f = q·B/(2π·m)', 'Revolution frequency of a proton f = q·B/(2π·m)'), ('yK', 'Наибольшая энергия протона K = (q·B·R)²/(2m)', 'Greatest proton energy K = (q·B·R)²/(2m)'), ('yV', 'Скорость на выходе', 'Speed at the exit')]),
  'cyFb', 'Схема условная: приближённо нерелятивистский протон (при 27 МэВ скорость около 0,23 c, поправка порядка 3%); q = 1,602·10⁻¹⁹ Кл, m = 1,673·10⁻²⁷ кг.',
  'A schematic drawing: an approximately non-relativistic proton (at 27 MeV the speed is about 0.23 c, a correction of about 3%); q = 1.602·10⁻¹⁹ C, m = 1.673·10⁻²⁷ kg.')
s2 = section('accelerator', 'Ускорители частиц', 'Particle accelerators',
 bd('<p>В циклотроне протон движется по спирали между двумя полукруглыми «дуантами». Магнитное поле лишь изгибает траекторию, а разгоняет электрическое поле в зазоре между дуантами; так как период не зависит от скорости, переменное напряжение подаётся с постоянной частотой. С каждым оборотом радиус растёт, и на краю частица получает энергию, определяемую радиусом и полем: <em>K = (q·B·R)²/(2m)</em>. Такие установки делают изотопы для медицины (диагностика опухолей), на более крупных — открывают новые частицы.</p>',
    '<p>In a cyclotron a proton moves along a spiral between two semicircular “dees”. The magnetic field only bends the path while the electric field in the gap between the dees accelerates; since the period does not depend on the speed an alternating voltage is applied at a constant frequency. With every turn the radius grows and at the edge the particle gains an energy fixed by the radius and the field: <em>K = (q·B·R)²/(2m)</em>. Such machines make isotopes for medicine (tumour diagnostics) and larger ones discover new particles.</p>')
 + formula('f = q·B / (2π·m),   K = (q·B·R)² / (2m)', 'энергию 1 МэВ = 1,6·10⁻¹³ Дж', '1 MeV = 1.6·10⁻¹³ J'),
 lab2)

lab3 = model(3, 'МАСС-СПЕКТРОМЕТР', 'THE MASS SPECTROMETER', 'msSvg', '0 0 600 250',
  slider('mv', 'Скорость ионов', 'Speed of the ions', 10, 300, 10, 100) + slider('mb', 'Индукция поля', 'Field induction', 0.1, 1, 0.05, 0.5),
  stats([('m20', 'Радиус полуокружности неона-20', 'Radius of the semicircle of neon-20'), ('m22', 'Радиус полуокружности неона-22', 'Radius of the semicircle of neon-22'), ('mD', 'Расстояние между пятнами на пластинке', 'Distance between the spots on the plate')]),
  'msFb', 'Схема условная: однозарядные ионы с одинаковой скоростью (скорость — в км/с); масса 20 и 22 а.е.м.; 1 а.е.м. = 1,661·10⁻²⁷ кг.',
  'A schematic drawing: singly charged ions of the same speed (the speed in km/s); masses 20 and 22 u; 1 u = 1.661·10⁻²⁷ kg.')
s3 = section('spectrometer', 'Взвешивание атомов', 'Weighing atoms',
 bd('<p>Ионы разных изотопов с одинаковым зарядом и скоростью описывают в магнитном поле дуги разного радиуса: чем тяжелее ион, тем больше <em>r = m·v/(q·B)</em>. Измерив радиус, находят массу. Так открывали изотопы (неон-20 и неон-22) и сегодня определяют состав веществ, возраст пород и допинг в крови.</p>',
    '<p>Ions of different isotopes with the same charge and speed describe arcs of different radius in a magnetic field: the heavier the ion the greater <em>r = m·v/(q·B)</em>. By measuring the radius the mass is found. This is how isotopes (neon-20 and neon-22) were discovered and today the composition of substances, the age of rocks and doping in blood are determined.</p>')
 + formula('m = q·B·r / v', 'расстояние между пятнами — разность диаметров 2r', 'the distance between the spots is the difference of the diameters 2r'),
 lab3)

tasks = [
 task(1, 'Сила на электрон', 'The force on an electron', 'Электрон летит со скоростью 10⁶ м/с перпендикулярно полю B = 1 мТл. Найдите силу Лоренца. (e = 1,602·10⁻¹⁹ Кл.)', 'An electron flies at 10⁶ m/s perpendicular to a field B = 1 mT. Find the Lorentz force. (e = 1.602·10⁻¹⁹ C.)',
  'v = 10⁶ м/с, B = 10⁻³ Тл', 'v = 10⁶ m/s, B = 10⁻³ T', 'F = q·v·B = 1,602·10⁻¹⁹ · 10⁶ · 10⁻³ = 1,6·10⁻¹⁶ Н.', 'F = q·v·B = 1.602·10⁻¹⁹ · 10⁶ · 10⁻³ = 1.6·10⁻¹⁶ N.', '≈ 1,6·10⁻¹⁶ Н (мала, но масса электрона ещё меньше).', '≈ 1.6·10⁻¹⁶ N (small but the electron mass is even smaller).', True),
 task(2, 'Радиус окружности', 'The radius of the circle', 'Найдите радиус окружности для электрона из задачи 1 (m = 9,11·10⁻³¹ кг).', 'Find the radius of the circle for the electron of problem 1 (m = 9.11·10⁻³¹ kg).',
  'm = 9,11·10⁻³¹ кг', 'm = 9.11·10⁻³¹ kg', 'r = m·v/(q·B) = 9,11·10⁻³¹ · 10⁶ / (1,602·10⁻¹⁹ · 10⁻³) = 9,11·10⁻²⁵ / 1,602·10⁻²² ≈ 5,7·10⁻³ м.', 'r = m·v/(q·B) = 9.11·10⁻³¹ · 10⁶ / (1.602·10⁻¹⁹ · 10⁻³) = 9.11·10⁻²⁵ / 1.602·10⁻²² ≈ 5.7·10⁻³ m.', '≈ 5,7 мм.', '≈ 5.7 mm.'),
 task(3, 'Период', 'The period', 'Найдите период обращения того же электрона и зависит ли он от скорости.', 'Find the period of revolution of the same electron and whether it depends on the speed.',
  'm, q, B', 'm, q, B', 'T = 2π·m/(q·B) = 6,283 · 9,11·10⁻³¹ / (1,602·10⁻²²) ≈ 3,6·10⁻⁸ с.<br>Скорость в формулу не входит — от неё не зависит.', 'T = 2π·m/(q·B) = 6.283 · 9.11·10⁻³¹ / (1.602·10⁻²²) ≈ 3.6·10⁻⁸ s.<br>The speed is not in the formula — it does not depend on it.', '≈ 36 нс; от скорости не зависит.', '≈ 36 ns; independent of the speed.'),
 task(4, 'Частота циклотрона', 'The cyclotron frequency', 'Протон в поле B = 1,5 Тл. Найдите частоту обращения. (m = 1,673·10⁻²⁷ кг.)', 'A proton in a field B = 1.5 T. Find the frequency of revolution. (m = 1.673·10⁻²⁷ kg.)',
  'B = 1,5 Тл', 'B = 1.5 T', 'f = q·B/(2π·m) = 1,602·10⁻¹⁹ · 1,5 / (6,283 · 1,673·10⁻²⁷) = 2,403·10⁻¹⁹ / 1,051·10⁻²⁶ ≈ 2,29·10⁷ Гц.', 'f = q·B/(2π·m) = 1.602·10⁻¹⁹ · 1.5 / (6.283 · 1.673·10⁻²⁷) = 2.403·10⁻¹⁹ / 1.051·10⁻²⁶ ≈ 2.29·10⁷ Hz.', '≈ 22,9 МГц.', '≈ 22.9 MHz.'),
 task(5, 'Энергия на выходе', 'Energy at the exit', 'Радиус циклотрона R = 0,5 м, B = 1,5 Тл. Найдите наибольшую энергию протона в МэВ.', 'The cyclotron radius is R = 0.5 m, B = 1.5 T. Find the greatest proton energy in MeV.',
  'R = 0,5 м', 'R = 0.5 m', 'K = (q·B·R)²/(2m) = (1,602·10⁻¹⁹ · 1,5 · 0,5)² / (2 · 1,673·10⁻²⁷) = (1,20·10⁻¹⁹)² / 3,346·10⁻²⁷ ≈ 4,3·10⁻¹² Дж.<br>В МэВ: 4,3·10⁻¹² / 1,602·10⁻¹³ ≈ 27 МэВ.', 'K = (q·B·R)²/(2m) = (1.602·10⁻¹⁹ · 1.5 · 0.5)² / (2 · 1.673·10⁻²⁷) = (1.20·10⁻¹⁹)² / 3.346·10⁻²⁷ ≈ 4.3·10⁻¹² J.<br>In MeV: 4.3·10⁻¹² / 1.602·10⁻¹³ ≈ 27 MeV.', '≈ 27 МэВ.', '≈ 27 MeV.'),
 task(6, 'Изотопы неона', 'Neon isotopes', 'Ионы неона-20 и неона-22 (заряд e) летят со скоростью 100 км/с в поле 0,5 Тл. Найдите радиусы и расстояние между пятнами. (1 а.е.м. = 1,661·10⁻²⁷ кг.)', 'Ions of neon-20 and neon-22 (charge e) fly at 100 km/s in a field of 0.5 T. Find the radii and the distance between the spots. (1 u = 1.661·10⁻²⁷ kg.)',
  'v = 10⁵ м/с, B = 0,5 Тл', 'v = 10⁵ m/s, B = 0.5 T', 'm₂₀ = 3,322·10⁻²⁶ кг, m₂₂ = 3,654·10⁻²⁶ кг.<br>r₂₀ = m·v/(q·B) = 3,322·10⁻²⁶ · 10⁵ / (1,602·10⁻¹⁹ · 0,5) ≈ 0,0415 м.<br>r₂₂ ≈ 0,0456 м.<br>Расстояние: 2·(0,0456 − 0,0415) ≈ 8,3·10⁻³ м.', 'm₂₀ = 3.322·10⁻²⁶ kg, m₂₂ = 3.654·10⁻²⁶ kg.<br>r₂₀ = m·v/(q·B) = 3.322·10⁻²⁶ · 10⁵ / (1.602·10⁻¹⁹ · 0.5) ≈ 0.0415 m.<br>r₂₂ ≈ 0.0456 m.<br>Distance: 2·(0.0456 − 0.0415) ≈ 8.3·10⁻³ m.', '4,15 см и 4,56 см; пятна на расстоянии ≈ 8,3 мм.', '4.15 cm and 4.56 cm; the spots are ≈ 8.3 mm apart.'),
]

quiz = [
 qz('Как направлена сила Лоренца относительно скорости частицы?', 'Перпендикулярно скорости', 'Вдоль скорости', 'Против скорости', 'Поэтому она работы не совершает.',
    'How is the Lorentz force directed relative to the particle’s velocity?', 'Perpendicular to the velocity', 'Along the velocity', 'Against the velocity', 'So it does no work.'),
 qz('Меняет ли магнитное поле скорость (модуль) заряда?', 'Нет, только направление', 'Да, ускоряет', 'Да, тормозит', 'Сила перпендикулярна движению.',
    'Does a magnetic field change the speed (magnitude) of a charge?', 'No, only the direction', 'Yes, it accelerates', 'Yes, it decelerates', 'The force is perpendicular to the motion.'),
 qz('По какой траектории движется заряд, влетевший перпендикулярно полю?', 'По окружности', 'По прямой', 'По параболе', 'Сила Лоренца — центростремительная.',
    'What path does a charge entering perpendicular to the field follow?', 'A circle', 'A straight line', 'A parabola', 'The Lorentz force is centripetal.'),
 qz('Как радиус окружности зависит от скорости?', 'Растёт с ростом скорости', 'Уменьшается', 'Не зависит', 'r = m·v/(q·B).',
    'How does the radius of the circle depend on speed?', 'It grows with speed', 'It decreases', 'It does not depend', 'r = m·v/(q·B).'),
 qz('От чего НЕ зависит период обращения заряда в поле?', 'От скорости', 'От массы', 'От индукции поля', 'T = 2πm/(qB).',
    'What does the period of revolution of a charge in a field NOT depend on?', 'The speed', 'The mass', 'The field induction', 'T = 2πm/(qB).'),
 qz('Что разгоняет частицы в циклотроне?', 'Электрическое поле в зазоре', 'Магнитное поле', 'Сила тяжести', 'Магнитное поле лишь искривляет путь.',
    'What accelerates the particles in a cyclotron?', 'The electric field in the gap', 'The magnetic field', 'Gravity', 'The magnetic field only bends the path.'),
 qz('Какой изотоп в масс-спектрометре даёт больший радиус?', 'Более тяжёлый', 'Более лёгкий', 'Одинаковые', 'r ~ m.',
    'Which isotope gives the greater radius in a mass spectrometer?', 'The heavier one', 'The lighter one', 'They are the same', 'r ~ m.'),
 qz('Что защищает Землю от заряженных частиц космоса?', 'Магнитное поле Земли', 'Облака', 'Озоновый слой', 'Поле отклоняет частицы силой Лоренца.',
    'What shields the Earth from charged particles of space?', 'The Earth’s magnetic field', 'Clouds', 'The ozone layer', 'The field deflects the particles by the Lorentz force.'),
]

js = JSL + r'''
const T={ru:{
 lrLabel:"Траектория заряда в магнитном поле",cyLabel:"Дуанты циклотрона и спираль протона",msLabel:"Два изотопа неона на пластинке",
 parts:["Электрон (−e)","Протон (+e)","Альфа-частица (+2e)"],
 lrFb:"Тяжелее и быстрее — шире окружность; сильнее поле — уже.",cyFb:"Энергия растёт как квадрат радиуса и поля.",msFb:"Тяжёлый изотоп оставляет пятно дальше."},
 en:{
 lrLabel:"The path of a charge in a magnetic field",cyLabel:"The dees of a cyclotron and a proton spiral",msLabel:"Two neon isotopes on a plate",
 parts:["Electron (−e)","Proton (+e)","Alpha particle (+2e)"],
 lrFb:"Heavier and faster — a wider circle; a stronger field — a narrower one.",cyFb:"The energy grows as the square of the radius and field.",msFb:"The heavy isotope leaves its spot farther away."}};
const PQ=[-1.602e-19,1.602e-19,3.204e-19],PM=[9.109e-31,1.673e-27,6.645e-27];
function drawLr(){const t=tt(),k=+$("lp").value,v=+$("lv").value*1e6,B=+$("lb").value*1e-3,q=Math.abs(PQ[k]),m=PM[k],F=q*v*B,r=m*v/(q*B),Tp=2*Math.PI*m/(q*B);
 const rr=Math.max(14,Math.min(100,25+Math.log10(r*1000+0.001)*28)),dir=PQ[k]<0?1:-1;
 let g='';for(let i=0;i<5;i++)for(let j=0;j<4;j++)g+=svgText(70+i*110,50+j*55,"⊗","#c9c2b0","middle",18);
 const cx=300,cy=125+dir*0;g+='<circle cx="'+cx+'" cy="'+(125-dir*rr)+'" r="'+rr+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><circle cx="'+cx+'" cy="125" r="6" fill="#b6533f"/>'+arrow(cx,125,cx+50,125,"#2f6f5d",3)+svgText(cx+54,120,"v","#2f6f5d","start",13)+arrow(cx,125,cx,125-dir*40,"#b6533f",3)+svgText(cx+8,125-dir*44,"F","#b6533f","start",13);
 $("lrSvg").innerHTML=g;$("lvOut").textContent=fmt(v/1e6,1)+" "+U("Мм/с","Mm/s");$("lbOut").textContent=fmt(B*1000,1)+" "+U("мТл","mT");
 const rs=r<1?(r<1e-3?fmt(r*1e6,1)+" "+U("мкм","µm"):fmt(r*1000,2)+" "+U("мм","mm")):fmt(r,2)+" "+U("м","m");
 $("lF").textContent=sci(F,2)+" "+U("Н","N");$("lR").textContent=rs;$("lT").textContent=sci(Tp,2)+" "+U("с","s");$("lrFb").textContent=t.lrFb}
["lp","lv","lb"].forEach(id=>$(id).addEventListener("input",drawLr));
function drawCy(){const t=tt(),B=+$("yb").value,R=+$("yr").value,q=1.602e-19,m=1.673e-27,f=q*B/(2*Math.PI*m),K=Math.pow(q*B*R,2)/(2*m),v=Math.sqrt(2*K/m);
 let g='<path d="M150 125 m-60 0 a60 60 0 0 1 120 0" fill="none"/><circle cx="300" cy="125" r="'+(50+R*60)+'" fill="#f4f1e8" stroke="#18181a" stroke-width="2"/><line x1="300" y1="'+(125-50-R*60)+'" x2="300" y2="'+(125+50+R*60)+'" stroke="#18181a" stroke-dasharray="4 3"/>';
 let p="M300 125";for(let a=0;a<=14;a+=0.1){const rr=(a/14)*(45+R*60);p+=" L"+(300+rr*Math.cos(a*1.0))+" "+(125-rr*Math.sin(a*1.0))}
 g+='<path d="'+p+'" fill="none" stroke="#b6533f" stroke-width="2.5"/>'+svgText(300,236,"B = "+fmt(B,2)+" "+U("Тл","T"),"#66666b","middle",12);
 $("cySvg").innerHTML=g;$("ybOut").textContent=fmt(B,2)+" "+U("Тл","T");$("yrOut").textContent=fmt(R,2)+" "+U("м","m");
 $("yF").textContent=fmt(f/1e6,1)+" "+U("МГц","MHz");$("yK").textContent=fmt(K/1.602e-13,1)+" "+U("МэВ","MeV");$("yV").textContent=fmt(v/1e6,1)+" "+U("Мм/с","Mm/s")+" ("+fmt(v/3e8*100,1)+"% "+U("скорости света","of light speed")+")";$("cyFb").textContent=t.cyFb}
["yb","yr"].forEach(id=>$(id).addEventListener("input",drawCy));
function drawMs(){const t=tt(),v=+$("mv").value*1000,B=+$("mb").value,u=1.661e-27,q=1.602e-19,r20=20*u*v/(q*B),r22=22*u*v/(q*B),D=2*(r22-r20);
 const sc=480/Math.max(0.2,2*r22*1.3);let g='<line x1="60" y1="210" x2="560" y2="210" stroke="#18181a" stroke-width="3"/>'+'<circle cx="'+(80+2*r20*sc)+'" cy="210" r="7" fill="#3f5f8f"/><circle cx="'+(80+2*r22*sc)+'" cy="210" r="7" fill="#b6533f"/>'+'<path d="M80 210 A '+(r20*sc)+' '+(r20*sc)+' 0 0 1 '+(80+2*r20*sc)+' 210" fill="none" stroke="#3f5f8f" stroke-width="2.5"/><path d="M80 210 A '+(r22*sc)+' '+(r22*sc)+' 0 0 1 '+(80+2*r22*sc)+' 210" fill="none" stroke="#b6533f" stroke-width="2.5"/>'+svgText(80+2*r20*sc,235,"20","#3f5f8f","middle",12)+svgText(80+2*r22*sc,235,"22","#b6533f","middle",12);
 $("msSvg").innerHTML=g;$("mvOut").textContent=Math.round(v/1000)+" "+U("км/с","km/s");$("mbOut").textContent=fmt(B,2)+" "+U("Тл","T");
 $("m20").textContent=fmt(r20*100,2)+" "+U("см","cm");$("m22").textContent=fmt(r22*100,2)+" "+U("см","cm");$("mD").textContent=fmt(D*1000,1)+" "+U("мм","mm");$("msFb").textContent=t.msFb}
["mv","mb"].forEach(id=>$(id).addEventListener("input",drawMs));
const LAB={ru:{lrSvg:T.ru.lrLabel,cySvg:T.ru.cyLabel,msSvg:T.ru.msLabel},en:{lrSvg:T.en.lrLabel,cySvg:T.en.cyLabel,msSvg:T.en.msLabel}};
function drawAll(){fillSel("lp",T[lang].parts,1);drawLr();drawCy();drawMs()}
'''

c = dict(n='46', slug='46-lorentz-force.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Сила Лоренца', 'The Lorentz force'),
 desc='Глава 46 Атласа физики: сила Лоренца, движение заряда в магнитном поле, циклотрон, масс-спектрометр, защита Земли от космических частиц.',
 lead=('Магнитное поле не разгоняет заряд, но искривляет его путь. Окружности частиц, циклотрон и взвешивание атомов.',
       'A magnetic field does not accelerate a charge but bends its path. Circles of particles, the cyclotron and weighing atoms.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('lorentz', 'Сила Лоренца', 'The Lorentz force'), ('accelerator', 'Ускорители', 'Accelerators'), ('spectrometer', 'Масс-спектрометр', 'Mass spectrometer'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Ускорители частиц делают кольцевыми: в большом кольце частицы бегут по кругу миллиарды раз. Но по закону Ньютона, чтобы тело двигалось по окружности, на него должна действовать сила, направленная к центру. Что-то должно «закручивать» протоны, и это что-то не должно разгонять их или тормозить сильнее, чем нужно.</p><p>Какая сила умеет только поворачивать, но не ускорять?</p>',
         '<p>Particle accelerators are made ring-shaped: in a big ring particles run round billions of times. But by Newton’s law for a body to move along a circle a force directed to the centre must act on it. Something has to “turn” the protons and this something must not speed them up or slow them down more than needed.</p><p>What force can only turn but not accelerate?</p>'),
 hint=stdhint('Заряд в магнитном поле', 'A charge in a magnetic field'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: сила Лоренца', 'The answer: the Lorentz force'),
 answer=('<p>Магнитное поле действует на движущийся заряд силой, перпендикулярной скорости: <em>F = q·v·B</em>. Такая сила не совершает работы, то есть не меняет скорость по величине, а лишь поворачивает её — это идеальная центростремительная сила. В кольце ускорителя мощные магниты удерживают пучок на окружности, а разгоняют частицы электрическим полем в особых промежутках.</p><p>Тем же способом магнитное поле Земли отклоняет заряженные частицы космических лучей и солнечного ветра, а попадающие вдоль силовых линий к полюсам вызывают полярные сияния.</p>',
         '<p>A magnetic field acts on a moving charge with a force perpendicular to the velocity: <em>F = q·v·B</em>. Such a force does no work, that is it does not change the speed in magnitude but only turns it — an ideal centripetal force. In an accelerator ring powerful magnets hold the beam on a circle while the particles are accelerated by an electric field in special gaps.</p><p>In the same way the Earth’s magnetic field deflects charged particles of cosmic rays and the solar wind while those arriving along the field lines to the poles cause auroras.</p>'),
 sources=[
  ('Сила Лоренца, движение заряда в магнитном поле, циклотрон, масс-спектрометр —', 'The Lorentz force, motion of a charge in a magnetic field, the cyclotron, the mass spectrometer —', LINK('https://openstax.org/books/university-physics-volume-2/pages/11-introduction', 'OpenStax University Physics, Vol. 2, гл. 11') + ', ' + LINK('https://en.wikipedia.org/wiki/Lorentz_force', 'Wikipedia: Lorentz force') + ', ' + LINK('https://en.wikipedia.org/wiki/Cyclotron', 'Wikipedia: Cyclotron')),
  ('Магнитосфера Земли и полярные сияния —', 'The Earth’s magnetosphere and auroras —', LINK('https://en.wikipedia.org/wiki/Magnetosphere', 'Wikipedia: Magnetosphere'))],
 note=stdnote('Значения B, скоростей и радиусов в моделях — учебные; циклотрон считается нерелятивистским (приближённо верно для энергий порядка десятков МэВ у протона).', 'The values of B, speeds and radii in the models are for teaching; the cyclotron is treated as non-relativistic (approximately valid for proton energies of the order of tens of MeV).'),
 prev=('45-capacitor.html', 'Глава 45 · Конденсатор', 'Chapter 45 · The capacitor'),
 next=('47-alternating-current.html', 'Глава 47 · Переменный ток', 'Chapter 47 · Alternating current'),
 js=js)
build(c)
