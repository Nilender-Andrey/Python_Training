"""
На вход программе подается натуральное число n. 
Напишите программу, которая выводит первые n строк треугольника Паскаля.

На вход программе подается число n (n ≥ 1).

Формат выходных данных

Пример:
4

Результат:
1
1 1
1 2 1
1 3 3 1
"""

# Решение:
n = int(input())
result = [[1]]

for i in range(n-1):
    raw = [1]+[sum(result[i][j-1:j+1]) for j in range(1, len(result[i]))]+[1]
    result.append(raw)

for e in result:
    print(*e)


""" Чуть улучшенное решение

result = [1]

for _ in range(int(input())):
    print(*result)
    result = [1, *[sum(result[j:j+2]) for j in range(len(result)-1)], 1]

"""
