"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

0 0 0 1
0 0 1 1
0 1 1 1
1 1 1 1 

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

# Ввод:
3
1 4 5
6 7 8
1 1 6

# Вывод:
8
"""

# Решение:
n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]

max = matrix[0][-1]

for i in range(n):
    for j in range(n):
        if i + j + 1 >= n and matrix[i][j] > max:
            max = matrix[i][j]

print(max)


# Более короткий вариант
"""
n = int(input())
a = [input().split() for _ in range(n)]
print(max([a[i][j] for i in range(n) for j in range(n) if i >= n-1-j]))
"""

# Интересный вариант
"""
#  берем размер матрицы
n = int(input())
#  выпиливаем матрицу из входных данных
matrix = [[int(x) for x in input().split()] for i in range(n)]
#  вычисляем больший (элемент) из больших (элементов) в бегущем срезе
answer = max(max(matrix[i][n-i-1:]) for i in range(n))
#  закидываем результат
print(answer)
"""
