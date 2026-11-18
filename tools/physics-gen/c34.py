# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'СТОЛКНОВЕНИЕ ДВУХ ТЕЛЕЖЕК', 'A COLLISION OF TWO CARTS', 'clSvg', '0 0 600 250',
  select('ck', 'Тип удара', 'Type of collision') + slider('c1', 'Масса первой тележки', 'Mass of the first cart', 1, 10, 0.5, 2) + slider('v1', 'Скорость первой', 'Speed of the first', -5, 5, 0.5, 3) + slider('c2', 'Масса второй тележки', 'Mass of the second cart', 1, 10, 0.5, 2) + slider('v2', 'Скорость второй', 'Speed of the second', -5, 5, 0.5, 0),
  stats([('cP', 'Суммарный импульс (до = после)', 'Total momentum (before = after)'), ('cV', 'Скорости после удара', 'Speeds after the collision'), ('cE', 'Потеряно энергии', 'Energy lost')]),
  'clFb', 'Схема условная: движение вдоль одной прямой без трения; скорость вправо положительна.',
  'A schematic drawing: motion along one line without friction; speed to the right is positive.')
s1 = section('mom', 'Импульс и закон сохранения', 'Momentum and its conservation',
 bd('<p><strong>Импульс</strong> тела — произведение массы на скорость: <em>p = m·v</em> (единица — кг·м/с). Это вектор, направленный как скорость. Второй закон Ньютона можно записать через импульс: <em>F·Δt = Δp</em> — произведение силы на время её действия (<strong>импульс силы</strong>) равно изменению импульса.</p><p>Если на систему тел не действуют внешние силы (или они уравновешены), то <strong>суммарный импульс системы сохраняется</strong>: что один потерял, то другой получил. Это следует из третьего закона Ньютона. Законом пользуются при ударах, взрывах и в ракетах.</p>',
    '<p>The <strong>momentum</strong> of a body is mass times velocity: <em>p = m·v</em> (unit — kg·m/s). It is a vector pointing as the velocity. Newton’s second law can be written through momentum: <em>F·Δt = Δp</em> — the product of force and the time it acts (the <strong>impulse of the force</strong>) equals the change of momentum.</p><p>If no external forces act on a system of bodies (or they are balanced) the <strong>total momentum of the system is conserved</strong>: what one lost the other gained. This follows from Newton’s third law. It is used for collisions, explosions and rockets.</p>')
 + formula('m₁v₁ + m₂v₂ = m₁v₁′ + m₂v₂′', 'при абсолютно неупругом ударе тела слипаются: v′ = (m₁v₁ + m₂v₂) / (m₁ + m₂)', 'in a perfectly inelastic collision the bodies stick together: v′ = (m₁v₁ + m₂v₂) / (m₁ + m₂)')
 + bd('<p>При <strong>упругом</strong> ударе сохраняется ещё и кинетическая энергия (бильярдные шары); при <strong>неупругом</strong> часть энергии уходит в деформацию и тепло (автомобили, глина), хотя импульс сохраняется в обоих случаях.</p>',
      '<p>In an <strong>elastic</strong> collision kinetic energy is also conserved (billiard balls); in an <strong>inelastic</strong> one part of the energy goes into deformation and heat (cars, clay) though momentum is conserved in both cases.</p>'),
 lab1)

lab2 = model(2, 'УДАР И ВРЕМЯ ТОРМОЖЕНИЯ', 'AN IMPACT AND THE STOPPING TIME', 'imSvg', '0 0 600 250',
  slider('im', 'Масса', 'Mass', 5, 100, 1, 60) + slider('iv', 'Скорость перед ударом', 'Speed before the impact', 1, 15, 0.5, 5) + slider('it', 'Время остановки', 'Stopping time', 0.01, 1, 0.01, 0.1),
  stats([('iJ', 'Изменение импульса Δp = m·v', 'Change of momentum Δp = m·v'), ('iF', 'Средняя сила F = Δp/Δt', 'Average force F = Δp/Δt'), ('iW', 'Во сколько раз больше веса', 'How many times the weight')]),
  'imFb', 'Схема условная: тело полностью останавливается за указанное время; сила усреднена.',
  'A schematic drawing: the body stops completely in the stated time; the force is averaged.')
s2 = section('impact', 'Почему важно время торможения', 'Why the stopping time matters',
 bd('<p>Из <em>F·Δt = Δp</em> следует, что при одном и том же изменении импульса сила тем меньше, чем дольше длится торможение: <em>F = Δp / Δt</em>. Поэтому приземляются на согнутые ноги, ловят мяч, отводя руки назад, ставят в автомобилях подушки безопасности и зоны смятия кузова, а на велосипед надевают шлем с мягкой прослойкой. Во всех случаях удар растягивают во времени и силу уменьшают.</p>',
    '<p>From <em>F·Δt = Δp</em> it follows that for the same change of momentum the force is smaller the longer the stopping lasts: <em>F = Δp / Δt</em>. That is why people land on bent legs, catch a ball drawing the hands back, cars have airbags and crumple zones and a bicycle helmet has a soft lining. In all cases the impact is spread out in time and the force reduced.</p>')
 + formula('F = Δp / Δt = m · v / Δt', 'в 10 раз дольше торможение — в 10 раз меньше средняя сила', 'ten times longer stopping — ten times smaller average force'),
 lab2)

lab3 = model(3, 'РАКЕТА', 'THE ROCKET', 'rkSvg', '0 0 600 250',
  slider('re', 'Скорость истечения газов', 'Exhaust speed', 1, 5, 0.1, 3) + slider('rm', 'Во сколько раз масса ракеты с топливом больше сухой', 'How many times the rocket with fuel outweighs the dry rocket', 1, 30, 0.5, 5),
  stats([('rV', 'Набранная скорость v = u·ln(m₀/m)', 'Speed gained v = u·ln(m₀/m)'), ('rO', 'Нужно для орбиты (7,8 км/с)', 'Needed for orbit (7.8 km/s)'), ('rT', 'Доля массы — топливо', 'Fraction of the mass that is fuel')]),
  'rkFb', 'Схема условная: ракета вне атмосферы и тяготения (идеальная формула Циолковского). Скорость истечения в км/с.',
  'A schematic drawing: a rocket outside the atmosphere and gravity (the ideal Tsiolkovsky formula). The exhaust speed in km/s.')
s3 = section('rocket', 'Реактивное движение', 'Jet propulsion',
 bd('<p>Ракете не нужно отталкиваться от воздуха. Она выбрасывает вниз раскалённые газы, и по закону сохранения импульса сама получает импульс вверх. Чем быстрее вылетают газы и чем больше их масса относительно ракеты, тем выше конечная скорость. Идеальная формула Циолковского:</p>',
    '<p>A rocket needs nothing to push off from. It throws hot gases backward and by the conservation of momentum gets an equal momentum forward. The faster the gases leave and the greater their mass relative to the rocket, the higher the final speed. The ideal Tsiolkovsky formula:</p>')
 + formula('v = u · ln(m₀ / m)', 'u — скорость истечения газов, m₀ — начальная масса (с топливом), m — конечная (без топлива)', 'u is the exhaust speed, m₀ the initial mass (with fuel), m the final mass (without fuel)')
 + bd('<p>Чтобы выйти на орбиту, нужно набрать около 7,8 км/с (глава 36), а скорость истечения у химических двигателей — несколько км/с. Поэтому почти вся стартовая масса ракеты — топливо, и ракеты делают многоступенчатыми, отбрасывая пустые баки.</p>',
      '<p>To reach orbit one must gain about 7.8 km/s (chapter 36) while the exhaust speed of chemical engines is a few km/s. So almost the entire launch mass of a rocket is fuel and rockets are built in stages, dropping empty tanks.</p>'),
 lab3)

tasks = [
 task(1, 'Импульс автомобиля', 'The momentum of a car', 'Найдите импульс автомобиля массой 1200 кг, едущего со скоростью 20 м/с.', 'Find the momentum of a 1,200 kg car moving at 20 m/s.',
  'm = 1200 кг, v = 20 м/с', 'm = 1,200 kg, v = 20 m/s', 'p = m·v = 1200 · 20 = 24 000 кг·м/с.', 'p = m·v = 1200 · 20 = 24,000 kg·m/s.', '24 000 кг·м/с.', '24,000 kg·m/s.', True),
 task(2, 'Ловля мяча', 'Catching a ball', 'Мяч массой 0,4 кг летит со скоростью 20 м/с. Какая средняя сила действует на ладонь, если мяч остановился за 0,02 с? А если вы смягчили удар и остановили мяч за 0,2 с?', 'A 0.4 kg ball flies at 20 m/s. What average force acts on the palm if the ball stops in 0.02 s? And if you cushion the catch and stop it in 0.2 s?',
  'm = 0,4 кг, v = 20 м/с', 'm = 0.4 kg, v = 20 m/s', 'Δp = 0,4 · 20 = 8 кг·м/с.<br>Δt = 0,02 с: F = 8 / 0,02 = 400 Н.<br>Δt = 0,2 с: F = 8 / 0,2 = 40 Н.', 'Δp = 0.4 · 20 = 8 kg·m/s.<br>Δt = 0.02 s: F = 8 / 0.02 = 400 N.<br>Δt = 0.2 s: F = 8 / 0.2 = 40 N.', '400 Н и 40 Н — в 10 раз меньше.', '400 N and 40 N — 10 times smaller.'),
 task(3, 'Слипшиеся автомобили', 'Cars that stick together', 'Автомобиль 1000 кг на скорости 20 м/с врезается в стоящий автомобиль 1000 кг, и они движутся вместе. Найдите скорость и потерянную энергию.', 'A 1,000 kg car at 20 m/s hits a stationary 1,000 kg car and they move together. Find the speed and the lost energy.',
  'm₁ = m₂ = 1000 кг, v₁ = 20 м/с, v₂ = 0', 'm₁ = m₂ = 1,000 kg, v₁ = 20 m/s, v₂ = 0', 'v′ = (1000·20) / 2000 = 10 м/с.<br>Энергия до: ½·1000·20² = 200 000 Дж.<br>После: ½·2000·10² = 100 000 Дж.<br>Потеряно 100 кДж.', 'v′ = (1000·20) / 2000 = 10 m/s.<br>Energy before: ½·1000·20² = 200,000 J.<br>After: ½·2000·10² = 100,000 J.<br>Lost 100 kJ.', '10 м/с; потеряна половина энергии (100 кДж).', '10 m/s; half the energy is lost (100 kJ).'),
 task(4, 'Отдача', 'Recoil', 'Человек массой 60 кг стоит на льду и бросает горизонтально мяч массой 2 кг со скоростью 12 м/с. С какой скоростью он покатится назад?', 'A 60 kg person standing on ice throws a 2 kg ball horizontally at 12 m/s. At what speed does he slide backward?',
  'M = 60 кг, m = 2 кг, v = 12 м/с', 'M = 60 kg, m = 2 kg, v = 12 m/s', 'Импульс системы до броска 0, значит M·V = m·v.<br>V = 2 · 12 / 60 = 0,4 м/с.', 'The momentum of the system before the throw is 0 so M·V = m·v.<br>V = 2 · 12 / 60 = 0.4 m/s.', '0,4 м/с в противоположную сторону.', '0.4 m/s in the opposite direction.'),
 task(5, 'Упругий удар', 'An elastic collision', 'Шар 2 кг со скоростью 3 м/с упруго ударяет по такому же шару, лежащему неподвижно. Найдите скорости после удара.', 'A 2 kg ball at 3 m/s elastically hits an identical stationary ball. Find the speeds after the collision.',
  'm₁ = m₂ = 2 кг, v₁ = 3 м/с', 'm₁ = m₂ = 2 kg, v₁ = 3 m/s', 'При упругом ударе равных масс скорости «обмениваются»:<br>v₁′ = 0, v₂′ = 3 м/с.<br>Проверка: импульс 6 → 6, энергия 9 → 9 Дж.', 'In an elastic collision of equal masses the speeds “exchange”:<br>v₁′ = 0, v₂′ = 3 m/s.<br>Check: momentum 6 → 6, energy 9 → 9 J.', '0 и 3 м/с — так ведут себя бильярдные шары.', '0 and 3 m/s — that is how billiard balls behave.'),
 task(6, 'Ракета на орбиту', 'A rocket to orbit', 'Скорость истечения газов 3 км/с. Какое отношение стартовой массы к конечной нужно, чтобы набрать 7,8 км/с? Какая доля массы — топливо?', 'The exhaust speed is 3 km/s. What ratio of the initial mass to the final is needed to gain 7.8 km/s? What fraction of the mass is fuel?',
  'u = 3 км/с, v = 7,8 км/с', 'u = 3 km/s, v = 7.8 km/s', 'ln(m₀/m) = v/u = 7,8/3 = 2,6.<br>m₀/m = e^2,6 ≈ 13,5.<br>Доля топлива: 1 − 1/13,5 ≈ 0,93.', 'ln(m₀/m) = v/u = 7.8/3 = 2.6.<br>m₀/m = e^2.6 ≈ 13.5.<br>Fuel fraction: 1 − 1/13.5 ≈ 0.93.', 'в 13,5 раза; около 93% стартовой массы — топливо (в идеале, без потерь на тяготение и сопротивление).', '13.5 times; about 93% of the launch mass is fuel (ideally, without gravity and drag losses).'),
]

quiz = [
 qz('Что такое импульс тела?', 'Произведение массы на скорость', 'Масса, делённая на скорость', 'Произведение силы на путь', 'p = m·v.',
    'What is the momentum of a body?', 'Mass times velocity', 'Mass divided by velocity', 'Force times distance', 'p = m·v.'),
 qz('Когда сохраняется суммарный импульс системы?', 'Когда внешние силы не действуют или уравновешены', 'Всегда, в любых условиях', 'Только при упругом ударе', 'Закон сохранения импульса требует замкнутой системы.',
    'When is the total momentum of a system conserved?', 'When external forces are absent or balanced', 'Always under any conditions', 'Only in an elastic collision', 'The law requires a closed system.'),
 qz('При неупругом ударе сохраняется…', 'Импульс, но не вся кинетическая энергия', 'Только энергия', 'Ничего', 'Часть энергии уходит в тепло и деформацию.',
    'In an inelastic collision what is conserved?', 'Momentum but not all kinetic energy', 'Only energy', 'Nothing', 'Part of the energy goes into heat and deformation.'),
 qz('Почему при прыжке надо приземляться на согнутые ноги?', 'Время торможения растёт и сила удара уменьшается', 'Уменьшается масса', 'Исчезает сила тяжести', 'F = Δp/Δt: больше Δt — меньше F.',
    'Why should you land on bent legs after a jump?', 'The stopping time grows and the force of the impact falls', 'The mass decreases', 'Gravity disappears', 'F = Δp/Δt: a larger Δt gives a smaller F.'),
 qz('Для чего нужны подушки безопасности?', 'Чтобы увеличить время остановки человека', 'Чтобы увеличить скорость', 'Чтобы уменьшить массу', 'Увеличение Δt снижает среднюю силу.',
    'What are airbags for?', 'To lengthen the time the person takes to stop', 'To increase the speed', 'To reduce the mass', 'A larger Δt lowers the average force.'),
 qz('На каком законе основано движение ракеты?', 'Сохранения импульса', 'Архимеда', 'Ома', 'Выброс газов назад даёт ракете импульс вперёд.',
    'On which law is rocket motion based?', 'Conservation of momentum', 'Archimedes’ principle', 'Ohm’s law', 'Throwing gas backward gives the rocket momentum forward.'),
 qz('Как увеличить конечную скорость ракеты по формуле Циолковского?', 'Увеличить скорость истечения или долю топлива', 'Уменьшить число ступеней', 'Использовать меньше топлива', 'v = u·ln(m₀/m).',
    'How can a rocket’s final speed be increased by the Tsiolkovsky formula?', 'Raise the exhaust speed or the fuel fraction', 'Reduce the number of stages', 'Use less fuel', 'v = u·ln(m₀/m).'),
 qz('Два одинаковых шара упруго сталкиваются, один неподвижен. Что произойдёт?', 'Движущийся остановится, а неподвижный поедет с той же скоростью', 'Оба остановятся', 'Оба поедут вдвое медленнее', 'При равных массах скорости «обмениваются».',
    'Two identical balls collide elastically, one stationary. What happens?', 'The moving one stops and the stationary one moves off with the same speed', 'Both stop', 'Both move at half the speed', 'For equal masses the speeds “exchange”.'),
]

js = r'''
const T={ru:{
 clLabel:"Две тележки до и после столкновения",imLabel:"График силы удара в зависимости от времени остановки",rkLabel:"Ракета и шкала скорости до орбитальной",
 kinds:["Упругий","Неупругий (слипаются)"],
 clFb:"Импульс системы сохраняется при любом ударе.",imFb:"Чем дольше остановка, тем меньше сила.",rkFb:"Для орбиты нужна почти вся масса — топливо."},
 en:{
 clLabel:"Two carts before and after a collision",imLabel:"A graph of the impact force against the stopping time",rkLabel:"A rocket and a speed scale up to orbital speed",
 kinds:["Elastic","Inelastic (stick together)"],
 clFb:"The momentum of the system is conserved in any collision.",imFb:"The longer the stopping, the smaller the force.",rkFb:"To reach orbit almost all the mass must be fuel."}};
function drawCl(){const t=tt(),k=+$("ck").value,m1=+$("c1").value,u1=+$("v1").value,m2=+$("c2").value,u2=+$("v2").value;
 let a1,a2;if(k===0){a1=((m1-m2)*u1+2*m2*u2)/(m1+m2);a2=((m2-m1)*u2+2*m1*u1)/(m1+m2)}else{a1=a2=(m1*u1+m2*u2)/(m1+m2)}
 const P=m1*u1+m2*u2,E0=0.5*m1*u1*u1+0.5*m2*u2*u2,E1=0.5*m1*a1*a1+0.5*m2*a2*a2;
 const bw=m=>30+m*6;let g='<line x1="30" y1="125" x2="570" y2="125" stroke="#18181a" stroke-width="2"/>';
 g+='<rect x="'+(120-bw(m1)/2)+'" y="'+(85-0)+'" width="'+bw(m1)+'" height="40" fill="#b6533f" stroke="#18181a"/><rect x="'+(180)+'" y="85" width="'+bw(m2)+'" height="40" fill="#3f5f8f" stroke="#18181a"/>'+svgText(120,108,"m₁","#fff","middle",12)+svgText(180+bw(m2)/2,108,"m₂","#fff","middle",12);
 g+=arrow(120,70,120+u1*18,70,"#18181a",3)+arrow(180+bw(m2)/2,60,180+bw(m2)/2+u2*18,60,"#18181a",3);
 g+='<rect x="'+(420-bw(m1)/2)+'" y="85" width="'+bw(m1)+'" height="40" fill="#b6533f" stroke="#18181a"/><rect x="'+(k===1?420+bw(m1)/2:480)+'" y="85" width="'+bw(m2)+'" height="40" fill="#3f5f8f" stroke="#18181a"/>'+svgText(420,108,"m₁","#fff","middle",12);
 g+=arrow(420,170,420+a1*18,170,"#2f6f5d",3)+arrow(480+bw(m2)/2,190,480+bw(m2)/2+a2*18,190,"#2f6f5d",3)+svgText(120,35,(lang==="ru"?"до":"before"),"#66666b","middle",12)+svgText(450,35,(lang==="ru"?"после":"after"),"#66666b","middle",12);
 $("clSvg").innerHTML=g;
 $("c1Out").textContent=fmt(m1,1)+UN[lang].kg;$("v1Out").textContent=fmt(u1,1)+UN[lang].ms;$("c2Out").textContent=fmt(m2,1)+UN[lang].kg;$("v2Out").textContent=fmt(u2,1)+UN[lang].ms;
 $("cP").textContent=fmt(P,1)+(lang==="ru"?" кг·м/с":" kg·m/s");$("cV").textContent=fmt(a1,2)+" ; "+fmt(a2,2)+UN[lang].ms;$("cE").textContent=fmt(E0-E1,1)+UN[lang].J;$("clFb").textContent=t.clFb}
["ck","c1","v1","c2","v2"].forEach(id=>$(id).addEventListener("input",drawCl));
function drawIm(){const t=tt(),m=+$("im").value,v=+$("iv").value,dt=+$("it").value,p=m*v,F=p/dt;
 const X=x=>50+Math.log10(x/0.01)/2*500,Y=f=>220-Math.min(1,Math.log10(Math.max(f,1))/6)*195;
 let g='<line x1="50" y1="220" x2="550" y2="220" stroke="#18181a"/><line x1="50" y1="20" x2="50" y2="220" stroke="#18181a"/>';
 [0.01,0.1,1].forEach(x=>g+=svgText(X(x),236,x,"#66666b","middle",10));[10,1000,100000].forEach(f=>g+=svgText(44,Y(f)+4,num(f),"#66666b","end",10)+'<line x1="50" y1="'+Y(f)+'" x2="550" y2="'+Y(f)+'" stroke="#e3e1da"/>');
 const pts=[];for(let i=0;i<=100;i++){const x=0.01*Math.pow(100,i/100);pts.push(X(x)+","+Y(p/x))}
 g+='<polyline fill="none" stroke="#3f5f8f" stroke-width="3" points="'+pts.join(" ")+'"/><circle cx="'+X(dt)+'" cy="'+Y(F)+'" r="7" fill="#b6533f"/>'+svgText(550,250,"Δt, "+(lang==="ru"?"с":"s"),"#66666b","end",10)+svgText(56,14,"F, N","#18181a","start",11);
 $("imSvg").innerHTML=g;
 $("imOut").textContent=m+UN[lang].kg;$("ivOut").textContent=fmt(v,1)+UN[lang].ms;$("itOut").textContent=fmt(dt,2)+UN[lang].s;
 $("iJ").textContent=fmt(p,0)+(lang==="ru"?" кг·м/с":" kg·m/s");$("iF").textContent=num(Math.round(F))+UN[lang].N;$("iW").textContent=fmt(F/(m*9.8),1)+"×";$("imFb").textContent=t.imFb}
["im","iv","it"].forEach(id=>$(id).addEventListener("input",drawIm));
function drawRk(){const t=tt(),u=+$("re").value,r=+$("rm").value,v=u*Math.log(r),frac=1-1/r;
 const X=s=>40+s/10*520;let g='<rect x="40" y="150" width="520" height="22" fill="#e3e1da"/><rect x="40" y="150" width="'+Math.max(0,Math.min(520,X(v)-40))+'" height="22" fill="'+(v>=7.8?"#2f6f5d":"#b6533f")+'"/>';
 [0,2,4,6,8,10].forEach(s=>g+='<line x1="'+X(s)+'" y1="145" x2="'+X(s)+'" y2="178" stroke="#18181a"/>'+svgText(X(s),195,s,"#66666b","middle",11));
 g+='<line x1="'+X(7.8)+'" y1="110" x2="'+X(7.8)+'" y2="150" stroke="#2f6f5d" stroke-width="2"/>'+svgText(X(7.8),102,(lang==="ru"?"орбита 7,8":"orbit 7.8"),"#2f6f5d","middle",11);
 g+='<polygon points="'+(X(Math.min(v,10)))+',60 '+(X(Math.min(v,10))-10)+',95 '+(X(Math.min(v,10))+10)+',95" fill="#18181a"/>'+svgText(560,230,"km/s","#66666b","end",10);
 $("rkSvg").innerHTML=g;
 $("reOut").textContent=fmt(u,1)+(lang==="ru"?" км/с":" km/s");$("rmOut").textContent=fmt(r,1);
 $("rV").textContent=fmt(v,2)+(lang==="ru"?" км/с":" km/s");$("rO").textContent=v>=7.8?(lang==="ru"?"да, хватает":"yes, enough"):(lang==="ru"?"нет, не хватает":"no, not enough");$("rT").textContent=fmt(frac*100,0)+"%";$("rkFb").textContent=t.rkFb}
["re","rm"].forEach(id=>$(id).addEventListener("input",drawRk));
const LAB={ru:{clSvg:T.ru.clLabel,imSvg:T.ru.imLabel,rkSvg:T.ru.rkLabel},en:{clSvg:T.en.clLabel,imSvg:T.en.imLabel,rkSvg:T.en.rkLabel}};
function drawAll(){fillSel("ck",T[lang].kinds,0);drawCl();drawIm();drawRk()}
'''

c = dict(n='34', slug='34-momentum.html', block='VI', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Импульс и закон его сохранения', 'Momentum and its conservation'),
 desc='Глава 34 Атласа физики: импульс тела и силы, закон сохранения импульса, упругие и неупругие удары, подушки безопасности, реактивное движение и формула Циолковского.',
 lead=('Почему приземляются на согнутые ноги, а ракета летит в пустоте. Импульс, удары и реактивное движение.',
       'Why people land on bent legs and a rocket flies in a void. Momentum, collisions and jet propulsion.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('mom', 'Импульс', 'Momentum'), ('impact', 'Время торможения', 'Stopping time'), ('rocket', 'Ракета', 'Rocket'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Мальчик спрыгивает с забора высотой в два метра. Если он приземлится на прямые ноги, боль будет такой, что можно сломать кость. Если же присядет и перекатится — ничего не почувствует. Скорость перед ударом и масса одни и те же.</p><p>Что изменилось, из-за чего сила удара стала меньше?</p>',
         '<p>A boy jumps off a fence two metres high. If he lands on straight legs the pain is such that a bone may break. If he crouches and rolls he feels nothing. The speed before the impact and the mass are the same.</p><p>What changed to make the force of the impact smaller?</p>'),
 hint=stdhint('Удар и время торможения', 'An impact and the stopping time'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: время остановки', 'The answer: the stopping time'),
 answer=('<p>Изменение импульса мальчика одно и то же — от <em>mv</em> до нуля. Но по закону <em>F·Δt = Δp</em> средняя сила <em>F = Δp / Δt</em>. На прямых ногах остановка занимает сотые доли секунды — сила огромна. Если присесть и перекатиться, время остановки в десять раз больше, и сила в десять раз меньше (модель 2).</p><p>Так же работают подушка безопасности, зона смятия кузова и мягкий шлем: они не меняют импульс, они растягивают время удара.</p>',
         '<p>The change of the boy’s momentum is the same — from <em>mv</em> to zero. But by <em>F·Δt = Δp</em> the average force is <em>F = Δp / Δt</em>. On straight legs the stop takes hundredths of a second — the force is huge. If he crouches and rolls the stopping time is ten times longer and the force ten times smaller (model 2).</p><p>An airbag, a car’s crumple zone and a soft helmet work the same way: they do not change the momentum, they stretch the time of the impact.</p>'),
 sources=[
  ('Импульс, закон сохранения импульса, удары —', 'Momentum, conservation of momentum, collisions —', LINK('https://openstax.org/books/university-physics-volume-1/pages/9-introduction', 'OpenStax University Physics, Vol. 1, гл. 9') + ', ' + LINK('https://en.wikipedia.org/wiki/Momentum', 'Wikipedia: Momentum')),
  ('Формула Циолковского —', 'The Tsiolkovsky rocket equation —', LINK('https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation', 'Wikipedia: Tsiolkovsky rocket equation')),
  ('Скорость истечения газов у химических ракетных двигателей — несколько км/с —', 'The exhaust speed of chemical rocket engines — a few km/s —', LINK('https://en.wikipedia.org/wiki/Specific_impulse', 'Wikipedia: Specific impulse'))],
 note=stdnote('Скорости и массы в моделях — условные; ракетная формула идеальная (без тяготения и сопротивления воздуха).', 'The speeds and masses in the models are assumed; the rocket formula is ideal (no gravity or air drag).'),
 prev=('33-newtons-laws.html', 'Глава 33 · Законы Ньютона', 'Chapter 33 · Newton’s laws'),
 next=('35-rotation-torque.html', 'Глава 35 · Вращение и момент силы', 'Chapter 35 · Rotation and torque'),
 js=js)
build(c)
