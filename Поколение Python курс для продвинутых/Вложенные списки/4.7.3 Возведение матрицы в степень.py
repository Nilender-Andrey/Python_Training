"""
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, 
затем элементы матрицы, 
затем натуральное число m.

# Ввод:
3
1 2 3
4 5 6
7 8 9
2

# Вывод
30 36 42
66 81 96
102 126 150
"""

# Решение

n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
m = int(input())


def multiply_matrices(matrix_1, matrix_2):
    n, m, k = len(matrix_1), len(matrix_1[0]), len(matrix_2[0])
    matrix_result = [[0]*k for _ in range(n)]

    for i in range(k):
        for j in range(n):
            for l in range(m):
                matrix_result[i][j] += matrix_1[i][l]*matrix_2[l][j]
    return matrix_result


matrix_result = multiply_matrices(matrix, matrix)

for i in range(m-2):
    matrix_result = multiply_matrices(matrix_result, matrix)

for i in range(n):
    print(*matrix_result[i])


# Более короткий вариант
"""
n = int(input())
m1 = [[int(j) for j in input().split()] for i in range(n)]
m = int(input())
res = m1

for l in range(m-1):
    res = [[sum([res[i][p] * m1[p][j] for p in range(n)]) for j in range(n)] for i in range(n)]

for r in res:
    print(*r)
"""

# С помощью встроенной библиотеки
""" 
# Импорт библиотеки numpy для работы с матрицами.
import numpy as np

# Считываем матрицу и числа n и m.
n = int(input())
matrix = np.array([list(map(int, input().split())) for _ in range(n)]).astype(np.int64)
m = int(input())

# Вычисляем итоговую матрицу.
matrix_power = np.linalg.matrix_power(matrix, m)

# Вывод результатов.
print(*[' '.join([f'{el}' for el in row.tolist()]) for row in matrix_power], sep='\n')
"""
