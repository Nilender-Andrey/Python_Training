# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input())
num_0 = []
num_p = []

for _ in range(n):
    i = int(input())
    if i == 0:
        num_0.append(i)
    elif i > 0:
        num_p.append(i)
    else:
        print(i)
print(*num_0, *num_p, sep="\n")

# еще вариант:

negatives, zeros, positives = [], [], []
for _ in range(int(input())):
    value = int(input())
    if value < 0:
        negatives.append(value)
    elif value == 0:
        zeros.append(value)
    elif value > 0:
        positives.append(value)
print(*negatives, *zeros, *positives, sep="\n")

# более аккуратное решение:

n = int(input())
x = [int(input()) for _ in range(n)]
[print(i) for i in x if i < 0]
[print(i) for i in x if i == 0]
[print(i) for i in x if i > 0]
