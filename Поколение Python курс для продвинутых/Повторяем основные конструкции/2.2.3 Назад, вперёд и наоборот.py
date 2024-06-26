"""
На вход программе подается строка текста из натуральных чисел. 
Из элементов строки формируется список чисел. 
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). 
Если в списке нечетное количество элементов, то последний остается на своем месте.
"""

# Решение (очень топорное)
list = input().split()
result = " ".join([" ".join(list[i:i+2][::-1])
                  for i in range(0, len(list), 2)])

print(result)

"""
   numbers = input().split()

  for i in range(0, len(numbers) - 1, 2):
      numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

  print(*numbers) 
"""

""" Очень классное решение
d = input().split()

d[:-1:2], d[1::2] = d[1::2], d[:-1:2]

print(*d)
"""
