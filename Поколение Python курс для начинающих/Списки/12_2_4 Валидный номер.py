# На вход программе подается строка текста.
# Напишите программу, которая определяет является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером если она имеет формат:

# abc-def-hijk или 7-abc-def-hijk

# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9

l = input().split("-")

if "".join(l).isdigit() and all([len(l[i]) == [1, 3, 3, 4][i] for i in range(-len(l), 0)]) and (l[0] == "7" or len(l[0]) == 3):
    print("YES")
else:
    print("NO")

# для читаемости:

l = input().split("-")

# что все знаки = цифры
a = "".join(l).isdigit()

# что длинна у всех правильная
b = all([len(l[i]) == [1, 3, 3, 4][i] for i in range(-len(l), 0)])

# что у первого значение 7 или длинна 3
c = (l[0] == "7" or len(l[0]) == 3)

if a and b and c:
    print("YES")
else:
    print("NO")


# еще вариант
l = input().split("-")
print(["NO", "YES"]["".join(l).isdigit() and all([len(l[i]) == [1, 3, 3, 4][i]
      for i in range(-len(l), 0)]) and (l[0] == "7" or len(l[0]) == 3)])
