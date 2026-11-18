# -*- coding: utf-8 -*-
from gen import *

LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

s1 = section('temp', 'Температура и тепловое движение', 'Temperature and thermal motion',
 bd('<p>В главе 2 мы узнали, что вещество состоит из частиц, которые непрерывно и беспорядочно движутся. Чем быстрее движутся частицы, тем сильнее нагрето тело. <strong>Температура</strong> показывает степень нагретости тела и связана со средней кинетической энергией беспорядочного движения его частиц.</p><p>Температуру измеряют <strong>термометром</strong>. Прибор приводят в контакт с телом и ждут, пока их температуры сравняются. Показание термометра — это температура самого термометра, поэтому для точного измерения ему нужно время и хороший контакт с телом.</p><p>Важно не путать температуру и «количество теплоты»: ложка кипятка и ведро воды комнатной температуры нагреты по-разному, но тепловой энергии больше в ведре (подробнее — в главе 10).</p>',
    '<p>In chapter 2 we learned that matter consists of particles in continual random motion. The faster the particles move, the hotter the body. <strong>Temperature</strong> shows how hot a body is and is related to the average kinetic energy of the random motion of its particles.</p><p>Temperature is measured with a <strong>thermometer</strong>. The instrument is brought into contact with the body and we wait until their temperatures become equal. A thermometer reads its own temperature, so an accurate measurement needs time and good contact with the body.</p><p>Do not confuse temperature with “amount of heat”: a spoonful of boiling water and a bucket of room-temperature water are heated differently, but the bucket holds more thermal energy (more in chapter 10).</p>'))

lab1 = model(1, 'ШКАЛЫ ТЕМПЕРАТУР', 'TEMPERATURE SCALES', 'scaSvg', '0 0 600 300',
  slider('st', 'Температура', 'Temperature', -60, 120, 1, 20),
  stats([('sK', 'Кельвины', 'Kelvin'), ('sF', 'Фаренгейты', 'Fahrenheit'), ('sC', 'Цельсий', 'Celsius')]),
  'scaFb', 'Схема условная. Реперные точки воды даны для нормального атмосферного давления. Комнатная температура показана примерно.',
  'A schematic drawing. The water reference points are for normal atmospheric pressure. Room temperature is shown approximately.')
s2 = section('scales', 'Шкалы: Цельсия, Кельвина, Фаренгейта', 'Scales: Celsius, Kelvin, Fahrenheit',
 bd('<p>В быту мы пользуемся шкалой <strong>Цельсия</strong>: 0 °C — температура таяния льда, 100 °C — температура кипения воды при нормальном атмосферном давлении. В физике основной шкалой считают шкалу <strong>Кельвина</strong>. Её нуль — <strong>абсолютный нуль</strong>, самая низкая возможная температура: 0 К = −273,15 °C. Деление шкалы (1 К) равно делению шкалы Цельсия, поэтому <em>разность</em> температур в кельвинах и градусах Цельсия одна и та же.</p><p>В некоторых странах (например, в США) используют шкалу <strong>Фаренгейта</strong>: вода замерзает при 32 °F и кипит при 212 °F.</p>',
    '<p>In daily life we use the <strong>Celsius</strong> scale: 0 °C is the melting point of ice and 100 °C is the boiling point of water at normal atmospheric pressure. In physics the main scale is the <strong>Kelvin</strong> scale. Its zero is <strong>absolute zero</strong>, the lowest possible temperature: 0 K = −273.15 °C. A division of the scale (1 K) equals a division of the Celsius scale, so a temperature <em>difference</em> is the same in kelvins and in degrees Celsius.</p><p>Some countries (for example the USA) use the <strong>Fahrenheit</strong> scale: water freezes at 32 °F and boils at 212 °F.</p>')
 + formula('T = t + 273,15 &nbsp;&nbsp; t<sub>F</sub> = 1,8 · t + 32', 'T — в кельвинах, t — в градусах Цельсия, t<sub>F</sub> — в градусах Фаренгейта', 'T in kelvins, t in degrees Celsius, t<sub>F</sub> in degrees Fahrenheit')
 + bd('<p>С 2019 года кельвин определяют через постоянную Больцмана — она связывает температуру с энергией частиц. Поэтому температура по шкале Кельвина никогда не бывает отрицательной.</p>',
      '<p>Since 2019 the kelvin has been defined through the Boltzmann constant, which links temperature to the energy of particles. So a temperature on the Kelvin scale is never negative.</p>'),
 lab1)

lab2 = model(2, 'ТЕПЛОВОЕ РАСШИРЕНИЕ', 'THERMAL EXPANSION', 'expSvg', '0 0 600 260',
  select('em', 'Материал', 'Material') + slider('el', 'Длина', 'Length', 10, 1000, 10, 100) + slider('ed', 'Нагрев', 'Temperature rise', 10, 80, 1, 50),
  stats([('eL', 'Удлинение', 'Extension'), ('eM', 'На 1 м длины', 'Per 1 m of length'), ('eR', 'Относительно', 'Relative')]),
  'expFb', 'Схема условная: удлинение на рисунке увеличено в 200 раз. Значения α — приближённые, для небольших перепадов температур.',
  'A schematic drawing: the extension is magnified 200 times. The α values are approximate, for modest temperature changes.')
s3 = section('expansion', 'Тепловое расширение', 'Thermal expansion',
 bd('<p>При нагревании почти все тела расширяются: частицы колеблются сильнее и в среднем отодвигаются друг от друга. Для твёрдого стержня удлинение пропорционально его длине и изменению температуры:</p>',
    '<p>When heated, almost all bodies expand: the particles vibrate more strongly and on average move farther apart. For a solid rod the extension is proportional to its length and to the change in temperature:</p>')
 + formula('Δl = α · l · Δt', 'α — коэффициент линейного расширения (1/К); Δt — изменение температуры', 'α is the coefficient of linear expansion (1/K); Δt is the change in temperature')
 + bd('<p>Величина α зависит от материала. Для стали она около 12·10⁻⁶ 1/К, для меди 17·10⁻⁶, для алюминия 25·10⁻⁶, для обычного стекла 9·10⁻⁶ 1/К. Поэтому на мостах оставляют температурные швы, а между рельсами в стыках — зазоры. Длинные рельсовые плети сваривают при определённой температуре и закрепляют: если жарой их нагреть сильнее, они упираются сами в себя и могут выгнуться.</p><p>На расширении жидкости основан обычный термометр: спирт или ртуть в стеклянной трубке расширяются заметно больше стекла, и столбик жидкости поднимается.</p><p>Вода — исключение. При нагревании от 0 до 4 °C она сжимается, и самая большая плотность воды — при 4 °C. Поэтому в глубоких пресных водоёмах зимой самая плотная вода у дна имеет температуру около 4 °C.</p>',
    '<p>The value of α depends on the material. For steel it is about 12·10⁻⁶ 1/K, for copper 17·10⁻⁶, for aluminium 25·10⁻⁶, for ordinary glass 9·10⁻⁶ 1/K. That is why bridges have expansion joints and rails are laid with gaps at the joints. Long welded rail strings are laid at a chosen temperature and fastened down: if heat warms them further they push against themselves and may buckle.</p><p>An ordinary thermometer is based on the expansion of a liquid: alcohol or mercury in a glass tube expands noticeably more than the glass, and the liquid column rises.</p><p>Water is an exception. When heated from 0 to 4 °C it contracts, and water is densest at 4 °C. So in deep fresh-water bodies in winter the densest water at the bottom is at about 4 °C.</p>'),
 lab2)

tasks = [
 task(1, 'Температура тела', 'Body temperature', 'Нормальная температура тела человека около 36,6 °C. Выразите её в кельвинах и градусах Фаренгейта.', 'Normal human body temperature is about 36.6 °C. Express it in kelvins and in degrees Fahrenheit.',
  't = 36,6 °C', 't = 36.6 °C', 'T = t + 273,15 = 36,6 + 273,15 = 309,75 К.<br>t<sub>F</sub> = 1,8 · 36,6 + 32 = 65,88 + 32 = 97,88 °F.', 'T = t + 273.15 = 36.6 + 273.15 = 309.75 K.<br>t<sub>F</sub> = 1.8 · 36.6 + 32 = 65.88 + 32 = 97.88 °F.',
  'примерно 309,8 К и 97,9 °F.', 'about 309.8 K and 97.9 °F.', True),
 task(2, 'Зимой в горах', 'Winter in the mountains', 'Зимней ночью температура воздуха −25 °C. Сколько это в кельвинах и в градусах Фаренгейта?', 'On a winter night the air temperature is −25 °C. How many kelvins and degrees Fahrenheit is that?',
  't = −25 °C', 't = −25 °C', 'T = −25 + 273,15 = 248,15 К.<br>t<sub>F</sub> = 1,8 · (−25) + 32 = −45 + 32 = −13 °F.', 'T = −25 + 273.15 = 248.15 K.<br>t<sub>F</sub> = 1.8 · (−25) + 32 = −45 + 32 = −13 °F.',
  'примерно 248 К и −13 °F. Температура в кельвинах положительна.', 'about 248 K and −13 °F. The temperature in kelvins is positive.'),
 task(3, 'Разность температур', 'Temperature difference', 'Вода нагрелась от 5 °C до 25 °C. На сколько кельвинов изменилась её температура?', 'Water warmed from 5 °C to 25 °C. By how many kelvins did its temperature change?',
  't₁ = 5 °C, t₂ = 25 °C', 't₁ = 5 °C, t₂ = 25 °C', 'В градусах Цельсия: Δt = 25 − 5 = 20 °C.<br>В кельвинах: T₁ = 278,15 К, T₂ = 298,15 К, ΔT = 20 К.', 'In degrees Celsius: Δt = 25 − 5 = 20 °C.<br>In kelvins: T₁ = 278.15 K, T₂ = 298.15 K, ΔT = 20 K.',
  '20 К. Изменение температуры в кельвинах и градусах Цельсия одинаково.', '20 K. A temperature change is the same in kelvins and in degrees Celsius.'),
 task(4, 'Стальной рельс', 'A steel rail', 'Стальной рельс длиной 25 м укладывают при −30 °C. Насколько он удлинится при нагреве до +40 °C? Для стали α ≈ 12·10⁻⁶ 1/К.', 'A 25 m steel rail is laid at −30 °C. By how much will it lengthen when warmed to +40 °C? For steel α ≈ 12·10⁻⁶ 1/K.',
  'l = 25 м, Δt = 70 К, α = 12·10⁻⁶ 1/К', 'l = 25 m, Δt = 70 K, α = 12·10⁻⁶ 1/K', 'Δl = α·l·Δt = 12·10⁻⁶ · 25 · 70 = 0,021 м.', 'Δl = α·l·Δt = 12·10⁻⁶ · 25 · 70 = 0.021 m.',
  '21 мм. Именно такой запас по длине нужно предусмотреть в стыках.', '21 mm. That is the allowance needed at the joints.'),
 task(5, 'Рельсовая плеть', 'A long rail string', 'Что произойдёт с километровой плетью рельса, если её нагреть на 50 К, а удлиниться ей не позволят? Каково «желаемое» удлинение?', 'What would happen to a one-kilometre rail string if it were heated by 50 K and not allowed to lengthen? What is the “wanted” extension?',
  'l = 1000 м, Δt = 50 К, α = 12·10⁻⁶ 1/К', 'l = 1000 m, Δt = 50 K, α = 12·10⁻⁶ 1/K', 'Δl = 12·10⁻⁶ · 1000 · 50 = 0,6 м.', 'Δl = 12·10⁻⁶ · 1000 · 50 = 0.6 m.',
  '0,6 м. Если плеть закреплена и не может удлиниться, в ней возникают огромные силы сжатия, и она может выгнуться. Поэтому плети закрепляют и укладывают при заданной температуре.', '0.6 m. If the string is fastened and cannot lengthen, huge compressive forces arise and it may buckle. That is why strings are fastened and laid at a set temperature.'),
 task(6, 'Мост', 'A bridge', 'Стальной мост длиной 100 м зимой имеет температуру −20 °C, летом +40 °C. Какой запас на расширение нужен?', 'A 100 m steel bridge is at −20 °C in winter and +40 °C in summer. What allowance for expansion is needed?',
  'l = 100 м, Δt = 60 К, α = 12·10⁻⁶ 1/К', 'l = 100 m, Δt = 60 K, α = 12·10⁻⁶ 1/K', 'Δl = 12·10⁻⁶ · 100 · 60 = 0,072 м.', 'Δl = 12·10⁻⁶ · 100 · 60 = 0.072 m.',
  'около 72 мм. Для этого в конструкции делают температурные швы.', 'about 72 mm. Expansion joints are built in for this.'),
]

quiz = [
 ('Чему равен абсолютный нуль по шкале Цельсия?', [('−273,15 °C', 'Верно: 0 К = −273,15 °C — самая низкая возможная температура.'), ('0 °C', 'Это температура таяния льда, а не абсолютный нуль.'), ('−100 °C', 'Такое значение не соответствует абсолютному нулю.')],
  'What is absolute zero on the Celsius scale?', [('−273.15 °C', 'Correct: 0 K = −273.15 °C, the lowest possible temperature.'), ('0 °C', 'That is the melting point of ice, not absolute zero.'), ('−100 °C', 'This value does not correspond to absolute zero.')], 0),
 ('Какова температура 20 °C по шкале Кельвина?', [('20 К', 'Число нужно увеличить на 273,15.'), ('293 К', 'Верно: 20 + 273,15 ≈ 293 К.'), ('−253 К', 'По шкале Кельвина температура не бывает отрицательной.')],
  'What is 20 °C on the Kelvin scale?', [('20 K', 'You must add 273.15 to the number.'), ('293 K', 'Correct: 20 + 273.15 ≈ 293 K.'), ('−253 K', 'A temperature on the Kelvin scale is never negative.')], 1),
 ('Температура выросла на 10 °C. На сколько кельвинов?', [('На 283 К', 'Прибавлять 273,15 нужно к самой температуре, а не к её изменению.'), ('На 10 К', 'Верно: деление шкалы Кельвина равно делению шкалы Цельсия.'), ('На 18 К', 'Это пересчёт для шкалы Фаренгейта (умножение на 1,8).')],
  'The temperature rose by 10 °C. By how many kelvins?', [('By 283 K', 'You add 273.15 to the temperature itself, not to its change.'), ('By 10 K', 'Correct: a division of the Kelvin scale equals a division of the Celsius scale.'), ('By 18 K', 'That is the conversion for the Fahrenheit scale (multiply by 1.8).')], 1),
 ('Почему между рельсами оставляют зазоры?', [('Чтобы рельсы не ржавели', 'Зазоры нужны не для защиты от коррозии.'), ('Чтобы рельсы могли расширяться при нагревании', 'Верно: летом металл удлиняется, и без зазоров рельсы выгнулись бы.'), ('Чтобы поезд меньше шумел', 'Наоборот, стыки создают стук; они нужны ради расширения.')],
  'Why are gaps left between rails?', [('To stop rails from rusting', 'Gaps are not there to prevent corrosion.'), ('So the rails can expand when heated', 'Correct: in summer the metal lengthens and without gaps the rails would buckle.'), ('To make the train quieter', 'On the contrary, joints create a clatter; they are there for expansion.')], 1),
 ('Какой стержень при одинаковых длине и нагреве удлинится больше: стальной или алюминиевый?', [('Стальной', 'У стали α меньше (около 12·10⁻⁶ 1/К).'), ('Алюминиевый', 'Верно: у алюминия α примерно 25·10⁻⁶ 1/К — вдвое больше, чем у стали.'), ('Одинаково', 'Удлинение зависит от материала через коэффициент α.')],
  'Which rod lengthens more for the same length and heating: steel or aluminium?', [('Steel', 'Steel has a smaller α (about 12·10⁻⁶ 1/K).'), ('Aluminium', 'Correct: aluminium’s α is about 25·10⁻⁶ 1/K, roughly twice that of steel.'), ('The same', 'The extension depends on the material through the coefficient α.')], 1),
 ('Что показывает температура тела?', [('Сколько в теле теплоты', 'Количество теплоты зависит ещё и от массы и вещества.'), ('Степень нагретости тела (связана со средней энергией движения частиц)', 'Верно.'), ('Из какого вещества тело', 'Вещество определяет другие свойства, а температура — степень нагретости.')],
  'What does the temperature of a body show?', [('How much heat the body contains', 'The amount of heat also depends on the mass and the substance.'), ('How hot the body is (related to the average energy of its particles’ motion)', 'Correct.'), ('What substance the body is made of', 'The substance determines other properties; temperature is how hot the body is.')], 1),
 ('На каком явлении основан жидкостный термометр?', [('На тепловом расширении жидкости', 'Верно: жидкость расширяется заметно сильнее стекла, и столбик растёт.'), ('На притяжении к Земле', 'Сила тяжести тут не определяет показание.'), ('На испарении жидкости', 'Испарение не лежит в основе показания жидкостного термометра.')],
  'What is a liquid thermometer based on?', [('The thermal expansion of the liquid', 'Correct: the liquid expands noticeably more than the glass, so the column rises.'), ('Attraction to the Earth', 'Gravity does not set the reading here.'), ('Evaporation of the liquid', 'Evaporation is not the basis of a liquid thermometer.')], 0),
 ('Стальной рельс длиной 10 м нагрели на 50 К (α = 12·10⁻⁶ 1/К). Насколько он удлинился?', [('6 мм', 'Верно: Δl = 12·10⁻⁶ · 10 · 50 = 0,006 м.'), ('60 мм', 'Это в десять раз больше: проверьте степень десяти.'), ('0,6 мм', 'Это в десять раз меньше расчётного значения.')],
  'A 10 m steel rail was heated by 50 K (α = 12·10⁻⁶ 1/K). By how much did it lengthen?', [('6 mm', 'Correct: Δl = 12·10⁻⁶ · 10 · 50 = 0.006 m.'), ('60 mm', 'That is ten times too much: check the power of ten.'), ('0.6 mm', 'That is ten times less than the computed value.')], 0),
]

js = r'''
const T={ru:{
 scaLabel:"Термометр и три шкалы температуры",expLabel:"Стержень до и после нагревания",
 mats:["Сталь (α = 12·10⁻⁶ 1/К)","Медь (α = 17·10⁻⁶ 1/К)","Алюминий (α = 25·10⁻⁶ 1/К)","Обычное стекло (α = 9·10⁻⁶ 1/К)"],
 scaFb:[["Ниже абсолютного нуля быть не может. Здесь температура не опускается ниже −60 °C.",-1e9],["Ниже точки замерзания воды (0 °C): вода превращается в лёд.",0],["Выше точки замерзания воды, но ниже комнатной температуры.",18],["Примерно комнатная температура.",24],["Тепло, но вода ещё жидкая.",99.5],["Температура кипения воды при нормальном давлении (100 °C).",100.5],["Выше 100 °C вода при нормальном давлении — пар.",1e9]],
 start:"До нагревания",end:"После нагревания",ext:"Удлинение (увеличено)",
 expFb:"Чем больше длина, перепад температур и коэффициент α, тем больше удлинение. У алюминия α примерно вдвое больше, чем у стали."},
 en:{
 scaLabel:"A thermometer and three temperature scales",expLabel:"A rod before and after heating",
 mats:["Steel (α = 12·10⁻⁶ 1/K)","Copper (α = 17·10⁻⁶ 1/K)","Aluminium (α = 25·10⁻⁶ 1/K)","Ordinary glass (α = 9·10⁻⁶ 1/K)"],
 scaFb:[["Below absolute zero is impossible. Here the temperature does not go below −60 °C.",-1e9],["Below the freezing point of water (0 °C): water turns to ice.",0],["Above the freezing point of water but below room temperature.",18],["About room temperature.",24],["Warm, but the water is still liquid.",99.5],["The boiling point of water at normal pressure (100 °C).",100.5],["Above 100 °C water at normal pressure is steam.",1e9]],
 start:"Before heating",end:"After heating",ext:"Extension (magnified)",
 expFb:"The greater the length, temperature change and coefficient α, the greater the extension. Aluminium’s α is roughly twice that of steel."}};
const ALPHA=[12e-6,17e-6,25e-6,9e-6];
function drawSca(){const t=tt(),c=+$("st").value,k=c+273.15,f=1.8*c+32,top=40,bot=260,Y=v=>bot-(v+60)/180*(bot-top);
 let g='<rect x="120" y="'+(top-10)+'" width="22" height="'+(bot-top+30)+'" rx="11" fill="#f2f2ef" stroke="#18181a" stroke-width="2"/><circle cx="131" cy="'+(bot+22)+'" r="17" fill="#b6533f" stroke="#18181a" stroke-width="2"/>';
 g+='<rect x="126" y="'+Y(c)+'" width="10" height="'+(bot+20-Y(c))+'" fill="#b6533f"/>';
 [[0,lang==="ru"?"лёд тает":"ice melts"],[20,lang==="ru"?"комнатная (≈20)":"room (≈20)"],[100,lang==="ru"?"вода кипит":"water boils"]].forEach(p=>{g+='<line x1="142" y1="'+Y(p[0])+'" x2="156" y2="'+Y(p[0])+'" stroke="#18181a"/>'+svgText(162,Y(p[0])+4,p[1],"#66666b","start",10)});
 for(let v=-60;v<=120;v+=20){g+='<line x1="106" y1="'+Y(v)+'" x2="120" y2="'+Y(v)+'" stroke="#18181a"/>'+svgText(100,Y(v)+4,v,"#66666b","end",10)}
 g+='<line x1="106" y1="'+Y(c)+'" x2="300" y2="'+Y(c)+'" stroke="#b6533f" stroke-dasharray="4 3"/>';
 g+=svgText(330,90,"°C: "+fmt(c,0),"#18181a","start",15)+svgText(330,126,"K: "+fmt(k,2),"#2f6f5d","start",15)+svgText(330,162,"°F: "+fmt(f,1),"#3f5f8f","start",15);
 g+=svgText(330,205,"0 K = −273,15 °C".replace(",",lang==="ru"?",":"."),"#66666b","start",11)+svgText(330,224,"T = t + 273,15".replace(",",lang==="ru"?",":"."),"#66666b","start",11);
 $("scaSvg").innerHTML=g;
 $("stOut").textContent=fmt(c,0)+" °C";$("sK").textContent=fmt(k,2)+" K";$("sF").textContent=fmt(f,1)+" °F";$("sC").textContent=fmt(c,0)+" °C";
 const fb=t.scaFb.find(x=>c<x[1]);$("scaFb").textContent=(fb||t.scaFb[t.scaFb.length-1])[0]}
$("st").addEventListener("input",drawSca);
function drawExp(){const t=tt(),i=+$("em").value,a=ALPHA[i],L=+$("el").value,dt=+$("ed").value,dl=a*L*dt,ext=Math.min(150,a*dt*360*200);
 let g=svgText(30,34,t.start,"#66666b","start",11)+'<rect x="40" y="46" width="360" height="22" fill="#8a8a8f" stroke="#18181a"/>';
 g+=svgText(30,112,t.end,"#66666b","start",11)+'<rect x="40" y="124" width="360" height="22" fill="#b6533f" stroke="#18181a"/><rect x="400" y="124" width="'+ext+'" height="22" fill="#e3a395" stroke="#18181a"/>';
 g+='<line x1="400" y1="60" x2="400" y2="190" stroke="#18181a" stroke-dasharray="3 3"/>'+arrow(400,176,400+Math.max(ext,4),176,"#2f6f5d",3)+svgText(400,200,t.ext+": "+fmt(dl*1000,1)+t.mm,"#2f6f5d","start",12);
 $("expSvg").innerHTML=g;
 $("elOut").textContent=L+t.m;$("edOut").textContent=dt+t.K;
 $("eL").textContent=fmt(dl*1000,1)+t.mm;$("eM").textContent=fmt(a*dt*1000,2)+t.mm;$("eR").textContent=fmt(a*dt*100,3)+" %";
 $("expFb").textContent=t.expFb}
["em","el","ed"].forEach(id=>$(id).addEventListener("input",drawExp));
const LAB={ru:{scaSvg:T.ru.scaLabel,expSvg:T.ru.expLabel},en:{scaSvg:T.en.scaLabel,expSvg:T.en.expLabel}};
function drawAll(){fillSel("em",T[lang].mats,0);drawSca();drawExp()}
'''

c = dict(n='08', slug='08-temperature.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Температура и термометры', 'Temperature and thermometers'),
 desc='Глава 8 Атласа физики: температура, шкалы Цельсия, Кельвина и Фаренгейта, абсолютный нуль, термометры, тепловое расширение.',
 lead=('Мороз на перевале, кипяток в чайнике, зазоры между рельсами. Эта глава начинает блок о тепловых явлениях: что такое температура, как её измеряют в разных шкалах и почему тела при нагревании расширяются.',
       'Frost on a mountain pass, boiling water in a kettle, gaps between rails. This chapter opens the block on thermal phenomena: what temperature is, how it is measured on different scales and why bodies expand when heated.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('temp', 'Температура', 'Temperature'), ('scales', 'Шкалы', 'Scales'), ('expansion', 'Расширение', 'Expansion'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Железнодорожные рельсы укладывают с небольшими зазорами в стыках, а на мостах делают специальные температурные швы. Летом зазоры почти закрываются, зимой они шире.</p><p>Зачем нужны зазоры? Что случилось бы с длинным рельсом, если сварить его без зазора и закрепить намертво, а потом сильно нагреть солнцем?</p>',
         '<p>Railway rails are laid with small gaps at the joints, and bridges have special expansion joints. In summer the gaps almost close; in winter they are wider.</p><p>Why are the gaps needed? What would happen to a long rail welded without gaps and fastened firmly, then strongly heated by the sun?</p>'),
 hint=('Подсказку даст модель «Тепловое расширение». Разгадка — в конце главы.', 'The “Thermal expansion” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: зачем нужны зазоры', 'The answer: why gaps are needed'),
 answer=('<p>Металл при нагревании удлиняется: Δl = α·l·Δt. Для стального рельса длиной 25 м и перепада температур 70 К удлинение около 21 мм (задача 4), а для километровой плети при нагреве на 50 К — 0,6 м (задача 5). Зазоры дают рельсам место, чтобы удлиняться, не упираясь друг в друга.</p><p>Если же сварить длинную плеть и закрепить, она не может удлиниться, и вместо удлинения в ней возникают огромные силы сжатия. Тогда в сильную жару рельс способен выгнуться. Поэтому плети закрепляют и укладывают при заданной температуре.</p>',
         '<p>Metal lengthens when heated: Δl = α·l·Δt. For a 25 m steel rail and a temperature swing of 70 K the extension is about 21 mm (problem 4), and for a kilometre-long string heated by 50 K it is 0.6 m (problem 5). Gaps give rails room to lengthen without pushing against each other.</p><p>If a long string is welded and fastened it cannot lengthen, and instead enormous compressive forces build up. In strong heat the rail can then buckle. That is why strings are fastened and laid at a set temperature.</p>'),
 sources=[
  ('Абсолютный нуль, шкала Кельвина, постоянная Больцмана —', 'Absolute zero, the Kelvin scale, the Boltzmann constant —', LINK('https://www.nist.gov/pml/boltzmann-constant', 'NIST: Boltzmann constant') + ', ' + LINK('https://technav.ieee.org/topic/kelvin/', 'IEEE TechNav: Kelvin')),
  ('Коэффициенты линейного расширения, формула Δl = α·l·Δt —', 'Linear expansion coefficients, the formula Δl = α·l·Δt —', LINK('https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_(OpenStax)/University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/01:_Temperature_and_Heat/1.04:_Thermal_Expansion', 'OpenStax University Physics II, 1.4: Thermal Expansion') + ', ' + LINK('https://phys.libretexts.org/Bookshelves/College_Physics/Book:_College_Physics_(OpenStax)/13:_Temperature_Kinetic_Theory_and_the_Gas_Laws/13.02:_Thermal_Expansion_of_Solids_and_Liquids', 'OpenStax College Physics 13.2')),
  ('Рельсовые плети, нейтральная температура, выгибание от жары —', 'Rail strings, neutral temperature, heat buckling —', LINK('https://interfacejournal.com/archives/644', 'Interface Journal: Preventing Track Buckles') + ', ' + LINK('https://www.trackopedia.info/encyclopedia/maintenance-of-way/mechanised-track-laying/welding-technology/neutralisation/', 'Trackopedia: Neutralisation')),
  ('Наибольшая плотность воды при 4 °C —', 'Water is densest at 4 °C —', LINK('https://engineeringtoolbox.com/water-thermal-properties--d_162.html', 'Engineering ToolBox: Water thermal properties'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения α — приближённые, из таблиц учебников.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The α values are approximate, from textbook tables.'),
 prev=('07-kinematics.html', 'Глава 07 · Кинематика', 'Chapter 07 · Kinematics'),
 next=('09-heat-transfer.html', 'Глава 09 · Теплопередача', 'Chapter 09 · Heat transfer'),
 js=js)
build(c)
