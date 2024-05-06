"""
На вход программе подаётся натуральное число. 
Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.
"""

# Решение
my_list = list(input())

k = 0
for i in range(3, len(my_list), 3):
    my_list.insert(-i-k, ",")
    k += 1
print("".join(my_list))


"""
    С использование стандартных возможностей
    #print(f'{int(str):,}')
"""

"""
Аккуратное решение через срезы:
num = input()
for idx in range(len(num) - 3, 0, -3):
    print(idx)
    num = num[:idx] + ',' + num[idx:]
print(num)
"""

"""
Решение через рекурсию:
def comma(st):
    if len(st) < 4:
        return st
    return comma(st[:-3]) + ',' + st[-3:]


print(comma(input()))
"""
