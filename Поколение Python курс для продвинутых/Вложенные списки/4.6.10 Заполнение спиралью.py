"""
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Напишите программу, которая создает матрицу размером n x m, заполнив её "спиралью" в соответствии с образцом.

# Ввод
4 5

# Вывод
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
"""

# Решение

n, m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
gs, vs = 0, 0
ge, ve = n, m
num, max = 0, n*m

while True:
    for j in range(vs, ve):
        num += 1
        matrix[gs][j] = num

    if num >= max:
        break

    gs += 1
    for j in range(gs, ge):
        num += 1
        matrix[j][ve-1] = num

    if num >= max:
        break

    ve -= 1
    for j in range(ve-1, vs-1, -1):
        num += 1
        matrix[ge-1][j] = num

    if num >= max:
        break

    ge -= 1
    for j in range(ge-1, gs-1, -1):
        num += 1
        matrix[j][vs] = num

    vs += 1
    if num >= max:
        break

for i in range(n):
    [print(str(j).ljust(3), end="") for j in matrix[i]]
    print()
