# На вход программе подается строка текста, содержащая натуральные числа.
# Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

s = input().replace(" ", "+")
print(s, "=", sum([int(i) for i in s.split("+")]), sep="")

# еще вариант

n = [int(i) for i in input().split()]
print(*n, sep='+', end='=')
print(sum(n))

# еще вариант

numbers = [int(number) for number in input().split()]
print(*numbers, sep='+', end=f'={sum(numbers)}')
