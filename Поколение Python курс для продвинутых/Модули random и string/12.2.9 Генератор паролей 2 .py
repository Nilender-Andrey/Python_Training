""" 
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, 
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).

Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

# Ввод:
9
7

# Вывод:
iHnPg7q
Njj9m3N
tQ9v5ut
6qPZ3tV
6gVScya
kU8ncAY
5CKX9Da
UTQRve4
FyRe8NN
"""

# Решение:

from string import *
from random import *

LUS = list(set(ascii_uppercase) - set('IO'))
LLS = list(set(ascii_lowercase) - set('lo'))
LN = list(set(digits) - set('01'))
ALL_S = LUS+LLS+LN


def generate_password(length):
    result = [choice(s) for s in (LUS, LLS, LN)]+[choice(ALL_S)
                                                  for _ in range(3, length)]
    shuffle(result)
    return "".join(result)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep="\n")
