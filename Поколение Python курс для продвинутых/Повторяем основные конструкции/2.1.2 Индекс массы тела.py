"""
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. 
ИМТ показывает весит человек больше или меньше нормы для своего роста. 
"""

weight, height = float(input()), float(input())

imt = weight / height**2

if imt < 18.5:
    print("Недостаточная масса")
elif imt > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")

# Интересные решения:
"""
1. Вычисляется индекс. 
2. В зависимости от результатов выражения [i < 18.5](приводится 0 или 1), получаем вариант из первого массива и добавляем его во второй.
3. В зависимости от результатов выражения [i > 25](приводится 0 или 1), получаем вариант из второго массива.
4. К результату приклеиваем общую часть

i = float(input()) / float(input()) ** 2
print([['Оптималь', 'Недостаточ'][i < 18.5], 'Избыточ'][i > 25] + 'ная масса')
"""

"""
1. Вычисляется индекс. 
2. Различные условия умножаются на строку которая должна выводиться если это условие True.
   При умножении bool приводится к 0 или 1, а умножение определяет сколько раз эта строка дублируется.
   т.е. если True, то 1 раз, если False, то 0. 
3. Выводим строку которая умножается на 1, остальные условия взаимоисключающие.

  imt = float(input()) / (float(input()) ** 2)
  print((imt < 18.5) * 'Недостаточная масса',  (18.5 <= imt <= 25)
        * 'Оптимальная масса', (imt > 25) * 'Избыточная масса')
"""

"""
1. Вычисляется индекс. 
2. Подготавливается кортеж с вариантами.
3. Вычисляем индекс кортежа.
   При математических действиях bool приводится к 0 или 1, в результате мы можем получить три варианта: 1, 0, -1.
   Что соответствует одному из результатов.
4. Добавляем слово 'масса'

imt = float(input())/float(input())**2
print(('Оптимальная', 'Избыточная', 'Недостаточная')
      [(imt > 25)-(imt < 18.5)], 'масса')
"""
