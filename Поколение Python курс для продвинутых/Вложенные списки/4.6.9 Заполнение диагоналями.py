"""
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Напишите программу, которая создает матрицу размером n х m, заполнив её "диагоналями" в соответствии с образцом.

# Пример
3 5

# Результат
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
"""

# Решение

# Принимаем параметры матрицы
n, m = map(int, input().split())
# Создаем скелет матрицы
matrix = [[0] * m for i in range(n)]
# Задаем отсчет с единицы
d = 1

for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
    for i in range(n):                  # Перебираем строки
        for j in range(m):              # Перебираем столбцы
            if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали

                # Присваиваем обнаруженной ячейке порядковый номер
                matrix[i][j] = d
                d += 1                  # Обновляем счетчик

# Распечатываем полученную матрицу
for i in range(n):
    [print(str(j).ljust(3), end="") for j in matrix[i]]
    print()


""" 
n, m = map(int, input().split())

# Создаем матрицу
matrix = [[0] * m for _ in range(n)]

# Создаем список сумм и координат
# Сумма нужна для правильной сортировки и является номером диагонали
template = sorted([(i + j, i, j) for i in range(n) for j in range(m)])

for id, item in enumerate(template):
    matrix[item[1]][item[2]] = id + 1

[print(*[str(item).ljust(3) for item in row]) for row in matrix]
"""

"""
n, m = [int(x) for x in input().split()]
l = [[0] * m for _ in range(n)]
k = 1
for j in range(m + n):
    for i in range(n):
        if 0 <= j - i < m:
            l[i][j - i] = k
            k += 1
for i in range(n):
    print(*l[i])
"""
