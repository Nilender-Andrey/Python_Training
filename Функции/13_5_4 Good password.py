# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

# Пароль является надежным если:

# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.


# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False

    is_up, is_low, is_num = False, False, False

    for c in password:
        if c.isdigit():
            is_num = True
        if c.islower():
            is_low = True
        if c.isupper():
            is_up = True
    return is_num and is_low and is_up


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


#  еще вариант
# объявление функции
def is_password_good(password):
    result = True

    if len(password) < 8:
        result = False
    if password.lower() == password:
        result = False
    if password.upper() == password:
        result = False
    if password.isalpha():
        result = False

    return result


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


# оптимальный вариант:
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()
print(is_password_good(txt))

# Встроенная функция all(последовательность) возвращает True, только если все элементы последовательности  истинные (или, если последовательность пуста).
# Если хотя бы один элемент последовательности  ложный функция вернёт False.

# Есть в python   аналогичная all() встроенная функция, называется any(iterable), которая возвращает True, если хотя бы какой-нибудь  элемент iterable возвращает истину.
# Если итерируемый объект пуст, возвращается False.
