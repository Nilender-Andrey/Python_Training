# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

"""
num = int(input())
flag = True
n = num % 10

while num and flag:
    flag = n == num % 10
    n = num % 10
    num //= 10

print("YES" if flag else "NO")
"""

# Оптимальное решение

num = input()
print("YES" if max(num) == min(num) else "NO")
