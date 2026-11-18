# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'ВЫЧИСЛЯЕМ ПО ШАГАМ', 'WORKING IT OUT STEP BY STEP', 'opSvg', '0 0 600 250',
  select('oe', 'Выражение', 'Expression') + slider('os', 'Шаг', 'Step', 0, 5, 1, 5),
  stats([('oN', 'Действий в выражении', 'Operations in the expression'), ('oA', 'Ответ', 'Answer'), ('oF', 'Что делаем на этом шаге', 'What we do at this step')]),
  'opFb', 'Двигайте ползунок «Шаг»: выражение упрощается по одному действию. Последняя строка — текущая.',
  'Move the “Step” slider: the expression simplifies one operation at a time. The last line is the current one.')
s1 = section('order', 'Что делать первым', 'What to do first',
 bd('<p>Чтобы все получали один и тот же ответ, математики договорились о <strong>порядке действий</strong>:</p><ol class="steps"><li>Сначала то, что <strong>в скобках</strong>.</li><li>Потом <strong>умножение и деление</strong> — слева направо.</li><li>Потом <strong>сложение и вычитание</strong> — слева направо.</li></ol><p>В выражении <em>20 − 6 + 4</em> нет скобок и умножения, поэтому идём слева направо: 20 − 6 = 14, потом 14 + 4 = 18.</p>',
    '<p>So that everybody gets the same answer, mathematicians agreed on the <strong>order of operations</strong>:</p><ol class="steps"><li>First what is <strong>in brackets</strong>.</li><li>Then <strong>multiplication and division</strong> — left to right.</li><li>Then <strong>addition and subtraction</strong> — left to right.</li></ol><p>In <em>20 − 6 + 4</em> there are no brackets or multiplication, so we go left to right: 20 − 6 = 14, then 14 + 4 = 18.</p>')
 + formula('2 + 2 · 2 = 2 + 4 = 6', 'сначала умножение', 'multiplication first'),
 lab1)

lab2 = model(2, 'СКОБКИ МЕНЯЮТ ОТВЕТ', 'BRACKETS CHANGE THE ANSWER', 'brSvg', '0 0 600 250',
  slider('ba', 'Число a', 'Number a', 1, 9, 1, 2) + slider('bb', 'Число b', 'Number b', 1, 9, 1, 3) + slider('bc', 'Число c', 'Number c', 1, 9, 1, 4),
  stats([('bN', 'Без скобок: a + b · c', 'No brackets: a + b · c'), ('bY', 'Со скобками: (a + b) · c', 'With brackets: (a + b) · c'), ('bD', 'Разница', 'Difference')]),
  'brFb', 'Одни и те же числа и знаки, а ответы разные: скобки меняют порядок действий.',
  'The same numbers and signs, but different answers: brackets change the order.')
s2 = section('brackets', 'Скобки', 'Brackets',
 bd('<p>Скобки говорят: «это действие делай первым». Сравните <em>2 + 3 · 4 = 14</em> и <em>(2 + 3) · 4 = 20</em>. Числа те же, а ответ разный. Поэтому скобки нужно ставить внимательно.</p>',
    '<p>Brackets say: “do this operation first”. Compare <em>2 + 3 · 4 = 14</em> and <em>(2 + 3) · 4 = 20</em>. The same numbers, a different answer. So brackets must be placed carefully.</p>')
 + formula('2 + 3 · 4 = 14,  (2 + 3) · 4 = 20', 'скобки меняют порядок', 'brackets change the order'),
 lab2)

lab3 = model(3, 'РАССТАВЬ ЗНАКИ', 'FIND THE SIGNS', 'sgSvg', '0 0 600 250',
  slider('ga', 'a', 'a', 1, 9, 1, 2) + slider('gb', 'b', 'b', 1, 9, 1, 3) + slider('gc', 'c', 'c', 1, 9, 1, 4) + slider('gt', 'Нужный ответ', 'Target', -20, 100, 1, 14),
  stats([('gM', 'Подходят вариантов', 'Matching options'), ('gW', 'Какие', 'Which')]),
  'sgFb', 'Из 9 комбинаций знаков выбираем те, при которых получается нужный ответ. Помните про порядок действий!',
  'Of the 9 sign combinations we pick those that give the target. Remember the order of operations!')
s3 = section('signs', 'Расставь знаки', 'Find the signs',
 bd('<p>Бывает наоборот: числа даны, а знаки надо подобрать. Для чисел 2, 3, 4 и ответа 14 подходит только <em>2 + 3 · 4 = 14</em>. Перебирая варианты, обязательно считайте по правилам — сначала умножение.</p>',
    '<p>Sometimes it works the other way: the numbers are given and the signs must be found. For the numbers 2, 3, 4 and the target 14 only <em>2 + 3 · 4 = 14</em> works. When you try the options, always calculate by the rules — multiplication first.</p>')
 + formula('2 ? 3 ? 4 = 14', 'ответ: 2 + 3 · 4', 'answer: 2 + 3 · 4'),
 lab3)

tasks = [
 task(1, 'Слева направо', 'Left to right', 'Вычислите 20 − 6 + 4.', 'Work out 20 − 6 + 4.',
  '20 − 6 + 4', '20 − 6 + 4', 'Только сложение и вычитание — идём слева направо: 20 − 6 = 14, затем 14 + 4 = 18. (Если сначала 6 + 4, получится 10 — это ошибка.)', 'Only addition and subtraction — go left to right: 20 − 6 = 14, then 14 + 4 = 18. (If you add 6 + 4 first you get 10 — a mistake.)', '18.', '18.', True),
 task(2, 'Со скобками', 'With brackets', 'Вычислите 5 + 4 · (10 − 7).', 'Work out 5 + 4 · (10 − 7).',
  '5 + 4 · (10 − 7)', '5 + 4 · (10 − 7)', '1) в скобках: 10 − 7 = 3. 2) умножение: 4 · 3 = 12. 3) сложение: 5 + 12 = 17.', '1) in brackets: 10 − 7 = 3. 2) multiplication: 4 · 3 = 12. 3) addition: 5 + 12 = 17.', '17.', '17.'),
 task(3, 'Покупка', 'A purchase', 'Мама купила 3 пакета молока по 12 сом и хлеб за 18 сом. Запишите выражение и найдите, сколько она заплатила.', 'Mother bought 3 cartons of milk at 12 soms and a loaf of bread for 18 soms. Write an expression and find how much she paid.',
  '3 по 12 сом и 18 сом', '3 at 12 soms and 18 soms', 'Выражение: 3 · 12 + 18. Сначала умножение: 36. Потом сложение: 36 + 18 = 54.', 'Expression: 3 · 12 + 18. First multiplication: 36. Then addition: 36 + 18 = 54.', '54 сома.', '54 soms.'),
 task(4, 'Расставьте скобки', 'Place the brackets', 'Расставьте скобки так, чтобы получилось 19: 2 + 3 · 4 − 1.', 'Place brackets so the result is 19: 2 + 3 · 4 − 1.',
  '2 + 3 · 4 − 1 = 19', '2 + 3 · 4 − 1 = 19', 'Без скобок: 2 + 12 − 1 = 13. Если сложить 2 и 3 первыми: (2 + 3) · 4 − 1 = 5 · 4 − 1 = 20 − 1 = 19.', 'Without brackets: 2 + 12 − 1 = 13. If we add 2 and 3 first: (2 + 3) · 4 − 1 = 5 · 4 − 1 = 20 − 1 = 19.', '(2 + 3) · 4 − 1 = 19.', '(2 + 3) · 4 − 1 = 19.'),
 task(5, 'Деление и умножение', 'Division and multiplication', 'Вычислите 12 : 3 · 2.', 'Work out 12 : 3 · 2.',
  '12 : 3 · 2', '12 : 3 · 2', 'Деление и умножение — слева направо: 12 : 3 = 4, затем 4 · 2 = 8.', 'Division and multiplication — left to right: 12 : 3 = 4, then 4 · 2 = 8.', '8.', '8.'),
]
quiz = [
 qz('Чему равно 2 + 2 · 2?', '6', '8', '4', 'Сначала умножение: 2 · 2 = 4, потом 2 + 4 = 6.',
    'What is 2 + 2 · 2?', '6', '8', '4', 'First multiplication: 2 · 2 = 4, then 2 + 4 = 6.'),
 qz('Что делают первым?', 'Действия в скобках', 'Сложение', 'Вычитание', 'Скобки указывают первое действие.',
    'What is done first?', 'Operations in brackets', 'Addition', 'Subtraction', 'Brackets mark the first operation.'),
 qz('Чему равно (2 + 2) · 2?', '8', '6', '4', 'В скобках 4, потом 4 · 2 = 8.',
    'What is (2 + 2) · 2?', '8', '6', '4', 'In brackets 4, then 4 · 2 = 8.'),
 qz('Чему равно 20 − 6 + 4?', '18', '10', '22', 'Слева направо: 14, потом 18.',
    'What is 20 − 6 + 4?', '18', '10', '22', 'Left to right: 14, then 18.'),
 qz('Чему равно 12 : 3 · 2?', '8', '2', '6', '12 : 3 = 4, 4 · 2 = 8.',
    'What is 12 : 3 · 2?', '8', '2', '6', '12 : 3 = 4, 4 · 2 = 8.'),
 qz('Что выполняется раньше: умножение или сложение?', 'Умножение', 'Сложение', 'Что стоит левее', '5 + 4 · 3 = 5 + 12 = 17.',
    'Which comes first: multiplication or addition?', 'Multiplication', 'Addition', 'Whatever is on the left', '5 + 4 · 3 = 5 + 12 = 17.'),
 qz('Чему равно 30 − 2 · (3 + 4)?', '16', '196', '24', '3 + 4 = 7, 2 · 7 = 14, 30 − 14 = 16.',
    'What is 30 − 2 · (3 + 4)?', '16', '196', '24', '3 + 4 = 7, 2 · 7 = 14, 30 − 14 = 16.'),
 qz('Сколько действий в выражении 5 + 4 · (10 − 7)?', '3', '2', '4', 'Вычитание, умножение, сложение.',
    'How many operations are in 5 + 4 · (10 − 7)?', '3', '2', '4', 'Subtraction, multiplication, addition.'),
]
js = MJS + r'''
const EXPR=["2 + 2 × 2","( 2 + 2 ) × 2","20 − 6 + 4","12 ÷ 3 × 2","5 + 4 × ( 10 − 7 )","30 − 2 × ( 3 + 4 )"];
const T={ru:{opLabel:"Выражение, упрощаемое по шагам",brLabel:"Два выражения с одними числами",sgLabel:"Девять вариантов знаков",br:"скобки",md:"умножение или деление",as:"сложение или вычитание",none:"начало",done:"готово"},
 en:{opLabel:"An expression simplified step by step",brLabel:"Two expressions with the same numbers",sgLabel:"Nine sign options",br:"brackets",md:"multiplication or division",as:"addition or subtraction",none:"start",done:"done"}};
function pretty(a){return (Array.isArray(a)?a.join(" "):a).replace(/\( /g,"(").replace(/ \)/g,")")}
function evalSteps(str){let tok=str.split(" ").map(x=>/^\d+$/.test(x)?+x:x);const lines=[tok.slice()],kinds=["none"];
 for(let guard=0;guard<20&&tok.length>1;guard++){let lo=0,hi=tok.length-1,i=tok.lastIndexOf("("),paren=false;
  if(i>=0){lo=i+1;hi=tok.indexOf(")",i)-1;paren=true}
  let k=-1;for(let p=lo;p<=hi;p++)if(tok[p]==="×"||tok[p]==="÷"){k=p;break}
  if(k<0)for(let p=lo;p<=hi;p++)if(tok[p]==="+"||tok[p]==="−"){k=p;break}
  if(k<0)break;const a=tok[k-1],b=tok[k+1],o=tok[k];const r=o==="×"?a*b:o==="÷"?a/b:o==="+"?a+b:a-b;
  tok.splice(k-1,3,r);if(paren&&tok[i]==="("&&tok[i+2]===")")tok.splice(i,3,tok[i+1]);
  lines.push(tok.slice());kinds.push(paren?"br":(o==="×"||o==="÷")?"md":"as")}
 return {lines:lines,kinds:kinds}}
function drawOp(){const t=T[lang],ex=+$("oe").value,E=evalSteps(EXPR[ex]),n=E.lines.length-1;const sl=$("os");sl.max=n;let s=Math.min(+sl.value,n);sl.value=s;let g="";
 for(let i=0;i<=s;i++){const cur=i===s;g+=TX(60,50+i*36,pretty(E.lines[i]),cur?COL.a:COL.mut,cur?26:20,"start",cur?600:400)}
 if(s>0)g+=TX(540,50+s*36,t[E.kinds[s]],COL.b,13,"end");
 $("opSvg").innerHTML=g;$("osOut").textContent=s+" / "+n;
 $("oN").textContent=n;$("oA").textContent=E.lines[n][0];$("oF").textContent=s===0?t.none:t[E.kinds[s]];
 $("opFb").textContent=s===n?U("Ответ: "+pretty(E.lines[0])+" = "+E.lines[n][0]+".","Answer: "+pretty(E.lines[0])+" = "+E.lines[n][0]+"."):U("Дальше: "+t[E.kinds[s+1]]+".","Next: "+t[E.kinds[s+1]]+".")}
["oe","os"].forEach(id=>$(id).addEventListener("input",drawOp));
function drawBr(){const a=+$("ba").value,b=+$("bb").value,c=+$("bc").value,n1=a+b*c,n2=(a+b)*c,mx=Math.max(n1,n2,1);let g="";
 [[n1,a+" + "+b+" · "+c,COL.a,60],[n2,"("+a+" + "+b+") · "+c,COL.b,140]].forEach(r=>{const w=r[0]/mx*400;g+=R(150,r[3],w,40,r[2],"none",0,4)+TX(140,r[3]+27,r[1],COL.ink,16,"end")+TX(158+w,r[3]+27,"= "+r[0],COL.ink,18,"start",600)});
 $("brSvg").innerHTML=g;$("baOut").textContent=a;$("bbOut").textContent=b;$("bcOut").textContent=c;
 $("bN").textContent=n1;$("bY").textContent=n2;$("bD").textContent=Math.abs(n2-n1);
 $("brFb").textContent=n1===n2?U("Здесь ответы совпали, но так бывает не всегда.","The answers coincide here, but this is not always so."):U("Ответы различаются на "+Math.abs(n2-n1)+".","The answers differ by "+Math.abs(n2-n1)+".")}
["ba","bb","bc"].forEach(id=>$(id).addEventListener("input",drawBr));
function f3(a,o1,b,o2,c){const ap=(x,o,y)=>o==="+"?x+y:o==="−"?x-y:x*y;return o2==="×"?ap(a,o1,b*c):ap(ap(a,o1,b),o2,c)}
function drawSg(){const a=+$("ga").value,b=+$("gb").value,c=+$("gc").value,tg=+$("gt").value,ops=["+","−","×"];let g="",hits=[];let idx=0;
 ops.forEach(o1=>ops.forEach(o2=>{const v=f3(a,o1,b,o2,c),ok=v===tg;const col=Math.floor(idx/3),row=idx%3,x=40+col*185,y=40+row*60;
  g+=R(x,y,170,46,ok?"#e1f0e8":COL.bg,ok?COL.c:COL.line,ok?3:1,4)+TX(x+85,y+20,a+" "+o1+" "+b+" "+o2+" "+c,COL.ink,15)+TX(x+85,y+39,"= "+v,ok?COL.c:COL.mut,15,"middle",ok?600:400);
  if(ok)hits.push(a+" "+o1+" "+b+" "+o2+" "+c);idx++}));
 $("sgSvg").innerHTML=g;$("gaOut").textContent=a;$("gbOut").textContent=b;$("gcOut").textContent=c;$("gtOut").textContent=tg;
 $("gM").textContent=hits.length;$("gW").textContent=hits.length?hits.join(";  "):"—";
 $("sgFb").textContent=hits.length?U("Нашли! Проверьте: умножение выполняется раньше.","Found! Check: multiplication goes first."):U("Такой ответ не получается ни с одной комбинацией — измените число или ответ.","No combination gives this target — change a number or the target.")}
["ga","gb","gc","gt"].forEach(id=>$(id).addEventListener("input",drawSg));
const LAB={ru:{opSvg:T.ru.opLabel,brSvg:T.ru.brLabel,sgSvg:T.ru.sgLabel},en:{opSvg:T.en.opLabel,brSvg:T.en.brLabel,sgSvg:T.en.sgLabel}};
function drawAll(){fillSel("oe",EXPR.map(pretty),0);drawOp();drawBr();drawSg()}
'''
c = dict(n='06', slug='06-order-of-operations.html', block='I', level_ru='ОСНОВЫ · 3–4 КЛАССЫ', level_en='BASICS · GRADES 3–4',
 title=('Порядок действий и скобки', 'Order of operations and brackets'),
 desc='Глава 6 Атласа математики: порядок действий, скобки, вычисление выражений по шагам, подбор знаков.',
 lead=('Почему 2 + 2 · 2 — это 6, а не 8: порядок действий, скобки и подбор знаков.',
       'Why 2 + 2 · 2 is 6, not 8: the order of operations, brackets and finding signs.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('order', 'Порядок', 'Order'), ('brackets', 'Скобки', 'Brackets'), ('signs', 'Знаки', 'Signs'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Айбек и Айдай вычисляют 2 + 2 · 2. Айбек говорит: «Два плюс два — четыре, умножить на два — восемь». Айдай говорит: «Шесть». Калькулятор показывает 6.</p><p>Кто прав и как Айбек получил 8?</p>',
         '<p>Aibek and Aidai work out 2 + 2 · 2. Aibek says: “Two plus two is four, times two is eight.” Aidai says: “Six.” The calculator shows 6.</p><p>Who is right and how did Aibek get 8?</p>'),
 hint=stdhint('Вычисляем по шагам', 'Working it out step by step'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 6', 'The answer: 6'),
 answer=('<p>Правильно 6. Айбек считал слева направо, не обращая внимания на знаки. А по правилу умножение выполняется раньше сложения: 2 · 2 = 4, и только потом 2 + 4 = 6. Хочешь получить 8 — поставь скобки: (2 + 2) · 2 = 8.</p>',
         '<p>The right answer is 6. Aibek went left to right, ignoring the signs. By the rule, multiplication goes before addition: 2 · 2 = 4 and only then 2 + 4 = 6. If you want 8, put in brackets: (2 + 2) · 2 = 8.</p>'),
 sources=[('Порядок действий —', 'Order of operations —', LINK('https://en.wikipedia.org/wiki/Order_of_operations', 'Wikipedia: Order of operations')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Сюжет придуман для атласа.', 'The story was invented for the atlas.'),
 prev=('05-column-arithmetic.html', 'Глава 5 · Действия в столбик', 'Chapter 5 · Column arithmetic'),
 next=('07-word-problems.html', 'Глава 7 · Текстовые задачи', 'Chapter 7 · Word problems'),
 js=js)
build(c)
