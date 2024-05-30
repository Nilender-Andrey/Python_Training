"""
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Напишите программу, которая создает матрицу размером n х m, заполнив её "змейкой" в соответствии с образцом.

# Пример
5 5

# Результат
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
"""

# Решение

n, m = map(int, input().split())
matrix = [[str(i * m + j + 1).ljust(3) for j in range(m)] for i in range(n)]

for i in range(n):
    if i % 2 == 1:
        matrix[i].reverse()
    print(*matrix[i])


""" Короче
n, m = map(int, input().split())
matrix = [[str(i * m + j + 1).ljust(3) for j in range(m)][::(-1)**i] for i in range(n)]

for i in range(n):
    print(*matrix[i])
"""

""" Еще короче
n, m = map(int, input().split())
[print(*[str(i * m + j + 1).ljust(3) for j in range(m)][::(-1)**i]) for i in range(n)]
"""
