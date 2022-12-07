# Дано натуральное число n \, (n > 9)n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

# Простой вариант:
# print(input()[1])

"""
# Мое решение:

num = int(input())
a, b = 0, num % 10

while num:
    b = a
    a = num % 10
    num //= 10

print(b)
"""

# Оптимальное решение:

n = int(input())
while n > 99:
    n //= 10
print(n % 10)
