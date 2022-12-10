
# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n.

"""
start, step = 1, 1
stop = int(input())//2+1


for i in range(2):

    if i % 2 != 0:
        start = stop
        stop = 0
        step *= -1

    for k in range(start, stop,  step):
        print("*"*k)
"""


# Оптимальное решение:
"""
n = int(input())

for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))
"""

# Еще хороший вариант:
n = int(input())

for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    print('*' * k)

# можно еще уменьшить, но теряется читаемость
