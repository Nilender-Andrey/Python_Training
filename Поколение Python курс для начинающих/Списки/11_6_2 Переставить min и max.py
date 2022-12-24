# На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
# Из данной строки формируется список чисел. 
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

l =[int(i) for i in input().split(" ")]

i_max = l.index(max(l))
i_min = l.index(min(l))
l[i_max], l[i_min] = l[i_min], l[i_max]

print(*l)

# Еще вариант:

l = input().split(" ")

i_max = l.index(max(l, key=int))
i_min = l.index(min(l, key=int))
l[i_max], l[i_min] = l[i_min], l[i_max]

print(*l)