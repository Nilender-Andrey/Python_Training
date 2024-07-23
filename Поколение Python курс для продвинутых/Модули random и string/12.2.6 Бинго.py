"""
Для игры в бинго требуется карточка размером 5x5, содержащая различные (уникальные) целые числа от 1 до 75(включительно), 
при этом центральная клетка является пустой (она заполняется числом 0x0).

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
"""

# Решение:
from random import *

nums = sample(range(1, 76), 25)
nums[12] = 0
matrix = [[str(nums.pop()).ljust(3) for _ in range(5)] for _ in range(5)]

for i in matrix:
    print(*i)


# Оригинальное заполнение матрицы:
"""
from random import sample

numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()
"""

# Решение без матрицы
"""
from random import sample as r

n = r(range(1, 75), 24)
n = n[:12] + [0] + n[12:]
[print(''.join(str(n[i * 5 + j]).ljust(3) for j in range(5))) for i in range(5)]
"""
