# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

"""
5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
язык

Результат:
Язык Python прекрасен
C# - отличный язык программирования
язык Python появился 20 февраля 1991
"""

n = int(input())
a = [input() for _ in range(n)]
s = input()
for i in a:
    if s.lower() in i.lower():
        print(i)
