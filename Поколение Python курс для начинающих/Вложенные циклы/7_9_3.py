# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из отрезка [a, b] с максимальной суммой делителей.
# Если таких чисел несколько, то выведите наибольшее из них.

a, b = int(input()), int(input())
number, summa = a, 0

for i in range(a, b+1):
    temp_sum = 0

    for j in range(1, i+1):
        if i % j == 0:
            temp_sum += j

    if temp_sum >= summa:
        summa, number = temp_sum, i

print(number, summa)
