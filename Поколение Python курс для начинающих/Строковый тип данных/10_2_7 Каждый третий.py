# На вход программе подается строка текста.
# Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....

s = input()
print(*[s[i] for i in range(len(s)) if i % 3 != 0], sep="")

# еще вариант

l = list(input())
del l[::3]
print(*l, sep="")
