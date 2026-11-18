# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ЗАКОН ОТРАЖЕНИЯ', 'THE LAW OF REFLECTION', 'lrSvg', '0 0 600 250',
  slider('la', 'Угол падения луча', 'Angle of the incident ray', 0, 80, 1, 40) + slider('ld', 'Поворот зеркала', 'Tilt of the mirror', -20, 20, 1, 0),
  stats([('lI', 'Угол падения i', 'Angle of incidence i'), ('lR', 'Угол отражения r', 'Angle of reflection r'), ('lT', 'Поворот отражённого луча', 'Turn of the reflected ray')]),
  'lrFb', 'Схема условная: углы отсчитываются от перпендикуляра к зеркалу; положительный наклон — по часовой стрелке.',
  'A schematic drawing: angles are measured from the perpendicular to the mirror; a positive tilt is clockwise.')
s1 = section('law', 'Закон отражения', 'The law of reflection',
 bd('<p>Когда свет падает на гладкую поверхность, он отражается. <strong>Закон отражения</strong>: падающий луч, отражённый луч и перпендикуляр к поверхности в точке падения лежат в одной плоскости, а <strong>угол падения равен углу отражения</strong>. Углы отсчитывают не от самой поверхности, а от перпендикуляра к ней.</p><p>От гладкого зеркала свет отражается в одном направлении — это <strong>зеркальное отражение</strong>. От шероховатой поверхности (бумага, стена) он рассеивается во все стороны — так мы видим несветящиеся предметы с любого места.</p>',
    '<p>When light falls on a smooth surface it is reflected. The <strong>law of reflection</strong>: the incident ray, the reflected ray and the perpendicular to the surface at the point of incidence lie in one plane and the <strong>angle of incidence equals the angle of reflection</strong>. The angles are measured not from the surface itself but from the perpendicular to it.</p><p>From a smooth mirror light is reflected in one direction — <strong>specular reflection</strong>. From a rough surface (paper, a wall) it is scattered in all directions — that is how we see non-luminous objects from any place.</p>')
 + formula('i = r', 'при повороте зеркала на угол δ отражённый луч поворачивается на 2δ', 'when the mirror turns by an angle δ the reflected ray turns by 2δ'),
 lab1)

lab2 = model(2, 'ПЛОСКОЕ ЗЕРКАЛО', 'A PLANE MIRROR', 'pmSvg', '0 0 600 250',
  slider('pd', 'Расстояние до зеркала', 'Distance to the mirror', 0.5, 5, 0.1, 2) + slider('ph', 'Ваш рост', 'Your height', 1.0, 2.0, 0.05, 1.7),
  stats([('pI', 'Изображение находится за зеркалом на', 'The image is behind the mirror at'), ('pR', 'Расстояние до своего изображения', 'Distance to your image'), ('pM', 'Наименьшая высота зеркала для полного роста', 'The smallest mirror height to see your full height')]),
  'pmFb', 'Схема условная: вид сбоку; зеркало вертикальное.',
  'A schematic drawing: a side view; the mirror is vertical.')
s2 = section('plane', 'Плоское зеркало', 'The plane mirror',
 bd('<p>В плоском зеркале мы видим <strong>мнимое изображение</strong>: оно получается на продолжении отражённых лучей, за зеркалом, и в нём не собираются реальные лучи. Изображение равно предмету по размеру, находится на таком же расстоянии за зеркалом, как предмет перед ним, и «перевёрнуто» слева направо.</p><p>Поэтому расстояние от вас до вашего изображения вдвое больше расстояния до зеркала. Из-за подобия треугольников, чтобы видеть себя в полный рост, зеркало должно быть вдвое ниже вас — независимо от расстояния до него.</p>',
    '<p>In a plane mirror we see a <strong>virtual image</strong>: it forms on the continuation of the reflected rays behind the mirror and no real rays gather in it. The image equals the object in size, is as far behind the mirror as the object is in front of it, and is “reversed” left to right.</p><p>So the distance from you to your image is twice the distance to the mirror. Because of similar triangles, to see yourself at full height the mirror must be half your height — whatever the distance to it.</p>')
 + formula('d′ = d,   h_зеркала = H / 2', 'мнимое изображение за зеркалом; минимальное зеркало вдвое ниже человека', 'a virtual image behind the mirror; the minimum mirror is half the person’s height'),
 lab2)

lab3 = model(3, 'ПАРАБОЛИЧЕСКОЕ ЗЕРКАЛО', 'A PARABOLIC MIRROR', 'pbSvg', '0 0 600 250',
  slider('bf', 'Фокусное расстояние', 'Focal length', 0.2, 1.0, 0.05, 0.5) + slider('bd', 'Диаметр зеркала', 'Mirror diameter', 0.5, 2.0, 0.1, 1.2),
  stats([('bH', 'Глубина чаши h = D²/(16f)', 'Depth of the bowl h = D²/(16f)'), ('bP', 'Мощность в фокусе', 'Power at the focus'), ('bT', 'Время нагрева 1 л воды от 20 до 100 °C', 'Time to heat 1 L of water from 20 to 100 °C')]),
  'pbFb', 'Схема условная: солнечная кухня. Освещённость 1000 Вт/м², коэффициент отражения 0,8, потерь тепла нет; в реальности воды греется дольше.',
  'A schematic drawing: a solar cooker. Illumination 1,000 W/m², reflectance 0.8, no heat losses; in reality water takes longer to heat.')
s3 = section('parab', 'Зеркало-концентратор', 'The concentrating mirror',
 bd('<p>У зеркала в форме параболоида есть замечательное свойство: все лучи, идущие параллельно оси, после отражения собираются в одной точке — <strong>фокусе</strong>. Поэтому им пользуются «наоборот» с источником света: прожектор и автомобильная фара с лампой в фокусе дают параллельный пучок, а спутниковая антенна и телескоп собирают далёкие сигналы в одной точке.</p><p>Солнечные кухни — чаши с зеркальной поверхностью — собирают солнечный свет с большой площади на маленькую кастрюлю. Мощность прямого солнечного света у поверхности Земли — около 1000 Вт на квадратный метр, а в горах, где воздух чистый и тонкий, света заметно больше. Профиль параболы: <em>y = x² / (4f)</em>.</p>',
    '<p>A mirror in the shape of a paraboloid has a remarkable property: all rays travelling parallel to the axis gather after reflection at one point — the <strong>focus</strong>. So it is used “in reverse” with a light source: a searchlight and a car headlight with the lamp at the focus give a parallel beam, while a satellite dish and a telescope gather distant signals at one point.</p><p>Solar cookers — bowls with a mirror surface — gather sunlight from a large area onto a small pot. The power of direct sunlight at the Earth’s surface is about 1,000 W per square metre and in the mountains, where the air is clean and thin, there is noticeably more light. The profile of the parabola: <em>y = x² / (4f)</em>.</p>'),
 lab3)

tasks = [
 task(1, 'Угол отражения', 'The angle of reflection', 'Луч падает на зеркало под углом 35° к перпендикуляру. Чему равны угол отражения и угол между падающим и отражённым лучами?', 'A ray falls on a mirror at 35° to the perpendicular. What are the angle of reflection and the angle between the incident and reflected rays?',
  'i = 35°', 'i = 35°', 'r = i = 35°.<br>Угол между лучами: 35° + 35° = 70°.', 'r = i = 35°.<br>The angle between the rays: 35° + 35° = 70°.', '35° и 70°.', '35° and 70°.', True),
 task(2, 'Поворот зеркала', 'Turning a mirror', 'Зеркало повернули на 10°, а луч остался прежним. На сколько повернулся отражённый луч?', 'A mirror is turned by 10° while the incident ray stays the same. By how much does the reflected ray turn?',
  'δ = 10°', 'δ = 10°', 'Отражённый луч поворачивается на 2δ = 20°.', 'The reflected ray turns by 2δ = 20°.', '20°.', '20°.'),
 task(3, 'Расстояние до изображения', 'Distance to the image', 'Вы стоите в 2 м от плоского зеркала. Каково расстояние от вас до вашего изображения?', 'You stand 2 m from a plane mirror. What is the distance from you to your image?',
  'd = 2 м', 'd = 2 m', 'Изображение за зеркалом на 2 м, значит, от вас до него 2 + 2 = 4 м.', 'The image is 2 m behind the mirror, so from you to it is 2 + 2 = 4 m.', '4 м.', '4 m.'),
 task(4, 'Зеркало на двери', 'A mirror on a door', 'Какой наименьшей высоты нужно зеркало, чтобы человек ростом 1,8 м видел себя в полный рост?', 'What is the smallest mirror height needed for a 1.8 m person to see their full height?',
  'H = 1,8 м', 'H = 1.8 m', 'h = H / 2 = 0,9 м (не зависит от расстояния до зеркала).', 'h = H / 2 = 0.9 m (independent of the distance to the mirror).', '0,9 м.', '0.9 m.'),
 task(5, 'Глубина чаши', 'The depth of a bowl', 'Параболическое зеркало с фокусным расстоянием 0,5 м и диаметром 1,2 м. Какова глубина чаши?', 'A parabolic mirror with a focal length of 0.5 m and a diameter of 1.2 m. How deep is the bowl?',
  'f = 0,5 м, D = 1,2 м', 'f = 0.5 m, D = 1.2 m', 'При x = D/2: h = x² / (4f) = D² / (16f) = 1,44 / 8 = 0,18 м.', 'At x = D/2: h = x² / (4f) = D² / (16f) = 1.44 / 8 = 0.18 m.', '18 см.', '18 cm.'),
 task(6, 'Солнечная кухня', 'A solar cooker', 'Зеркало диаметром 1,2 м собирает свет с освещённостью 1000 Вт/м² (отражение 0,8). За какое время можно нагреть 1 л воды от 20 до 100 °C (потери не учитывать)? c = 4186 Дж/(кг·°C).', 'A mirror of 1.2 m diameter gathers light of 1,000 W/m² (reflectance 0.8). How long to heat 1 L of water from 20 to 100 °C (ignore losses)? c = 4,186 J/(kg·°C).',
  'D = 1,2 м, I = 1000 Вт/м², k = 0,8, m = 1 кг, Δt = 80 °C', 'D = 1.2 m, I = 1,000 W/m², k = 0.8, m = 1 kg, Δt = 80 °C', 'S = π·D²/4 = 1,131 м².<br>P = I·S·k = 1000 · 1,131 · 0,8 ≈ 905 Вт.<br>Q = c·m·Δt = 4186 · 1 · 80 = 334 880 Дж.<br>t = Q / P ≈ 370 с ≈ 6 мин.', 'S = π·D²/4 = 1.131 m².<br>P = I·S·k = 1000 · 1.131 · 0.8 ≈ 905 W.<br>Q = c·m·Δt = 4186 · 1 · 80 = 334,880 J.<br>t = Q / P ≈ 370 s ≈ 6 min.', 'около 6 минут в идеале; в жизни дольше из-за потерь.', 'about 6 minutes ideally; in life longer because of losses.'),
]

quiz = [
 qz('Чему равен угол отражения?', 'Углу падения', 'Вдвое больше угла падения', 'Нулю', 'Закон отражения: i = r.',
    'What does the angle of reflection equal?', 'The angle of incidence', 'Twice the angle of incidence', 'Zero', 'The law of reflection: i = r.'),
 qz('От чего отсчитывают углы падения и отражения?', 'От перпендикуляра к поверхности', 'От самой поверхности', 'От горизонта', 'Так принято в законе отражения.',
    'From what are the angles of incidence and reflection measured?', 'The perpendicular to the surface', 'The surface itself', 'The horizon', 'That is the convention in the law of reflection.'),
 qz('Какое изображение даёт плоское зеркало?', 'Мнимое, равное предмету', 'Действительное, уменьшенное', 'Действительное, увеличенное', 'Лучи не пересекаются, изображение за зеркалом.',
    'What image does a plane mirror give?', 'Virtual, equal to the object', 'Real, reduced', 'Real, magnified', 'The rays do not meet; the image is behind the mirror.'),
 qz('Если подойти к зеркалу ближе, видимый рост изображения…', 'Не изменится', 'Увеличится', 'Уменьшится', 'Изображение всегда равно предмету.',
    'If you step closer to the mirror the apparent height of your image…', 'Does not change', 'Grows', 'Shrinks', 'The image always equals the object.'),
 qz('На сколько повернётся отражённый луч при повороте зеркала на 15°?', 'На 30°', 'На 15°', 'На 7,5°', 'Поворот отражённого луча — 2δ.',
    'By how much does the reflected ray turn when the mirror turns 15°?', 'By 30°', 'By 15°', 'By 7.5°', 'The reflected ray turns by 2δ.'),
 qz('Почему мы видим бумагу с любого места?', 'Она рассеивает свет во все стороны', 'Она сама светится', 'Она отражает свет в одну сторону', 'Шероховатая поверхность даёт рассеянное отражение.',
    'Why can we see paper from any place?', 'It scatters light in all directions', 'It glows itself', 'It reflects light in one direction', 'A rough surface gives diffuse reflection.'),
 qz('Что собирает параболическое зеркало в одной точке?', 'Лучи, параллельные оси', 'Любые лучи', 'Лучи, идущие под углом 45°', 'Это свойство параболоида.',
    'What does a parabolic mirror gather at one point?', 'Rays parallel to the axis', 'Any rays', 'Rays at 45°', 'It is the property of a paraboloid.'),
 qz('Какой минимальной высоты нужно зеркало, чтобы увидеть себя в полный рост?', 'Вдвое ниже вашего роста', 'Вашего роста', 'Вдвое выше вашего роста', 'Подобие треугольников даёт H/2.',
    'What is the minimum mirror height needed to see your full height?', 'Half your height', 'Your height', 'Twice your height', 'Similar triangles give H/2.'),
]

js = r'''
const T={ru:{
 lrLabel:"Луч, падающий на зеркало, и отражённый луч",pmLabel:"Человек, плоское зеркало и мнимое изображение за ним",pbLabel:"Параболическое зеркало: параллельные лучи собираются в фокусе",
 lrFb:"Угол падения равен углу отражения; при повороте зеркала на δ луч поворачивается на 2δ.",pmFb:"Изображение за зеркалом так же далеко, как вы перед ним.",pbFb:"Лучи, идущие параллельно оси, собираются в фокусе."},
 en:{
 lrLabel:"A ray falling on a mirror and the reflected ray",pmLabel:"A person, a plane mirror and the virtual image behind it",pbLabel:"A parabolic mirror: parallel rays gather at the focus",
 lrFb:"The angle of incidence equals the angle of reflection; when the mirror turns by δ the ray turns by 2δ.",pmFb:"The image behind the mirror is as far as you are in front of it.",pbFb:"Rays parallel to the axis gather at the focus."}};
function drawLr(){const t=tt(),a=+$("la").value,dl=+$("ld").value,A=a*Math.PI/180,D=dl*Math.PI/180;
 const cx=300,cy=150,d=[Math.sin(A),Math.cos(A)],n=[-Math.sin(D),Math.cos(D)],dn=d[0]*n[0]+d[1]*n[1];
 const r=[d[0]-2*dn*n[0],d[1]-2*dn*n[1]];
 const ix=cx-d[0]*130,iy=cy-d[1]*130;
 let g='<line x1="'+(cx-200*Math.cos(D))+'" y1="'+(cy-200*Math.sin(D))+'" x2="'+(cx+200*Math.cos(D))+'" y2="'+(cy+200*Math.sin(D))+'" stroke="#3f5f8f" stroke-width="5"/>';
 g+='<line x1="'+cx+'" y1="'+cy+'" x2="'+(cx+Math.sin(D)*110)+'" y2="'+(cy-Math.cos(D)*110)+'" stroke="#9a9a9a" stroke-dasharray="4 3"/>';
 g+=arrow(ix,iy,cx,cy,"#f0a020",3)+arrow(cx,cy,cx+r[0]*130,cy+r[1]*130,"#b6533f",3);
 const ang=Math.round(Math.abs(a+dl));
 $("lrSvg").innerHTML=g;
 $("laOut").textContent=a+"°";$("ldOut").textContent=dl+"°";
 $("lI").textContent=ang+"°";$("lR").textContent=ang+"°";$("lT").textContent=Math.abs(2*dl)+"°";$("lrFb").textContent=t.lrFb}
["la","ld"].forEach(id=>$(id).addEventListener("input",drawLr));
function drawPm(){const t=tt(),d=+$("pd").value,H=+$("ph").value,sc=60;
 const xm=300,xp=xm-d*sc,xi=xm+d*sc,y0=200;
 let g='<line x1="'+xm+'" y1="20" x2="'+xm+'" y2="220" stroke="#3f5f8f" stroke-width="5"/><line x1="30" y1="220" x2="570" y2="220" stroke="#c9c2b0"/>';
 g+='<line x1="'+xp+'" y1="220" x2="'+xp+'" y2="'+(220-H*80)+'" stroke="#18181a" stroke-width="6"/><line x1="'+xi+'" y1="220" x2="'+xi+'" y2="'+(220-H*80)+'" stroke="#18181a" stroke-width="6" stroke-dasharray="5 4" opacity="0.5"/>';
 g+='<line x1="'+xp+'" y1="'+(220-H*80)+'" x2="'+xi+'" y2="'+(220-H*80)+'" stroke="#f0a020" stroke-dasharray="3 3"/>';
 g+=svgText(xp,238,"d","#18181a","middle",11)+svgText(xi,238,"d","#9a9a9a","middle",11);
 g+='<rect x="'+(xm-3)+'" y="'+(220-H*80*0.75)+'" width="6" height="'+(H*80/2)+'" fill="#b6533f"/>';
 $("pmSvg").innerHTML=g;
 $("pdOut").textContent=fmt(d,1)+UN[lang].m;$("phOut").textContent=fmt(H,2)+UN[lang].m;
 $("pI").textContent=fmt(d,1)+UN[lang].m;$("pR").textContent=fmt(2*d,1)+UN[lang].m;$("pM").textContent=fmt(H/2,2)+UN[lang].m;$("pmFb").textContent=t.pmFb}
["pd","ph"].forEach(id=>$(id).addEventListener("input",drawPm));
function drawPb(){const t=tt(),f=+$("bf").value,D=+$("bd").value,sc=170/1.0,hh=D*sc/2;
 const px=x=>x,py=x=>x;
 const X0=140,Yc=125;let pts=[];for(let i=-50;i<=50;i++){const y=i/50*D/2;const x=y*y/(4*f);pts.push((X0+x*sc)+","+(Yc-y*sc))}
 let g='<polyline fill="none" stroke="#3f5f8f" stroke-width="4" points="'+pts.join(" ")+'"/><line x1="40" y1="125" x2="570" y2="125" stroke="#c9c2b0" stroke-dasharray="4 3"/>';
 const fx=X0+f*sc;[-0.85,-0.55,-0.25,0.25,0.55,0.85].forEach(k=>{const y=k*D/2,x=y*y/(4*f);g+='<line x1="'+(X0+x*sc+260)+'" y1="'+(Yc-y*sc)+'" x2="'+(X0+x*sc)+'" y2="'+(Yc-y*sc)+'" stroke="#f0a020"/><line x1="'+(X0+x*sc)+'" y1="'+(Yc-y*sc)+'" x2="'+fx+'" y2="'+Yc+'" stroke="#f0a020"/>'});
 g+='<circle cx="'+fx+'" cy="'+Yc+'" r="6" fill="#b6533f"/>'+svgText(fx,Yc+22,"F","#b6533f","middle",13);
 const h=D*D/(16*f),S=Math.PI*D*D/4,P=1000*S*0.8,Q=4186*80,tm=Q/P;
 $("pbSvg").innerHTML=g;
 $("bfOut").textContent=fmt(f,2)+UN[lang].m;$("bdOut").textContent=fmt(D,1)+UN[lang].m;
 $("bH").textContent=fmt(h*100,0)+(lang==="ru"?" см":" cm");$("bP").textContent=fmt(P,0)+UN[lang].W;$("bT").textContent=fmt(tm/60,1)+UN[lang].min;$("pbFb").textContent=t.pbFb}
["bf","bd"].forEach(id=>$(id).addEventListener("input",drawPb));
const LAB={ru:{lrSvg:T.ru.lrLabel,pmSvg:T.ru.pmLabel,pbSvg:T.ru.pbLabel},en:{lrSvg:T.en.lrLabel,pmSvg:T.en.pmLabel,pbSvg:T.en.pbLabel}};
function drawAll(){drawLr();drawPm();drawPb()}
'''

c = dict(n='30', slug='30-reflection.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Отражение света', 'Reflection of light'),
 desc='Глава 30 Атласа физики: закон отражения, плоское зеркало, мнимое изображение, параболическое зеркало и солнечная кухня.',
 lead=('Зеркало в прихожей и солнечная кухня в горах. Закон отражения, мнимое изображение, параболическое зеркало.',
       'A mirror in the hall and a solar cooker in the mountains. The law of reflection, the virtual image, the parabolic mirror.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('law', 'Закон отражения', 'Law of reflection'), ('plane', 'Плоское зеркало', 'Plane mirror'), ('parab', 'Параболическое зеркало', 'Parabolic mirror'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вы хотите видеть себя в зеркале в полный рост и просите отца купить большое зеркало — «во весь рост». Отец говорит: «Достаточно вдвое меньшего, и неважно, далеко ты стоишь или близко». Вы не верите.</p><p>Кто прав: можно ли увидеть себя целиком в зеркале вдвое ниже вашего роста?</p>',
         '<p>You want to see yourself full-length in a mirror and ask your father to buy a big one — “the full height”. He says: “A mirror half that size is enough and it does not matter whether you stand far or near.” You do not believe it.</p><p>Who is right: can you see yourself whole in a mirror half your height?</p>'),
 hint=stdhint('Плоское зеркало', 'A plane mirror'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: подобные треугольники', 'The answer: similar triangles'),
 answer=('<p>Отец прав. Луч от макушки, отражаясь, должен попасть в глаз, а луч от ступней — тоже. Изображение находится за зеркалом так же далеко, как вы перед ним, и из подобия треугольников нижний край зеркала должен быть на середине расстояния от глаза до пола, а верхний — на середине расстояния от глаза до макушки. Вместе это ровно половина роста, и расстояние до зеркала в расчёте сокращается.</p><p>Проверьте: с зеркалом 0,9 м человек ростом 1,8 м видит себя полностью (задача 4).</p>',
         '<p>Your father is right. The ray from the top of the head must reflect into the eye and so must the ray from the feet. The image is as far behind the mirror as you are in front of it and from similar triangles the lower edge of the mirror must be halfway between the eye and the floor and the upper edge halfway between the eye and the top of the head. Together that is exactly half your height and the distance to the mirror cancels out in the calculation.</p><p>Check: with a 0.9 m mirror a 1.8 m person sees themselves entirely (problem 4).</p>'),
 sources=[
  ('Закон отражения, плоское зеркало, мнимое изображение —', 'The law of reflection, the plane mirror, the virtual image —', LINK('https://openstax.org/books/university-physics-volume-3/pages/1-5-reflection', 'OpenStax University Physics, Vol. 3, § 1.5') + ', ' + LINK('https://en.wikipedia.org/wiki/Reflection_(physics)', 'Wikipedia: Reflection')),
  ('Параболическое зеркало и солнечная кухня —', 'The parabolic mirror and the solar cooker —', LINK('https://en.wikipedia.org/wiki/Parabolic_reflector', 'Wikipedia: Parabolic reflector') + ', ' + LINK('https://en.wikipedia.org/wiki/Solar_cooker', 'Wikipedia: Solar cooker')),
  ('Освещённость прямым солнечным светом ≈ 1000 Вт/м² —', 'Direct sunlight irradiance ≈ 1,000 W/m² —', LINK('https://en.wikipedia.org/wiki/Solar_irradiance', 'Wikipedia: Solar irradiance')),
  ('Удельная теплоёмкость воды 4186 Дж/(кг·°C) — глава 10 этого атласа.', 'The specific heat capacity of water, 4,186 J/(kg·°C) — chapter 10 of this atlas.', '')],
 note=stdnote('Освещённость 1000 Вт/м² и коэффициент отражения 0,8 — условные значения для модели солнечной кухни.', 'The irradiance of 1,000 W/m² and the reflectance of 0.8 are assumed values for the solar-cooker model.'),
 prev=('29-light-and-shadows.html', 'Глава 29 · Свет и тени', 'Chapter 29 · Light and shadows'),
 next=('31-refraction-lenses.html', 'Глава 31 · Преломление и линзы', 'Chapter 31 · Refraction and lenses'),
 js=js)
build(c)
