# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Степень как повторное умножение', 'A power as repeated multiplication'),
 [('r', 'a', 'Основание', 'Base', 2, 9, 1, 2), ('r', 'n', 'Показатель', 'Exponent', 1, 10, 1, 5)],
 [('Запись', 'Notation'), ('Произведение', 'Product'), ('Значение', 'Value')],
 'aⁿ — произведение n множителей, равных a. Степень растёт очень быстро.', 'aⁿ is a product of n factors equal to a. Powers grow very fast.', ('Степень растёт', 'A power grows'),
 r'''const val=Math.pow(v.a,v.n);let g="";for(let i=0;i<v.n;i++)g+=R(30+i*54,50,48,48,[COL.a,COL.b,COL.c][i%3],COL.ink,1.5,6)+TX(54+i*54,82,v.a,"#fff",20,"middle",700);
 g+=TX(300,160,v.a+supn(v.n)+" = "+val.toLocaleString("ru"),COL.ink,26,"middle",700);
 return {svg:g,st:[v.a+supn(v.n),Array(v.n).fill(v.a).join(" · "),val.toLocaleString("ru")],fb:U("Любое число в нулевой степени равно 1: a⁰ = 1.","Any number to the power zero is 1: a⁰ = 1.")}''', '0 0 600 190')

m2 = M(('Свойства степеней', 'Properties of powers'),
 [('r', 'a', 'Основание', 'Base', 2, 5, 1, 2), ('r', 'm', 'Показатель m', 'Exponent m', 1, 6, 1, 3), ('r', 'n', 'Показатель n', 'Exponent n', 1, 6, 1, 2)],
 [('aᵐ · aⁿ', 'aᵐ · aⁿ'), ('aᵐ : aⁿ (m ≥ n)', 'aᵐ : aⁿ (m ≥ n)'), ('(aᵐ)ⁿ', '(aᵐ)ⁿ')],
 'При умножении показатели складываются, при делении вычитаются, при возведении степени в степень — умножаются.', 'When multiplying the exponents add, when dividing they subtract, when raising a power to a power they multiply.', ('Свойства в числах', 'The properties in numbers'),
 r'''const a=v.a,m=v.m,n=v.n;const rows=[[a+supn(m)+" · "+a+supn(n)+" = "+a+supn(m+n),Math.pow(a,m+n)],[a+supn(m)+" : "+a+supn(n)+" = "+(m>=n?a+supn(m-n):"—"),m>=n?Math.pow(a,m-n):"—"],["("+a+supn(m)+")"+supn(n)+" = "+a+supn(m*n),Math.pow(a,m*n)]];let g="";
 rows.forEach((r,i)=>{g+=R(30,15+i*60,540,50,COL.bg,COL.line,1.5,6)+TX(50,47+i*60,r[0],COL.ink,19,"start",600)+TX(560,47+i*60,r[1],COL.a,19,"end",700)});
 return {svg:g,st:[Math.pow(a,m+n),m>=n?Math.pow(a,m-n):"—",Math.pow(a,m*n)],fb:U("Проверьте числом: "+a+supn(m)+" = "+Math.pow(a,m)+", "+a+supn(n)+" = "+Math.pow(a,n)+".",a+supn(m)+" = "+Math.pow(a,m)+", "+a+supn(n)+" = "+Math.pow(a,n)+".")}''', '0 0 600 200')

m3 = M(('Стандартный вид числа', 'Scientific notation'),
 [('r', 'e', 'Порядок (степень 10)', 'Order (power of 10)', -6, 9, 1, 3), ('r', 'm', 'Мантисса × 10', 'Mantissa × 10', 10, 99, 1, 15)],
 [('Число', 'Number'), ('В стандартном виде', 'In scientific notation'), ('Примеры в мире', 'A real-world scale')],
 'Любое число записывают как m · 10ⁿ, где 1 ≤ m < 10. Так удобно записывать очень большие и очень малые числа.', 'Any number can be written as m · 10ⁿ where 1 ≤ m < 10. This is handy for very large and very small numbers.', ('Масштаб чисел', 'The scale of numbers'),
 r'''const mm=v.m/10,x=mm*Math.pow(10,v.e); let g="";const X=t=>40+(t+6)/15*520;g+=L(40,110,560,110,COL.ink,3);for(let t=-6;t<=9;t+=3)g+=L(X(t),104,X(t),116,COL.ink,2)+TX(X(t),138,"10"+(t<0?"⁻":"")+supn(Math.abs(t)),COL.mut,13);
 g+=C(X(v.e+Math.log10(mm)),110,9,COL.a)+TX(300,60,fnum(mm,1)+" · 10"+(v.e<0?"⁻":"")+supn(Math.abs(v.e)),COL.a,28,"middle",700);
 return {svg:g,st:[x>=1e7||x<1e-3?x.toExponential(2):fnum(x,Math.max(0,-v.e+1)),fnum(mm,1)+" · 10"+(v.e<0?"⁻":"")+supn(Math.abs(v.e)),v.e<=-3?U("мельче миллиметра","smaller than a millimetre"):v.e<=0?U("доли метра","fractions of a metre"):v.e<=3?U("до километров","up to kilometres"):U("гигантские расстояния","enormous distances")],fb:U("Показатель 10 показывает, на сколько знаков сдвинута запятая.","The exponent of 10 shows how many places the point is shifted.")}''', '0 0 600 160')

chapter('26', '26-powers-monomials.html', 'IV', ('Степени и одночлены', 'Powers and monomials'),
 ('Что такое степень числа, как умножать и делить степени и как записывать очень большие и малые числа.', 'What a power of a number is, how to multiply and divide powers and how to write very large and very small numbers.'),
 ('Легенда о шахматах: изобретателю предложили награду, и он попросил на первой клетке доски одно зерно, на второй — два, на третьей — четыре и так далее, удваивая на каждой из 64 клеток.\n\nСколько зёрен будет на 11-й клетке? Много ли это?', 'The chess legend: an inventor was offered a reward and asked for one grain on the first square of the board, two on the second, four on the third and so on, doubling on each of the 64 squares.\n\nHow many grains will be on the 11th square? Is that a lot?'),
 ('Разгадка: 1 024 зерна', 'The answer: 1,024 grains'),
 ('На n-й клетке зёрен 2ⁿ⁻¹. На 11-й: 2¹⁰ = 1 024. Звучит скромно, но на 64-й клетке уже 2⁶³ ≈ 9 · 10¹⁸ зёрен, а всего на доске — около 1,8 · 10¹⁹. Это больше, чем можно собрать за всю историю земледелия. Степени растут стремительно.', 'On the nth square there are 2ⁿ⁻¹ grains. On the 11th: 2¹⁰ = 1,024. Sounds modest, but on the 64th square there are already 2⁶³ ≈ 9 · 10¹⁸ grains, and on the whole board about 1.8 · 10¹⁹. That is more than could be gathered in the whole history of farming. Powers grow fast.'),
 [S('def', 'Что такое степень', 'What a power is', ('<strong>Степень</strong> aⁿ — произведение n множителей, равных a: 2⁵ = 2 · 2 · 2 · 2 · 2 = 32. Число a — основание, n — показатель. Особые случаи: a¹ = a, a⁰ = 1 (при a ≠ 0). Чётная степень отрицательного числа положительна: (−2)⁴ = 16, нечётная — отрицательна: (−2)³ = −8.', 'A <strong>power</strong> aⁿ is a product of n factors equal to a: 2⁵ = 2 · 2 · 2 · 2 · 2 = 32. The number a is the base, n the exponent. Special cases: a¹ = a, a⁰ = 1 (for a ≠ 0). An even power of a negative number is positive: (−2)⁴ = 16, an odd one is negative: (−2)³ = −8.'),
    ('aⁿ = a · a · … · a  (n раз)', '', 'aⁿ = a · a · … · a  (n times)'), m1),
  S('rules', 'Свойства степеней', 'Properties of powers', ('aᵐ · aⁿ = aᵐ⁺ⁿ; aᵐ : aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ; (ab)ⁿ = aⁿbⁿ. Почему так: aᵐ · aⁿ — это m + n множителей a подряд. <strong>Одночлен</strong> — произведение чисел и букв в степенях, например 3x²y. При умножении одночленов коэффициенты умножают, а степени одинаковых букв складывают.', 'aᵐ · aⁿ = aᵐ⁺ⁿ; aᵐ : aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ; (ab)ⁿ = aⁿbⁿ. Why: aᵐ · aⁿ is m + n factors a in a row. A <strong>monomial</strong> is a product of numbers and letters to powers, for example 3x²y. When multiplying monomials we multiply coefficients and add the exponents of equal letters.'),
    ('aᵐ · aⁿ = aᵐ⁺ⁿ', '(3x²)(2x³) = 6x⁵', '(3x²)(2x³) = 6x⁵'), m2),
  S('sci', 'Стандартный вид числа', 'Scientific notation', ('Числа записывают в виде m · 10ⁿ, где 1 ≤ m &lt; 10, n — целое. Например, 3 000 000 = 3 · 10⁶, а 0,00025 = 2,5 · 10⁻⁴. Расстояние от Земли до Солнца ≈ 1,5 · 10¹¹ м, диаметр атома — порядка 10⁻¹⁰ м.', 'Numbers are written as m · 10ⁿ with 1 ≤ m &lt; 10 and integer n. For example, 3,000,000 = 3 · 10⁶ and 0.00025 = 2.5 · 10⁻⁴. The distance from Earth to the Sun ≈ 1.5 · 10¹¹ m; an atom’s diameter is of the order of 10⁻¹⁰ m.'),
    ('m · 10ⁿ,  1 ≤ m < 10', '', 'm · 10ⁿ,  1 ≤ m < 10'), m3)],
 [TK(('Значение степени', 'Value of a power'), ('Найдите 3⁴ и (−2)³.', 'Find 3⁴ and (−2)³.'), '3 · 3 · 3 · 3', '3⁴ = 81. (−2)³ = −8.', '81; −8.'),
  TK(('Свойства', 'Properties'), ('Упростите 5³ · 5⁴ и 7⁸ : 7⁵.', 'Simplify 5³ · 5⁴ and 7⁸ : 7⁵.'), '', '5⁷ и 7³.', '5⁷; 7³.'),
  TK(('Степень степени', 'Power of a power'), ('Упростите (x²)³.', 'Simplify (x²)³.'), '', 'Показатели умножаем: x⁶.', 'x⁶.'),
  TK(('Одночлен', 'A monomial'), ('Умножьте 4a²b на 3ab³.', 'Multiply 4a²b by 3ab³.'), '', '12 · a³ · b⁴ = 12a³b⁴.', '12a³b⁴.'),
  TK(('Стандартный вид', 'Scientific notation'), ('Запишите 45 000 000 и 0,0032 в стандартном виде.', 'Write 45,000,000 and 0.0032 in scientific notation.'), '', '4,5 · 10⁷ и 3,2 · 10⁻³.', '4,5 · 10⁷; 3,2 · 10⁻³.')],
 [Q('2⁵ =', '2⁵ =', '32', '10', '25', ('2 · 2 · 2 · 2 · 2.', '2 · 2 · 2 · 2 · 2.')),
  Q('a⁰ (a ≠ 0) =', 'a⁰ (a ≠ 0) =', '1', '0', 'a', ('По определению.', 'By definition.')),
  Q('x³ · x⁴ =', 'x³ · x⁴ =', 'x⁷', 'x¹²', '2x⁷', ('Показатели складываем.', 'The exponents add.')),
  Q('(x²)⁵ =', '(x²)⁵ =', 'x¹⁰', 'x⁷', 'x²⁵', ('Показатели умножаем.', 'The exponents multiply.')),
  Q('(−3)² =', '(−3)² =', '9', '−9', '6', ('Минус на минус — плюс.', 'Minus times minus — plus.')),
  Q('−3² =', '−3² =', '−9', '9', '−6', ('Минус стоит перед степенью.', 'The minus is outside the power.')),
  Q('Число 6 000 в стандартном виде', 'The number 6,000 in scientific notation', '6 · 10³', '60 · 10²', '0,6 · 10⁴', ('1 ≤ m &lt; 10.', '1 ≤ m &lt; 10.')),
  Q('0,0007 =', '0.0007 =', '7 · 10⁻⁴', '7 · 10⁴', '7 · 10⁻³', ('Запятая сдвинута на 4 знака влево.', 'The point shifted 4 places left.'))],
 src=[('Wikipedia: Exponentiation', 'https://en.wikipedia.org/wiki/Exponentiation'), ('Wikipedia: Scientific notation', 'https://en.wikipedia.org/wiki/Scientific_notation'), ('Wikipedia: Wheat and chessboard problem', 'https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem')])
