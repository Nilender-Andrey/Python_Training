# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно.


a, b = int(input()), int(input())

for i in range(a, b+1):
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5 + 1)):  # уменьшаем цикл
        break
    else:                                  # если цикл не завершился break, сработает else
        print(i)
