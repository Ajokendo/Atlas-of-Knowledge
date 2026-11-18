# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Числа со знаком на прямой', 'Signed numbers on a line'),
 [('r', 'a', 'Число a', 'Number a', -15, 15, 1, -4), ('r', 'b', 'Число b', 'Number b', -15, 15, 1, 6)],
 [('Модуль a и b', 'Absolute values of a and b'), ('Что больше', 'Which is greater'), ('Расстояние между ними', 'Distance between them')],
 'Положительные числа лежат справа от нуля, отрицательные — слева. Модуль — расстояние до нуля.', 'Positive numbers are right of zero, negative ones left. The absolute value is the distance to zero.', ('Числовая прямая от −15 до 15', 'A number line from −15 to 15'),
 r'''const X=t=>300+t*18;let g=L(20,120,580,120,COL.ink,3);for(let t=-15;t<=15;t++)g+=L(X(t),t%5===0?110:115,X(t),t%5===0?130:125,COL.ink,t%5===0?2:1)+(t%5===0?TX(X(t),150,t,COL.mut,12):"");
 g+=L(X(v.a),70,X(v.a),120,COL.a,2)+C(X(v.a),120,9,COL.a)+TX(X(v.a),60,v.a,COL.a,16,"middle",700)+C(X(v.b),120,9,COL.b)+TX(X(v.b),90,v.b,COL.b,16,"middle",700)+L(X(v.a),185,X(v.b),185,COL.c,4)+TX((X(v.a)+X(v.b))/2,205,U("расстояние "+Math.abs(v.a-v.b),"distance "+Math.abs(v.a-v.b)),COL.c,14,"middle",600);
 return {svg:g,st:["|"+v.a+"| = "+Math.abs(v.a)+",  |"+v.b+"| = "+Math.abs(v.b),v.a===v.b?"=":v.a>v.b?v.a+" > "+v.b:v.b+" > "+v.a,"|"+v.a+" − "+v.b+"| = "+Math.abs(v.a-v.b)],fb:U("Чем правее число на прямой, тем оно больше.","The further right on the line, the greater the number.")}''')

m2 = M(('Сложение и вычитание чисел со знаком', 'Adding and subtracting signed numbers'),
 [('r', 'a', 'Первое слагаемое', 'First addend', -10, 10, 1, 3), ('r', 'b', 'Второе слагаемое', 'Second addend', -10, 10, 1, -7)],
 [('Сумма', 'Sum'), ('Разность a − b', 'Difference a − b'), ('Куда шагнули', 'Where the step goes')],
 'Прибавить положительное — шаг вправо, отрицательное — шаг влево. Вычитание числа — это прибавление противоположного.', 'Adding a positive number is a step right, a negative one — a step left. Subtracting a number is adding its opposite.', ('Два шага по числовой прямой', 'Two steps along the number line'),
 r'''const X=t=>300+t*14;let g=L(20,120,580,120,COL.ink,3);for(let t=-20;t<=20;t+=5)g+=L(X(t),112,X(t),128,COL.ink,2)+TX(X(t),148,t,COL.mut,12);
 const s=v.a+v.b;g+=arrow(X(0),90,X(v.a),90,COL.a,3)+arrow(X(v.a),60,X(s),60,COL.b,3)+C(X(s),120,9,COL.c)+TX(X(s),175,s,COL.c,18,"middle",700)+TX(X(v.a/2),80,v.a,COL.a,14,"middle",600)+TX(X((v.a+s)/2),50,(v.b>=0?"+":"")+v.b,COL.b,14,"middle",600);
 return {svg:g,st:[v.a+" + ("+v.b+") = "+s,v.a+" − ("+v.b+") = "+(v.a-v.b),v.b>=0?U("вправо","right"):U("влево","left")],fb:U("Вычитание: "+v.a+" − ("+v.b+") = "+v.a+" + ("+(-v.b)+") = "+(v.a-v.b)+".","Subtraction: "+v.a+" − ("+v.b+") = "+v.a+" + ("+(-v.b)+") = "+(v.a-v.b)+".")}''')

m3 = M(('Умножение и деление: правило знаков', 'Multiplication and division: the sign rule'),
 [('r', 'a', 'Множитель a', 'Factor a', -9, 9, 1, -3), ('r', 'b', 'Множитель b', 'Factor b', -9, 9, 1, 4)],
 [('Произведение', 'Product'), ('Знак результата', 'Sign of the result'), ('Частное a : b', 'Quotient a : b')],
 'Одинаковые знаки — плюс, разные — минус. Нуль на знак не влияет.', 'The same signs give plus, different signs give minus. Zero has no sign.', ('Таблица знаков', 'A table of signs'),
 r'''let g="";const sg=[["+","+","+"],["+","−","−"],["−","+","−"],["−","−","+"]];const cs=v.a>0?"+":v.a<0?"−":"0",cb=v.b>0?"+":v.b<0?"−":"0";
 sg.forEach((r,i)=>{const act=r[0]===cs&&r[1]===cb;g+=R(120,20+i*48,360,40,act?"#f4dfd8":COL.bg,act?COL.a:COL.line,act?3:1.5,4)+TX(190,47+i*48,r[0]+" · "+r[1],COL.ink,20,"middle",600)+TX(300,47+i*48,"=",COL.mut,20)+TX(410,47+i*48,r[2],r[2]==="+"?COL.c:COL.a,22,"middle",700)});
 const pr=v.a*v.b;return {svg:g,st:[v.a+" · "+v.b+" = "+pr,pr>0?U("плюс","plus"):pr<0?U("минус","minus"):U("нуль","zero"),v.b===0?U("на нуль делить нельзя","cannot divide by zero"):fnum(v.a/v.b,3)],fb:U("Минус на минус даёт плюс: долг, который сняли, — это прибыль.","A minus times a minus gives a plus: removing a debt is a gain.")}''', '0 0 600 220')

chapter('22', '22-integers-rationals.html', 'IV', ('Целые и рациональные числа', 'Integers and rational numbers'),
 ('Откуда берутся отрицательные числа, как их складывать и умножать и почему «минус на минус даёт плюс».', 'Where negative numbers come from, how to add and multiply them and why “a minus times a minus gives a plus”.'),
 ('Утром в Караколе было −8 °C, к полудню потеплело на 11 градусов, а к ночи похолодало на 5.\n\nКакая температура была ночью?', 'In the morning it was −8 °C in Karakol, by noon it warmed by 11 degrees and by night it cooled by 5.\n\nWhat was the temperature at night?'),
 ('Разгадка: −2 °C', 'The answer: −2 °C'),
 ('Считаем шагами по числовой прямой: −8 + 11 = 3 (в полдень +3 °C), затем 3 − 5 = −2. Ночью температура была −2 °C. Градусник — готовая вертикальная числовая прямая: потепление — шаг вверх, похолодание — шаг вниз.', 'We count with steps on the number line: −8 + 11 = 3 (at noon +3 °C), then 3 − 5 = −2. At night it was −2 °C. A thermometer is a ready-made vertical number line: warming is a step up, cooling a step down.'),
 [S('line', 'Отрицательные числа и модуль', 'Negative numbers and absolute value', ('<strong>Целые числа</strong> — это натуральные числа, им противоположные и нуль. Вместе с дробями они образуют <strong>рациональные числа</strong>. На прямой положительные числа справа от нуля, отрицательные слева; большее число стоит правее. <strong>Модуль</strong> |a| — расстояние от a до нуля: |−4| = 4.', '<strong>Integers</strong> are the natural numbers, their opposites and zero. Together with fractions they form the <strong>rational numbers</strong>. On the line positive numbers are right of zero, negative left; the greater number stands further right. The <strong>absolute value</strong> |a| is the distance from a to zero: |−4| = 4.'),
    ('|a − b| — расстояние между a и b', '', '|a − b| is the distance between a and b'), m1),
  S('add', 'Сложение и вычитание', 'Adding and subtracting', ('Прибавить положительное число — сдвиг вправо, отрицательное — влево. Вычитание заменяют сложением с противоположным числом: a − b = a + (−b). Так, 3 − (−7) = 3 + 7 = 10. Числа с одинаковыми знаками складываются по модулю, с разными — вычитаются модули, знак берут у числа с большим модулем.', 'Adding a positive number is a shift right, a negative one — left. Subtraction is replaced by adding the opposite: a − b = a + (−b). So 3 − (−7) = 3 + 7 = 10. Numbers with the same sign add by absolute values; with different signs we subtract the absolute values and take the sign of the number with the larger absolute value.'),
    ('a − b = a + (−b)', '', 'a − b = a + (−b)'), m2),
  S('mul', 'Умножение и деление', 'Multiplying and dividing', ('Знак произведения и частного: одинаковые знаки — «+», разные — «−». Почему (−3) · (−4) = 12? Умножение на −4 — «обратить» четыре раза по 3. Если 3 · (−4) = −12 — долг, то отнять долг — значит получить плюс. Деление на нуль не определено.', 'The sign of a product and a quotient: the same signs — “+”, different — “−”. Why is (−3) · (−4) = 12? Multiplying by −4 means “reversing” four times 3. If 3 · (−4) = −12 is a debt, then taking away a debt gives a plus. Division by zero is undefined.'),
    ('(−)·(−) = +;  (−)·(+) = −', '', '(−)·(−) = +;  (−)·(+) = −'), m3)],
 [TK(('Сравнить', 'Compare'), ('Расположите по возрастанию: 3, −5, 0, −1, 2.', 'Order ascending: 3, −5, 0, −1, 2.'), 'Левее — меньше', '−5, −1, 0, 2, 3.', ('−5 &lt; −1 &lt; 0 &lt; 2 &lt; 3.', '−5 &lt; −1 &lt; 0 &lt; 2 &lt; 3.')),
  TK(('Сложить', 'Add'), ('Найдите −7 + 12 и −7 − 5.', 'Find −7 + 12 and −7 − 5.'), '', '−7 + 12 = 5 (разность модулей 12 − 7, знак «+»). −7 − 5 = −12.', '5; −12.'),
  TK(('Вычесть отрицательное', 'Subtract a negative'), ('Найдите 4 − (−6).', 'Find 4 − (−6).'), '4 + 6', 'Вычитание заменяем сложением с противоположным: 4 + 6 = 10.', '10.'),
  TK(('Умножить', 'Multiply'), ('Найдите (−6) · (−3) и (−18) : 6.', 'Find (−6) · (−3) and (−18) : 6.'), '', 'Одинаковые знаки — плюс: 18. Разные — минус: −3.', '18; −3.'),
  TK(('Температура', 'Temperature'), ('Было −3 °C. Стало на 9 градусов теплее, затем на 12 холоднее. Сколько стало?', 'It was −3 °C. It became 9 degrees warmer, then 12 colder. What is it now?'), '−3 + 9 − 12', '−3 + 9 = 6; 6 − 12 = −6.', '−6 °C.')],
 [Q('Какое число меньше?', 'Which number is smaller?', '−7', '−2', '0', ('Левее — меньше.', 'Further left — smaller.')),
  Q('|−9| =', '|−9| =', '9', '−9', '0', ('Расстояние до нуля — 9.', 'The distance to zero is 9.')),
  Q('−4 + 10 =', '−4 + 10 =', '6', '−6', '14', ('Шаг вправо на 10.', 'A step right by 10.')),
  Q('5 − (−3) =', '5 − (−3) =', '8', '2', '−8', ('5 + 3.', '5 + 3.')),
  Q('(−2) · (−7) =', '(−2) · (−7) =', '14', '−14', '9', ('Минус на минус — плюс.', 'Minus times minus is plus.')),
  Q('(−20) : 4 =', '(−20) : 4 =', '−5', '5', '−80', ('Разные знаки — минус.', 'Different signs — minus.')),
  Q('Можно ли делить на нуль?', 'Can we divide by zero?', ('Нет, не определено', 'No, undefined'), ('Да, получится 0', 'Yes, we get 0'), ('Да, получится 1', 'Yes, we get 1'), ('Деление на нуль не определено.', 'Division by zero is undefined.')),
  Q('Расстояние между −3 и 5', 'The distance between −3 and 5', '8', '2', '−8', ('|5 − (−3)| = 8.', '|5 − (−3)| = 8.'))],
 src=[('Wikipedia: Negative number', 'https://en.wikipedia.org/wiki/Negative_number'), ('Wikipedia: Rational number', 'https://en.wikipedia.org/wiki/Rational_number')],
 note=('Температуры придуманы для задачи; это не данные наблюдений.', 'The temperatures are made up for the problem; they are not observations.'))
