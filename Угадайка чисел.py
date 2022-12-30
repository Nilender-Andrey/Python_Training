# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100
#  и просит пользователя угадать это число.

# Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.

# Если догадка меньше случайного числа,
# то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.

# Если пользователь угадывает число, то программа должна поздравить его
# и вывести сообщение 'Вы угадали, поздравляем!'.

from random import *


def is_valid(s, border):
    return s.isdigit() and 0 <= int(s) <= border

def pick_phrase(count, word_0, word_1, word_2): 
    rem = count % 100
    if rem < 11 or rem > 14:
        rem = count % 10
        if(rem == 1):
             return word_1
        if rem >= 2 and rem <= 4:
             return word_2
    return word_0   

def engine(border):
    print("Какое число загадано?")
    random_num = randint(0, border)
    count = 1

    while True:
        num = input()
        if not is_valid(num, border):
            print(
               f"А может быть все-таки введем целое число от 1 до {border}?")
            continue
        num = int(num)

        if num < random_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif num > random_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            str = pick_phrase(count, "попыток", "попытка", "попытки")

            print("Вы угадали, поздравляем!",
                  f"Вам понадобилось {count} {str}")

            if input("Еще разок? Введите 'Да' или 'Нет' ").lower() == "да":
                engine(border)
               
            else:
                print(
                    "Спасибо, что играли в числовую угадайку. Еще увидимся...", sep="\n")
                break
        count += 1

def getBorder():
    str = input("Играем от 0 до ..., введите число: ")
    while not str.isdigit():
        str = input("Не подходит, введите число: ")
    return int(str)

def game():
    print("Добро пожаловать в числовую угадайку")
    border = getBorder()
    engine(border)

game()
