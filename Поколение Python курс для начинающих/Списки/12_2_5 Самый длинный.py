# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

print(len(sorted(input().split(), key=len, reverse=True)[0]))

# еще вариант
print(len(sorted(input().split(), key=len)[-1]))

# еще вариант
print(max([len(a) for a in input().split()]))

# еще вариант
print(len(max(input().split(), key=len)))
