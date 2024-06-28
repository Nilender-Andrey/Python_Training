"""
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). 
Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова, каждое на отдельной строке. Напишите программу, которая определяет, являются ли они анаграммами.

# Ввод:
thing
night

# Вывод:
YES
"""

# Решение:

print("YES" if sorted(list(input())) == sorted(list(input())) else "NO")


# С использованием списков:
"""
dict1, dict2 = {}, {}

for i in input():
    dict1[i] = dict1.setdefault(i, 0) + 1

for i in input():
    dict2[i] = dict2.setdefault(i, 0) + 1
    
print('YES' if dict1 == dict2 else 'NO')
"""

# Интересное решение:
"""
a1 = tuple(sorted(input()))
a2 = tuple(sorted(input()))

d = {a1: "NO", a2: "YES"}

print(d[a1])
"""
