# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

# объявление функции
def get_factors(num):
    return [i for i in range(1, num+1) if num % i == 0]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


# более оптимальный вариант:

def get_factors(num):
    return [i for i in range(1, num//2 + 1) if num % i == 0] + [num]


n = int(input())
print(get_factors(n))
