# На вход программе подается натуральное число n, n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

num = int(input())
a1, a2 = [], []

for _ in range(num):
    a1.append(int(input()))

for i in range(1, len(a1)):
    a2.append(a1[i]+a1[i-1])
print(a2)

# оптимальное решение:
n, a = int(input()), int(input())
lst = []
for _ in range(n-1):
    b = int(input())
    lst.append(a + b)
    a = b
print(lst)
