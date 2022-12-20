# На вход программе подается натуральное число n.
# Напишите программу, которая создает список состоящий из делителей введенного числа.

num = int(input())
arr = []

for i in range(1, num//2+1):
    if num % i == 0:
        arr.append(i)
arr.append(num)
print(arr)
