# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ГЛАЗ И ОЧКИ', 'THE EYE AND SPECTACLES', 'eySvg', '0 0 600 250',
  select('ey', 'Какое у человека зрение', 'The person’s eyesight') + slider('ed', 'Расстояние до предмета', 'Distance to the object', 0.1, 6, 0.1, 0.5) + slider('eg', 'Очки', 'Spectacles', -5, 5, 0.5, 0),
  stats([('eA', 'Нужная аккомодация', 'Accommodation needed'), ('eR', 'Что видит человек', 'What the person sees'), ('eP', 'Диапазон резкого зрения (с очками)', 'Range of sharp sight (with the spectacles)')]),
  'eyFb', 'Схема условная: упрощённая модель глаза — тонкая линза на расстоянии 17 мм от сетчатки; расслабленный нормальный глаз имеет силу 58,8 дптр, а аккомодация добавляет до 4 дптр. Очки считаются тонкой линзой у глаза.',
  'A schematic drawing: a simplified eye model — a thin lens 17 mm from the retina; a relaxed normal eye has a power of 58.8 dioptres and accommodation adds up to 4 dioptres. Spectacles are treated as a thin lens at the eye.')
s1 = section('eye', 'Глаз как оптический прибор', 'The eye as an optical instrument',
 bd('<p>Глаз устроен как маленький фотоаппарат. Роговица и хрусталик — это собирающая линза, а на сетчатке получается <strong>уменьшенное, действительное и перевёрнутое</strong> изображение (мозг «переворачивает» его обратно). Радужка с зрачком работает как диафрагма: на ярком свету зрачок сужается.</p><p>Расстояние от хрусталика до сетчатки неизменно (около 17 мм в упрощённой модели), поэтому, чтобы видеть резко и далёкое, и близкое, глаз <strong>меняет оптическую силу хрусталика</strong> — это <strong>аккомодация</strong>. Для предмета на расстоянии <em>d</em> нужна сила около <em>58,8 + 1/d</em> диоптрий. Чем ближе предмет, тем сильнее надо напрягать глаз.</p>',
    '<p>The eye is built like a small camera. The cornea and lens form a converging lens and a <strong>reduced, real, inverted</strong> image forms on the retina (the brain “turns” it back). The iris with the pupil works as a diaphragm: in bright light the pupil narrows.</p><p>The distance from the lens to the retina is constant (about 17 mm in the simplified model) so to see both far and near sharply the eye <strong>changes the optical power of its lens</strong> — this is <strong>accommodation</strong>. For an object at distance <em>d</em> the power needed is about <em>58.8 + 1/d</em> dioptres. The nearer the object the harder the eye must strain.</p>')
 + bd('<p>У <strong>близорукого</strong> человека глаз слишком «сильный» (или длинный): изображение далёкого предмета собирается перед сетчаткой, вдаль видно размыто, зато вблизи хорошо. Ему нужны очки с <em>рассеивающими</em> линзами (отрицательные диоптрии). У <strong>дальнозоркого</strong> глаз слишком «слабый»: изображение попадает за сетчатку, особенно плохо видно вблизи. Ему нужны <em>собирающие</em> линзы (положительные диоптрии).</p>',
      '<p>For a <strong>short-sighted</strong> person the eye is too “strong” (or too long): the image of a distant object forms in front of the retina so distance is blurred while near is fine. They need spectacles with <em>diverging</em> lenses (negative dioptres). For a <strong>long-sighted</strong> person the eye is too “weak”: the image falls behind the retina, especially bad for near. They need <em>converging</em> lenses (positive dioptres).</p>'),
 lab1)

lab2 = model(2, 'МИКРОСКОП', 'THE MICROSCOPE', 'mcSvg', '0 0 600 250',
  slider('mo', 'Фокусное расстояние объектива', 'Focal length of the objective', 0.2, 1.0, 0.05, 0.5) + slider('me', 'Фокусное расстояние окуляра', 'Focal length of the eyepiece', 1.0, 5.0, 0.1, 2.5) + slider('ml', 'Длина тубуса (расстояние между линзами)', 'Tube length (distance between the lenses)', 10, 20, 1, 16),
  stats([('mM', 'Увеличение M = L·25/(f₁·f₂)', 'Magnification M = L·25/(f₁·f₂)'), ('mS', 'Лупа с тем же окуляром: 25/f₂', 'A magnifier of the same eyepiece: 25/f₂')]),
  'mcFb', 'Схема условная: фокусные расстояния и длина тубуса — в сантиметрах; 25 см — расстояние наилучшего зрения.',
  'A schematic drawing: focal lengths and the tube length in centimetres; 25 cm is the distance of most distinct vision.')
s2 = section('micro', 'Лупа и микроскоп', 'The magnifier and the microscope',
 bd('<p>Расстояние наилучшего зрения нормального глаза — около 25 см: ближе предмет уже нельзя рассмотреть резко. <strong>Лупа</strong> — собирающая линза с малым <em>f</em>: предмет помещают чуть ближе фокуса, и получается мнимое увеличенное изображение. Увеличение лупы <em>M ≈ 25 / f</em> (f в сантиметрах): с f = 5 см оно равно 5.</p><p><strong>Микроскоп</strong> состоит из двух линз: <strong>объектива</strong> с очень малым <em>f₁</em> и <strong>окуляра</strong>. Объектив даёт действительное увеличенное изображение, окуляр работает как лупа и увеличивает его ещё раз. Общее увеличение — примерно произведение увеличений обеих ступеней:</p>',
    '<p>The distance of most distinct vision of a normal eye is about 25 cm: an object nearer than that cannot be seen sharply. A <strong>magnifier</strong> is a converging lens with a small <em>f</em>: the object is placed just inside the focus and a virtual magnified image results. The magnification of a magnifier is <em>M ≈ 25 / f</em> (f in centimetres): with f = 5 cm it is 5.</p><p>A <strong>microscope</strong> consists of two lenses: an <strong>objective</strong> with a very small <em>f₁</em> and an <strong>eyepiece</strong>. The objective gives a real magnified image and the eyepiece works as a magnifier and magnifies it once more. The total magnification is roughly the product of the magnifications of both stages:</p>')
 + formula('M ≈ L · 25 / (f₁ · f₂)', 'L — расстояние между линзами, f₁ и f₂ — фокусные расстояния объектива и окуляра (см)', 'L is the distance between the lenses, f₁ and f₂ the focal lengths of the objective and eyepiece (cm)'),
 lab2)

lab3 = model(3, 'ТЕЛЕСКОП', 'THE TELESCOPE', 'tlSvg', '0 0 600 250',
  slider('to', 'Фокусное расстояние объектива', 'Focal length of the objective', 100, 2000, 50, 900) + slider('te', 'Фокусное расстояние окуляра', 'Focal length of the eyepiece', 4, 40, 1, 25),
  stats([('tM', 'Увеличение M = f₁/f₂', 'Magnification M = f₁/f₂'), ('tL', 'Луна выглядит как предмет под углом', 'The Moon looks like an object of angle'), ('tT', 'Длина трубы', 'Length of the tube')]),
  'tlFb', 'Схема условная: фокусные расстояния в миллиметрах; угловой размер Луны принят 0,52°.',
  'A schematic drawing: focal lengths in millimetres; the angular size of the Moon is taken as 0.52°.')
s3 = section('tele', 'Телескоп', 'The telescope',
 bd('<p>Телескоп-рефрактор тоже из двух линз: <strong>объектив</strong> с большим фокусным расстоянием <em>f₁</em> собирает свет далёкого предмета и строит его изображение в фокусе, а <strong>окуляр</strong> с малым <em>f₂</em> рассматривает это изображение как лупа. Увеличение телескопа — <strong>угловое</strong>: во сколько раз растёт угол, под которым виден предмет:</p>',
    '<p>A refracting telescope also has two lenses: an <strong>objective</strong> with a large focal length <em>f₁</em> gathers the light of a distant object and forms its image in the focus and an <strong>eyepiece</strong> with a small <em>f₂</em> views that image as a magnifier. The magnification of a telescope is <strong>angular</strong>: how many times the angle at which the object is seen grows:</p>')
 + formula('M = f₁ / f₂', 'большой объектив с большим f₁ собирает больше света — видны более тусклые звёзды', 'a large objective with a large f₁ gathers more light — fainter stars are visible')
 + bd('<p>Для наблюдений звёзд важен тёмный и чистый воздух. Высокогорные места Кыргызстана, где воздух сухой, тонкий и далёк от городских огней, хорошо подходят для наблюдений неба. Диаметр объектива определяет, сколько света соберёт телескоп, а увеличение подбирают заменой окуляра.</p>',
      '<p>For observing stars dark and clean air matters. The high mountain places of Kyrgyzstan, where the air is dry and thin and far from city lights, suit observing the sky well. The diameter of the objective sets how much light the telescope gathers and the magnification is chosen by changing the eyepiece.</p>'),
 lab3)

tasks = [
 task(1, 'Сила глаза', 'The power of the eye', 'Расстояние от хрусталика до сетчатки 17 мм. Какова оптическая сила расслабленного глаза, смотрящего вдаль?', 'The distance from the lens to the retina is 17 mm. What is the optical power of a relaxed eye looking at a distant object?',
  'di = 0,017 м, d = ∞', 'di = 0.017 m, d = ∞', 'Изображение бесконечно далёкого предмета — в фокусе: f = 17 мм.<br>D = 1/f = 1/0,017 ≈ 58,8 дптр.', 'The image of an infinitely distant object is in the focus: f = 17 mm.<br>D = 1/f = 1/0.017 ≈ 58.8 dioptres.', 'около 58,8 дптр.', 'about 58.8 dioptres.', True),
 task(2, 'Чтение с 25 см', 'Reading at 25 cm', 'На сколько должна увеличиться сила глаза (аккомодация), чтобы читать книгу на расстоянии 25 см?', 'By how much must the eye’s power (accommodation) increase to read a book at 25 cm?',
  'd = 0,25 м', 'd = 0.25 m', 'Добавка к силе: 1/d = 1/0,25 = 4 дптр (для расслабленного глаза нужно было бы 58,8, теперь 62,8).', 'The addition to the power: 1/d = 1/0.25 = 4 dioptres (a relaxed eye had 58.8, now 62.8).', '4 дптр — предельная аккомодация взрослого нормального глаза.', '4 dioptres — the limit of accommodation of an adult normal eye.'),
 task(3, 'Очки для близорукого', 'Spectacles for short sight', 'Дальше 50 см близорукий человек ничего не видит резко. Какие очки ему нужны, чтобы видеть далёкие предметы?', 'A short-sighted person sees nothing sharply beyond 50 cm. What spectacles does he need to see distant objects?',
  'дальняя точка 0,5 м', 'far point 0.5 m', 'Линза должна из бесконечности «сделать» мнимое изображение на расстоянии 0,5 м: f = −0,5 м.<br>D = 1/f = −2 дптр.', 'The lens must turn infinity into a virtual image at 0.5 m: f = −0.5 m.<br>D = 1/f = −2 dioptres.', '−2 дптр — рассеивающие линзы.', '−2 dioptres — diverging lenses.'),
 task(4, 'Лупа', 'A magnifier', 'Лупа имеет фокусное расстояние 5 см. Какое у неё увеличение (при расстоянии наилучшего зрения 25 см)?', 'A magnifier has a focal length of 5 cm. What is its magnification (with a distance of most distinct vision of 25 cm)?',
  'f = 5 см', 'f = 5 cm', 'M ≈ 25 / f = 25 / 5 = 5.', 'M ≈ 25 / f = 25 / 5 = 5.', 'в 5 раз.', '5 times.'),
 task(5, 'Микроскоп', 'A microscope', 'Объектив с f₁ = 0,5 см, окуляр с f₂ = 2,5 см, расстояние между линзами 16 см. Найдите увеличение микроскопа.', 'An objective with f₁ = 0.5 cm, an eyepiece with f₂ = 2.5 cm, the distance between the lenses 16 cm. Find the magnification of the microscope.',
  'f₁ = 0,5 см, f₂ = 2,5 см, L = 16 см', 'f₁ = 0.5 cm, f₂ = 2.5 cm, L = 16 cm', 'M ≈ L · 25 / (f₁ · f₂) = 16 · 25 / (0,5 · 2,5) = 400 / 1,25 = 320.', 'M ≈ L · 25 / (f₁ · f₂) = 16 · 25 / (0.5 · 2.5) = 400 / 1.25 = 320.', 'около 320 раз.', 'about 320 times.'),
 task(6, 'Телескоп и Луна', 'A telescope and the Moon', 'Телескоп с объективом f₁ = 900 мм и окуляром f₂ = 25 мм. Найдите увеличение и под каким углом покажется Луна (в небе она видна под углом 0,52°).', 'A telescope with an objective f₁ = 900 mm and an eyepiece f₂ = 25 mm. Find the magnification and the angle at which the Moon will appear (in the sky it is seen at 0.52°).',
  'f₁ = 900 мм, f₂ = 25 мм, φ = 0,52°', 'f₁ = 900 mm, f₂ = 25 mm, φ = 0.52°', 'M = f₁ / f₂ = 900 / 25 = 36.<br>φ′ = M · φ = 36 · 0,52° ≈ 18,7°.', 'M = f₁ / f₂ = 900 / 25 = 36.<br>φ′ = M · φ = 36 · 0.52° ≈ 18.7°.', '36× и около 19° — Луна кажется в 36 раз шире.', '36× and about 19° — the Moon looks 36 times wider.'),
]

quiz = [
 qz('Какое изображение получается на сетчатке глаза?', 'Действительное, перевёрнутое, уменьшенное', 'Мнимое, прямое', 'Увеличенное и прямое', 'Глаз работает как собирающая линза.',
    'What image forms on the retina of the eye?', 'Real, inverted, reduced', 'Virtual, upright', 'Magnified and upright', 'The eye works as a converging lens.'),
 qz('Что такое аккомодация?', 'Изменение оптической силы хрусталика', 'Сужение зрачка', 'Движение глаза', 'Хрусталик меняет кривизну, чтобы видеть на разном расстоянии.',
    'What is accommodation?', 'A change in the optical power of the lens', 'Narrowing of the pupil', 'Movement of the eye', 'The lens changes curvature to see at different distances.'),
 qz('Какие линзы нужны близорукому?', 'Рассеивающие', 'Собирающие', 'Плоские', 'Близорукий глаз слишком «сильный», его ослабляют.',
    'What lenses does a short-sighted person need?', 'Diverging', 'Converging', 'Flat', 'A short-sighted eye is too “strong” and is weakened.'),
 qz('Какие линзы нужны дальнозоркому?', 'Собирающие', 'Рассеивающие', 'Никакие', 'Дальнозоркий глаз слишком «слабый», его усиливают.',
    'What lenses does a long-sighted person need?', 'Converging', 'Diverging', 'None', 'A long-sighted eye is too “weak” and is strengthened.'),
 qz('Чему равно увеличение лупы с f = 5 см?', '5', '25', '0,2', 'M ≈ 25 / f = 25 / 5.',
    'What is the magnification of a magnifier with f = 5 cm?', '5', '25', '0.2', 'M ≈ 25 / f = 25 / 5.'),
 qz('Из чего состоит микроскоп?', 'Из объектива и окуляра', 'Из зеркала и лампы', 'Из призмы', 'Две линзовые ступени дают большое увеличение.',
    'What does a microscope consist of?', 'An objective and an eyepiece', 'A mirror and a lamp', 'A prism', 'Two lens stages give a large magnification.'),
 qz('Как найти увеличение телескопа-рефрактора?', 'f объектива / f окуляра', 'f окуляра / f объектива', 'f объектива · f окуляра', 'M = f₁ / f₂.',
    'How is the magnification of a refracting telescope found?', 'f of objective / f of eyepiece', 'f of eyepiece / f of objective', 'f of objective · f of eyepiece', 'M = f₁ / f₂.'),
 qz('Что даёт больший объектив телескопа?', 'Больше света — видны более тусклые звёзды', 'Меньше света', 'Только цвет', 'Площадь объектива определяет собираемый свет.',
    'What does a larger telescope objective give?', 'More light — fainter stars are visible', 'Less light', 'Only colour', 'The area of the objective sets the light gathered.'),
]

js = r'''
const T={ru:{
 eyLabel:"Глаз, линза очков и точка, где собираются лучи, относительно сетчатки",mcLabel:"Микроскоп из двух линз: объектив и окуляр",tlLabel:"Телескоп-рефрактор: объектив и окуляр",
 kinds:["Нормальное зрение","Близорукость (+3 дптр)","Дальнозоркость (−2 дптр)"],
 sharp:"резко",front:"размыто: фокус перед сетчаткой",back:"размыто: фокус за сетчаткой",
 eyFb:"Попробуйте разные очки: у близорукого минус сдвигает фокус на сетчатку.",mcFb:"Малое f объектива и окуляра — большое увеличение.",tlFb:"Большое f объектива и малое f окуляра — большое увеличение."},
 en:{
 eyLabel:"The eye, a spectacle lens and the point where rays gather relative to the retina",mcLabel:"A microscope of two lenses: objective and eyepiece",tlLabel:"A refracting telescope: objective and eyepiece",
 kinds:["Normal sight","Short sight (+3 D)","Long sight (−2 D)"],
 sharp:"sharp",front:"blurred: focus in front of the retina",back:"blurred: focus behind the retina",
 eyFb:"Try different spectacles: for a short-sighted person a minus lens moves the focus onto the retina.",mcFb:"A small f of the objective and eyepiece — a large magnification.",tlFb:"A large f of the objective and a small f of the eyepiece — a large magnification."}};
const EX=[0,3,-2],P0=58.8,AM=4;
function limitStr(ex){const far=ex>0?1/ex:Infinity,nearP=ex+AM,near=nearP>0?1/nearP:Infinity;
 const fs=far===Infinity?"∞":fmt(far*100,0)+(lang==="ru"?" см":" cm"),ns=near===Infinity?"∞":fmt(near*100,0)+(lang==="ru"?" см":" cm");return (lang==="ru"?"от ":"from ")+ns+(lang==="ru"?" до ":" to ")+fs}
function drawEy(){const t=tt(),k=+$("ey").value,ex=EX[k],d=+$("ed").value,gl=+$("eg").value;
 const need=1/d+P0-(P0+ex)-gl;
 const a=Math.min(AM,Math.max(0,need)),err=P0+ex+a+gl-1/d-P0;
 let st=Math.abs(err)<0.25?t.sharp:(err>0?t.front:t.back);
 const rel=P0/(P0+err);const fx=Math.max(0.4,Math.min(1.6,rel));
 let g='<ellipse cx="300" cy="125" rx="130" ry="80" fill="#f7f4ea" stroke="#18181a" stroke-width="2.5"/><path d="M430 85 Q448 125 430 165" fill="none" stroke="#3f5f8f" stroke-width="5"/>'+svgText(442,185,(lang==="ru"?"сетчатка":"retina"),"#3f5f8f","middle",10);
 g+='<ellipse cx="200" cy="125" rx="10" ry="38" fill="#bcd4e6" stroke="#18181a"/>';
 if(gl!==0)g+='<ellipse cx="150" cy="125" rx="'+(gl>0?8:4)+'" ry="48" fill="none" stroke="#2f6f5d" stroke-width="3"/>'+svgText(150,200,fmt(gl,1)+" D","#2f6f5d","middle",12);
 const fxp=200+(430-200)*fx;
 [-24,0,24].forEach(y=>{g+='<line x1="60" y1="'+(125+y*1.5)+'" x2="200" y2="'+(125+y)+'" stroke="#f0a020"/><line x1="200" y1="'+(125+y)+'" x2="'+fxp+'" y2="125" stroke="#f0a020"/>'});
 g+='<circle cx="'+fxp+'" cy="125" r="5" fill="#b6533f"/>';
 $("eySvg").innerHTML=g;
 $("edOut").textContent=fmt(d,1)+UN[lang].m;$("egOut").textContent=fmt(gl,1)+" D";
 $("eA").textContent=need<0?"< 0 D":(need>AM?fmt(need,1)+" D (> "+AM+")":fmt(need,1)+" D");$("eR").textContent=st;$("eP").textContent=limitStr(ex+gl);$("eyFb").textContent=t.eyFb}
["ey","ed","eg"].forEach(id=>$(id).addEventListener("input",drawEy));
function drawMc(){const t=tt(),fo=+$("mo").value,fe=+$("me").value,L=+$("ml").value,M=L*25/(fo*fe);
 const X0=120;let g='<line x1="40" y1="125" x2="560" y2="125" stroke="#c9c2b0"/>';
 g+='<ellipse cx="'+X0+'" cy="125" rx="6" ry="30" fill="#bcd4e6" stroke="#18181a" stroke-width="2"/><ellipse cx="'+(X0+L*18)+'" cy="125" rx="9" ry="45" fill="#bcd4e6" stroke="#18181a" stroke-width="2"/>';
 g+='<line x1="'+(X0-60)+'" y1="125" x2="'+(X0-60)+'" y2="108" stroke="#2f6f5d" stroke-width="5"/><line x1="'+(X0+L*9)+'" y1="125" x2="'+(X0+L*9)+'" y2="'+(125+Math.min(60,17*Math.min(M/10,3.5)))+'" stroke="#b6533f" stroke-width="5"/>';
 g+=svgText(X0,70,(lang==="ru"?"объектив":"objective"),"#18181a","middle",11)+svgText(X0+L*18,55,(lang==="ru"?"окуляр":"eyepiece"),"#18181a","middle",11);
 $("mcSvg").innerHTML=g;
 $("moOut").textContent=fmt(fo,2)+(lang==="ru"?" см":" cm");$("meOut").textContent=fmt(fe,1)+(lang==="ru"?" см":" cm");$("mlOut").textContent=L+(lang==="ru"?" см":" cm");
 $("mM").textContent=num(Math.round(M))+"×";$("mS").textContent=fmt(25/fe,1)+"×";$("mcFb").textContent=t.mcFb}
["mo","me","ml"].forEach(id=>$(id).addEventListener("input",drawMc));
function drawTl(){const t=tt(),f1=+$("to").value,f2=+$("te").value,M=f1/f2,ang=0.52*M;
 const len=Math.min(420,60+f1/2000*340);
 let g='<line x1="40" y1="125" x2="560" y2="125" stroke="#c9c2b0" stroke-dasharray="4 3"/><rect x="80" y="95" width="'+len+'" height="60" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/><ellipse cx="80" cy="125" rx="7" ry="32" fill="#bcd4e6" stroke="#18181a" stroke-width="2"/><ellipse cx="'+(80+len)+'" cy="125" rx="4" ry="14" fill="#bcd4e6" stroke="#18181a" stroke-width="2"/>';
 g+=svgText(80,85,"f₁","#18181a","middle",12)+svgText(80+len,85,"f₂","#18181a","middle",12);
 $("tlSvg").innerHTML=g;
 $("toOut").textContent=f1+UN[lang].mm;$("teOut").textContent=f2+UN[lang].mm;
 $("tM").textContent=fmt(M,1)+"×";$("tL").textContent=fmt(ang,1)+"°";$("tT").textContent=num(Math.round(f1+f2))+UN[lang].mm;$("tlFb").textContent=t.tlFb}
["to","te"].forEach(id=>$(id).addEventListener("input",drawTl));
const LAB={ru:{eySvg:T.ru.eyLabel,mcSvg:T.ru.mcLabel,tlSvg:T.ru.tlLabel},en:{eySvg:T.en.eyLabel,mcSvg:T.en.mcLabel,tlSvg:T.en.tlLabel}};
function drawAll(){fillSel("ey",T[lang].kinds,0);drawEy();drawMc();drawTl()}
'''

c = dict(n='32', slug='32-eye-and-instruments.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Глаз и оптические приборы', 'The eye and optical instruments'),
 desc='Глава 32 Атласа физики: глаз как линза, аккомодация, близорукость и очки, лупа, микроскоп и телескоп.',
 lead=('Почему вдаль видно размыто, а вблизи резко, и как очки это исправляют. Глаз, лупа, микроскоп и телескоп.',
       'Why distance looks blurred while near is sharp and how spectacles fix it. The eye, the magnifier, the microscope and the telescope.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('eye', 'Глаз', 'The eye'), ('micro', 'Лупа и микроскоп', 'Magnifier and microscope'), ('tele', 'Телескоп', 'Telescope'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Девочка читает книгу без проблем, а вот снежные вершины на горизонте для неё — размытое пятно. Она надела очки с «минусовыми» стёклами: вершины стали резкими, но когда она снимает очки и берёт книгу — читать по-прежнему легко.</p><p>Почему глазу одной девочки проще смотреть вблизи, чем вдаль, и как стёкла помогают?</p>',
         '<p>A girl reads a book with no trouble but the snowy peaks on the horizon are a blur for her. She puts on spectacles with “minus” lenses: the peaks become sharp, but when she takes them off and picks up the book reading is still easy.</p><p>Why is it easier for this girl’s eye to look near than far, and how do the lenses help?</p>'),
 hint=stdhint('Глаз и очки', 'The eye and spectacles'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: близорукость', 'The answer: short sight'),
 answer=('<p>У девочки близорукость: глаз слишком «сильный» (или слишком длинный). Лучи от далёких вершин собираются в точку перед сетчаткой, и на сетчатке получается размытое пятно. Для близких предметов лучи расходятся — этого как раз хватает, чтобы фокус упал на сетчатку, поэтому вблизи видно резко без напряжения.</p><p>Рассеивающая (минусовая) линза очков слегка расфокусирует пучок и сдвигает фокус назад на сетчатку (модель 1: выберите «Близорукость» и поставьте очки −3 D). Для дальней точки 50 см нужны очки −2 дптр (задача 3).</p>',
         '<p>The girl is short-sighted: her eye is too “strong” (or too long). Rays from distant peaks gather at a point in front of the retina and a blurred patch forms on the retina. For near objects the rays diverge — which is just enough to move the focus onto the retina, so near is sharp without strain.</p><p>The diverging (minus) lens of the spectacles slightly spreads the beam and moves the focus back onto the retina (model 1: choose “Short sight” and set the spectacles to −3 D). For a far point of 50 cm spectacles of −2 dioptres are needed (problem 3).</p>'),
 sources=[
  ('Глаз как оптическая система, аккомодация, близорукость и дальнозоркость —', 'The eye as an optical system, accommodation, short and long sight —', LINK('https://openstax.org/books/university-physics-volume-3/pages/2-5-the-eye', 'OpenStax University Physics, Vol. 3, § 2.5 «The Eye»') + ', ' + LINK('https://en.wikipedia.org/wiki/Human_eye', 'Wikipedia: Human eye')),
  ('Лупа, микроскоп, телескоп, угловое увеличение —', 'The magnifier, the microscope, the telescope, angular magnification —', LINK('https://openstax.org/books/university-physics-volume-3/pages/2-6-the-camera', 'OpenStax University Physics, Vol. 3, гл. 2') + ', ' + LINK('https://en.wikipedia.org/wiki/Magnification', 'Wikipedia: Magnification') + ', ' + LINK('https://en.wikipedia.org/wiki/Refracting_telescope', 'Wikipedia: Refracting telescope')),
  ('Угловой размер Луны ≈ 0,52° —', 'The angular size of the Moon ≈ 0.52° —', LINK('https://en.wikipedia.org/wiki/Moon', 'Wikipedia: Moon'))],
 note=stdnote('Модель глаза упрощённая (линза в 17 мм от сетчатки, аккомодация до 4 дптр); значения ползунков и параметры приборов — условные.', 'The eye model is simplified (a lens 17 mm from the retina, accommodation up to 4 D); the slider values and instrument parameters are assumed.'),
 prev=('31-refraction-lenses.html', 'Глава 31 · Преломление и линзы', 'Chapter 31 · Refraction and lenses'),
 next=('33-newtons-laws.html', 'Глава 33 · Законы Ньютона', 'Chapter 33 · Newton’s laws'),
 js=js)
build(c)
