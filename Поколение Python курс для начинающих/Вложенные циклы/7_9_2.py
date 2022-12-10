# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n.
"""
1
121
12321
1234321
123454321

"""
# Мое решение:

num = int(input())

for i in range(1, num+1):
    t, s = 1, 1
    for j in range(i*2-1):
        print(t, end="")
        if t == i:
            s = -1
        t += s
    print()


# Оптимальное решение:

num = int(input())

for i in range(1, num+1):
    for j in range(1, i*2):
        print(min(j, i * 2 - j), end='')
    print()
