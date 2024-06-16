"""
Напишите программу, которая транспонирует квадратную матрицу.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

# Ввод:
3
1 2 3
4 5 6
7 8 9

# Вывод
1 4 7
2 5 8
3 6 9
"""

# Решение

n = int(input())
matrix = [input().split() for _ in range(n)]

[print(*[matrix[j][i] for j in range(n)]) for i in range(n)]


"""
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)
"""
