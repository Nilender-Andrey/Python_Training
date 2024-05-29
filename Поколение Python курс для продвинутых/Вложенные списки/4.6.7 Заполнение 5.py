"""
На вход программе на одной строке подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером n x m, заполнив её в соответствии с образцом.

# Пример
5 5

# Результат
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
"""

# Решение

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
    [print(str(matrix[i][j]).ljust(3), end="") for j in range(m)]
    print()


""" Вариант с перестановкой
n, m = map(int, input().split())
matrix = [[*range(1, m + 1)]] 

for i in range(1, n+1):
    row = list(matrix[i-1])
    row.insert(m - 1, row.pop(0))
    matrix.append(row)
    
for i in range(n):
    [print(str(j).ljust(3), end="") for j in matrix[i]]
    print()
"""

""" Вариант с перестановкой 
n, m = map(int, input().split())
row = list(range(1, m + 1))

for _ in range(n):
    print(*row)
    x = row.pop(0)
    row.append(x)
"""

""" Вариант с перестановкой через срезы
n, m = map(int, input().split())
a = [i for i in range(1, m+1)]

for i in range(n):
    print(*a)
    a = a[1:] + a[:1]
"""
