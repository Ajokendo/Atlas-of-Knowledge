# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ТЕНЬ И ВЫСОТА СОЛНЦА', 'A SHADOW AND THE HEIGHT OF THE SUN', 'shSvg', '0 0 600 250',
  slider('sh', 'Высота предмета', 'Height of the object', 0.5, 20, 0.5, 5) + slider('sa', 'Высота Солнца над горизонтом', 'Elevation of the Sun above the horizon', 5, 85, 1, 40),
  stats([('sL', 'Длина тени L = H / tg α', 'Shadow length L = H / tan α'), ('sK', 'Отношение тени к высоте', 'Ratio of shadow to height')]),
  'shFb', 'Схема условная: ровная земля, параллельные лучи Солнца (Солнце очень далеко).',
  'A schematic drawing: level ground, parallel rays of the Sun (the Sun is very far away).')
s1 = section('straight', 'Свет идёт прямо: тени', 'Light travels straight: shadows',
 bd('<p>Источники света (Солнце, лампа, огонь) излучают свет, который в однородной среде идёт по прямым линиям — <strong>лучам</strong>. Поэтому за непрозрачным предметом возникает <strong>тень</strong> — область, куда свет не попадает. Если источник не точечный, края тени размыты — это <strong>полутень</strong>.</p><p>Прямолинейность света позволяет измерять высоту по длине тени. Лучи Солнца почти параллельны, и предмет с его тенью образуют прямоугольный треугольник. Треугольники для двух предметов подобны, если Солнце на одной высоте, поэтому</p>',
    '<p>Light sources (the Sun, a lamp, fire) emit light that travels in straight lines — <strong>rays</strong> — in a uniform medium. So behind an opaque object a <strong>shadow</strong> arises — a region the light does not reach. If the source is not a point the edges of the shadow are blurred — this is the <strong>penumbra</strong>.</p><p>The straightness of light lets us measure heights from the length of a shadow. The Sun’s rays are almost parallel and an object with its shadow form a right-angled triangle. The triangles for two objects are similar if the Sun is at one height, therefore</p>')
 + formula('H₁ / L₁ = H₂ / L₂,   L = H / tg α', 'зная шест и его тень, можно найти высоту дерева, юрты или здания', 'knowing a pole and its shadow we can find the height of a tree, a yurt or a building')
 + bd('<p>На прямолинейности света основаны и <strong>затмения</strong>. Когда Луна встаёт между Землёй и Солнцем, её тень падает на Землю — солнечное затмение; когда Земля закрывает Солнце от Луны — лунное.</p>',
      '<p>Eclipses are also based on the straightness of light. When the Moon stands between the Earth and the Sun its shadow falls on the Earth — a solar eclipse; when the Earth hides the Sun from the Moon — a lunar eclipse.</p>'),
 lab1)

lab2 = model(2, 'КАМЕРА-ОБСКУРА', 'A PINHOLE CAMERA', 'pcSvg', '0 0 600 250',
  slider('ph', 'Высота предмета', 'Height of the object', 0.5, 10, 0.5, 2) + slider('pd', 'Расстояние до предмета', 'Distance to the object', 1, 30, 1, 10) + slider('ps', 'Глубина ящика', 'Depth of the box', 5, 50, 1, 20),
  stats([('pI', 'Высота изображения h = H·s/d', 'Height of the image h = H·s/d'), ('pS', 'Изображение', 'The image')]),
  'pcFb', 'Схема условная: маленькое отверстие, глубина ящика в сантиметрах.',
  'A schematic drawing: a tiny hole, the depth of the box in centimetres.')
s2 = section('pinhole', 'Камера-обскура', 'The pinhole camera',
 bd('<p>Если в тёмном ящике проделать маленькое отверстие, на задней стенке получится <strong>перевёрнутое изображение</strong> предметов снаружи: каждая точка предмета посылает через отверстие один тонкий луч. Из подобия треугольников высота изображения <em>h = H·s/d</em>, где <em>d</em> — расстояние до предмета, <em>s</em> — глубина ящика.</p><p>Это самый простой «фотоаппарат». Чем меньше отверстие, тем резче, но тусклее изображение. Так устроены и первые фотографические камеры, и безобъективные камеры для наблюдения за затмениями.</p>',
    '<p>If a small hole is made in a dark box an <strong>inverted image</strong> of the objects outside forms on the back wall: each point of an object sends one thin ray through the hole. From similar triangles the image height is <em>h = H·s/d</em>, where <em>d</em> is the distance to the object and <em>s</em> the depth of the box.</p><p>This is the simplest “camera”. The smaller the hole the sharper but dimmer the image. The first photographic cameras and the lensless cameras for watching eclipses are built this way.</p>')
 + formula('h / H = s / d', 'изображение перевёрнуто; уменьшается при удалении предмета', 'the image is inverted and shrinks as the object moves away'),
 lab2)

lab3 = model(3, 'КАК ДОЛГО ИДЁТ СВЕТ', 'HOW LONG LIGHT TAKES', 'ltSvg', '0 0 600 250',
  select('lo', 'До какого объекта', 'To which object'),
  stats([('lD', 'Расстояние', 'Distance'), ('lT', 'Время пути света', 'Light travel time')]),
  'ltFb', 'Схема условная, без масштаба. Скорость света c = 299 792 458 м/с (точное значение); расстояния округлены.',
  'A schematic drawing, not to scale. The speed of light c = 299,792,458 m/s (the exact value); the distances are rounded.')
s3 = section('speed', 'Скорость света', 'The speed of light',
 bd('<p>Свет движется очень быстро, но не мгновенно. В вакууме его скорость <strong>c = 299 792 458 м/с</strong> — это примерно 300 000 км/с. Ничто не движется быстрее. За секунду свет семь с половиной раз обогнул бы Землю по экватору.</p><p>Далёкие объекты мы видим такими, какими они были, когда свет от них вышел: Луну — на 1,3 секунды в прошлом, Солнце — на 8,3 минуты, ближайшую звезду — на четыре года. Поэтому расстояния в космосе удобно измерять временем: <strong>световой год</strong> — расстояние, которое свет проходит за год (около 9,46 триллиона километров).</p>',
    '<p>Light travels very fast but not instantly. In a vacuum its speed is <strong>c = 299,792,458 m/s</strong> — about 300,000 km/s. Nothing travels faster. In a second light would go round the Earth along the equator seven and a half times.</p><p>We see distant objects as they were when the light left them: the Moon 1.3 seconds in the past, the Sun 8.3 minutes, the nearest star four years. So distances in space are conveniently measured in time: a <strong>light-year</strong> is the distance light covers in a year (about 9.46 trillion kilometres).</p>')
 + formula('t = s / c', 'c ≈ 3·10⁸ м/с', 'c ≈ 3·10⁸ m/s'),
 lab3)

tasks = [
 task(1, 'Высота дерева', 'The height of a tree', 'Шест высотой 2 м отбрасывает тень 1,5 м, а тополь — тень 12 м. Найдите высоту тополя.', 'A 2 m pole casts a 1.5 m shadow and a poplar a 12 m shadow. Find the height of the poplar.',
  'H₁ = 2 м, L₁ = 1,5 м, L₂ = 12 м', 'H₁ = 2 m, L₁ = 1.5 m, L₂ = 12 m', 'H₂ / L₂ = H₁ / L₁, H₂ = 2 · 12 / 1,5 = 16 м.', 'H₂ / L₂ = H₁ / L₁, H₂ = 2 · 12 / 1.5 = 16 m.', '16 м.', '16 m.', True),
 task(2, 'Длинная тень', 'A long shadow', 'Столб высотой 10 м, Солнце стоит на высоте 30°. Какова длина тени? tg 30° = 0,577.', 'A 10 m pole, the Sun at an elevation of 30°. What is the length of the shadow? tan 30° = 0.577.',
  'H = 10 м, α = 30°', 'H = 10 m, α = 30°', 'L = H / tg α = 10 / 0,577 ≈ 17,3 м.', 'L = H / tan α = 10 / 0.577 ≈ 17.3 m.', 'около 17,3 м.', 'about 17.3 m.'),
 task(3, 'Камера-обскура', 'A pinhole camera', 'Человек ростом 2 м стоит в 10 м от камеры-обскуры глубиной 20 см. Какова высота его изображения?', 'A 2 m person stands 10 m from a pinhole camera 20 cm deep. What is the height of the image?',
  'H = 2 м, d = 10 м, s = 0,2 м', 'H = 2 m, d = 10 m, s = 0.2 m', 'h = H·s / d = 2 · 0,2 / 10 = 0,04 м = 4 см.', 'h = H·s / d = 2 · 0.2 / 10 = 0.04 m = 4 cm.', '4 см, перевёрнутое.', '4 cm, inverted.'),
 task(4, 'Свет от Луны', 'Light from the Moon', 'Расстояние до Луны 384 400 км. За какое время свет от неё доходит до Земли? c = 3·10⁸ м/с (точнее, 299 792 458 м/с).', 'The distance to the Moon is 384,400 km. How long does light from it take to reach Earth? c = 3·10⁸ m/s (more exactly 299,792,458 m/s).',
  's = 3,844·10⁸ м', 's = 3.844·10⁸ m', 't = s / c = 3,844·10⁸ / 2,998·10⁸ ≈ 1,28 с.', 't = s / c = 3.844·10⁸ / 2.998·10⁸ ≈ 1.28 s.', 'около 1,3 с.', 'about 1.3 s.'),
 task(5, 'Свет от Солнца', 'Light from the Sun', 'Расстояние до Солнца 1,496·10¹¹ м. За какое время идёт свет?', 'The distance to the Sun is 1.496·10¹¹ m. How long does light take?',
  's = 1,496·10¹¹ м', 's = 1.496·10¹¹ m', 't = 1,496·10¹¹ / 2,998·10⁸ ≈ 499 с ≈ 8,3 мин.', 't = 1.496·10¹¹ / 2.998·10⁸ ≈ 499 s ≈ 8.3 min.', 'около 8,3 минуты.', 'about 8.3 minutes.'),
 task(6, 'Радиолокация Луны', 'Radar on the Moon', 'Сигнал отправили к Луне и приняли отражённым. Сколько времени он идёт туда и обратно?', 'A signal is sent to the Moon and received reflected. How long does it take to go and return?',
  's = 3,844·10⁸ м', 's = 3.844·10⁸ m', 'Путь туда и обратно 2s: t = 2 · 3,844·10⁸ / 2,998·10⁸ ≈ 2,56 с.', 'The path there and back is 2s: t = 2 · 3.844·10⁸ / 2.998·10⁸ ≈ 2.56 s.', 'около 2,6 с.', 'about 2.6 s.'),
]

quiz = [
 qz('Как распространяется свет в однородной среде?', 'По прямым линиям', 'По кривым', 'Зигзагами', 'Прямолинейность света объясняет тени и затмения.',
    'How does light travel in a uniform medium?', 'In straight lines', 'Along curves', 'In zigzags', 'The straightness of light explains shadows and eclipses.'),
 qz('Что такое тень?', 'Область, куда свет не попадает', 'Отражённый свет', 'Источник света', 'За непрозрачным предметом свет не проходит.',
    'What is a shadow?', 'A region the light does not reach', 'Reflected light', 'A source of light', 'Light does not pass behind an opaque object.'),
 qz('Когда наступает солнечное затмение?', 'Когда Луна встаёт между Землёй и Солнцем', 'Когда Земля между Луной и Солнцем', 'Когда Солнце гаснет', 'Тень Луны падает на Землю.',
    'When does a solar eclipse occur?', 'When the Moon is between the Earth and the Sun', 'When the Earth is between the Moon and the Sun', 'When the Sun goes out', 'The Moon’s shadow falls on the Earth.'),
 qz('Какое изображение даёт камера-обскура?', 'Перевёрнутое', 'Прямое', 'Увеличенное втрое', 'Лучи через отверстие пересекаются, поэтому изображение перевёрнуто.',
    'What image does a pinhole camera give?', 'Inverted', 'Upright', 'Magnified three times', 'The rays cross at the hole so the image is inverted.'),
 qz('Чему равна скорость света в вакууме (примерно)?', '300 000 км/с', '300 км/с', '3 000 км/с', 'c ≈ 3·10⁸ м/с.',
    'What is the speed of light in a vacuum (approximately)?', '300,000 km/s', '300 km/s', '3,000 km/s', 'c ≈ 3·10⁸ m/s.'),
 qz('За какое время свет от Солнца доходит до Земли?', 'Около 8 минут', 'Около 1 секунды', 'Около суток', 'Расстояние 1,5·10¹¹ м делим на 3·10⁸ м/с — около 500 с.',
    'How long does light from the Sun take to reach Earth?', 'About 8 minutes', 'About 1 second', 'About a day', 'The distance 1.5·10¹¹ m divided by 3·10⁸ m/s is about 500 s.'),
 qz('Что такое световой год?', 'Расстояние, которое свет проходит за год', 'Время, за которое свет доходит до Солнца', 'Единица яркости', 'Это единица длины, а не времени.',
    'What is a light-year?', 'The distance light covers in a year', 'The time light takes to reach the Sun', 'A unit of brightness', 'It is a unit of length, not of time.'),
 qz('Как изменится тень шеста, когда Солнце поднимается выше?', 'Станет короче', 'Станет длиннее', 'Не изменится', 'L = H / tg α: чем больше α, тем короче тень.',
    'How does a pole’s shadow change as the Sun rises higher?', 'It becomes shorter', 'It becomes longer', 'It does not change', 'L = H / tan α: the greater α, the shorter the shadow.'),
]

js = r'''
const T={ru:{
 shLabel:"Предмет, солнечные лучи и тень на земле",pcLabel:"Камера-обскура с перевёрнутым изображением",ltLabel:"Расстояние от Земли и время пути света",
 objs:["Луна","Солнце","Юпитер (в ближайшей точке)","Проксима Центавра"],
 shFb:"Чем выше Солнце, тем короче тень.",pcFb:"Дальше предмет — меньше изображение; изображение перевёрнуто.",ltFb:"Свет идёт быстро, но космос огромен."},
 en:{
 shLabel:"An object, the Sun’s rays and its shadow on the ground",pcLabel:"A pinhole camera with an inverted image",ltLabel:"The distance from Earth and the light travel time",
 objs:["The Moon","The Sun","Jupiter (at closest approach)","Proxima Centauri"],
 shFb:"The higher the Sun, the shorter the shadow.",pcFb:"The farther the object the smaller the image; the image is inverted.",ltFb:"Light is fast but space is huge."}};
const C=299792458,DIST=[3.844e8,1.496e11,5.88e11,4.0114e16];
function timeStr(s){if(s<120)return fmt(s,2)+UN[lang].s;if(s<7200)return fmt(s/60,1)+UN[lang].min;if(s<86400*2)return fmt(s/3600,1)+UN[lang].h;return fmt(s/31557600,2)+(lang==="ru"?" лет":" years")}
function distStr(m){if(m<1e12)return num(Math.round(m/1000))+UN[lang].km;return fmt(m/9.4607e15,2)+(lang==="ru"?" св. года":" ly")}
function drawSh(){const t=tt(),H=+$("sh").value,a=+$("sa").value,r=a*Math.PI/180,L=H/Math.tan(r);
 const sc=Math.min(150/H,500/(L+1));const hp=Math.min(150,H*sc),Lp=Math.min(480,L*sc),x0=60;
 let g='<line x1="30" y1="210" x2="570" y2="210" stroke="#18181a" stroke-width="2"/><line x1="'+x0+'" y1="210" x2="'+x0+'" y2="'+(210-hp)+'" stroke="#18181a" stroke-width="5"/>';
 g+='<line x1="'+x0+'" y1="210" x2="'+(x0+Lp)+'" y2="210" stroke="#555" stroke-width="7" opacity="0.5"/><line x1="'+x0+'" y1="'+(210-hp)+'" x2="'+(x0+Lp)+'" y2="210" stroke="#f0a020" stroke-width="2" stroke-dasharray="6 4"/>';
 g+='<circle cx="'+(x0-18+0)+'" cy="30" r="16" fill="#f0a020"/>'+svgText(x0+Lp/2,230,"L = "+fmt(L,1)+UN[lang].m,"#18181a","middle",12)+svgText(x0+8,200-hp/2,"H = "+fmt(H,1)+UN[lang].m,"#18181a","start",12);
 $("shSvg").innerHTML=g;
 $("shOut").textContent=fmt(H,1)+UN[lang].m;$("saOut").textContent=a+"°";
 $("sL").textContent=fmt(L,1)+UN[lang].m;$("sK").textContent=fmt(L/H,2);$("shFb").textContent=t.shFb}
["sh","sa"].forEach(id=>$(id).addEventListener("input",drawSh));
function drawPc(){const t=tt(),H=+$("ph").value,d=+$("pd").value,s=+$("ps").value,h=H*s/100/d*100;
 const ph=Math.min(70,H/10*70),ih=Math.min(70,h/12*70+2);
 let g='<rect x="300" y="60" width="240" height="130" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/><line x1="300" y1="60" x2="300" y2="118" stroke="#18181a" stroke-width="4"/><line x1="300" y1="132" x2="300" y2="190" stroke="#18181a" stroke-width="4"/>';
 g+='<line x1="60" y1="125" x2="60" y2="'+(125-ph)+'" stroke="#2f6f5d" stroke-width="6"/><line x1="'+540+'" y1="125" x2="540" y2="'+(125+ih)+'" stroke="#2f6f5d" stroke-width="6"/>';
 g+='<line x1="60" y1="'+(125-ph)+'" x2="540" y2="'+(125+ih)+'" stroke="#f0a020"/><line x1="60" y1="125" x2="540" y2="125" stroke="#f0a020" stroke-dasharray="4 3"/>';
 g+=svgText(60,150,"H","#18181a","middle",12)+svgText(540,205,"h = "+fmt(h,1)+(lang==="ru"?" см":" cm"),"#18181a","end",12);
 $("pcSvg").innerHTML=g;
 $("phOut").textContent=fmt(H,1)+UN[lang].m;$("pdOut").textContent=d+UN[lang].m;$("psOut").textContent=s+(lang==="ru"?" см":" cm");
 $("pI").textContent=fmt(h,2)+(lang==="ru"?" см":" cm");$("pS").textContent=lang==="ru"?"перевёрнутое":"inverted";$("pcFb").textContent=t.pcFb}
["ph","pd","ps"].forEach(id=>$(id).addEventListener("input",drawPc));
function drawLt(){const t=tt(),k=+$("lo").value,s=DIST[k],tm=s/C;
 let g='<circle cx="60" cy="125" r="22" fill="#3f5f8f"/><line x1="90" y1="125" x2="500" y2="125" stroke="#f0a020" stroke-width="3" stroke-dasharray="8 5"/><circle cx="530" cy="125" r="'+(k===1?30:k===2?24:k===3?10:12)+'" fill="'+(k===1?"#f0a020":"#9a9a9a")+'"/>';
 g+=svgText(60,170,(lang==="ru"?"Земля":"Earth"),"#18181a","middle",12)+svgText(530,170,t.objs[k],"#18181a","middle",11)+svgText(300,110,timeStr(tm),"#b6533f","middle",18);
 $("ltSvg").innerHTML=g;
 $("lD").textContent=distStr(s);$("lT").textContent=timeStr(tm);$("ltFb").textContent=t.ltFb}
$("lo").addEventListener("input",drawLt);
const LAB={ru:{shSvg:T.ru.shLabel,pcSvg:T.ru.pcLabel,ltSvg:T.ru.ltLabel},en:{shSvg:T.en.shLabel,pcSvg:T.en.pcLabel,ltSvg:T.en.ltLabel}};
function drawAll(){fillSel("lo",T[lang].objs,0);drawSh();drawPc();drawLt()}
'''

c = dict(n='29', slug='29-light-and-shadows.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Свет и тени', 'Light and shadows'),
 desc='Глава 29 Атласа физики: прямолинейность света, тень и затмения, камера-обскура, скорость света и расстояния в космосе.',
 lead=('Как измерить высоту дерева по тени и сколько идёт к нам свет от Солнца. Лучи, тени, камера-обскура, скорость света.',
       'How to measure the height of a tree from its shadow and how long light takes to reach us from the Sun. Rays, shadows, the pinhole camera, the speed of light.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('straight', 'Лучи и тени', 'Rays and shadows'), ('pinhole', 'Камера-обскура', 'Pinhole camera'), ('speed', 'Скорость света', 'Speed of light'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вы идёте по аллее, а рядом растёт огромный тополь. Залезть на него нельзя, рулетки нет — только метровая палка и солнечный день. Но высоту тополя вы измерите с точностью до полуметра.</p><p>Как это сделать, никуда не залезая?</p>',
         '<p>You walk along an avenue beside a huge poplar. Climbing it is out of the question and you have no tape — only a one-metre stick and a sunny day. Yet you will measure the poplar’s height to within half a metre.</p><p>How can you do it without climbing?</p>'),
 hint=stdhint('Тень и высота Солнца', 'A shadow and the height of the Sun'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: подобные треугольники', 'The answer: similar triangles'),
 answer=('<p>Воткните палку вертикально и измерьте её тень шагами, а потом тень тополя — теми же шагами. Лучи Солнца почти параллельны, поэтому палка с тенью и дерево с тенью образуют подобные прямоугольные треугольники: <em>H / L = h / l</em>. Если палка 1 м даёт тень 0,75 м, а тополь — 12 м, то он высотой 1 · 12 / 0,75 = 16 м (модель 1 и задача 1).</p><p>Измерять надо в одно время, пока высота Солнца не изменилась.</p>',
         '<p>Stick the pole upright and measure its shadow in paces, then the poplar’s shadow in the same paces. The Sun’s rays are almost parallel so the pole with its shadow and the tree with its shadow form similar right triangles: <em>H / L = h / l</em>. If a 1 m pole gives a 0.75 m shadow and the poplar 12 m, then it is 1 · 12 / 0.75 = 16 m tall (model 1 and problem 1).</p><p>You must measure at one time, while the Sun’s height has not changed.</p>'),
 sources=[
  ('Прямолинейность света, лучи, тени, камера-обскура —', 'Straight-line travel of light, rays, shadows, the pinhole camera —', LINK('https://openstax.org/books/university-physics-volume-3/pages/1-introduction-to-the-nature-of-light', 'OpenStax University Physics, Vol. 3, гл. 1') + ', ' + LINK('https://en.wikipedia.org/wiki/Pinhole_camera', 'Wikipedia: Pinhole camera')),
  ('Скорость света c = 299 792 458 м/с —', 'The speed of light c = 299,792,458 m/s —', LINK('https://physics.nist.gov/cgi-bin/cuu/Value?c', 'NIST: speed of light in vacuum')),
  ('Расстояния до Луны, Солнца, Юпитера и Проксимы Центавра —', 'Distances to the Moon, the Sun, Jupiter and Proxima Centauri —', LINK('https://en.wikipedia.org/wiki/Lunar_distance', 'Wikipedia: Lunar distance') + ', ' + LINK('https://en.wikipedia.org/wiki/Astronomical_unit', 'Wikipedia: Astronomical unit') + ', ' + LINK('https://en.wikipedia.org/wiki/Jupiter', 'Wikipedia: Jupiter') + ', ' + LINK('https://en.wikipedia.org/wiki/Proxima_Centauri', 'Wikipedia: Proxima Centauri'))],
 note=stdnote('Значения ползунков в моделях — условные; расстояния до небесных тел округлены.', 'The slider values in the models are assumed; the distances to celestial bodies are rounded.'),
 prev=('28-earthquakes.html', 'Глава 28 · Землетрясения', 'Chapter 28 · Earthquakes'),
 next=('30-reflection.html', 'Глава 30 · Отражение света', 'Chapter 30 · Reflection of light'),
 js=js)
build(c)
