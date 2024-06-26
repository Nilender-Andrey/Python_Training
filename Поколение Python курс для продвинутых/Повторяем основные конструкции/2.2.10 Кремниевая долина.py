"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника".
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы.

Формат входных данных
В первой строке подаётся число n – количество холодильников. 
В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

Пример:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

Результат:
1 2 3
"""

# Решение в лоб

my_list = [input() for _ in range(int(input()))]

search_str = "anton"
result = []

for i, str in enumerate(my_list):
    temp_str = ""
    for c in str:
        if search_str[len(temp_str)] == c:
            temp_str += c

        if temp_str == search_str:
            result.append(i+1)
            break

print(*result)

""" немного другая логика и короче
for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break    
"""

"""Регулярное выражение
import re

n = int(input())

for i in range(n):
    s = input()

    if re.search(r"a.*n.*t.*o.*n", s):
        print(i + 1, end=" ")
"""
