# -*- coding: utf-8 -*-
"""Реестр глав и блоков математики. Дополняется при добавлении новых глав."""
BLOCKS = [
 dict(id='I', ru='Числа и счёт', en='Numbers and counting',
      note_ru='Начальная школа: язык проще, больше интерактива. Темы, а не классы: учитель сам выбирает, когда давать тему по программе. Уровень — основы.',
      note_en='Primary school: simpler language, more interactivity. Organised by topic, not by grade: teachers choose when to use each topic. Level — basics.'),

 dict(id='II', ru='Фигуры, величины и данные', en='Shapes, quantities and data',
      note_ru='Начальная и средняя школа: фигуры, измерения, периметр и площадь, симметрия, диаграммы и закономерности. Темы, а не классы. Уровень — основы.',
      note_en='Primary and middle school: shapes, measurement, perimeter and area, symmetry, charts and patterns. Organised by topic, not by grade. Level — basics.'),
]
# n, slug, ru, en, descRu, descEn, block
CHAPTERS = [
 ('01', '01-numbers-to-20.html', 'Числа до 20: счёт и состав числа', 'Numbers to 20: counting and parts of a number',
  'Счёт до 20, десяток и единицы, состав числа, сравнение на числовом луче.', 'Counting to 20, tens and ones, parts of a number, comparing on the number line.', 'I'),
 ('02', '02-add-subtract.html', 'Сложение и вычитание', 'Addition and subtraction',
  'Прыжки по лучу, переход через десяток, связь сложения и вычитания.', 'Jumps on the line, crossing the ten, addition and subtraction as a family.', 'I'),
 ('03', '03-place-value.html', 'Разряды и числа до 1000', 'Place value and numbers to 1000',
  'Сотни, десятки, единицы; сравнение трёхзначных чисел; округление.', 'Hundreds, tens, ones; comparing three-digit numbers; rounding.', 'I'),
 ('04', '04-multiply-divide.html', 'Умножение и деление', 'Multiplication and division',
  'Умножение как сложение одинаковых, деление с остатком, таблица умножения.', 'Multiplication as repeated addition, division with remainder, the multiplication table.', 'I'),
 ('05', '05-column-arithmetic.html', 'Действия в столбик', 'Column arithmetic',
  'Сложение, вычитание и умножение многозначных чисел, перенос и заём, прикидка.', 'Adding, subtracting and multiplying big numbers, carrying and borrowing, estimating.', 'I'),
 ('06', '06-order-of-operations.html', 'Порядок действий и скобки', 'Order of operations and brackets',
  'Почему 2 + 2 · 2 = 6, скобки, вычисление по шагам, подбор знаков.', 'Why 2 + 2 · 2 = 6, brackets, step-by-step evaluation, finding signs.', 'I'),
 ('07', '07-word-problems.html', 'Текстовые задачи', 'Word problems',
  'Схемы из отрезков, «на сколько» и «во сколько раз», покупка и сдача в сомах.', 'Bar diagrams, “by how much” and “how many times”, shopping and change in soms.', 'I'),
 ('08', '08-fractions-intro.html', 'Доли и дроби', 'Parts and fractions',
  'Числитель и знаменатель, сравнение долей, доля от числа, равные дроби.', 'Numerator and denominator, comparing fractions, a fraction of a number, equal fractions.', 'I'),
 ('09', '09-points-lines-angles.html', 'Точки, линии, углы, фигуры', 'Points, lines, angles, shapes',
  'Отрезок, луч, прямая; виды углов; многоугольники.', 'Segment, ray, line; kinds of angles; polygons.', 'II'),
 ('10', '10-quantities.html', 'Длина, масса, время, деньги', 'Length, mass, time, money',
  'Единицы длины, часы и минуты, деньги в сомах.', 'Units of length, hours and minutes, money in soms.', 'II'),
 ('11', '11-perimeter-area.html', 'Периметр и площадь прямоугольника', 'Perimeter and area of a rectangle',
  'Забор и грядка, площадь в клетках, наибольшая площадь при данном периметре.', 'A fence and a bed, area in squares, the greatest area for a given perimeter.', 'II'),
 ('12', '12-symmetry.html', 'Симметрия и орнамент', 'Symmetry and ornament',
  'Осевая симметрия, оси правильных многоугольников, узоры с поворотами.', 'Mirror symmetry, axes of regular polygons, rotational patterns.', 'II'),
 ('13', '13-data-charts.html', 'Таблицы и диаграммы', 'Tables and charts',
  'Столбчатая диаграмма, как читать график, обрезанная ось.', 'A bar chart, reading a graph, the truncated axis.', 'II'),
 ('14', '14-patterns-logic.html', 'Закономерности и логика', 'Patterns and logic',
  'Числовые последовательности, формулы закономерностей, круги Эйлера.', 'Number sequences, pattern formulas, Venn diagrams.', 'II'),
]
