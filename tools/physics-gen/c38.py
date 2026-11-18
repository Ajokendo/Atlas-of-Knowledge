# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ЭНЕРГИЯ ФОТОНА', 'THE ENERGY OF A PHOTON', 'phSvg', '0 0 600 250',
  slider('pl', 'Длина волны', 'Wavelength', 200, 1000, 10, 500),
  stats([('pE', 'Энергия фотона E = h·f', 'Photon energy E = h·f'), ('pF', 'Частота f = c/λ', 'Frequency f = c/λ'), ('pR', 'Область спектра', 'Region of the spectrum')]),
  'phFb', 'Схема условная: волновой пакет — один фотон; h·c ≈ 1240 эВ·нм; 1 эВ = 1,6·10⁻¹⁹ Дж.',
  'A schematic drawing: the wave packet is one photon; h·c ≈ 1,240 eV·nm; 1 eV = 1.6·10⁻¹⁹ J.')
s1 = section('photon', 'Свет состоит из фотонов', 'Light consists of photons',
 bd('<p>Свет — волна, но обменивается энергией с веществом <em>порциями</em> — <strong>фотонами</strong>. Энергия фотона пропорциональна частоте (постоянная Планка <em>h = 6,63·10⁻³⁴ Дж·с</em>). Фотон фиолетового света несёт больше энергии, чем красного, а фотон ультрафиолета — больше, чем видимого. Для удобства энергию атомных процессов измеряют в <strong>электронвольтах</strong> (эВ).</p>',
    '<p>Light is a wave but it exchanges energy with matter in <em>portions</em> — <strong>photons</strong>. The energy of a photon is proportional to the frequency (Planck’s constant <em>h = 6.63·10⁻³⁴ J·s</em>). A photon of violet light carries more energy than red and an ultraviolet photon more than a visible one. For convenience the energies of atomic processes are measured in <strong>electronvolts</strong> (eV).</p>')
 + formula('E = h · f = h·c / λ ≈ 1240 эВ·нм / λ', 'чем короче длина волны, тем больше энергия фотона', 'the shorter the wavelength the greater the photon energy')
 + bd('<p>Видимому свету (380–750 нм) соответствуют фотоны с энергией примерно 1,7–3,3 эВ. Фотоны ультрафиолета могут разрушать молекулы кожи и ДНК — поэтому в горах, где воздуха над головой меньше, загар «жёстче».</p>',
      '<p>Visible light (380–750 nm) corresponds to photons of about 1.7–3.3 eV. Ultraviolet photons can damage skin molecules and DNA — that is why in the mountains, where there is less air overhead, sunburn is “harsher”.</p>'),
 lab1)

lab2 = model(2, 'ФОТОЭФФЕКТ', 'THE PHOTOELECTRIC EFFECT', 'peSvg', '0 0 600 250',
  select('pm', 'Металл', 'Metal') + slider('pw', 'Длина волны света', 'Wavelength of light', 200, 800, 10, 400) + slider('pi', 'Яркость света', 'Brightness of light', 1, 10, 1, 5),
  stats([('qE', 'Энергия фотона', 'Photon energy'), ('qK', 'Наибольшая энергия электрона K = E − A', 'The greatest electron energy K = E − A'), ('qI', 'Ток (условные единицы)', 'Current (arbitrary units)'), ('qL', 'Красная граница λ₀ = hc/A', 'The red limit λ₀ = hc/A')]),
  'peFb', 'Схема условная: работа выхода A — округлённые значения (цезий 2,1; натрий 2,3; цинк 4,3; медь 4,7 эВ), условные.',
  'A schematic drawing: the work function A — rounded values (caesium 2.1; sodium 2.3; zinc 4.3; copper 4.7 eV), assumed.')
s2 = section('photoeffect', 'Фотоэффект: свет выбивает электроны', 'The photoelectric effect: light knocks electrons out',
 bd('<p>Если освещать металл, он может испускать электроны. Опыты показали странное: всё решает <em>цвет</em> (частота), а не яркость. Красный свет, даже очень яркий, не выбивает электронов из цинка, а слабый ультрафиолет выбивает сразу. Эйнштейн объяснил это так: один фотон отдаёт всю энергию одному электрону. Часть энергии (<strong>работа выхода A</strong>) уходит на выход из металла, остальное — кинетическая энергия электрона:</p>',
    '<p>If a metal is illuminated it may emit electrons. Experiments showed something odd: the <em>colour</em> (frequency) decides, not the brightness. Red light, however bright, knocks no electrons out of zinc while weak ultraviolet does at once. Einstein explained it: one photon gives all its energy to one electron. Part of the energy (the <strong>work function A</strong>) is spent leaving the metal and the rest becomes the kinetic energy of the electron:</p>')
 + formula('K = h·f − A', 'если h·f < A, электроны не вылетают при любой яркости; яркость меняет число электронов (ток), но не их энергию', 'if h·f < A no electrons escape at any brightness; brightness changes the number of electrons (the current) but not their energy')
 + bd('<p>На фотоэффекте работают фотоэлементы: солнечные батареи, датчики света и автоматические двери. Для Кыргызстана с его солнечными днями это особенно важно — крупную солнечную электростанцию планируют построить в Иссык-Кульской области.</p>',
      '<p>Photocells work by the photoelectric effect: solar panels, light sensors and automatic doors. This is especially relevant for sunny Kyrgyzstan — a large solar power station is planned in the Issyk-Kul region.</p>'),
 lab2)

lab3 = model(3, 'СКОЛЬКО ФОТОНОВ В ЛУЧЕ', 'HOW MANY PHOTONS IN A BEAM', 'lzSvg', '0 0 600 250',
  slider('lp', 'Мощность луча', 'Beam power', 0.1, 5, 0.1, 1) + slider('ll', 'Длина волны', 'Wavelength', 400, 700, 10, 650),
  stats([('lE', 'Энергия одного фотона', 'Energy of one photon'), ('lN', 'Фотонов в секунду', 'Photons per second')]),
  'lzFb', 'Схема условная: монохроматический луч указки; мощность в милливаттах.',
  'A schematic drawing: a monochromatic laser-pointer beam; the power in milliwatts.')
s3 = section('count', 'Фотоны можно считать', 'Photons can be counted',
 bd('<p>Если известна мощность света <em>P</em> и энергия одного фотона <em>E</em>, число фотонов в секунду <em>N = P / E</em>. Даже у слабой лазерной указки это огромное число — поэтому свет кажется непрерывным. Лишь в очень слабом свете (глаз реагирует на единицы фотонов в тёмной комнате) его «зернистость» становится заметной.</p>',
    '<p>If the power of light <em>P</em> and the energy of one photon <em>E</em> are known the number of photons per second is <em>N = P / E</em>. Even a weak laser pointer emits an enormous number so light seems continuous. Only in very dim light (the eye responds to just a few photons in a dark room) does its “graininess” become noticeable.</p>')
 + formula('N = P / (h·f)', 'энергию фотона нужно перевести из эВ в джоули: 1 эВ = 1,6·10⁻¹⁹ Дж', 'the photon energy must be converted from eV to joules: 1 eV = 1.6·10⁻¹⁹ J'),
 lab3)

tasks = [
 task(1, 'Энергия и частота', 'Energy and frequency', 'Найдите энергию и частоту фотона зелёного света с длиной волны 500 нм.', 'Find the energy and frequency of a photon of green light of wavelength 500 nm.',
  'λ = 500 нм, c = 3·10⁸ м/с', 'λ = 500 nm, c = 3·10⁸ m/s', 'E = 1240 / 500 = 2,48 эВ.<br>f = c/λ = 3·10⁸ / 5·10⁻⁷ = 6,0·10¹⁴ Гц.', 'E = 1240 / 500 = 2.48 eV.<br>f = c/λ = 3·10⁸ / 5·10⁻⁷ = 6.0·10¹⁴ Hz.', '2,48 эВ; 6,0·10¹⁴ Гц.', '2.48 eV; 6.0·10¹⁴ Hz.', True),
 task(2, 'Лазерная указка', 'A laser pointer', 'Красная указка мощностью 1 мВт, длина волны 650 нм. Сколько фотонов она излучает за секунду?', 'A red pointer of power 1 mW, wavelength 650 nm. How many photons does it emit per second?',
  'P = 10⁻³ Вт, λ = 650 нм', 'P = 10⁻³ W, λ = 650 nm', 'E = 1240 / 650 = 1,91 эВ = 1,91 · 1,6·10⁻¹⁹ = 3,06·10⁻¹⁹ Дж.<br>N = P/E = 10⁻³ / 3,06·10⁻¹⁹ ≈ 3,3·10¹⁵ в секунду.', 'E = 1240 / 650 = 1.91 eV = 1.91 · 1.6·10⁻¹⁹ = 3.06·10⁻¹⁹ J.<br>N = P/E = 10⁻³ / 3.06·10⁻¹⁹ ≈ 3.3·10¹⁵ per second.', 'около 3,3·10¹⁵ фотонов в секунду.', 'about 3.3·10¹⁵ photons per second.'),
 task(3, 'Энергия электрона', 'Electron energy', 'Свет с длиной волны 400 нм падает на натрий (A = 2,3 эВ). Найдите наибольшую энергию вылетающих электронов.', 'Light of wavelength 400 nm falls on sodium (A = 2.3 eV). Find the greatest energy of the emitted electrons.',
  'λ = 400 нм, A = 2,3 эВ', 'λ = 400 nm, A = 2.3 eV', 'E = 1240 / 400 = 3,1 эВ.<br>K = E − A = 3,1 − 2,3 = 0,8 эВ.', 'E = 1240 / 400 = 3.1 eV.<br>K = E − A = 3.1 − 2.3 = 0.8 eV.', '0,8 эВ.', '0.8 eV.'),
 task(4, 'Красная граница цинка', 'The red limit of zinc', 'Найдите самую длинную волну, при которой цинк (A = 4,3 эВ) ещё даёт фотоэффект. К какой области она относится?', 'Find the longest wavelength at which zinc (A = 4.3 eV) still shows the photoelectric effect. Which region is it?',
  'A = 4,3 эВ', 'A = 4.3 eV', 'λ₀ = 1240 / 4,3 ≈ 288 нм — это ультрафиолет (видимый свет начинается с 380 нм).', 'λ₀ = 1240 / 4.3 ≈ 288 nm — ultraviolet (visible light begins at 380 nm).', '≈ 288 нм, ультрафиолет: от видимого света цинк не светится электронами.', '≈ 288 nm, ultraviolet: visible light ejects no electrons from zinc.'),
 task(5, 'Красный свет и цезий', 'Red light and caesium', 'Цезий: A = 2,1 эВ. Даст ли фотоэффект красный свет 700 нм, как бы ярко ни светил? А синий 450 нм — какая энергия электронов?', 'Caesium: A = 2.1 eV. Will red light of 700 nm give the effect however bright it is? And blue 450 nm — what electron energy?',
  'λ = 700 и 450 нм', 'λ = 700 and 450 nm', 'Красный: E = 1240 / 700 = 1,77 эВ < 2,1 — нет.<br>Синий: E = 1240 / 450 = 2,76 эВ; K = 2,76 − 2,1 = 0,66 эВ.', 'Red: E = 1240 / 700 = 1.77 eV < 2.1 — no.<br>Blue: E = 1240 / 450 = 2.76 eV; K = 2.76 − 2.1 = 0.66 eV.', 'красный — нет; синий — 0,66 эВ.', 'red — no; blue — 0.66 eV.'),
 task(6, 'Вдвое ярче', 'Twice as bright', 'Синий свет 450 нм на цезии сделали вдвое ярче. Что изменилось: ток, энергия электронов?', 'Blue light of 450 nm on caesium is made twice as bright. What changed: the current, the electron energy?',
  'яркость × 2', 'brightness × 2', 'Фотонов вдвое больше — электронов вдвое больше, ток вырос вдвое.<br>Энергия каждого фотона та же, поэтому K = 0,66 эВ не изменилась.', 'There are twice as many photons — twice as many electrons so the current doubled.<br>Each photon’s energy is the same so K = 0.66 eV did not change.', 'ток вдвое больше; энергия электронов прежняя.', 'the current doubles; the electron energy is unchanged.'),
]

quiz = [
 qz('Чему пропорциональна энергия фотона?', 'Частоте света', 'Яркости света', 'Скорости света в стекле', 'E = h·f.',
    'What is the photon energy proportional to?', 'The frequency of light', 'The brightness of light', 'The speed of light in glass', 'E = h·f.'),
 qz('У какого света фотоны несут больше энергии?', 'У фиолетового', 'У красного', 'У всех одинаково', 'Короче волна — больше энергия.',
    'Whose photons carry more energy?', 'Violet', 'Red', 'All the same', 'The shorter the wave the greater the energy.'),
 qz('Чем определяется, будет ли фотоэффект?', 'Частотой света и работой выхода', 'Только яркостью', 'Размером пластины', 'Нужно h·f > A.',
    'What decides whether the photoelectric effect occurs?', 'The frequency of light and the work function', 'The brightness only', 'The size of the plate', 'We need h·f > A.'),
 qz('Что изменится, если сделать свет ярче (частота прежняя, фотоэффект есть)?', 'Вырастет ток', 'Вырастет энергия электронов', 'Фотоэффект исчезнет', 'Фотонов больше, но энергия каждого та же.',
    'What changes if the light is made brighter (same frequency, the effect occurs)?', 'The current grows', 'The electron energy grows', 'The effect disappears', 'More photons but the same energy each.'),
 qz('Как найти наибольшую энергию вылетевшего электрона?', 'K = h·f − A', 'K = h·f + A', 'K = A / f', 'Энергия фотона минус работа выхода.',
    'How to find the greatest energy of the emitted electron?', 'K = h·f − A', 'K = h·f + A', 'K = A / f', 'The photon energy minus the work function.'),
 qz('Чему примерно равно h·c в эВ·нм?', '1240', '124', '12 400', 'E[эВ] = 1240 / λ[нм].',
    'What is h·c approximately in eV·nm?', '1240', '124', '12,400', 'E[eV] = 1240 / λ[nm].'),
 qz('Красный свет не выбивает электроны из цинка. Что поможет?', 'Ультрафиолет', 'Более яркий красный свет', 'Более длинная волна', 'Нужен фотон с энергией больше A.',
    'Red light ejects no electrons from zinc. What will help?', 'Ultraviolet', 'Brighter red light', 'A longer wavelength', 'We need a photon with energy above A.'),
 qz('Сколько фотонов в секунду излучает лазер мощностью P при энергии фотона E?', 'P / E', 'P · E', 'E / P', 'N = P / E.',
    'How many photons per second does a laser of power P emit at photon energy E?', 'P / E', 'P · E', 'E / P', 'N = P / E.'),
]

js = JSL + r'''
const T={ru:{
 phLabel:"Фотон — порция света",peLabel:"Свет выбивает электроны из металла",lzLabel:"Луч указки состоит из фотонов",
 metals:["Цезий (A = 2,1 эВ)","Натрий (A = 2,3 эВ)","Цинк (A = 4,3 эВ)","Медь (A = 4,7 эВ)"],reg:["ультрафиолет","видимый свет","инфракрасное"],none:"нет фотоэффекта",
 phFb:"Короче волна — больше энергия фотона.",peFb:"Решает цвет света, а не яркость.",lzFb:"Даже слабый луч — это огромное число фотонов."},
 en:{
 phLabel:"A photon is a portion of light",peLabel:"Light knocks electrons out of a metal",lzLabel:"A pointer beam consists of photons",
 metals:["Caesium (A = 2.1 eV)","Sodium (A = 2.3 eV)","Zinc (A = 4.3 eV)","Copper (A = 4.7 eV)"],reg:["ultraviolet","visible light","infrared"],none:"no photoelectric effect",
 phFb:"The shorter the wave the greater the photon energy.",peFb:"The colour of light decides, not the brightness.",lzFb:"Even a weak beam is an enormous number of photons."}};
const AW=[2.1,2.3,4.3,4.7];
function drawPh(){const t=tt(),l=+$("pl").value,E=1240/l,f=3e8/(l*1e-9);
 let g='<path d="M30 125 ';const per=Math.max(14,l/10);for(let x=30;x<=570;x+=4){const env=Math.exp(-Math.pow((x-300)/110,2));g+=' L'+x+' '+(125-70*env*Math.sin((x-30)/per*Math.PI*2))}
 g+='" fill="none" stroke="'+hue(l)+'" stroke-width="3"/>'+svgText(300,235,"λ = "+l+" "+U("нм","nm"),"#66666b","middle",12);
 $("phSvg").innerHTML=g;$("plOut").textContent=l+" "+U("нм","nm");
 $("pE").textContent=fmt(E,2)+" "+U("эВ","eV");$("pF").textContent=sci(f,2)+" "+U("Гц","Hz");$("pR").textContent=l<380?t.reg[0]:l<=750?t.reg[1]:t.reg[2];$("phFb").textContent=t.phFb}
$("pl").addEventListener("input",drawPh);
function drawPe(){const t=tt(),k=+$("pm").value,A=AW[k],l=+$("pw").value,I=+$("pi").value,E=1240/l,K=E-A,ok=K>0;
 let g='<rect x="200" y="150" width="200" height="30" fill="#9a9a9a" stroke="#18181a"/>';
 for(let i=0;i<I;i++){const x=120+i*40+(i%2)*10;g+='<line x1="'+x+'" y1="20" x2="'+(x+40)+'" y2="145" stroke="'+hue(l)+'" stroke-width="3"/>'}
 if(ok)for(let i=0;i<Math.min(I,8);i++){const x=220+i*22;g+=arrow(x,148,x+10,148-30-Math.min(40,K*18),"#2f6f5d",2)+'<circle cx="'+(x+10)+'" cy="'+(148-30-Math.min(40,K*18))+'" r="4" fill="#2f6f5d"/>'}
 else g+=svgText(300,125,t.none,"#b6533f","middle",16);
 $("peSvg").innerHTML=g;$("pwOut").textContent=l+" "+U("нм","nm");$("piOut").textContent=I;
 $("qE").textContent=fmt(E,2)+" "+U("эВ","eV");$("qK").textContent=ok?fmt(K,2)+" "+U("эВ","eV"):"—";$("qI").textContent=ok?String(I):"0";$("qL").textContent=fmt(1240/A,0)+" "+U("нм","nm");$("peFb").textContent=t.peFb}
["pm","pw","pi"].forEach(id=>$(id).addEventListener("input",drawPe));
function drawLz(){const t=tt(),P=+$("lp").value*1e-3,l=+$("ll").value,E=1240/l,N=P/(E*1.602e-19);
 let g='<rect x="30" y="105" width="90" height="40" fill="#18181a"/>';for(let i=0;i<14;i++){g+='<circle cx="'+(140+i*30)+'" cy="'+(125+((i*7)%5-2)*3)+'" r="5" fill="'+hue(l)+'"/>'}
 $("lzSvg").innerHTML=g;$("lpOut").textContent=fmt(P*1e3,1)+" "+U("мВт","mW");$("llOut").textContent=l+" "+U("нм","nm");
 $("lE").textContent=fmt(E,2)+" "+U("эВ","eV")+" ("+sci(E*1.602e-19,2)+" "+U("Дж","J")+")";$("lN").textContent=sci(N,1)+" /"+U("с","s");$("lzFb").textContent=t.lzFb}
["lp","ll"].forEach(id=>$(id).addEventListener("input",drawLz));
const LAB={ru:{phSvg:T.ru.phLabel,peSvg:T.ru.peLabel,lzSvg:T.ru.lzLabel},en:{phSvg:T.en.phLabel,peSvg:T.en.peLabel,lzSvg:T.en.lzLabel}};
function drawAll(){fillSel("pm",T[lang].metals,1);drawPh();drawPe();drawLz()}
'''

c = dict(n='38', slug='38-photons-photoelectric.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Фотоны и фотоэффект', 'Photons and the photoelectric effect'),
 desc='Глава 38 Атласа физики: фотоны, энергия фотона E = hf, фотоэффект и уравнение Эйнштейна, красная граница, солнечные батареи.',
 lead=('Свет приходит порциями. Почему слабый ультрафиолет выбивает электроны, а яркий красный — нет, и как работают солнечные батареи.',
       'Light arrives in portions. Why weak ultraviolet knocks electrons out while bright red does not, and how solar panels work.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('photon', 'Фотоны', 'Photons'), ('photoeffect', 'Фотоэффект', 'Photoeffect'), ('count', 'Счёт фотонов', 'Counting photons'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Опыт XIX века: пластину цинка освещают лампой. Яркая красная лампа — электроны не вылетают, хотя энергия света огромна. Слабая ультрафиолетовая лампа — электроны вылетают сразу, без задержки. Волновая теория света предсказывала обратное: чем ярче свет, тем сильнее должен «раскачивать» электроны.</p><p>Почему решает не яркость, а цвет?</p>',
         '<p>A nineteenth-century experiment: a zinc plate is illuminated by a lamp. A bright red lamp — no electrons come out though the light energy is huge. A weak ultraviolet lamp — electrons come out at once, without delay. The wave theory of light predicted the opposite: the brighter the light the more strongly it should “shake” the electrons.</p><p>Why does the colour decide, not the brightness?</p>'),
 hint=stdhint('Фотоэффект', 'The photoelectric effect'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: один фотон — один электрон', 'The answer: one photon — one electron'),
 answer=('<p>Электрон получает энергию от одного фотона целиком, а не накапливает её от многих. Фотон красного света несёт около 1,8 эВ — меньше работы выхода цинка (4,3 эВ), и сколько бы таких фотонов ни было, ни один из них не выбьет электрон. Фотон ультрафиолета несёт больше 4,3 эВ — одного достаточно, и электрон вылетает мгновенно.</p><p>Яркость определяет только <em>число</em> фотонов, то есть число вылетевших электронов (ток). За это объяснение Эйнштейн получил Нобелевскую премию по физике 1921 года.</p>',
         '<p>The electron takes its energy from a single photon in full rather than accumulating it from many. A photon of red light carries about 1.8 eV — less than the work function of zinc (4.3 eV) and however many such photons there are none will knock out an electron. An ultraviolet photon carries more than 4.3 eV — one is enough and the electron leaves instantly.</p><p>Brightness determines only the <em>number</em> of photons, that is the number of emitted electrons (the current). For this explanation Einstein received the 1921 Nobel Prize in Physics.</p>'),
 sources=[
  ('Фотоны, фотоэффект, уравнение Эйнштейна —', 'Photons, the photoelectric effect, Einstein’s equation —', LINK('https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect', 'OpenStax University Physics, Vol. 3, § 6.2') + ', ' + LINK('https://en.wikipedia.org/wiki/Photoelectric_effect', 'Wikipedia: Photoelectric effect')),
  ('Нобелевская премия 1921 года —', 'The 1921 Nobel Prize —', LINK('https://www.nobelprize.org/prizes/physics/1921/summary/', 'NobelPrize.org')),
  ('Планируемая солнечная электростанция в Иссык-Кульской области —', 'The planned solar power station in the Issyk-Kul region —', LINK('https://24.kg/english/352462_Russia_to_consider_building_small_modular_reactors_in_Kyrgyzstan__Putin', '24.kg'))],
 note=stdnote('Значения работы выхода округлены и условны; точные значения зависят от состояния поверхности металла.', 'The work function values are rounded and assumed; exact values depend on the state of the metal surface.'),
 prev=('37-conservation-laws.html', 'Глава 37 · Законы сохранения', 'Chapter 37 · Conservation laws'),
 next=('39-atom.html', 'Глава 39 · Атом', 'Chapter 39 · The atom'),
 js=js)
build(c)
