"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

1 0 0 0 1
1 1 0 1 1
1 1 1 1 1
1 1 0 1 1
1 0 0 0 1

На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Пример:
3
1 4 5
6 7 8
1 1 6

# Результат:
8
"""

# Решение

n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]

max = matrix[0][0]

for i in range(n):
    for j in range(n):
        if ((i >= j and i <= n-1-j) or (i <= j and i >= n-1-j)) and matrix[i][j] > max:
            max = matrix[i][j]

print(max)


""" Тоже, но компактнее

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(max([matrix[i][j] for i in range(n) for j in range(n) if (i>=j and i<=n-1-j) or (i<=j and i>=n-1-j)]))

"""

""" Интересное решение
Используем зеркальную симметричность относительно двух центральных осей (горизонталей и вертикалой), 
разбивающих заштрихованную область на 4-е треугольника:

1 0 0 0 3
1 1 0 3 3
1 1 1 3 3
2 2 0 4 4
2 0 0 0 4

Идея в том, чтобы обходить лишь треугольник №1, 
соответствующие элементы в 3-х остальных четвертях можно получить зеркальным отображением элементов первого треугольника, 
относительно двух осей. Такое отображение можно получить (среди прочего) с помощью побитового оператора ~. 
Например, элемент треугольника №2, зеркально симметричный элементу из треугольника №1, 
с индексами (i, j) - m[i][j] можно найти с помощью преобразования m[i][n-j-1] или m[i][-j-1] или более компактно: m[i][~j].

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
print(max(max(m[i][j], m[i][~j], m[~i][j], m[~i][~j]) for i in range(n // 2 + 1) for j in range(i + 1)))

"""
