# На вход программе подается одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв.

# s.lower() приводит все символы строки к нижнему регистру

s = input()
count_gl, count_sg = 0, 0

for c in s.lower():
    if c in "ауоыиэяюёе":
        count_gl += 1
    if c in "бвгджзйклмнпрстфхцчшщ":
        count_sg += 1
print("Количество гласных букв равно", count_gl)
print("Количество согласных букв равно", count_sg)
