# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Геометрическая прогрессия', 'Geometric progression'),
 [('r', 'b1', 'Первый член b₁', 'First term b₁', 1, 10, 1, 2), ('r', 'q', 'Знаменатель q', 'Common ratio q', 0.5, 3, 0.5, 2), ('r', 'n', 'Номер n', 'Term number n', 1, 10, 1, 6)],
 [('n-й член bₙ = b₁·qⁿ⁻¹', 'nth term bₙ = b₁·qⁿ⁻¹'), ('Первые члены', 'The first terms'), ('Характер роста', 'Kind of growth')],
 'Каждый следующий член получается умножением предыдущего на одно и то же число q — знаменатель.', 'Each next term is got by multiplying the previous one by the same number q — the common ratio.', ('Члены прогрессии (столбики)', 'The terms of the progression (bars)'),
 r'''const T=[];for(let i=0;i<10;i++)T.push(v.b1*Math.pow(v.q,i));const mx=Math.max(...T);let g="";T.forEach((t,i)=>{const h=Math.max(2,t/mx*170);g+=R(40+i*54,195-h,44,h,i+1===v.n?COL.a:COL.b,"none",0,3)+TX(62+i*54,190-h,fnum(t,t>=100?0:1),COL.ink,11,"middle",600)});
 const bn=v.b1*Math.pow(v.q,v.n-1);return {svg:g,st:[v.b1+"·"+v.q+"^"+(v.n-1)+" = "+fnum(bn,2),T.slice(0,5).map(x=>fnum(x,2)).join(", ")+", …",v.q>1?U("быстрый рост","fast growth"):v.q<1?U("убывание","decay"):U("постоянная","constant")],fb:U("При q > 1 члены растут очень быстро — сравните с арифметической прогрессией.","For q > 1 the terms grow very fast — compare with an arithmetic progression.")}''', '0 0 600 205')

m2 = M(('Сумма и бесконечная сумма', 'The sum and the infinite sum'),
 [('r', 'b1', 'Первый член', 'First term', 1, 20, 1, 10), ('r', 'q', 'Знаменатель q', 'Common ratio q', -0.9, 0.9, 0.1, 0.5), ('r', 'n', 'Число членов', 'Number of terms', 1, 20, 1, 8)],
 [('Сумма n членов', 'Sum of n terms'), ('Сумма всех (если |q| < 1)', 'Sum of all (if |q| < 1)'), ('Не хватает до предела', 'Shortfall from the limit')],
 'Если |q| &lt; 1, члены убывают и сумма бесконечного числа членов существует: S = b₁ / (1 − q).', 'If |q| &lt; 1 the terms decrease and the sum of infinitely many terms exists: S = b₁ / (1 − q).', ('Частичные суммы приближаются к пределу', 'Partial sums approach the limit'),
 r'''const qq=v.q===1?0.5:v.q,Sinf=v.b1/(1-qq);const G=Gr({x0:0,x1:21,y0:Math.min(0,Sinf*0.5),y1:Math.max(Sinf,v.b1)*1.3,L:80,T:10,W:460,H:210});let g=G.grid(5,Math.max(1,Math.round(Sinf/4)));let s=0,sn=0;for(let k=1;k<=20;k++){s+=v.b1*Math.pow(qq,k-1);if(k===v.n)sn=s;g+=G.pt(k,s,k===v.n?COL.a:COL.b,k===v.n?8:4)}
 g+=G.seg(0,Sinf,21,Sinf,COL.c,2);return {svg:g,st:[fnum(sn,3),fnum(Sinf,3),fnum(Sinf-sn,4)],fb:U("Горизонтальная линия — предел суммы b₁/(1 − q) = "+fnum(Sinf,2)+".","The horizontal line is the limit of the sum b₁/(1 − q) = "+fnum(Sinf,2)+".")}''', '0 0 600 250')

m3 = M(('Сложные проценты', 'Compound interest'),
 [('r', 'P', 'Вклад, сомов', 'Deposit, som', 1000, 50000, 1000, 10000), ('r', 'p', 'Годовая ставка, % (условная)', 'Annual rate, % (illustrative)', 1, 20, 1, 8), ('r', 'y', 'Лет', 'Years', 1, 30, 1, 15)],
 [('Простые проценты', 'Simple interest'), ('Сложные проценты', 'Compound interest'), ('Разница', 'The difference')],
 'При сложных процентах проценты начисляются и на проценты: сумма растёт как геометрическая прогрессия со знаменателем 1 + p/100.', 'With compound interest interest is paid on interest too: the sum grows as a geometric progression with ratio 1 + p/100.', ('Рост вклада: простые и сложные проценты', 'Growth of a deposit: simple and compound interest'),
 r'''const r=v.p/100,sim=t=>v.P*(1+r*t),com=t=>v.P*Math.pow(1+r,t),mx=Math.max(com(v.y),sim(v.y));const G=Gr({x0:0,x1:v.y,y0:0,y1:mx*1.1,L:90,T:10,W:450,H:210});let g=G.grid(Math.max(1,Math.round(v.y/6)),Math.round(mx/4/1000)*1000||1000)+G.fn(sim,COL.b,3,0,v.y)+G.fn(com,COL.a,3.5,0,v.y);
 return {svg:g,st:[Math.round(sim(v.y)).toLocaleString("ru"),Math.round(com(v.y)).toLocaleString("ru"),"+"+Math.round(com(v.y)-sim(v.y)).toLocaleString("ru")],fb:U("Ставка условная, это не прогноз и не совет по вложениям. Чем дольше срок, тем сильнее разница.","The rate is illustrative, not a forecast or investment advice. The longer the term, the bigger the difference.")}''', '0 0 600 250')

chapter('48', '48-geometric-progression.html', 'VI', ('Геометрическая прогрессия', 'Geometric progression'),
 ('Прогрессия, где члены умножаются на одно и то же число: быстрый рост, убывание и сложные проценты.', 'A progression where terms are multiplied by the same number: fast growth, decay and compound interest.'),
 ('Лист бумаги толщиной 0,1 мм складывают пополам снова и снова.\n\nКакой будет толщина после 30 сложений, если бы это было возможно?', 'A sheet of paper 0.1 mm thick is folded in half again and again.\n\nHow thick would it be after 30 folds, if that were possible?'),
 ('Разгадка: около 107 км', 'The answer: about 107 km'),
 ('Толщина удваивается при каждом сложении: bₙ = 0,1 · 2ⁿ мм. После 30 сложений: 0,1 · 2³⁰ ≈ 0,1 · 1,07 · 10⁹ мм ≈ 107 000 000 мм = 107 км. Это больше высоты любой горы. На деле больше 7–12 сложений листа сделать нельзя, но расчёт показывает, как стремительно растёт геометрическая прогрессия.', 'The thickness doubles with each fold: bₙ = 0.1 · 2ⁿ mm. After 30 folds: 0.1 · 2³⁰ ≈ 0.1 · 1.07 · 10⁹ mm ≈ 107,000,000 mm = 107 km. That is higher than any mountain. In practice a sheet can be folded only 7–12 times but the calculation shows how fast a geometric progression grows.'),
 [S('def', 'Определение и формула члена', 'Definition and the nth term', ('<strong>Геометрическая прогрессия</strong> — последовательность, где каждый член равен предыдущему, умноженному на постоянное число <strong>q ≠ 0</strong> (знаменатель): bₙ = b₁ · qⁿ⁻¹. При q &gt; 1 члены растут, при 0 &lt; q &lt; 1 убывают, при q &lt; 0 знаки чередуются. Квадрат среднего члена равен произведению соседних: bₙ² = bₙ₋₁ · bₙ₊₁.', 'A <strong>geometric progression</strong> is a sequence where each term equals the previous one multiplied by a constant number <strong>q ≠ 0</strong> (the common ratio): bₙ = b₁ · qⁿ⁻¹. For q &gt; 1 the terms grow, for 0 &lt; q &lt; 1 they decrease, for q &lt; 0 the signs alternate. The square of a middle term equals the product of its neighbours: bₙ² = bₙ₋₁ · bₙ₊₁.'),
    ('bₙ = b₁ · qⁿ⁻¹', '', 'bₙ = b₁ · qⁿ⁻¹'), m1),
  S('sum', 'Сумма членов', 'The sum of terms', ('Сумма первых n членов при q ≠ 1: <strong>Sₙ = b₁(qⁿ − 1)/(q − 1)</strong>. Если |q| &lt; 1, сумма бесконечного числа членов существует и равна <strong>S = b₁/(1 − q)</strong>. Например, 1 + ½ + ¼ + … = 2.', 'The sum of the first n terms for q ≠ 1: <strong>Sₙ = b₁(qⁿ − 1)/(q − 1)</strong>. If |q| &lt; 1, the sum of infinitely many terms exists and equals <strong>S = b₁/(1 − q)</strong>. For example 1 + ½ + ¼ + … = 2.'),
    ('S = b₁/(1 − q),  |q| < 1', '', 'S = b₁/(1 − q),  |q| < 1'), m2),
  S('comp', 'Сложные проценты', 'Compound interest', ('Если сумма P растёт на p % в год и проценты присоединяются, то через t лет она равна <strong>P · (1 + p/100)ᵗ</strong> — геометрическая прогрессия. Простые проценты дают арифметическую прогрессию P(1 + pt/100). Сложные проценты со временем обгоняют простые.', 'If a sum P grows by p% a year and the interest is added, then after t years it equals <strong>P · (1 + p/100)ᵗ</strong> — a geometric progression. Simple interest gives an arithmetic progression P(1 + pt/100). Compound interest outpaces simple interest in time.'),
    ('A = P(1 + p/100)ᵗ', '', 'A = P(1 + p/100)ᵗ'), m3)],
 [TK(('Член', 'A term'), ('b₁ = 3, q = 2. Найдите b₅.', 'b₁ = 3, q = 2. Find b₅.'), '3 · 2⁴', '3 · 16 = 48.', '48.'),
  TK(('Знаменатель', 'Ratio'), ('Прогрессия 2, 6, 18, … Найдите q и b₅.', 'The progression 2, 6, 18, … Find q and b₅.'), 'q = 6 : 2', 'q = 3, b₅ = 2 · 3⁴ = 162.', ('q = 3; b₅ = 162.', 'q = 3; b₅ = 162.')),
  TK(('Сумма', 'Sum'), ('Найдите 1 + 2 + 4 + 8 + 16.', 'Find 1 + 2 + 4 + 8 + 16.'), 'b₁ = 1, q = 2, n = 5', '(2⁵ − 1)/(2 − 1) = 31.', '31.'),
  TK(('Бесконечная сумма', 'Infinite sum'), ('Найдите 6 + 3 + 1,5 + …', 'Find 6 + 3 + 1.5 + …'), 'q = 1/2', 'S = 6/(1 − 0,5) = 12.', '12.'),
  TK(('Проценты', 'Interest'), ('1 000 сомов растут на 10 % в год (условно). Сколько будет через 2 года?', '1,000 som grows by 10% a year (illustrative). How much after 2 years?'), '1000 · 1,1²', '1000 · 1,21 = 1 210.', ('1 210 сомов.', '1,210 som.'))],
 [Q('b₁ = 2, q = 3. b₃ =', 'b₁ = 2, q = 3. b₃ =', '18', '12', '8', ('2 · 3².', '2 · 3².')),
  Q('Знаменатель 5, 10, 20, …', 'The ratio of 5, 10, 20, …', '2', '5', '10', ('10 : 5.', '10 : 5.')),
  Q('Сумма 1 + 2 + 4 + 8', 'The sum 1 + 2 + 4 + 8', '15', '14', '16', ('(2⁴ − 1).', '(2⁴ − 1).')),
  Q('1 + ½ + ¼ + … =', '1 + ½ + ¼ + … =', '2', '1', '∞', ('1/(1 − ½).', '1/(1 − ½).')),
  Q('Если q = −1, члены', 'If q = −1 the terms', ('чередуют знак', 'alternate in sign'), ('растут', 'grow'), ('убывают', 'decrease'), ('Умножение на −1.', 'Multiplying by −1.')),
  Q('Геометрическая прогрессия задаётся умножением на', 'A geometric progression is built by multiplying by', ('постоянное число', 'a constant number'), ('номер члена', 'the term number'), ('разность', 'a difference'), ('Знаменатель.', 'The ratio.')),
  Q('Что быстрее растёт при больших n?', 'What grows faster for large n?', ('2ⁿ', '2ⁿ'), ('2n', '2n'), ('n + 2', 'n + 2'), ('Показательный рост.', 'Exponential growth.')),
  Q('Сложные проценты — это', 'Compound interest is', ('проценты на проценты', 'interest on interest'), ('проценты только на начальную сумму', 'interest only on the initial sum'), ('налог', 'a tax'), ('Определение.', 'The definition.'))],
 src=[('Wikipedia: Geometric progression', 'https://en.wikipedia.org/wiki/Geometric_progression'), ('Wikipedia: Compound interest', 'https://en.wikipedia.org/wiki/Compound_interest')],
 note=('Ставка в примерах условная; это не финансовый совет.', 'The rate in the examples is illustrative; it is not financial advice.'))
