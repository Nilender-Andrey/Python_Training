"""
Латинским квадратом порядка n называется квадратная матрица размером n x n, 
каждая строка и каждый столбец которой содержат все числа от 1 до n. 

Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, 
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

# Ввод:
4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4

# Вывод:
YES
"""

# Решение:
n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
s = set(range(1, n+1))

for i in matrix:
    if s != set(i):
        print("NO")
        exit()

matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]

for i in matrix:
    if s != set(i):
        print("NO")
        exit()
else:
    print("YES")


# Аккуратное решение:
"""
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break
        
print(result)
"""
