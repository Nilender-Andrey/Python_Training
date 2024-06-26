"""
Напишите программу, которая выводит список хорошистов и отличников в классе.

На вход программе подается натуральное число n, 
далее следует n строк с фамилией школьника и его оценкой на каждой из них.

Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, 
а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

# Ввод:
5
Круглов 4
Кузнецов 5
Федин 4
Тарасов 2
Словецкий 3

# Вывод:
Круглов 4
Кузнецов 5
Федин 4
Тарасов 2
Словецкий 3

Круглов 4
Кузнецов 5
Федин 4
"""

# Решение:
students = [tuple(input().split()) for _ in range(int(input()))]
excellent_students = filter(lambda x: int(x[1]) >= 4, students)

for student in students:
    print(*student)

print()

for student in excellent_students:
    print(*student)

# Более короткий вариант
"""
pup = [input() for _ in range(int(input()))]

print(*pup, sep='\n')
print()
[print(x) for x in pup if int(x[-1]) > 3]
"""
