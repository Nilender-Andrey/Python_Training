"""
На вход программе подаются натуральное число n ≥ 1, а затем n различных натуральных чисел, каждое на отдельной строке. 
Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.

# Ввод:
6
1234567890
87654321
34567890
987234356
1236789
987532

# Вывод:
3 7 8
"""

# Решение:
from functools import reduce

n = int(input())
set_list = [set(input()) for _ in range(n)]
result = sorted(reduce(lambda s, i: s & i, set_list))
print(*result)


# Более простое решение:
"""
n, my_set = int(input()), set(input())

for _ in range(n - 1):
    my_set = my_set & set(input())

print(*sorted(my_set, key=int))
"""

# Однострочные решения
"""
print(*sorted(set.intersection(*(set(input()) for i in range(int(input()))))))

print(*sorted(set.intersection(*map(set, [set(input()) for _ in range(int(input()))]))))
"""
