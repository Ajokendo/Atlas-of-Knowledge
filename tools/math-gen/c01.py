# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'СЧИТАЕМ ПЯТЁРКАМИ И ДЕСЯТКАМИ', 'COUNTING IN FIVES AND TENS', 'cnSvg', '0 0 600 250',
  slider('cn', 'Сколько предметов', 'How many objects', 0, 20, 1, 17),
  stats([('cNum', 'Число', 'Number'), ('cWord', 'Словами', 'In words'), ('cTE', 'Десятки и единицы', 'Tens and ones')]),
  'cnFb', 'Каждая рамка — один десяток: 2 ряда по 5 клеток. Так видно сразу, сколько всего, и не нужно считать по одному.',
  'Each frame is one ten: 2 rows of 5 cells. You see the total at once, with no need to count one by one.')
s1 = section('count', 'Считаем и записываем', 'Counting and writing numbers',
 bd('<p>Чтобы быстро и без ошибок узнать, сколько предметов, их <strong>группируют</strong>: по пять и по десять. Пять пальцев на руке, десять — на двух. Если собрать 10 предметов, получится <strong>один десяток</strong>. Всё, что осталось сверху, — <strong>единицы</strong>.</p><p>Число 17 — это 1 десяток и 7 единиц. Поэтому его записывают двумя цифрами: <em>1</em> десяток и <em>7</em> единиц. А <strong>нуль</strong> означает «ничего нет».</p>',
    '<p>To find out quickly and without mistakes how many things there are, we <strong>group</strong> them: in fives and in tens. Five fingers on one hand, ten on two. When you collect 10 things you get <strong>one ten</strong>. Whatever is left over is <strong>ones</strong>.</p><p>The number 17 is 1 ten and 7 ones. That is why it is written with two digits: <em>1</em> ten and <em>7</em> ones. And <strong>zero</strong> means “nothing there”.</p>')
 + formula('17 = 10 + 7', 'число = десятки + единицы', 'number = tens + ones'),
 lab1)

lab2 = model(2, 'СОСТАВ ЧИСЛА', 'PARTS OF A NUMBER', 'ptSvg', '0 0 600 250',
  slider('pt', 'Число', 'Number', 2, 20, 1, 10) + slider('pa', 'Первая часть', 'First part', 0, 20, 1, 4),
  stats([('pEq', 'Равенство', 'Equation'), ('pB', 'Вторая часть', 'Second part'), ('pN', 'Сколько разных пар (без учёта порядка)', 'How many different pairs (order ignored)')]),
  'ptFb', 'Двигайте ползунок «Первая часть» — вторая часть меняется сама. Сумма всегда равна числу.',
  'Move the “First part” slider — the second part changes by itself. The sum is always the number.')
s2 = section('parts', 'Состав числа', 'Parts of a number',
 bd('<p>Любое число можно разложить на две части. Например, 10 = 4 + 6 = 5 + 5 = 7 + 3. Части можно менять местами: 4 + 6 = 6 + 4. Если знаешь одну часть и всё число, вторую находишь вычитанием: <em>10 − 4 = 6</em>.</p>',
    '<p>Any number can be split into two parts. For example 10 = 4 + 6 = 5 + 5 = 7 + 3. The parts can swap places: 4 + 6 = 6 + 4. If you know one part and the whole number, you find the other part by subtracting: <em>10 − 4 = 6</em>.</p>')
 + formula(bi('часть + часть = число', 'part + part = number'), 'число − одна часть = другая часть', 'number − one part = the other part'),
 lab2)

lab3 = model(3, 'БОЛЬШЕ, МЕНЬШЕ, РАВНО', 'GREATER, LESS, EQUAL', 'cpSvg', '0 0 600 250',
  slider('cx', 'Первое число', 'First number', 0, 20, 1, 7) + slider('cy', 'Второе число', 'Second number', 0, 20, 1, 12),
  stats([('cS', 'Сравнение', 'Comparison'), ('cD', 'Разница', 'Difference'), ('cW', 'Кто правее', 'Which is further right')]),
  'cpFb', 'На числовом луче число, которое правее, — больше. Числа растут слева направо.',
  'On the number line the number that is further right is greater. Numbers grow from left to right.')
s3 = section('compare', 'Больше, меньше, равно', 'Greater, less, equal',
 bd('<p>Числа стоят на <strong>числовом луче</strong> по порядку: 0, 1, 2, 3… Чем правее — тем число больше. Знак <em>&gt;</em> значит «больше», знак <em>&lt;</em> — «меньше», знак <em>=</em> — «равно». Острый конец знака смотрит на меньшее число.</p>',
    '<p>Numbers stand on the <strong>number line</strong> in order: 0, 1, 2, 3… The further right, the greater the number. The sign <em>&gt;</em> means “greater than”, <em>&lt;</em> means “less than”, <em>=</em> means “equal”. The pointed end of the sign looks at the smaller number.</p>')
 + formula('7 &lt; 12', '7 меньше 12 на 5', '7 is less than 12 by 5'),
 lab3)

tasks = [
 task(1, 'Сколько овец', 'How many sheep', 'Чабан Эрлан поставил овец рядами по 5. Получилось 3 полных ряда и ещё 2 овцы. Сколько всего овец?', 'The shepherd Erlan put his sheep in rows of 5. There are 3 full rows and 2 more sheep. How many sheep are there?',
  '3 ряда по 5, ещё 2', '3 rows of 5, and 2 more', '5 + 5 + 5 = 15. Ещё 2: 15 + 2 = 17.', '5 + 5 + 5 = 15. Two more: 15 + 2 = 17.', '17 овец.', '17 sheep.', True),
 task(2, 'Состав числа 12', 'Parts of 12', 'Число 12 разложили на две части. Одна часть — 5. Чему равна вторая?', 'The number 12 is split into two parts. One part is 5. What is the other?',
  '12 = 5 + ?', '12 = 5 + ?', '12 − 5 = 7. Проверим: 5 + 7 = 12.', '12 − 5 = 7. Check: 5 + 7 = 12.', '7.', '7.'),
 task(3, 'Какое число больше', 'Which number is greater', 'Сравните числа 14 и 9. На сколько одно больше другого?', 'Compare the numbers 14 and 9. By how much is one greater than the other?',
  '14 и 9', '14 and 9', '14 правее 9 на числовом луче, значит 14 &gt; 9. От 9 до 14 пять шагов: 10, 11, 12, 13, 14.', '14 is right of 9 on the number line, so 14 &gt; 9. From 9 to 14 there are five steps: 10, 11, 12, 13, 14.', '14 &gt; 9, на 5 больше.', '14 &gt; 9, greater by 5.'),
 task(4, 'Десятки и единицы', 'Tens and ones', 'Из каких десятков и единиц состоит число 19? А число 20?', 'What tens and ones make up the number 19? And the number 20?',
  '19 и 20', '19 and 20', '19: один десяток и 9 единиц, 19 = 10 + 9. Прибавим 1: 9 единиц и ещё одна — это 10 единиц, то есть ещё один десяток. Получаем 2 десятка и 0 единиц.', '19: one ten and 9 ones, 19 = 10 + 9. Add 1: 9 ones and one more make 10 ones, which is one more ten. We get 2 tens and 0 ones.', '19 = 1 дес. 9 ед.; 20 = 2 дес. 0 ед.', '19 = 1 ten 9 ones; 20 = 2 tens 0 ones.'),
 task(5, 'Соседи числа', 'Neighbours of a number', 'Назовите число перед 15 и число после 15. Сколько чисел между 12 и 16?', 'Name the number before 15 and the number after 15. How many numbers lie between 12 and 16?',
  '15; от 12 до 16', '15; from 12 to 16', 'Перед 15 стоит 14, после — 16. Между 12 и 16 стоят 13, 14, 15 — три числа.', 'Before 15 comes 14, after it 16. Between 12 and 16 stand 13, 14, 15 — three numbers.', '14 и 16; три числа.', '14 and 16; three numbers.'),
]

quiz = [
 qz('Сколько десятков и единиц в числе 17?', '1 десяток и 7 единиц', '7 десятков и 1 единица', '17 десятков', '17 = 10 + 7.',
    'How many tens and ones are in the number 17?', '1 ten and 7 ones', '7 tens and 1 one', '17 tens', '17 = 10 + 7.'),
 qz('Что значит цифра 0 в числе 20?', 'Единиц нет', 'Десятков нет', 'Это не число', 'В числе 20 два десятка и ни одной единицы.',
    'What does the digit 0 mean in the number 20?', 'There are no ones', 'There are no tens', 'It is not a number', 'The number 20 has two tens and no ones.'),
 qz('Какое число больше: 8 или 13?', '13', '8', 'Они равны', '13 стоит правее 8 на числовом луче.',
    'Which number is greater: 8 or 13?', '13', '8', 'They are equal', '13 is right of 8 on the number line.'),
 qz('Число 10 разложили на 4 и ещё одну часть. Какая это часть?', '6', '5', '14', '10 − 4 = 6.',
    'The number 10 is split into 4 and another part. What is that part?', '6', '5', '14', '10 − 4 = 6.'),
 qz('Какой знак поставить: 9 ? 15', '&lt;', '&gt;', '=', '9 меньше 15.',
    'Which sign goes here: 9 ? 15', '&lt;', '&gt;', '=', '9 is less than 15.'),
 qz('Какое число стоит сразу после 19?', '20', '18', '21', 'Считаем: …, 18, 19, 20.',
    'Which number comes right after 19?', '20', '18', '21', 'Counting: …, 18, 19, 20.'),
 qz('Сколько пятёрок в числе 15?', '3', '5', '15', '5 + 5 + 5 = 15.',
    'How many fives are there in the number 15?', '3', '5', '15', '5 + 5 + 5 = 15.'),
 qz('Сколько разных способов разложить 4 на две части (с нулём, порядок не важен)?', '3: 0+4, 1+3, 2+2', '2', '5', '0 + 4, 1 + 3 и 2 + 2; 3 + 1 — то же, что 1 + 3.',
    'How many different ways to split 4 into two parts (with zero, order ignored)?', '3: 0+4, 1+3, 2+2', '2', '5', '0 + 4, 1 + 3 and 2 + 2; 3 + 1 is the same as 1 + 3.'),
]

js = MJS + r'''
const T={ru:{cnLabel:"Две рамки-десятка с точками",ptLabel:"Число из двух частей",cpLabel:"Два числа на числовом луче",
 words:["нуль","один","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать","двадцать"],
 less:"меньше",more:"больше",eq:"равны",left:"левое",right:"правое",same:"оба на одном месте"},
 en:{cnLabel:"Two ten-frames with dots",ptLabel:"A number made of two parts",cpLabel:"Two numbers on a number line",
 words:["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"],
 less:"less",more:"greater",eq:"equal",left:"the left one",right:"the right one",same:"both in the same place"}};
function drawCn(){const n=+$("cn").value,t=T[lang];let g="";
 for(let f=0;f<2;f++){const ox=50+f*290;g+=R(ox,40,250,100,COL.bg,COL.ink,2);
  for(let i=1;i<5;i++)g+=L(ox+i*50,40,ox+i*50,140,COL.line,1);g+=L(ox,90,ox+250,90,COL.line,1);
  for(let k=0;k<10;k++){const idx=f*10+k;if(idx<n){const col=k%5,row=Math.floor(k/5);g+=C(ox+25+col*50,65+row*50,17,(idx<10?COL.a:COL.b))}}}
 const five=Math.floor(n/5),rest=n%5;let parts=[];for(let i=0;i<five;i++)parts.push("5");if(rest)parts.push(String(rest));
 g+=TX(300,190,n===0?"0":(parts.join(" + ")+" = "+n),COL.ink,22);
 g+=TX(300,225,U("Первый десяток — красный, второй — синий","The first ten is red, the second is blue"),COL.mut,13);
 $("cnSvg").innerHTML=g;$("cnOut").textContent=n;
 $("cNum").textContent=n;$("cWord").textContent=t.words[n];
 $("cTE").textContent=Math.floor(n/10)+" "+U("дес.","tens")+" "+(n%10)+" "+U("ед.","ones");
 $("cnFb").textContent=n===0?U("Ноль: ни одного предмета.","Zero: not a single object."):n===10?U("Ровно один десяток!","Exactly one ten!"):n===20?U("Два десятка — двадцать.","Two tens — twenty."):U("Считай пятёрками: "+parts.join(" + ")+".","Count in fives: "+parts.join(" + ")+".")}
$("cn").addEventListener("input",drawCn);
function drawPt(){const tot=+$("pt").value,a0=$("pa");a0.max=tot;let a=Math.min(+a0.value,tot);a0.value=a;const b=tot-a;let g="";
 const w=Math.min(26,520/tot),x0=300-tot*w/2;
 for(let i=0;i<tot;i++)g+=R(x0+i*w+1,70,w-2,w-2,i<a?COL.a:COL.b,"none",0,4);
 g+=TX(x0+a*w/2,70+w+22,String(a),COL.a,22,"middle",600)+TX(x0+a*w+b*w/2,70+w+22,String(b),COL.b,22,"middle",600);
 g+=TX(300,190,a+" + "+b+" = "+tot,COL.ink,28)+TX(300,225,tot+" − "+a+" = "+b,COL.mut,16);
 $("ptSvg").innerHTML=g;$("ptOut").textContent=tot;$("paOut").textContent=a;
 $("pEq").textContent=a+" + "+b+" = "+tot;$("pB").textContent=b;$("pN").textContent=Math.floor(tot/2)+1;
 $("ptFb").textContent=a===b?U("Две равные части: "+tot+" = "+a+" + "+a+".","Two equal parts: "+tot+" = "+a+" + "+a+"."):U("Поменяем части местами: "+b+" + "+a+" = "+tot+".","Swap the parts: "+b+" + "+a+" = "+tot+".")}
["pt","pa"].forEach(id=>$(id).addEventListener("input",drawPt));
function drawCp(){const x=+$("cx").value,y=+$("cy").value,t=T[lang];let g=numLine(40,560,150,0,20,1,1);
 const X=px(x,40,560,0,20),Y=px(y,40,560,0,20);
 g+=C(X,110,14,COL.a)+TX(X,115,String(x),"#fff",13,"middle",600)+C(Y,70,14,COL.b)+TX(Y,75,String(y),"#fff",13,"middle",600);
 g+=L(X,124,X,150,COL.a,1)+L(Y,84,Y,150,COL.b,1);
 const sign=x<y?"&lt;":x>y?"&gt;":"=";
 g+=TX(300,36,x+" "+sign+" "+y,COL.ink,24);
 $("cpSvg").innerHTML=g;$("cxOut").textContent=x;$("cyOut").textContent=y;
 $("cS").innerHTML=x+" "+sign+" "+y;$("cD").textContent=Math.abs(x-y);$("cW").textContent=x===y?t.same:(x>y?U("первое","the first"):U("второе","the second"));
 $("cpFb").textContent=x===y?U(x+" и "+y+" равны.",x+" and "+y+" are equal."):x<y?U(x+" меньше "+y+" на "+(y-x)+": от "+x+" до "+y+" надо пройти "+(y-x)+" шагов вправо.",x+" is less than "+y+" by "+(y-x)+": from "+x+" to "+y+" you go "+(y-x)+" steps right."):U(x+" больше "+y+" на "+(x-y)+".",x+" is greater than "+y+" by "+(x-y)+".")}
["cx","cy"].forEach(id=>$(id).addEventListener("input",drawCp));
const LAB={ru:{cnSvg:T.ru.cnLabel,ptSvg:T.ru.ptLabel,cpSvg:T.ru.cpLabel},en:{cnSvg:T.en.cnLabel,ptSvg:T.en.ptLabel,cpSvg:T.en.cpLabel}};
function drawAll(){drawCn();drawPt();drawCp()}
'''

c = dict(n='01', slug='01-numbers-to-20.html', block='I', level_ru='ОСНОВЫ · 1–2 КЛАССЫ', level_en='BASICS · GRADES 1–2',
 title=('Числа до 20: счёт и состав числа', 'Numbers to 20: counting and parts of a number'),
 desc='Глава 1 Атласа математики: счёт до 20, десяток и единицы, состав числа, сравнение чисел на числовом луче.',
 lead=('Как не сбиться, считая овец: группируем по пять и по десять, раскладываем числа на части и сравниваем их.',
       'How not to lose count of sheep: group by fives and tens, split numbers into parts and compare them.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('count', 'Счёт', 'Counting'), ('parts', 'Состав числа', 'Parts'), ('compare', 'Сравнение', 'Comparing'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Чабан Эрлан вечером загоняет овец в кошару. Считать по одной долго, и он легко сбивается. Поэтому он ставит овец рядами по пять. Сегодня получилось 3 полных ряда и ещё 2 овцы в последнем ряду.</p><p>Сколько овец у Эрлана? А если ставить рядами по десять — сколько будет полных рядов и сколько овец останется?</p>',
         '<p>In the evening the shepherd Erlan drives his sheep into the pen. Counting them one by one takes long, and he easily loses count. So he lines the sheep up in rows of five. Today there are 3 full rows and 2 more sheep in the last row.</p><p>How many sheep does Erlan have? And if he used rows of ten — how many full rows and how many sheep would be left over?</p>'),
 hint=stdhint('Считаем пятёрками и десятками', 'Counting in fives and tens'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 17 овец', 'The answer: 17 sheep'),
 answer=('<p>Три ряда по пять — это 5 + 5 + 5 = 15. Ещё две овцы: 15 + 2 = 17. Если ставить по десять, получится один полный ряд (10 овец) и 7 останутся: 17 = 10 + 7. Сколько бы ни было овец, запись числа не меняется: это один десяток и семь единиц.</p>',
         '<p>Three rows of five make 5 + 5 + 5 = 15. Two more sheep: 15 + 2 = 17. With rows of ten there is one full row (10 sheep) and 7 are left over: 17 = 10 + 7. Whatever way you group them, the number stays the same: one ten and seven ones.</p>'),
 sources=[
  ('Счёт и числовой луч —', 'Counting and the number line —', LINK('https://en.wikipedia.org/wiki/Counting', 'Wikipedia: Counting') + ', ' + LINK('https://en.wikipedia.org/wiki/Number_line', 'Wikipedia: Number line')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e, гл. 1'))],
 note=stdnote('Сюжет про чабана придуман для атласа.', 'The story of the shepherd was invented for the atlas.'),
 prev=('../index.html', 'Содержание блока', 'Block contents'),
 next=('02-add-subtract.html', 'Глава 2 · Сложение и вычитание', 'Chapter 2 · Addition and subtraction'),
 js=js)
build(c)
