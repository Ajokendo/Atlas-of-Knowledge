# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Два кубика: сумма очков', 'Two dice: the sum'),
 [('r', 's', 'Сумма очков', 'The sum', 2, 12, 1, 7)],
 [('Благоприятных исходов', 'Favourable outcomes'), ('Всех исходов', 'All outcomes'), ('Вероятность P', 'Probability P')],
 'Классическая вероятность: P = m / n, где n — число равновозможных исходов, m — число благоприятных. У двух кубиков n = 36.', 'Classical probability: P = m / n where n is the number of equally likely outcomes and m the number of favourable ones. For two dice n = 36.', ('Таблица исходов 6 × 6', 'The 6 × 6 table of outcomes'),
 r'''let g="",m=0;for(let a=1;a<=6;a++)for(let b=1;b<=6;b++){const x=150+(b-1)*52,y=18+(a-1)*36,ok=a+b===v.s;if(ok)m++;g+=R(x,y,50,34,ok?COL.b:COL.bg,COL.mut,1,3)+TX(x+25,y+22,String(a+b),ok?COL.bg:COL.ink,15,"middle",ok?700:400)}
 g+=TX(120,120,U("кубик 1","die 1"),COL.mut,12,"end")+TX(300,246,U("кубик 2","die 2"),COL.mut,12,"middle");
 return {svg:g,st:[m,36,m+"/36 = "+fnum(m/36,3)+" ≈ "+fnum(m/36*100,1)+"%"],fb:v.s===7?U("Сумма 7 — самая вероятная: 6 способов из 36.","Sum 7 is the most likely: 6 ways out of 36."):U("Чем ближе сумма к 7, тем больше способов её получить.","The closer the sum is to 7, the more ways to get it.")}''', '0 0 600 255')

m2 = M(('Противоположное событие', 'The complementary event'),
 [('r', 'p', 'Вероятность успеха за попытку', 'Success probability per try', 0.05, 0.9, 0.05, 0.2), ('r', 'k', 'Число попыток k', 'Number of tries k', 1, 15, 1, 5)],
 [('P(ни одного успеха)', 'P(no success)'), ('P(хотя бы один успех)', 'P(at least one success)'), ('Сумма', 'The sum')],
 'Вероятности события и противоположного дают 1. Для «хотя бы один» проще найти «ни одного»: P = 1 − (1 − p)ᵏ.', 'The probabilities of an event and its opposite add to 1. For “at least one” it is easier to find “none”: P = 1 − (1 − p)ᵏ.', ('Как растёт шанс «хотя бы раз»', 'How the chance of “at least once” grows'),
 r'''const G=Gr({x0:0,x1:15,y0:0,y1:1.05,L:80,T:10,W:470,H:210});const f=n=>1-Math.pow(1-v.p,n);let g=G.grid(5,0.25)+G.fn(x=>1-Math.pow(1-v.p,x),COL.a,3.5,0,15)+G.pt(v.k,f(v.k),COL.b,8)+G.seg(0,1,15,1,COL.c,1.5,true);
 const none=Math.pow(1-v.p,v.k);
 return {svg:g,st:[fnum(none,4),fnum(1-none,4),fnum(none+1-none,2)],fb:U("Даже при малом шансе p многократные попытки делают успех почти неизбежным.","Even with a small chance p many tries make success almost certain.")}''', '0 0 600 250')

m3 = M(('Частота и вероятность', 'Frequency and probability'),
 [('r', 'p', 'Вероятность p', 'Probability p', 0.1, 0.9, 0.1, 0.5), ('r', 'n', 'Число испытаний n', 'Number of trials n', 10, 2000, 10, 200)],
 [('Частота успехов', 'Frequency of successes'), ('Вероятность p', 'Probability p'), ('Отличие', 'Difference')],
 'Частота события в серии испытаний при росте n всё ближе к вероятности (закон больших чисел). Последовательность «испытаний» — псевдослучайная, детерминированная, чтобы все видели одно и то же.', 'The frequency of an event in a series of trials gets closer to the probability as n grows (the law of large numbers). The sequence of “trials” is pseudo-random and deterministic so that everyone sees the same.', ('Частота в зависимости от n', 'Frequency against n'),
 r'''let s=12345;const rnd=()=>{s=(s+0x6D2B79F5)|0;let t=Math.imul(s^(s>>>15),1|s);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296};const N=2000,fr=[];let hits=0;for(let i=1;i<=N;i++){if(rnd()<v.p)hits++;fr.push(hits/i)}
 const G=Gr({x0:0,x1:N,y0:0,y1:1,L:80,T:10,W:470,H:210});let g=G.grid(500,0.25)+G.seg(0,v.p,N,v.p,COL.c,2,true);let pts=[];for(let i=1;i<=v.n;i+=Math.max(1,Math.floor(v.n/200)))pts.push([G.X(i),G.Y(fr[i-1])]);g+=pline(pts,COL.a,3)+G.pt(v.n,fr[v.n-1],COL.b,7);
 return {svg:g,st:[fnum(fr[v.n-1],4),fnum(v.p,2),fnum(Math.abs(fr[v.n-1]-v.p),4)],fb:U("После 10 испытаний частота «скачет», после 1000 — почти равна p, но совпадает с ней редко точно.","After 10 trials the frequency jumps around; after 1000 it is close to p but rarely exactly equal.")}''', '0 0 600 250')

chapter('71', '71-probability.html', 'X', ('Вероятность события', 'Probability of an event'),
 ('Равновозможные исходы, формула P = m/n, противоположные события и закон больших чисел.', 'Equally likely outcomes, the formula P = m/n, complementary events and the law of large numbers.'),
 ('В настольной игре нужно выбросить на двух кубиках сумму 7 или 12, чтобы выйти из «тюрьмы». Что выгоднее ждать?', 'In a board game you must roll a sum of 7 or 12 with two dice to get out of “jail”. Which one is better to wait for?'),
 ('Разгадка: 7 — в шесть раз вероятнее', 'The answer: 7 is six times as likely'),
 ('Всего 36 равновозможных пар. Сумма 7 получается шестью способами (1+6, 2+5, 3+4 и обратные), сумма 12 — единственным (6+6). Поэтому P(7) = 6/36 = 1/6, а P(12) = 1/36. Знание вероятностей помогает в играх, но не гарантирует результат в каждой отдельной партии.', 'There are 36 equally likely pairs. A sum of 7 arises in six ways (1+6, 2+5, 3+4 and the reverses), a sum of 12 in only one (6+6). So P(7) = 6/36 = 1/6 and P(12) = 1/36. Knowing probabilities helps in games but does not guarantee the result of any single round.'),
 [S('cl', 'Классическая вероятность', 'Classical probability', ('Если все n исходов опыта равновозможны, а событию благоприятны m из них, то <strong>P(A) = m / n</strong>. Всегда 0 ≤ P ≤ 1: 0 — невозможное, 1 — достоверное. Бросок монеты: P(орёл) = 1/2. Одна карта из 36: P(туз) = 4/36 = 1/9.', 'If all n outcomes of an experiment are equally likely and m of them favour the event then <strong>P(A) = m / n</strong>. Always 0 ≤ P ≤ 1: 0 — impossible, 1 — certain. Coin toss: P(heads) = 1/2. One card from 36: P(ace) = 4/36 = 1/9.'),
    ('P(A) = m / n', '', 'P(A) = m / n'), m1),
  S('opp', 'Противоположные и несовместные события', 'Complementary and mutually exclusive events', ('<strong>P(не A) = 1 − P(A)</strong>. Несовместные события не происходят вместе, поэтому P(A или B) = P(A) + P(B). Для «хотя бы один» удобно считать через противоположное: 1 − (вероятность «ни одного»).', '<strong>P(not A) = 1 − P(A)</strong>. Mutually exclusive events cannot occur together, so P(A or B) = P(A) + P(B). For “at least one” it is convenient to use the opposite: 1 − (the probability of “none”).'),
    ('P(не A) = 1 − P(A)', '', 'P(not A) = 1 − P(A)'), m2),
  S('freq', 'Частота и закон больших чисел', 'Frequency and the law of large numbers', ('Опыт можно повторять: <strong>частота</strong> = число успехов / число испытаний. При большом числе испытаний частота приближается к вероятности — так оценивают вероятность, когда исходы неравновозможны (бракованная деталь, дождливый день). Но на коротких сериях разброс велик.', 'An experiment can be repeated: the <strong>frequency</strong> = successes / trials. For many trials the frequency approaches the probability — this is how probability is estimated when outcomes are not equally likely (a faulty part, a rainy day). But short series vary a lot.'),
    ('частота → P при n → ∞', '', 'frequency → P as n → ∞'), m3)],
 [TK(('Кубик', 'A die'), ('Вероятность выпадения чётного числа на кубике?', 'The probability of rolling an even number on a die?'), '', '3/6 = 1/2.', '1/2.'),
  TK(('Сумма', 'The sum'), ('Вероятность суммы 5 на двух кубиках?', 'The probability of a sum of 5 on two dice?'), '1+4, 2+3, 3+2, 4+1', '4/36 = 1/9.', '1/9.'),
  TK(('Противоположное', 'Complement'), ('Вероятность дождя 0,3. Вероятность отсутствия дождя?', 'The probability of rain is 0.3. The probability of no rain?'), '', '1 − 0,3 = 0,7.', '0.7.'),
  TK(('Хотя бы раз', 'At least once'), ('Монету бросили 3 раза. Вероятность хотя бы одного орла?', 'A coin is tossed 3 times. The probability of at least one head?'), '', '1 − (1/2)³ = 7/8.', '7/8.'),
  TK(('Карты', 'Cards'), ('Из колоды 36 карт берут одну. Вероятность красной масти?', 'One card from a 36-card deck. The probability of a red suit?'), '', '18/36 = 1/2.', '1/2.')],
 [Q('P(A) = ', 'P(A) = ', ('m / n', 'm / n'), ('n / m', 'n / m'), ('m · n', 'm · n'), ('Благоприятные к всем.', 'Favourable to all.')),
  Q('Вероятность достоверного события', 'The probability of a certain event', '1', '0', '0,5', ('Всегда происходит.', 'Always happens.')),
  Q('P(не A) =', 'P(not A) =', '1 − P(A)', 'P(A) − 1', '−P(A)', ('Дополнение.', 'Complement.')),
  Q('Исходов у двух кубиков', 'Outcomes for two dice', '36', '12', '6', ('6 · 6.', '6 · 6.')),
  Q('Сумма 12 на двух кубиках: вероятность', 'A sum of 12 on two dice: probability', '1/36', '1/12', '1/6', ('Только 6+6.', 'Only 6+6.')),
  Q('Вероятность может быть', 'A probability can be', ('от 0 до 1', 'from 0 to 1'), ('от −1 до 1', 'from −1 to 1'), ('больше 1', 'greater than 1'), ('Определение.', 'Definition.')),
  Q('Закон больших чисел: частота при росте n', 'The law of large numbers: the frequency as n grows', ('приближается к P', 'approaches P'), ('равна P', 'equals P'), ('растёт', 'grows'), ('Приближается.', 'Approaches.')),
  Q('Монета, 2 броска, хотя бы один орёл', 'A coin, 2 tosses, at least one head', '3/4', '1/2', '1/4', ('1 − 1/4.', '1 − 1/4.'))],
 src=[('Wikipedia: Probability', 'https://en.wikipedia.org/wiki/Probability'), ('Wikipedia: Law of large numbers', 'https://en.wikipedia.org/wiki/Law_of_large_numbers'), ('OpenStax: Introductory Statistics 2e', 'https://openstax.org/details/books/introductory-statistics-2e')],
 note=('Сюжет с настольной игрой придуман; «испытания» в модели — псевдослучайные.', 'The board-game story is invented; the “trials” in the model are pseudo-random.'))
