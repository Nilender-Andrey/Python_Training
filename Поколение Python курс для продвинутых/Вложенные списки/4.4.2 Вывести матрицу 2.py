"""
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, 
выводит их в виде матрицы, выводит пустую строку, 
и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

# Пример:
4
2
и
швец
и
жнец
и
на
дуде
игрец

# Результат
и швец
и жнец
и на
дуде игрец

и и и дуде
швец жнец на игрец
"""

# Решение

n, m = int(input()), int(input())

matrix_1 = [[0]*m for _ in range(n)]
matrix_2 = [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        value = input()
        matrix_1[i][j] = value
        matrix_2[j][i] = value


def print_matrix(matrix):
    for item in matrix:
        print(*item)
    print()


print_matrix(matrix_1)
print_matrix(matrix_2)


"""
n, m = int(input()), int(input())
arr = [[input() for _ in range(m)] for _ in range(n)]

for row in arr:
    print(*row)
print()

for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')
    print()
"""

""" Еще короче

n, m = int(input()), int(input())
w = [[input() for _ in range(m)] for _ in range(n)]
[print(*r) for r in w]
print()
[print(*[w[j][i] for j in range(n)]) for i in range(m)]

"""
