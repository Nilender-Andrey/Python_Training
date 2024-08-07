""" 
На вход программе подается натуральное число n, n > 1. 
Напишите программу, которая выводит в порядке возрастания все несократимые дроби, 
заключённые между 0 и 1, знаменатель которых не превосходит n.

# Ввод:
5

# Вывод:
1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
"""

# Решение:
from fractions import Fraction as F

print(*sorted(list({F(j, i) for i in range(1, int(input())+1)
      for j in range(1, i)})), sep="\n")


# То же, но не одной строкой
""" 
from fractions import Fraction

numbers = set()

for i in range(2, int(input()) + 1):
    for j in range(1, i):
        numbers.add(Fraction(j, i))
        
print(*sorted(numbers), sep='\n')
"""
