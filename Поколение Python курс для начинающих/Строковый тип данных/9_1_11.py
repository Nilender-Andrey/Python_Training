# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.

num = int(input())
result = ""
while num:
    result = str(num % 2)+result
    num //= 2
print(result)
