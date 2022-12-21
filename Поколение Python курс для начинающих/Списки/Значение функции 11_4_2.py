# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции
# f(x) = x^2 + 2x + 1x, каждое на отдельной строке.

n = int(input())
a = []
for _ in range(n):
    n = int(input())
    print(n)
    a.append(n**2 + 2*n + 1)

print("", *a, sep="\n")

# еще вариант:
numbers = [int(input()) for _ in range(int(input()))]
print(*numbers, '', *[(x + 1) ** 2 for x in numbers], sep='\n')
