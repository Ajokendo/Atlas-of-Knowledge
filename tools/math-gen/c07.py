# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'СХЕМА: ЧАСТИ И ЦЕЛОЕ', 'DIAGRAM: PARTS AND WHOLE', 'pwSvg', '0 0 600 250',
  select('pu', 'Что надо найти', 'What to find') + slider('p1', 'Первая часть', 'First part', 1, 20, 1, 12) + slider('p2', 'Вторая часть', 'Second part', 1, 20, 1, 17),
  stats([('pK', 'Что ищем', 'Unknown'), ('pA', 'Действие', 'Operation'), ('pR', 'Ответ', 'Answer')]),
  'pwFb', 'Целое — длинный отрезок сверху, части — внизу. Вопросительный знак стоит там, где число неизвестно.',
  'The whole is the long bar on top, the parts below. The question mark stands where the number is unknown.')
s1 = section('parts', 'Рисуем задачу', 'Drawing the problem',
 bd('<p>Задачу легче решить, если её <strong>нарисовать отрезками</strong>. Целое — длинный отрезок, части — короткие. Если неизвестно целое, части <strong>складываем</strong>. Если неизвестна часть, из целого <strong>вычитаем</strong> известную часть.</p>',
    '<p>A problem is easier to solve if you <strong>draw it with bars</strong>. The whole is a long bar, the parts are short ones. If the whole is unknown, we <strong>add</strong> the parts. If a part is unknown, we <strong>subtract</strong> the known part from the whole.</p>')
 + formula(bi('целое = часть + часть', 'whole = part + part'), 'часть = целое − другая часть', 'part = whole − the other part'),
 lab1)

lab2 = model(2, 'НА СКОЛЬКО И ВО СКОЛЬКО РАЗ', 'BY HOW MUCH AND HOW MANY TIMES', 'cpSvg', '0 0 600 250',
  slider('ca', 'Первое число', 'First number', 1, 30, 1, 18) + slider('cb', 'Второе число', 'Second number', 1, 30, 1, 6),
  stats([('cD', 'На сколько отличаются', 'By how much they differ'), ('cK', 'Во сколько раз', 'How many times')]),
  'cpFb', 'Чтобы узнать, на сколько одно число больше, — вычитаем. Чтобы узнать, во сколько раз, — делим.',
  'To find by how much one number is greater — we subtract. To find how many times — we divide.')
s2 = section('compare', 'Сравниваем числа в задаче', 'Comparing numbers in a problem',
 bd('<p>Два разных вопроса звучат похоже. «<strong>На сколько</strong> больше?» — это <em>вычитание</em>: 18 − 6 = 12. «<strong>Во сколько раз</strong> больше?» — это <em>деление</em>: 18 : 6 = 3. А «в 3 раза больше» — это 6 · 3 = 18.</p>',
    '<p>Two different questions sound alike. “<strong>By how much</strong> is it greater?” is <em>subtraction</em>: 18 − 6 = 12. “<strong>How many times</strong> greater?” is <em>division</em>: 18 : 6 = 3. And “3 times as many” means 6 · 3 = 18.</p>')
 + formula('18 − 6 = 12;  18 : 6 = 3', 'на 12 больше; в 3 раза больше', '12 more; 3 times as many'),
 lab2)

lab3 = model(3, 'ПОКУПКА И СДАЧА (СОМЫ)', 'SHOPPING AND CHANGE (SOMS)', 'shSvg', '0 0 600 250',
  slider('sp', 'Цена одной вещи', 'Price of one item', 5, 50, 5, 15) + slider('sk', 'Сколько штук', 'How many items', 1, 9, 1, 4) + select('sb', 'Платим', 'We pay with'),
  stats([('sC', 'Стоимость', 'Cost'), ('sD', 'Сдача', 'Change'), ('sS', 'Хватает ли денег', 'Is it enough')]),
  'shFb', 'Сначала считаем стоимость: цена · количество. Потом сдачу: деньги − стоимость.',
  'First the cost: price · quantity. Then the change: money − cost.')
s3 = section('money', 'Задача в два действия: покупка', 'A two-step problem: shopping',
 bd('<p>Многие задачи решаются в два действия. 4 тетради по 15 сом, платим 100 сом. <strong>1)</strong> Сколько стоят тетради? 15 · 4 = 60 сом. <strong>2)</strong> Сколько сдачи? 100 − 60 = 40 сом. Каждое действие отвечает на свой вопрос.</p>',
    '<p>Many problems are solved in two steps. 4 notebooks at 15 soms, we pay 100 soms. <strong>1)</strong> How much do the notebooks cost? 15 · 4 = 60 soms. <strong>2)</strong> How much change? 100 − 60 = 40 soms. Each step answers its own question.</p>')
 + formula('100 − 15 · 4 = 40', 'сдача = деньги − цена · количество', 'change = money − price · quantity'),
 lab3)

tasks = [
 task(1, 'Сколько у них вместе', 'How much do they have together', 'У Айбека 12 сом, а у Айдай на 5 сом больше. Сколько денег у них вместе?', 'Aibek has 12 soms and Aidai has 5 soms more. How much money do they have together?',
  '12 сом; на 5 сом больше', '12 soms; 5 soms more', '1) У Айдай: 12 + 5 = 17 сом. 2) Вместе: 12 + 17 = 29 сом.', '1) Aidai has: 12 + 5 = 17 soms. 2) Together: 12 + 17 = 29 soms.', '29 сом.', '29 soms.', True),
 task(2, 'Тетради и сдача', 'Notebooks and change', 'Четыре тетради по 15 сом. Сколько сдачи со 100 сом?', 'Four notebooks at 15 soms each. How much change from 100 soms?',
  '4 тетради по 15 сом, 100 сом', '4 notebooks at 15 soms, 100 soms', '1) Стоимость: 15 · 4 = 60 сом. 2) Сдача: 100 − 60 = 40 сом.', '1) Cost: 15 · 4 = 60 soms. 2) Change: 100 − 60 = 40 soms.', '40 сом.', '40 soms.'),
 task(3, 'На сколько больше', 'How many more', 'В одном классе 38 учеников, в другом 25. На сколько больше учеников в первом?', 'One class has 38 pupils and another 25. By how many are there more pupils in the first?',
  '38 и 25', '38 and 25', '«На сколько больше» — вычитание: 38 − 25 = 13.', '“By how many more” is subtraction: 38 − 25 = 13.', 'на 13 учеников.', 'by 13 pupils.'),
 task(4, 'В несколько раз меньше', 'Several times fewer', 'У Эрлана 18 овец, а у Азата в 3 раза меньше. Сколько овец у Азата?', 'Erlan has 18 sheep and Azat has 3 times fewer. How many sheep does Azat have?',
  '18 овец; в 3 раза меньше', '18 sheep; 3 times fewer', '«В 3 раза меньше» — делим на 3: 18 : 3 = 6.', '“3 times fewer” means divide by 3: 18 : 3 = 6.', '6 овец.', '6 sheep.'),
 task(5, 'Мальчики и девочки', 'Boys and girls', 'В классе 28 учеников, из них 12 мальчиков. Сколько девочек? На сколько девочек больше?', 'A class has 28 pupils, 12 of them boys. How many girls? By how many are there more girls?',
  '28 всего, 12 мальчиков', '28 in all, 12 boys', 'Целое — 28, известная часть — 12. Девочек: 28 − 12 = 16. Больше на 16 − 12 = 4.', 'The whole is 28, the known part is 12. Girls: 28 − 12 = 16. More by 16 − 12 = 4.', '16 девочек, на 4 больше.', '16 girls, 4 more.'),
]
quiz = [
 qz('В классе 28 учеников, 12 мальчиков. Как найти число девочек?', '28 − 12', '28 + 12', '28 · 12', 'Целое минус известная часть.',
    'A class has 28 pupils, 12 are boys. How do you find the number of girls?', '28 − 12', '28 + 12', '28 · 12', 'The whole minus the known part.'),
 qz('Как узнать, на сколько 38 больше 25?', 'Вычесть: 38 − 25', 'Сложить', 'Разделить', '«На сколько» — вычитание.',
    'How do you find by how much 38 is greater than 25?', 'Subtract: 38 − 25', 'Add', 'Divide', '“By how much” is subtraction.'),
 qz('Как узнать, во сколько раз 18 больше 6?', 'Разделить: 18 : 6', 'Вычесть', 'Умножить', '«Во сколько раз» — деление.',
    'How do you find how many times 18 is greater than 6?', 'Divide: 18 : 6', 'Subtract', 'Multiply', '“How many times” is division.'),
 qz('Что значит «в 5 раз больше, чем 4»?', '4 · 5 = 20', '4 + 5 = 9', '4 : 5', 'Берём 4 пять раз.',
    'What does “5 times as many as 4” mean?', '4 · 5 = 20', '4 + 5 = 9', '4 : 5', 'Take 4 five times.'),
 qz('Сколько стоят 3 пакета по 12 сом?', '36 сом', '15 сом', '24 сом', '12 · 3 = 36.',
    'How much do 3 cartons at 12 soms cost?', '36 soms', '15 soms', '24 soms', '12 · 3 = 36.'),
 qz('Сколько сдачи со 100 сом, если купили на 64 сома?', '36 сом', '46 сом', '164 сома', '100 − 64 = 36.',
    'How much change from 100 soms if you bought goods worth 64 soms?', '36 soms', '46 soms', '164 soms', '100 − 64 = 36.'),
 qz('У Азата 5 орехов, у Бека на 3 больше. Сколько у Бека?', '8', '15', '2', '«На 3 больше» — прибавляем: 5 + 3 = 8.',
    'Azat has 5 nuts, Bek has 3 more. How many does Bek have?', '8', '15', '2', '“3 more” — we add: 5 + 3 = 8.'),
 qz('С чего лучше начать решение задачи?', 'Понять вопрос и нарисовать схему', 'Сразу складывать числа', 'Угадать ответ', 'Схема показывает, что известно и что надо найти.',
    'What is the best way to start solving a problem?', 'Understand the question and draw a diagram', 'Start adding numbers right away', 'Guess the answer', 'A diagram shows what is known and what is to be found.'),
]
js = MJS + r'''
const T={ru:{pwLabel:"Схема из отрезков: целое и две части",cpLabel:"Два отрезка разной длины",shLabel:"Стоимость покупки и деньги",un:["целое","первая часть","вторая часть"],yes:"хватает",no:"не хватает",som:" сом"},
 en:{pwLabel:"A bar diagram: the whole and two parts",cpLabel:"Two bars of different length",shLabel:"The cost of a purchase and the money",un:["the whole","the first part","the second part"],yes:"enough",no:"not enough",som:" soms"}};
function drawPw(){const t=T[lang],u=+$("pu").value,p1=+$("p1").value,p2=+$("p2").value,whole=p1+p2;const sc=480/whole;let g="";
 const x0=60,w1=p1*sc,w2=p2*sc;
 g+=R(x0,40,whole*sc,44,u===0?"#fff4e0":COL.bg,u===0?COL.d:COL.ink,u===0?3:2,4)+TX(x0+whole*sc/2,69,u===0?"?":String(whole),COL.ink,22,"middle",600);
 g+=R(x0,120,w1,44,u===1?"#fff4e0":COL.a,u===1?COL.d:"none",u===1?3:0,4)+TX(x0+w1/2,149,u===1?"?":String(p1),u===1?COL.ink:"#fff",22,"middle",600);
 g+=R(x0+w1,120,w2,44,u===2?"#fff4e0":COL.b,u===2?COL.d:"none",u===2?3:0,4)+TX(x0+w1+w2/2,149,u===2?"?":String(p2),u===2?COL.ink:"#fff",22,"middle",600);
 g+=L(x0,100,x0,115,COL.mut,1)+L(x0+whole*sc,100,x0+whole*sc,115,COL.mut,1);
 const known=u===0?"":u===1?p2:p1;const ans=u===0?whole:u===1?p1:p2;const act=u===0?p1+" + "+p2:whole+" − "+known;
 g+=TX(300,215,act+" = "+ans,COL.ink,26);
 $("pwSvg").innerHTML=g;$("p1Out").textContent=p1;$("p2Out").textContent=p2;
 $("pK").textContent=t.un[u];$("pA").textContent=act;$("pR").textContent=ans;
 $("pwFb").textContent=u===0?U("Целое неизвестно — части складываем.","The whole is unknown — we add the parts."):U("Часть неизвестна — из целого вычитаем известную часть.","A part is unknown — we subtract the known part from the whole.")}
["pu","p1","p2"].forEach(id=>$(id).addEventListener("input",drawPw));
function drawCp(){const a=+$("ca").value,b=+$("cb").value,sc=480/Math.max(a,b);let g="";
 g+=R(60,50,a*sc,36,COL.a,"none",0,4)+TX(52,75,"A = "+a,COL.ink,14,"end")+R(60,120,b*sc,36,COL.b,"none",0,4)+TX(52,145,"B = "+b,COL.ink,14,"end");
 const hi=Math.max(a,b),lo=Math.min(a,b);
 if(a!==b){const y=a>b?120:50;g+=R(60+lo*sc,a>b?50:120,(hi-lo)*sc,36,"none",COL.d,3,4)+TX(60+lo*sc+(hi-lo)*sc/2,a>b?75:145,String(hi-lo),COL.ink,18,"middle",600)}
 const k=hi%lo===0?hi/lo:null;g+=TX(300,215,(a>=b?"A":"B")+U(" больше на "+(hi-lo)," is greater by "+(hi-lo))+(k&&hi!==lo?U(" и в "+k+" раз(а)"," and "+k+" times"):""),COL.ink,18);
 $("cpSvg").innerHTML=g;$("caOut").textContent=a;$("cbOut").textContent=b;
 $("cD").textContent=hi-lo;$("cK").textContent=k?U("в "+k+" раз(а)",k+" times"):U("нацело не делится","not a whole number");
 $("cpFb").textContent=a===b?U("Числа равны: разница 0, больше в 1 раз.","The numbers are equal: difference 0, 1 time as many."):U(hi+" − "+lo+" = "+(hi-lo)+(k?"; "+hi+" : "+lo+" = "+k:"; "+hi+" на "+lo+" нацело не делится."),hi+" − "+lo+" = "+(hi-lo)+(k?"; "+hi+" : "+lo+" = "+k:"; "+hi+" is not divisible by "+lo+"."))}
["ca","cb"].forEach(id=>$(id).addEventListener("input",drawCp));
function drawSh(){const t=T[lang],p=+$("sp").value,k=+$("sk").value,bills=[50,100,200,500],bill=bills[+$("sb").value],cost=p*k,ch=bill-cost;const sc=520/Math.max(bill,cost);let g="";
 g+=R(40,45,cost*sc,40,COL.a,"none",0,4)+TX(40+cost*sc+8,72,U("стоимость ","cost ")+cost,COL.ink,15,"start")+R(40,120,bill*sc,40,COL.b,"none",0,4)+TX(40+bill*sc+8,147,U("деньги ","money ")+bill,COL.ink,15,"start");
 if(ch>0)g+=R(40+cost*sc,120,ch*sc,40,"none",COL.d,3,4)+TX(40+cost*sc+ch*sc/2,146,U("сдача ","change ")+ch,COL.ink,14,"middle");
 g+=TX(300,215,bill+" − "+p+" · "+k+" = "+ch,COL.ink,22);
 $("shSvg").innerHTML=g;$("spOut").textContent=p+t.som;$("skOut").textContent=k;
 $("sC").textContent=p+" · "+k+" = "+cost+t.som;$("sD").textContent=ch>=0?ch+t.som:"—";$("sS").textContent=ch>=0?t.yes:t.no;
 $("shFb").textContent=ch>=0?U("Сдача: "+ch+" сом.","Change: "+ch+" soms."):U("Не хватает "+(-ch)+" сом.","Short by "+(-ch)+" soms.")}
["sp","sk","sb"].forEach(id=>$(id).addEventListener("input",drawSh));
const LAB={ru:{pwSvg:T.ru.pwLabel,cpSvg:T.ru.cpLabel,shSvg:T.ru.shLabel},en:{pwSvg:T.en.pwLabel,cpSvg:T.en.cpLabel,shSvg:T.en.shLabel}};
function drawAll(){fillSel("pu",T[lang].un,0);fillSel("sb",["50","100","200","500"].map(x=>x+T[lang].som),1);drawPw();drawCp();drawSh()}
'''
c = dict(n='07', slug='07-word-problems.html', block='I', level_ru='ОСНОВЫ · 2–4 КЛАССЫ', level_en='BASICS · GRADES 2–4',
 title=('Текстовые задачи', 'Word problems'),
 desc='Глава 7 Атласа математики: решение текстовых задач, схемы из отрезков, «на сколько» и «во сколько раз», задачи в два действия, сдача в сомах.',
 lead=('Как не запутаться в условии: рисуем задачу отрезками, отличаем «на сколько» от «во сколько раз», решаем в два действия.',
       'How not to get tangled in a problem: drawing it with bars, telling “by how much” from “how many times”, solving in two steps.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('parts', 'Схема', 'Diagram'), ('compare', 'Сравнение', 'Comparing'), ('money', 'Покупка', 'Shopping'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>У Айбека 12 сом. У Айдай на 5 сом больше, чем у Айбека. Сколько денег у них вместе?</p><p>Многие сразу отвечают «17». Подумайте: на какой вопрос отвечает число 17?</p>',
         '<p>Aibek has 12 soms. Aidai has 5 soms more than Aibek. How much money do they have together?</p><p>Many people at once answer “17”. Think: what question does the number 17 answer?</p>'),
 hint=stdhint('Схема: части и целое', 'Diagram: parts and whole'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 29 сом', 'The answer: 29 soms'),
 answer=('<p>17 — это деньги Айдай: 12 + 5. А спрашивают, сколько у них <em>вместе</em>. Значит, нужно второе действие: 12 + 17 = 29 сом. Если нарисовать отрезки, это видно сразу: целое состоит из двух частей — у Айбека и у Айдай.</p>',
         '<p>17 is Aidai’s money: 12 + 5. But the question asks how much they have <em>together</em>. So a second step is needed: 12 + 17 = 29 soms. If you draw the bars it is clear at once: the whole consists of two parts — Aibek’s and Aidai’s.</p>'),
 sources=[('Текстовые задачи —', 'Word problems —', LINK('https://en.wikipedia.org/wiki/Word_problem_(mathematics_education)', 'Wikipedia: Word problem (mathematics education)')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Условия и цены в задачах придуманы для атласа.', 'The conditions and prices in the problems were invented for the atlas.'),
 prev=('06-order-of-operations.html', 'Глава 6 · Порядок действий', 'Chapter 6 · Order of operations'),
 next=('08-fractions-intro.html', 'Глава 8 · Доли и дроби', 'Chapter 8 · Parts and fractions'),
 js=js)
build(c)
