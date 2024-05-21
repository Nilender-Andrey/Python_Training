"""
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Пример:
a b c d

Результат:
[['a'], ['b'], ['c'], ['d']]
"""

# Решение:

list_str = input().split()
result = []

for c in list_str:
    if result and c in result[-1]:
        result[-1].append(c)
    else:
        result.append([c])

print(result)


""" Интересное решение

from itertools import groupby # Группирует элементы по значению. 

s = input().split()
print(list(list(seq) for sym, seq in groupby(s)))
"""
