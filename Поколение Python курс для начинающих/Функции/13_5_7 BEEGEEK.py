# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# Напишите функцию is_valid_password(password),
# которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является действительным паролем BEEGEEK банка
# и False в противном случае.

# объявление функции
def is_valid_password(password):
    password = password.split(":")
    a, b, c = password[0], int(password[1]), int(password[2])

    if len(password) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False

    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
