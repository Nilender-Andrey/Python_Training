# Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

"""
num = int(input())
flag = True

while num//10 and flag:
    flag = num % 10 <= num // 10 % 10
    num //= 10

print("YES" if flag else "NO")

"""

# Оптимальное решение

n = int(input())

while n % 10 <= n // 10 % 10:
    n //= 10

print('YES' if n < 10 else 'NO')
