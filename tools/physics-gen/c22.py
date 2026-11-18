# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ПОЛЕ ПРЯМОГО ПРОВОДА', 'THE FIELD OF A STRAIGHT WIRE', 'swSvg', '0 0 600 250',
  slider('si', 'Сила тока', 'Current', 1, 1000, 1, 100) + slider('sr', 'Расстояние от провода', 'Distance from the wire', 1, 100, 1, 10),
  stats([('sB', 'Индукция B = μ₀I/(2πr)', 'Flux density B = μ₀I/(2πr)'), ('sE', 'Против поля Земли (50 мкТл)', 'Against the Earth’s field (50 µT)')]),
  'swFb', 'Схема условная: поле показано кольцами вокруг провода; расстояние в сантиметрах. μ₀ = 4π·10⁻⁷ Тл·м/А.',
  'A schematic drawing: the field is shown as rings around the wire; the distance is in centimetres. μ₀ = 4π·10⁻⁷ T·m/A.')
s1 = section('wire', 'Ток создаёт магнитное поле', 'A current creates a magnetic field',
 bd('<p>В 1820 году датчанин Эрстед заметил, что стрелка компаса отклоняется, если рядом по проводу идёт ток. Значит, <strong>ток создаёт магнитное поле</strong>. Вокруг прямого провода линии поля — окружности, лежащие в плоскостях, перпендикулярных проводу. Направление находят по <strong>правилу правой руки</strong>: если большой палец направить вдоль тока, согнутые четыре пальца покажут направление линий поля.</p><p>Индукция поля прямого тока на расстоянии <em>r</em> от провода:</p>',
    '<p>In 1820 the Dane Ørsted noticed that a compass needle deflects when a current flows in a nearby wire. So <strong>a current creates a magnetic field</strong>. Around a straight wire the field lines are circles lying in planes perpendicular to the wire. The direction is found by the <strong>right-hand rule</strong>: point the thumb along the current and the four curled fingers show the direction of the field lines.</p><p>The flux density of a straight current at distance <em>r</em> from the wire is:</p>')
 + formula('B = μ₀ · I / (2π · r)', 'μ₀ = 4π·10⁻⁷ Тл·м/А — магнитная постоянная; поле убывает как 1/r', 'μ₀ = 4π·10⁻⁷ T·m/A is the magnetic constant; the field falls as 1/r'),
 lab1)

lab2 = model(2, 'КАТУШКА И ЭЛЕКТРОМАГНИТ', 'A COIL AND AN ELECTROMAGNET', 'ceSvg', '0 0 600 250',
  select('cc', 'Сердечник', 'Core') + slider('ci', 'Сила тока', 'Current', 0.1, 5, 0.1, 1) + slider('cn', 'Число витков на 10 см', 'Turns per 10 cm', 50, 1000, 10, 300),
  stats([('cB', 'Индукция внутри B = μ₀μ·nI', 'Flux density inside B = μ₀μ·nI'), ('cK', 'Против поля Земли', 'Against the Earth’s field')]),
  'ceFb', 'Схема условная: длинная катушка; относительная проницаемость сердечника принята 500 (железо; на деле она зависит от сорта и поля). Выше насыщения (около 1,5–2 Тл) железо усиливает поле уже слабее, модель этого не учитывает.',
  'A schematic drawing: a long coil; the relative permeability of the core is taken as 500 (iron; in fact it depends on the grade and field). Above saturation (about 1.5–2 T) iron boosts the field less, which the model does not account for.')
s2 = section('coil', 'Катушка и электромагнит', 'The coil and the electromagnet',
 bd('<p>Если провод свернуть в <strong>катушку</strong> (соленоид), поля витков складываются, а внутри длинной катушки поле почти однородное:</p>',
    '<p>If a wire is wound into a <strong>coil</strong> (solenoid) the fields of the turns add up, and inside a long coil the field is nearly uniform:</p>')
 + formula('B = μ₀ · n · I', 'n — число витков на единицу длины; с железным сердечником поле растёт в сотни раз: B = μ₀μ · n · I', 'n is the number of turns per unit length; with an iron core the field grows hundreds of times: B = μ₀μ · n · I')
 + bd('<p>Катушка с сердечником — <strong>электромагнит</strong>. В отличие от обычного магнита его включают и выключают током и регулируют силу. Так работают звонки, реле, подъёмные краны на металлоломе, магнитные замки и томографы.</p>',
      '<p>A coil with a core is an <strong>electromagnet</strong>. Unlike an ordinary magnet it is switched on and off by current and its strength is adjusted. That is how bells, relays, scrap-metal cranes, magnetic locks and tomographs work.</p>'),
 lab2)

lab3 = model(3, 'СИЛА НА ПРОВОД С ТОКОМ', 'THE FORCE ON A CURRENT-CARRYING WIRE', 'fcSvg', '0 0 600 250',
  slider('fb', 'Индукция поля', 'Flux density', 0.05, 1, 0.05, 0.5) + slider('fi', 'Сила тока', 'Current', 1, 20, 1, 10) + slider('fl', 'Длина проводника в поле', 'Length of the conductor in the field', 0.05, 1, 0.05, 0.2),
  stats([('fF', 'Сила Ампера F = B·I·L', 'Ampère force F = B·I·L'), ('fM', 'Эквивалентно весу груза', 'Equivalent to the weight of a load')]),
  'fcFb', 'Схема условная: проводник перпендикулярен линиям поля; g = 9,8 Н/кг.', 'A schematic drawing: the conductor is perpendicular to the field lines; g = 9.8 N/kg.')
s3 = section('force', 'Сила Ампера и электродвигатель', 'The Ampère force and the electric motor',
 bd('<p>Магнитное поле действует на проводник с током. Если проводник длиной <em>L</em> расположен перпендикулярно линиям поля, то на него действует <strong>сила Ампера</strong>:</p>',
    '<p>A magnetic field acts on a conductor carrying current. If a conductor of length <em>L</em> is perpendicular to the field lines it experiences the <strong>Ampère force</strong>:</p>')
 + formula('F = B · I · L', 'направление — по правилу левой руки: линии поля входят в ладонь, четыре пальца по току, отогнутый палец покажет силу', 'the direction is by the left-hand rule: field lines enter the palm, four fingers along the current, the thumb shows the force')
 + bd('<p>На этой силе работает <strong>электродвигатель</strong>: рамка с током в магнитном поле поворачивается, а коллектор вовремя меняет направление тока, и вращение продолжается. Такие двигатели стоят в дрелях, стиральных машинах, электромобилях.</p>',
      '<p>The <strong>electric motor</strong> works on this force: a loop carrying current in a magnetic field turns, and a commutator reverses the current at the right moment so the rotation continues. Such motors are in drills, washing machines and electric cars.</p>'),
 lab3)

tasks = [
 task(1, 'Поле провода', 'Field of a wire', 'Найдите индукцию поля на расстоянии 10 см от прямого провода с током 100 А. μ₀ = 4π·10⁻⁷ Тл·м/А.', 'Find the flux density 10 cm from a straight wire carrying 100 A. μ₀ = 4π·10⁻⁷ T·m/A.',
  'I = 100 А, r = 0,1 м', 'I = 100 A, r = 0.1 m', 'B = μ₀·I / (2π·r) = 4π·10⁻⁷ · 100 / (2π · 0,1) = 2·10⁻⁷ · 100 / 0,1 = 2·10⁻⁴ Тл.', 'B = μ₀·I / (2π·r) = 4π·10⁻⁷ · 100 / (2π · 0.1) = 2·10⁻⁷ · 100 / 0.1 = 2·10⁻⁴ T.',
  '200 мкТл — в 4 раза сильнее поля Земли (50 мкТл).', '200 µT — 4 times stronger than the Earth’s field (50 µT).', True),
 task(2, 'Поле катушки', 'Field of a coil', 'Катушка имеет 500 витков на длине 0,2 м, ток 2 А. Найдите индукцию поля внутри (без сердечника).', 'A coil has 500 turns over 0.2 m, current 2 A. Find the flux density inside (no core).',
  'N = 500, l = 0,2 м, I = 2 А', 'N = 500, l = 0.2 m, I = 2 A', 'n = N / l = 2500 витков/м.<br>B = μ₀·n·I = 4π·10⁻⁷ · 2500 · 2 ≈ 6,3·10⁻³ Тл.', 'n = N / l = 2,500 turns/m.<br>B = μ₀·n·I = 4π·10⁻⁷ · 2,500 · 2 ≈ 6.3·10⁻³ T.',
  'около 6,3 мТл — в 125 раз сильнее поля Земли.', 'about 6.3 mT — 125 times the Earth’s field.'),
 task(3, 'С железным сердечником', 'With an iron core', 'Во сколько раз вырастет поле катушки из задачи 2, если вставить железный сердечник с проницаемостью 500?', 'By what factor does the coil’s field of problem 2 grow if an iron core of permeability 500 is inserted?',
  'μ = 500', 'μ = 500', 'B = μ₀·μ·n·I — в μ раз больше: 6,3 мТл · 500 ≈ 3,1 Тл.', 'B = μ₀·μ·n·I — μ times greater: 6.3 mT · 500 ≈ 3.1 T.',
  'в 500 раз. На деле железо насыщается около 1,5–2 Тл, поэтому реальный выигрыш меньше.', '500 times. In reality iron saturates at about 1.5–2 T, so the real gain is smaller.'),
 task(4, 'Сила Ампера', 'The Ampère force', 'Проводник длиной 0,2 м с током 10 А находится в поле 0,5 Тл перпендикулярно линиям. Найдите силу.', 'A 0.2 m conductor carrying 10 A is in a 0.5 T field, perpendicular to the lines. Find the force.',
  'L = 0,2 м, I = 10 А, B = 0,5 Тл', 'L = 0.2 m, I = 10 A, B = 0.5 T', 'F = B·I·L = 0,5 · 10 · 0,2 = 1 Н.', 'F = B·I·L = 0.5 · 10 · 0.2 = 1 N.',
  '1 Н — вес груза в 100 г.', '1 N — the weight of a 100 g load.'),
 task(5, 'Какой ток нужен', 'What current is needed', 'Какой ток надо пропустить по прямому проводнику длиной 0,5 м в поле 0,2 Тл, чтобы сила Ампера уравновесила вес проводника массой 20 г?', 'What current must flow in a straight conductor of length 0.5 m in a 0.2 T field for the Ampère force to balance the weight of a 20 g conductor?',
  'L = 0,5 м, B = 0,2 Тл, m = 0,02 кг', 'L = 0.5 m, B = 0.2 T, m = 0.02 kg', 'B·I·L = m·g, I = m·g / (B·L) = 0,02 · 9,8 / (0,2 · 0,5) = 0,196 / 0,1 = 1,96 А.', 'B·I·L = m·g, I = m·g / (B·L) = 0.02 · 9.8 / (0.2 · 0.5) = 0.196 / 0.1 = 1.96 A.',
  'около 2 А.', 'about 2 A.'),
 task(6, 'Линия электропередачи', 'A power line', 'По проводу линии течёт ток 500 А. Какая индукция создаётся на земле, на 10 м ниже провода? Сравните с полем Земли.', 'A current of 500 A flows in a power-line wire. What flux density is created on the ground, 10 m below it? Compare with the Earth’s field.',
  'I = 500 А, r = 10 м', 'I = 500 A, r = 10 m', 'B = 2·10⁻⁷ · I / r = 2·10⁻⁷ · 500 / 10 = 10⁻⁵ Тл = 10 мкТл.', 'B = 2·10⁻⁷ · I / r = 2·10⁻⁷ · 500 / 10 = 10⁻⁵ T = 10 µT.',
  '10 мкТл — это в 5 раз слабее поля Земли (50 мкТл); от одного провода постоянного тока.', '10 µT — 5 times weaker than the Earth’s field (50 µT); for a single direct-current wire.'),
]

quiz = [
 ('Кто и как обнаружил, что ток создаёт магнитное поле?', [('Эрстед: стрелка компаса отклонилась возле провода с током', 'Верно.'), ('Ньютон: яблоко упало', 'Это закон тяготения.'), ('Архимед: вода вытеснилась', 'Это закон Архимеда.')],
  'Who discovered, and how, that a current creates a magnetic field?', [('Ørsted: a compass needle deflected near a wire with current', 'Correct.'), ('Newton: an apple fell', 'That is the law of gravitation.'), ('Archimedes: water was displaced', 'That is Archimedes’ principle.')], 0),
 ('Какой формы линии магнитного поля вокруг прямого провода с током?', [('Окружности вокруг провода', 'Верно.'), ('Прямые вдоль провода', 'Они охватывают провод.'), ('Расходящиеся лучи', 'Это поле заряда.')],
  'What shape are the magnetic field lines around a straight wire with current?', [('Circles around the wire', 'Correct.'), ('Straight lines along the wire', 'They go round the wire.'), ('Diverging rays', 'That is the field of a charge.')], 0),
 ('Как поле прямого тока зависит от расстояния до провода?', [('Убывает как 1/r', 'Верно.'), ('Растёт с расстоянием', 'Оно слабеет.'), ('Не зависит', 'Зависит от расстояния.')],
  'How does the field of a straight current depend on distance from the wire?', [('Falls as 1/r', 'Correct.'), ('Grows with distance', 'It weakens.'), ('Does not depend', 'It depends on distance.')], 0),
 ('Что получится, если в катушку с током вставить железный сердечник?', [('Поле резко возрастёт', 'Верно: железо усиливает поле в сотни раз.'), ('Поле исчезнет', 'Железо усиливает поле.'), ('Не изменится', 'Железо сильно влияет.')],
  'What happens if an iron core is put into a coil carrying current?', [('The field grows sharply', 'Correct: iron boosts the field hundreds of times.'), ('The field disappears', 'Iron boosts the field.'), ('Nothing changes', 'Iron has a strong effect.')], 0),
 ('Чем электромагнит удобнее постоянного магнита?', [('Его включают и выключают током и регулируют силу', 'Верно.'), ('Он слабее', 'Электромагнит может быть сильнее.'), ('Он не требует энергии', 'Он потребляет энергию при токе.')],
  'How is an electromagnet more convenient than a permanent magnet?', [('It is switched on and off by current and its strength is adjusted', 'Correct.'), ('It is weaker', 'An electromagnet can be stronger.'), ('It needs no energy', 'It uses energy when current flows.')], 0),
 ('По какой формуле находят силу Ампера (проводник перпендикулярен полю)?', [('F = B·I·L', 'Верно.'), ('F = B / (I·L)', 'Такой формулы нет.'), ('F = I·L / B', 'Такой формулы нет.')],
  'By which formula is the Ampère force found (conductor perpendicular to the field)?', [('F = B·I·L', 'Correct.'), ('F = B / (I·L)', 'There is no such formula.'), ('F = I·L / B', 'There is no such formula.')], 0),
 ('На каком явлении основана работа электродвигателя?', [('Действие магнитного поля на проводник с током', 'Верно.'), ('Электролиз', 'Это другое явление.'), ('Тепловое расширение', 'Это другое явление.')],
  'On what phenomenon is the electric motor based?', [('The action of a magnetic field on a conductor with current', 'Correct.'), ('Electrolysis', 'That is another phenomenon.'), ('Thermal expansion', 'That is another phenomenon.')], 0),
 ('Что нужно изменить, чтобы поле катушки стало вдвое сильнее (без сердечника)?', [('Вдвое увеличить ток', 'Верно: B ~ I.'), ('Вдвое уменьшить ток', 'Тогда поле ослабнет.'), ('Ничего', 'Поле зависит от тока и числа витков.')],
  'What must change for a coil’s field to double (no core)?', [('Double the current', 'Correct: B ~ I.'), ('Halve the current', 'The field would weaken.'), ('Nothing', 'The field depends on current and turns.')], 0),
]

js = r'''
const T={ru:{
 swLabel:"Провод с током и кольца магнитного поля вокруг него",ceLabel:"Катушка с током и поле внутри неё",fcLabel:"Проводник с током между полюсами магнита",
 cores:["Воздух (без сердечника)","Железный сердечник"],
 swFb:"Дальше от провода — слабее поле: B ~ 1/r.",ceFb:"Больше витков и тока — сильнее поле; железо усиливает его в сотни раз.",fcFb:"Сила прямо пропорциональна индукции, току и длине."},
 en:{
 swLabel:"A wire with current and rings of its magnetic field",ceLabel:"A coil with current and the field inside it",fcLabel:"A conductor with current between the poles of a magnet",
 cores:["Air (no core)","Iron core"],
 swFb:"The farther from the wire, the weaker the field: B ~ 1/r.",ceFb:"More turns and current — a stronger field; iron boosts it hundreds of times.",fcFb:"The force is directly proportional to flux density, current and length."}};
const MU0=4*Math.PI*1e-7;
function tb(B){return B>=1?fmt(B,2)+(lang==="ru"?" Тл":" T"):B>=1e-3?fmt(B*1e3,1)+(lang==="ru"?" мТл":" mT"):fmt(B*1e6,1)+(lang==="ru"?" мкТл":" µT")}
function drawSw(){const t=tt(),I=+$("si").value,r=+$("sr").value/100,B=MU0*I/(2*Math.PI*r);
 let g='<circle cx="300" cy="125" r="8" fill="#18181a"/>'+svgText(300,128,"•","#fff","middle",10);
 [30,55,85,120].forEach((R,k)=>{g+='<circle cx="300" cy="125" r="'+R+'" fill="none" stroke="'+(k===0?"#b6533f":"#c9c2b0")+'" stroke-width="'+(3-k*0.5)+'"/>'});
 const R=Math.min(120,25+r*100*3);g+='<circle cx="300" cy="125" r="'+R+'" fill="none" stroke="#2f6f5d" stroke-width="2" stroke-dasharray="5 3"/>';
 g+=arrow(300,125-R,320,125-R,"#2f6f5d",2)+svgText(300,240,"r = "+fmt(r*100,0)+(lang==="ru"?" см":" cm"),"#66666b","middle",12);
 $("swSvg").innerHTML=g;
 $("siOut").textContent=num(I)+" A";$("srOut").textContent=fmt(r*100,0)+(lang==="ru"?" см":" cm");
 $("sB").textContent=tb(B);$("sE").textContent=fmt(B/50e-6,2)+"×";$("swFb").textContent=t.swFb}
["si","sr"].forEach(id=>$(id).addEventListener("input",drawSw));
function drawCe(){const t=tt(),core=+$("cc").value,I=+$("ci").value,n=+$("cn").value*10,B=MU0*(core?500:1)*n*I;
 let g='<rect x="140" y="100" width="320" height="50" rx="6" fill="'+(core?"#9a9a9a":"#f1efe8")+'" stroke="#18181a" stroke-width="2"/>';
 for(let k=0;k<14;k++){g+='<path d="M'+(150+k*22)+' 90 Q'+(156+k*22)+' 125 '+(150+k*22+12)+' 160" fill="none" stroke="#b87333" stroke-width="3"/>'}
 const L=Math.min(130,10+Math.log10(1+B*1e5)*28);
 g+=arrow(300,70,300+L,70,"#2f6f5d",3)+svgText(300,60,"B","#2f6f5d","middle",13);
 $("ceSvg").innerHTML=g;
 $("ciOut").textContent=fmt(I,1)+" A";$("cnOut").textContent=+$("cn").value;
 $("cB").textContent=tb(B);$("cK").textContent=B/50e-6>=1000?num(Math.round(B/50e-6))+"×":fmt(B/50e-6,1)+"×";$("ceFb").textContent=t.ceFb}
["cc","ci","cn"].forEach(id=>$(id).addEventListener("input",drawCe));
function drawFc(){const t=tt(),B=+$("fb").value,I=+$("fi").value,L=+$("fl").value,F=B*I*L;
 let g='<rect x="120" y="40" width="130" height="170" fill="#3f5f8f" stroke="#18181a"/><rect x="350" y="40" width="130" height="170" fill="#b6533f" stroke="#18181a"/>'+svgText(185,130,"N","#fff","middle",24)+svgText(415,130,"S","#fff","middle",24);
 g+='<line x1="250" y1="125" x2="350" y2="125" stroke="#18181a" stroke-width="5"/>'+svgText(300,105,"I","#18181a","middle",13);
 const Lf=Math.min(80,8+F*10);
 g+=arrow(300,125,300,125-Lf,"#2f6f5d",3)+svgText(318,125-Lf,"F","#2f6f5d","start",13);
 $("fcSvg").innerHTML=g;
 $("fbOut").textContent=fmt(B,2)+(lang==="ru"?" Тл":" T");$("fiOut").textContent=I+" A";$("flOut").textContent=fmt(L,2)+(lang==="ru"?" м":" m");
 $("fF").textContent=fmt(F,2)+(lang==="ru"?" Н":" N");$("fM").textContent=fmt(F/9.8*1000,0)+(lang==="ru"?" г":" g");$("fcFb").textContent=t.fcFb}
["fb","fi","fl"].forEach(id=>$(id).addEventListener("input",drawFc));
const LAB={ru:{swSvg:T.ru.swLabel,ceSvg:T.ru.ceLabel,fcSvg:T.ru.fcLabel},en:{swSvg:T.en.swLabel,ceSvg:T.en.ceLabel,fcSvg:T.en.fcLabel}};
function drawAll(){fillSel("cc",T[lang].cores,0);drawSw();drawCe();drawFc()}
'''

c = dict(n='22', slug='22-magnetic-field-of-current.html', block='IV', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Магнитное поле тока', 'The magnetic field of a current'),
 desc='Глава 22 Атласа физики: опыт Эрстеда, поле прямого тока и катушки, электромагнит, сила Ампера, электродвигатель.',
 lead=('Электрический ток действует на стрелку компаса, а электромагнит поднимает целые автомобили. Магнитное поле тока, катушка и сила Ампера.',
       'An electric current acts on a compass needle, and an electromagnet lifts whole cars. The magnetic field of a current, the coil and the Ampère force.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('wire', 'Поле провода', 'Field of a wire'), ('coil', 'Электромагнит', 'Electromagnet'), ('force', 'Сила Ампера', 'Ampère force'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На заводе по переработке металлолома подъёмный кран вешает на цепь тяжёлую плиту. Она хватает груду железного лома, поднимает её и переносит, а потом по команде оператора лом разом отпускает. Плита нигде не цепляется крюками и не зажимает груз.</p><p>Как можно «держать» и «отпускать» железо на расстоянии?</p>',
         '<p>At a scrap-metal recycling plant a crane hangs a heavy plate on a chain. It grips a heap of iron scrap, lifts and carries it, then on the operator’s command drops it all at once. The plate has no hooks and does not clamp the load.</p><p>How can one “hold” and “release” iron at a distance?</p>'),
 hint=('Подсказку даст модель «Катушка и электромагнит». Разгадка — в конце главы.', 'The “A coil and an electromagnet” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: подъёмный электромагнит', 'The answer: the lifting electromagnet'),
 answer=('<p>Плита — электромагнит: большая катушка с железным сердечником. Пока по ней идёт ток, поле намагничивает железный лом, и он притягивается. Стоит отключить ток — поле исчезает, и лом падает. Сила притяжения зависит от тока и числа витков (модель 2), а железный сердечник усиливает поле в сотни раз.</p><p>Постоянным магнитом так управлять нельзя: его нельзя «выключить».</p>',
         '<p>The plate is an electromagnet: a large coil with an iron core. While current flows in it the field magnetizes the scrap iron and it is attracted. Cut the current and the field disappears and the scrap falls. The pull depends on the current and the number of turns (model 2), and the iron core boosts the field hundreds of times.</p><p>A permanent magnet cannot be controlled like that: it cannot be “switched off”.</p>'),
 sources=[
  ('Опыт Эрстеда, поле прямого тока и катушки, μ₀ = 4π·10⁻⁷ Тл·м/А —', 'Ørsted’s experiment, the field of a straight wire and coil, μ₀ = 4π·10⁻⁷ T·m/A —', LINK('https://openstax.org/books/university-physics-volume-2/pages/12-introduction', 'OpenStax University Physics, Vol. 2, гл. 12') + ', ' + LINK('https://en.wikipedia.org/wiki/Solenoid', 'Wikipedia: Solenoid')),
  ('Сила Ампера, электродвигатель —', 'The Ampère force, the electric motor —', LINK('https://openstax.org/books/university-physics-volume-2/pages/11-introduction', 'OpenStax University Physics, Vol. 2, гл. 11')),
  ('Магнитное поле Земли 25–65 мкТл —', 'The Earth’s field 25–65 µT —', LINK('https://en.wikipedia.org/wiki/Earth%27s_magnetic_field', 'Wikipedia: Earth’s magnetic field'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Проницаемость сердечника 500 — условная.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The core permeability of 500 is assumed.'),
 prev=('21-magnets.html', 'Глава 21 · Магниты', 'Chapter 21 · Magnets'),
 next=('23-induction.html', 'Глава 23 · Электромагнитная индукция', 'Chapter 23 · Electromagnetic induction'),
 js=js)
build(c)
