# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

# объявление функции
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2


# объявление функции
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# еще вариант
# через рекурсию

# объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:  # при выполнении условия => число не простое
            return get_next_prime(num)  # повторяем
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
