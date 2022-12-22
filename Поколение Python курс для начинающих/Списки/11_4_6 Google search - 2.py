# На вход программе подается натуральное число n, затем n строк.
# Затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

"""
5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
2
язык
python

Результат:
Язык Python прекрасен
язык Python появился 20 февраля 1991
"""

n = int(input())
strings = [input() for _ in range(n)]

k = int(input())
searches = [input() for _ in range(k)]

a = []

for string in strings:
    count = 0
    for search in searches:
        if search.lower() in string.lower():
            count += 1
    if count == len(searches):
        a.append(string)
print(*a, sep="\n")

# Оптимальное решение:

n = int(input())
strings = [input() for _ in range(n)]

k = int(input())
searches = [input() for _ in range(k)]

for string in strings:
    for search in searches:
        if search.lower() not in string.lower():
            break
    else:
        print(string)
