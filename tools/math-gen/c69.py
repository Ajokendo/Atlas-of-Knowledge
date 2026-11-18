# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Принцип умножения: дерево выбора', 'The multiplication principle: a choice tree'),
 [('r', 'a', 'Основных блюд', 'Main dishes', 1, 5, 1, 3), ('r', 'b', 'Напитков', 'Drinks', 1, 4, 1, 2), ('r', 'c', 'Десертов', 'Desserts', 1, 4, 1, 2)],
 [('Обедов из блюда и напитка', 'Lunches of dish and drink'), ('Обедов из трёх частей', 'Lunches of three parts'), ('Формула', 'Formula')],
 'Если первый выбор можно сделать a способами, а после него второй — b способами, то пар a·b. Каждая ветвь дерева — один вариант.', 'If the first choice can be made in a ways and after it the second in b ways then there are a·b pairs. Each branch of the tree is one option.', ('Дерево вариантов (блюдо → напиток)', 'The tree of options (dish → drink)'),
 r'''let g=C(60,130,6,COL.ink);const dy=Math.min(40,210/(v.a*v.b)*1.0);let k=0;const tot=v.a*v.b,H=Math.min(210,tot*26);for(let i=0;i<v.a;i++){const y1=20+(i+0.5)*H/v.a;g+=L(60,130,260,y1,COL.a,2)+C(260,y1,5,COL.a)+TX(240,y1-9,U("блюдо ","dish ")+(i+1),COL.a,11,"middle");for(let j=0;j<v.b;j++){const y2=20+(k+0.5)*H/tot;k++;g+=L(260,y1,420,y2,COL.b,1.5)+C(420,y2,3.5,COL.b)}}
 g+=TX(520,135,U("вариантов: ","options: ")+tot,COL.ink,14,"middle",700);
 return {svg:g,st:[tot,tot*v.c,v.a+"·"+v.b+"·"+v.c+" = "+tot*v.c],fb:U("Каждый новый выбор умножает число вариантов.","Each new choice multiplies the number of options.")}''', '0 0 600 250')

m2 = M(('Правило суммы и пересечение', 'The sum rule and overlap'),
 [('r', 'm', 'В кружке математики', 'In the maths club', 5, 30, 1, 18), ('r', 'c', 'В шахматном кружке', 'In the chess club', 5, 30, 1, 14), ('r', 'b', 'В обоих', 'In both', 0, 5, 1, 4)],
 [('Только математика', 'Only maths'), ('Только шахматы', 'Only chess'), ('Всего учеников', 'Total students')],
 'Если множества не пересекаются, общее число — сумма. Если пересекаются, пересечение считается дважды: |A ∪ B| = |A| + |B| − |A ∩ B|.', 'If sets do not overlap the total is the sum. If they overlap the intersection is counted twice: |A ∪ B| = |A| + |B| − |A ∩ B|.', ('Диаграмма Венна', 'A Venn diagram'),
 r'''const b=Math.min(v.b,v.m,v.c);let g=C(230,110,90,COL.a+"44",COL.a,3)+C(340,110,90,COL.b+"44",COL.b,3)+TX(190,115,String(v.m-b),COL.ink,22,"middle",700)+TX(385,115,String(v.c-b),COL.ink,22,"middle",700)+TX(285,115,String(b),COL.ink,22,"middle",700)+TX(200,30,U("математика","maths"),COL.a,13,"middle",700)+TX(370,30,U("шахматы","chess"),COL.b,13,"middle",700);
 return {svg:g,st:[v.m-b,v.c-b,(v.m+v.c-b)],fb:U("Складывая "+v.m+" и "+v.c+", мы дважды посчитали учеников из обоих кружков — вычтите пересечение.","Adding the two club sizes counts those in both twice — subtract the overlap.")}''', '0 0 600 230')

m3 = M(('Сколько кодов', 'How many codes'),
 [('r', 'n', 'Позиций в коде', 'Positions in the code', 2, 8, 1, 4), ('r', 'd', 'Символов на позицию', 'Symbols per position', 2, 36, 1, 10), ('s', 'rep', 'Повторы', 'Repeats', ['разрешены', 'запрещены'], ['allowed', 'not allowed'], 0)],
 [('Число кодов', 'Number of codes'), ('Перебор по 1 коду/с', 'Trying 1 code/s'), ('Формула', 'Formula')],
 'С повторами n позиций с d символами дают dⁿ кодов; без повторов — d·(d−1)·…·(d−n+1). Каждая лишняя позиция умножает число кодов.', 'With repeats n positions of d symbols give dⁿ codes; without repeats d·(d−1)·…·(d−n+1). Each extra position multiplies the number of codes.', ('Рост числа кодов с длиной', 'Growth of the number of codes with length'),
 r'''const cnt=m=>{let r=1;for(let i=0;i<m;i++)r*=v.rep===0?v.d:Math.max(0,v.d-i);return r};const tot=cnt(v.n);let g=L(50,200,560,200,COL.ink,2);const mx=cnt(8),lg=x=>Math.log10(Math.max(1,x));for(let i=1;i<=8;i++){const h=170*lg(cnt(i))/Math.max(1,lg(mx)),x=60+(i-1)*62;g+=R(x,200-h,44,h,i===v.n?COL.b:COL.a,COL.ink,1,2)+TX(x+22,218,String(i),COL.ink,12)}g+=TX(300,18,U("высота ∝ log (число кодов)","height ∝ log (number of codes)"),COL.mut,11);
 const sec=tot,tm=sec<60?fnum(sec,0)+U(" с"," s"):sec<3600?fnum(sec/60,1)+U(" мин"," min"):sec<86400?fnum(sec/3600,1)+U(" ч"," h"):sec<86400*365?fnum(sec/86400,1)+U(" сут"," days"):fnum(sec/86400/365,1)+U(" лет"," years");
 return {svg:g,st:[tot.toLocaleString("ru-RU"),tm,v.rep===0?v.d+"^"+v.n:U("произведение убывающих","product of decreasing numbers")],fb:U("Условная оценка: реальные системы защищены иначе; важно лишь, как быстро растёт число вариантов.","An illustrative estimate: real systems are protected differently; the point is how fast the number of options grows.")}''', '0 0 600 230')

chapter('69', '69-counting-rules.html', 'X', ('Правила суммы и произведения', 'The sum and product rules'),
 ('Как пересчитать варианты, не перебирая их все: дерево выбора, умножение, сложение, пересечение множеств.', 'How to count options without listing them all: the choice tree, multiplication, addition, overlapping sets.'),
 ('В столовой на обед можно выбрать одно из 3 первых блюд, одно из 4 вторых и один из 2 напитков. Сколько разных обедов можно составить?', 'In a canteen you can choose one of 3 first courses, one of 4 main courses and one of 2 drinks. How many different lunches are possible?'),
 ('Разгадка: 24 обеда', 'The answer: 24 lunches'),
 ('К каждому из 3 первых блюд подходит любое из 4 вторых — это 3 · 4 = 12 пар; к каждой пары любой из 2 напитков — 12 · 2 = 24 обеда. Такой подсчёт называют принципом (правилом) умножения. Его удобно представлять деревом: каждая ветвь — один вариант. (Меню придумано для задачи.)', 'Each of the 3 first courses goes with any of the 4 main courses — 3 · 4 = 12 pairs; with each pair any of 2 drinks — 12 · 2 = 24 lunches. This counting is called the multiplication principle. It is handy to picture it as a tree: each branch is one option. (The menu is invented for the exercise.)'),
 [S('mul', 'Правило произведения', 'The product rule', ('Если выбор состоит из последовательных шагов, и на первом шаге n₁ способов, на втором n₂ (при любом первом) и т. д., то всего <strong>n₁ · n₂ · … · nₖ</strong> способов. Пример: код из 4 цифр — 10⁴ = 10 000 вариантов (с повторами).', 'If a choice consists of successive steps with n₁ ways on the first, n₂ on the second (for any first), and so on, there are <strong>n₁ · n₂ · … · nₖ</strong> ways in total. Example: a 4-digit code — 10⁴ = 10,000 options (with repeats).'),
    ('n₁ · n₂ · … · nₖ', '', 'n₁ · n₂ · … · nₖ'), m1),
  S('sum', 'Правило суммы', 'The sum rule', ('Если объект можно выбрать либо из одного набора (n способов), либо из другого (m способов), и наборы не пересекаются, то всего n + m. При пересечении: <strong>|A ∪ B| = |A| + |B| − |A ∩ B|</strong> — общие элементы нужно вычесть, чтобы не считать дважды.', 'If an object can be chosen either from one set (n ways) or from another (m ways) and the sets do not overlap then there are n + m in total. With overlap: <strong>|A ∪ B| = |A| + |B| − |A ∩ B|</strong> — common elements are subtracted so as not to count twice.'),
    ('|A ∪ B| = |A| + |B| − |A ∩ B|', '', '|A ∪ B| = |A| + |B| − |A ∩ B|'), m2),
  S('code', 'Рост числа вариантов', 'Growth of options', ('Число вариантов растёт очень быстро: пароль из 8 символов-цифр — 10⁸ (100 млн), из 8 букв и цифр (36 символов) — около 2,8 · 10¹². Поэтому длина пароля важнее хитрости. Без повторов: d · (d−1) · … · (d−n+1).', 'The number of options grows very fast: an 8-digit password — 10⁸ (100 million), 8 letters and digits (36 symbols) — about 2.8 · 10¹². So length matters more than cleverness. Without repeats: d · (d−1) · … · (d−n+1).'),
    ('dⁿ', '', 'dⁿ'), m3)],
 [TK(('Обед', 'Lunch'), ('3 первых, 4 вторых, 2 напитка. Сколько обедов?', '3 first courses, 4 mains, 2 drinks. How many lunches?'), '', '3 · 4 · 2 = 24.', '24.'),
  TK(('Код', 'Code'), ('Сколько кодов из 3 цифр?', 'How many 3-digit codes?'), '', '10³ = 1000.', '1000.'),
  TK(('Без повторов', 'No repeats'), ('Сколько трёхзначных чисел из разных цифр 1–9?', 'How many 3-digit numbers of distinct digits 1–9?'), '', '9 · 8 · 7 = 504.', '504.'),
  TK(('Пересечение', 'Overlap'), ('В классе 12 играют в футбол, 9 — в волейбол, 5 — и там и там. Сколько всего играют?', 'In a class 12 play football, 9 volleyball, 5 both. How many play in total?'), '', '12 + 9 − 5 = 16.', '16.'),
  TK(('Дорога', 'Routes'), ('Из A в B 3 дороги, из B в C 2 дороги. Сколько путей A → C?', 'From A to B 3 roads, from B to C 2 roads. How many routes A → C?'), '', '3 · 2 = 6.', '6.')],
 [Q('Первых блюд 2, вторых 5. Вариантов обеда из двух блюд', 'First courses 2, mains 5. Lunch options from two dishes', '10', '7', '25', ('2 · 5.', '2 · 5.')),
  Q('Число 3-значных кодов из цифр', 'The number of 3-digit codes of digits', '1000', '30', '100', ('10³.', '10³.')),
  Q('Принцип умножения применяют, когда выбор', 'The multiplication principle is used when a choice is', ('состоит из шагов', 'made of steps'), ('делится на два набора', 'split into two sets'), ('случаен', 'random'), ('Шаг за шагом.', 'Step by step.')),
  Q('|A ∪ B| =', '|A ∪ B| =', '|A| + |B| − |A ∩ B|', '|A| + |B|', '|A| · |B|', ('Вычитаем пересечение.', 'Subtract the overlap.')),
  Q('Дорог A→B 4, B→C 3, путей A→C', 'Roads A→B 4, B→C 3, routes A→C', '12', '7', '1', ('4 · 3.', '4 · 3.')),
  Q('Пароль длиннее — вариантов', 'A longer password gives', ('больше', 'more options'), ('меньше', 'fewer options'), ('столько же', 'the same'), ('Каждая позиция умножает.', 'Each position multiplies.')),
  Q('Трёхзначных чисел из разных цифр 1–9', 'Three-digit numbers of distinct digits 1–9', '504', '729', '27', ('9·8·7.', '9·8·7.')),
  Q('Правило суммы без пересечения: 5 + 7 =', 'The sum rule without overlap: 5 + 7 =', '12', '35', '2', ('Складываем.', 'Add.'))],
 src=[('Wikipedia: Rule of product', 'https://en.wikipedia.org/wiki/Rule_of_product'), ('Wikipedia: Rule of sum', 'https://en.wikipedia.org/wiki/Rule_of_sum'), ('Wikipedia: Inclusion–exclusion principle', 'https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle'), ('OpenStax: Introductory Statistics 2e', 'https://openstax.org/details/books/introductory-statistics-2e')],
 note=('Меню и числа в задачах придуманы для атласа.', 'The menu and numbers in the exercises are invented for the atlas.'))
