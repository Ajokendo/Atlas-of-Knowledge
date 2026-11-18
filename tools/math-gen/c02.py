# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'ПРЫЖКИ ПО ЧИСЛОВОМУ ЛУЧУ', 'JUMPS ON THE NUMBER LINE', 'jmSvg', '0 0 600 250',
  select('jo', 'Действие', 'Operation') + slider('ja', 'Первое число', 'First number', 0, 20, 1, 8) + slider('jb', 'Второе число', 'Second number', 0, 20, 1, 5),
  stats([('jE', 'Пример', 'Sum'), ('jR', 'Ответ', 'Answer'), ('jS', 'Шагов', 'Steps')]),
  'jmFb', 'Сложение — прыжки вправо, вычитание — прыжки влево. Ползунками меняйте числа.',
  'Addition is jumping right, subtraction is jumping left. Change the numbers with the sliders.')
s1 = section('line', 'Сложить — значит прибавить', 'To add means to put together',
 bd('<p>Когда мы <strong>складываем</strong>, мы соединяем части и получаем целое: <em>8 + 5 = 13</em>. Числа, которые складывают, — <strong>слагаемые</strong>, результат — <strong>сумма</strong>. Когда мы <strong>вычитаем</strong>, мы убираем часть: <em>13 − 5 = 8</em>.</p><p>От перемены мест слагаемых сумма не меняется: 8 + 5 = 5 + 8. Поэтому к большему числу удобно прибавлять меньшее.</p>',
    '<p>When we <strong>add</strong>, we join parts and get a whole: <em>8 + 5 = 13</em>. The numbers we add are the <strong>addends</strong>, the result is the <strong>sum</strong>. When we <strong>subtract</strong>, we take a part away: <em>13 − 5 = 8</em>.</p><p>Swapping the addends does not change the sum: 8 + 5 = 5 + 8. So it is handy to add the smaller number to the bigger one.</p>')
 + formula('a + b = b + a', 'слагаемые можно менять местами', 'the addends can swap places'),
 lab1)

lab2 = model(2, 'ПЕРЕХОД ЧЕРЕЗ ДЕСЯТОК', 'CROSSING THE TEN', 'tnSvg', '0 0 600 250',
  slider('ta', 'Первое число (от 6 до 9)', 'First number (6 to 9)', 6, 9, 1, 8) + slider('tb', 'Второе число (от 3 до 9)', 'Second number (3 to 9)', 3, 9, 1, 7),
  stats([('tFill', 'Дополняем до 10', 'Fill up to 10'), ('tLeft', 'Остаётся прибавить', 'Still to add'), ('tAns', 'Сумма', 'Sum')]),
  'tnFb', 'Сначала дополняем первое число до десятка, потом прибавляем остаток.',
  'First fill the first number up to the ten, then add what is left.')
s2 = section('ten', 'Переход через десяток', 'Crossing the ten',
 bd('<p>Как сложить 8 + 7 и не считать по одному? Разложим 7 на 2 и 5. Сначала 8 + 2 = 10 — получился полный десяток. Потом 10 + 5 = 15. Этот приём называется <strong>переход через десяток</strong>.</p>',
    '<p>How do you add 8 + 7 without counting one by one? Split 7 into 2 and 5. First 8 + 2 = 10 — a full ten. Then 10 + 5 = 15. This trick is called <strong>crossing the ten</strong>.</p>')
 + formula('8 + 7 = 8 + 2 + 5 = 10 + 5 = 15', 'до десятка не хватает 2', 'it takes 2 to reach the ten'),
 lab2)

lab3 = model(3, 'СЕМЕЙКА ЧИСЕЛ', 'A FAMILY OF NUMBERS', 'fmSvg', '0 0 600 250',
  slider('fa', 'Первая часть', 'First part', 1, 15, 1, 6) + slider('fb', 'Вторая часть', 'Second part', 1, 15, 1, 9),
  stats([('f1', 'Сложение', 'Addition'), ('f2', 'Вычитание 1', 'Subtraction 1'), ('f3', 'Вычитание 2', 'Subtraction 2')]),
  'fmFb', 'Три числа — четыре примера. Если знаешь сложение, знаешь и вычитание.',
  'Three numbers — four equations. If you know the addition, you know the subtraction too.')
s3 = section('family', 'Сложение и вычитание дружат', 'Addition and subtraction are friends',
 bd('<p>Вычитание — это сложение наоборот. Из примера <em>6 + 9 = 15</em> получаются ещё три: 9 + 6 = 15, 15 − 6 = 9 и 15 − 9 = 6. Чтобы проверить вычитание, прибавьте то, что вычли: 15 − 6 = 9, а 9 + 6 = 15.</p>',
    '<p>Subtraction is addition in reverse. From <em>6 + 9 = 15</em> you get three more: 9 + 6 = 15, 15 − 6 = 9 and 15 − 9 = 6. To check a subtraction, add back what you took away: 15 − 6 = 9, and 9 + 6 = 15.</p>')
 + formula('c − a = b', 'проверка: b + a = c', 'check: b + a = c'),
 lab3)

tasks = [
 task(1, 'Лепёшки на базаре', 'Flatbreads at the bazaar', 'Утром продали 8 лепёшек, днём 7. Сколько всего продали?', 'In the morning 8 flatbreads were sold, in the afternoon 7. How many were sold in total?',
  '8 и 7', '8 and 7', '8 + 7: дополним 8 до десятка. 7 = 2 + 5. 8 + 2 = 10, 10 + 5 = 15.', '8 + 7: fill 8 up to ten. 7 = 2 + 5. 8 + 2 = 10, 10 + 5 = 15.', '15 лепёшек.', '15 flatbreads.', True),
 task(2, 'Сколько осталось', 'How many are left', 'В корзине было 15 яблок. 6 яблок съели. Сколько осталось?', 'There were 15 apples in a basket. 6 apples were eaten. How many are left?',
  '15 и 6', '15 and 6', '15 − 6: сначала вычтем 5, получится 10. Потом ещё 1: 10 − 1 = 9. Проверка: 9 + 6 = 15.', '15 − 6: first subtract 5 to get 10. Then 1 more: 10 − 1 = 9. Check: 9 + 6 = 15.', '9 яблок.', '9 apples.'),
 task(3, 'Семейка 7, 5, 12', 'The family 7, 5, 12', 'Составьте все четыре примера из чисел 7, 5 и 12.', 'Write all four equations using the numbers 7, 5 and 12.',
  '7, 5, 12', '7, 5, 12', '7 + 5 = 12 и 5 + 7 = 12. Вычитание: 12 − 7 = 5 и 12 − 5 = 7.', '7 + 5 = 12 and 5 + 7 = 12. Subtraction: 12 − 7 = 5 and 12 − 5 = 7.', '7 + 5 = 12; 5 + 7 = 12; 12 − 7 = 5; 12 − 5 = 7.', '7 + 5 = 12; 5 + 7 = 12; 12 − 7 = 5; 12 − 5 = 7.'),
 task(4, 'Неизвестное слагаемое', 'The missing addend', 'Найдите число: □ + 6 = 14.', 'Find the number: □ + 6 = 14.',
  '□ + 6 = 14', '□ + 6 = 14', 'Целое — 14, известная часть — 6. Другая часть: 14 − 6 = 8. Проверка: 8 + 6 = 14.', 'The whole is 14, the known part is 6. The other part: 14 − 6 = 8. Check: 8 + 6 = 14.', '□ = 8.', '□ = 8.'),
 task(5, 'Удобный порядок', 'A handy order', 'Вычислите 3 + 9 удобным способом.', 'Work out 3 + 9 in a handy way.',
  '3 + 9', '3 + 9', 'Поменяем слагаемые: 9 + 3. К большему прибавляем меньшее. 9 + 1 = 10, ещё 2 — 12.', 'Swap the addends: 9 + 3. Add the smaller to the bigger. 9 + 1 = 10, 2 more — 12.', '12.', '12.'),
]
quiz = [
 qz('Как называется результат сложения?', 'Сумма', 'Слагаемое', 'Разность', 'Сумма — это результат сложения.',
    'What is the result of an addition called?', 'The sum', 'An addend', 'The difference', 'The sum is the result of an addition.'),
 qz('Чему равно 9 + 6?', '15', '14', '16', '9 + 1 = 10, 10 + 5 = 15.',
    'What is 9 + 6?', '15', '14', '16', '9 + 1 = 10, 10 + 5 = 15.'),
 qz('Чему равно 14 − 8?', '6', '7', '22', '8 + 6 = 14.',
    'What is 14 − 8?', '6', '7', '22', '8 + 6 = 14.'),
 qz('Какой пример можно составить из 4 + 9 = 13?', '13 − 9 = 4', '13 + 9 = 4', '9 − 4 = 13', 'Вычитание — сложение наоборот.',
    'Which equation follows from 4 + 9 = 13?', '13 − 9 = 4', '13 + 9 = 4', '9 − 4 = 13', 'Subtraction is addition in reverse.'),
 qz('Что можно менять местами без изменения суммы?', 'Слагаемые', 'Числа при вычитании', 'Знаки', '8 + 5 = 5 + 8, а 8 − 5 ≠ 5 − 8.',
    'What can swap places without changing the sum?', 'The addends', 'The numbers in a subtraction', 'The signs', '8 + 5 = 5 + 8, but 8 − 5 ≠ 5 − 8.'),
 qz('Сколько надо добавить к 7, чтобы получить 10?', '3', '2', '4', '7 + 3 = 10.',
    'How much must be added to 7 to get 10?', '3', '2', '4', '7 + 3 = 10.'),
 qz('Найдите □: □ − 5 = 7.', '12', '2', '35', 'Было 12, убрали 5 — осталось 7. Проверка: 7 + 5 = 12.',
    'Find □: □ − 5 = 7.', '12', '2', '35', 'It was 12, 5 taken away — 7 left. Check: 7 + 5 = 12.'),
 qz('Чему равно 20 − 20?', '0', '20', '1', 'Если убрать всё, ничего не останется.',
    'What is 20 − 20?', '0', '20', '1', 'If you take away everything, nothing is left.'),
]
js = MJS + r'''
const T={ru:{jmLabel:"Прыжки по числовому лучу",tnLabel:"Сложение через десяток",fmLabel:"Три числа семейки",add:"сложить",sub:"вычесть"},
 en:{jmLabel:"Jumps on the number line",tnLabel:"Addition through the ten",fmLabel:"Three numbers of a family",add:"add",sub:"subtract"}};
function drawJm(){const t=T[lang],op=+$("jo").value,a=+$("ja").value;let b=+$("jb").value;if(op===1&&b>a){b=a;$("jb").value=b}
 const r=op===0?a+b:a-b;const MX=op===0?Math.max(20,Math.min(40,a+b)):20;let g=numLine(30,570,170,0,MX,1,MX>20?5:1);
 const X=v=>px(v,30,570,0,MX);g+=C(X(a),170,7,COL.b);
 const step=(X(1)-X(0));const dir=op===0?1:-1;
 for(let i=0;i<b;i++){const x1=X(a+dir*i),x2=X(a+dir*(i+1));g+='<path d="M'+x1+' 168 Q'+((x1+x2)/2)+' 120 '+x2+' 168" fill="none" stroke="'+COL.a+'" stroke-width="2"/>'}
 g+=C(X(r),170,9,COL.a)+TX(300,40,a+(op===0?" + ":" − ")+b+" = "+r,COL.ink,28)+TX(X(r),215,String(r),COL.a,14,"middle",600);
 $("jmSvg").innerHTML=g;$("jaOut").textContent=a;$("jbOut").textContent=b;
 $("jE").textContent=a+(op===0?" + ":" − ")+b;$("jR").textContent=r;$("jS").textContent=b;
 $("jmFb").textContent=op===0?U("Прибавить "+b+": "+b+" прыжков вправо от "+a+".","Add "+b+": "+b+" jumps right from "+a+"."):U("Вычесть "+b+": "+b+" прыжков влево от "+a+".","Subtract "+b+": "+b+" jumps left from "+a+".")}
["jo","ja","jb"].forEach(id=>$(id).addEventListener("input",drawJm));
function drawTn(){const a=+$("ta").value,b=+$("tb").value,need=10-a,rest=b-need,s=a+b;let g="";
 const cell=22,x0=30;
 for(let i=0;i<a;i++)g+=C(x0+i*cell+11,70,9,COL.a);
 for(let i=0;i<b;i++){const k=a+i;g+=C(x0+(k%10)*cell+(k>=10?0:0)+11+(k>=10?0:0),k>=10?100:70,9,i<need?COL.d:COL.b)}
 g+=TX(300,160,a+" + "+b+" = "+a+" + "+need+" + "+Math.max(rest,0)+" = 10 + "+Math.max(rest,0)+" = "+s,COL.ink,20);
 g+=TX(300,195,U("Красные — первое число, жёлтые — дополняем до десятка, синие — остаток","Red — the first number, yellow — fill up to ten, blue — the rest"),COL.mut,12);
 if(rest<0)g=C(0,0,0)+TX(300,125,U("Здесь переход через десяток не нужен: сумма меньше 10.","No crossing needed here: the sum is below 10."),COL.ink,16);
 $("tnSvg").innerHTML=g;$("taOut").textContent=a;$("tbOut").textContent=b;
 $("tFill").textContent=need;$("tLeft").textContent=Math.max(rest,0);$("tAns").textContent=s;
 $("tnFb").textContent=U("До десятка у "+a+" не хватает "+need+". Берём "+need+" от "+b+": остаётся "+Math.max(rest,0)+".","To reach ten, "+a+" needs "+need+". Take "+need+" from "+b+": "+Math.max(rest,0)+" is left.")}
["ta","tb"].forEach(id=>$(id).addEventListener("input",drawTn));
function drawFm(){const a=+$("fa").value,b=+$("fb").value,c=a+b;let g="";
 g+=TX(300,60,String(c),"#fff",26,"middle",600).replace("<text",'<circle cx="300" cy="52" r="26" fill="'+COL.ink+'"/><text');
 g+=L(300,78,160,150,COL.line,2)+L(300,78,440,150,COL.line,2);
 g+=C(160,170,26,COL.a)+TX(160,178,String(a),"#fff",24,"middle",600)+C(440,170,26,COL.b)+TX(440,178,String(b),"#fff",24,"middle",600);
 g+=TX(300,168,"+",COL.ink,30)+TX(300,215,U("целое — наверху, части — внизу","the whole is on top, the parts below"),COL.mut,12);
 $("fmSvg").innerHTML=g;$("faOut").textContent=a;$("fbOut").textContent=b;
 $("f1").textContent=a+" + "+b+" = "+c+";  "+b+" + "+a+" = "+c;$("f2").textContent=c+" − "+a+" = "+b;$("f3").textContent=c+" − "+b+" = "+a;
 $("fmFb").textContent=U("Проверка: "+b+" + "+a+" = "+c+".","Check: "+b+" + "+a+" = "+c+".")}
["fa","fb"].forEach(id=>$(id).addEventListener("input",drawFm));
const LAB={ru:{jmSvg:T.ru.jmLabel,tnSvg:T.ru.tnLabel,fmSvg:T.ru.fmLabel},en:{jmSvg:T.en.jmLabel,tnSvg:T.en.tnLabel,fmSvg:T.en.fmLabel}};
function drawAll(){fillSel("jo",[T[lang].add,T[lang].sub],0);drawJm();drawTn();drawFm()}
'''
c = dict(n='02', slug='02-add-subtract.html', block='I', level_ru='ОСНОВЫ · 1–2 КЛАССЫ', level_en='BASICS · GRADES 1–2',
 title=('Сложение и вычитание', 'Addition and subtraction'),
 desc='Глава 2 Атласа математики: сложение и вычитание до 20, переход через десяток, связь сложения и вычитания.',
 lead=('Как быстро сложить 8 + 7 и не считать по одному: прыжки по лучу, переход через десяток и семейки чисел.',
       'How to add 8 + 7 quickly without counting one by one: jumps on the line, crossing the ten, and number families.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('line', 'Прыжки', 'Jumps'), ('ten', 'Через десяток', 'Crossing ten'), ('family', 'Семейка', 'Family'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На базаре продавщица Айгуль утром продала 8 лепёшек, а днём ещё 7. Покупатели торопятся, а считать по одной лепёшке долго.</p><p>Как быстро понять, сколько лепёшек она продала за день?</p>',
         '<p>At the bazaar the seller Aigul sold 8 flatbreads in the morning and 7 more in the afternoon. Customers are in a hurry, and counting flatbreads one by one takes long.</p><p>How can she quickly tell how many flatbreads she sold in a day?</p>'),
 hint=stdhint('Переход через десяток', 'Crossing the ten'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 15 лепёшек', 'The answer: 15 flatbreads'),
 answer=('<p>Айгуль делает так: 8 + 7 = 8 + 2 + 5. Сначала 8 + 2 = 10 — полный десяток. Потом 10 + 5 = 15. Это быстрее, чем считать по одному, и так легко проверить себя: 15 − 7 = 8.</p>',
         '<p>Aigul does it like this: 8 + 7 = 8 + 2 + 5. First 8 + 2 = 10 — a full ten. Then 10 + 5 = 15. This is faster than counting one by one, and it is easy to check: 15 − 7 = 8.</p>'),
 sources=[('Сложение и вычитание —', 'Addition and subtraction —', LINK('https://en.wikipedia.org/wiki/Addition', 'Wikipedia: Addition') + ', ' + LINK('https://en.wikipedia.org/wiki/Subtraction', 'Wikipedia: Subtraction')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Сюжет про Айгуль придуман для атласа.', 'The story of Aigul was invented for the atlas.'),
 prev=('01-numbers-to-20.html', 'Глава 1 · Числа до 20', 'Chapter 1 · Numbers to 20'),
 next=('03-place-value.html', 'Глава 3 · Разряды и числа до 1000', 'Chapter 3 · Place value and numbers to 1000'),
 js=js)
build(c)
