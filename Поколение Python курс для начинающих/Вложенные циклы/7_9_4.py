# На вход программе подается натуральное число n.
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

for i in range(1, int(input())+1):
    s = str(i)

    for j in range(1, i+1):
        if i % j == 0:
            s += "+"
    print(s)
