""" 
В игре Scrabble каждая буква приносит определенное количество баллов. 
Общая стоимость слова – сумма баллов его букв. 
Чем реже буква встречается, тем больше она ценится:
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

Напишите программу подсчета итоговой стоимости введенного слова.

# Ввод:
DANSER

# Вывод:
7
"""

# Решение:
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

print(sum([k for i in input() for k, v in d.items() if i in v]))
