"""
На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. 
Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. 
При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. 
Нажатие цифры 2, 3, 4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.

1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
0	space (пробел)

Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.
На вход программе подается одна строка – текстовое сообщение.

Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.
Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в приведенной выше таблице.

# Ввод:
Hello, World!

# Вывод:
4433555555666110966677755531111
"""

# Решение
d = {
    ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
    "a": '2', "b": '22', "c": '222',
    "d": '3', "e": '33', "f": '333',
    "g": '4', "h": '44', "i": '444',
    "j": '5', "k": '55', "l": '555',
    "m": '6', "n": '66', "o": '666',
    "p": '7', "q": '77', "r": '777', "s": '7777',
    "t": '8', "u": '88', "v": '888',
    "w": '9', "x": '99', "y": '999', "z": '9999',
    " ": '0'
}

print("".join([d[i] for i in input().lower() if i in d]))


# Еще решение:
"""
keyboard = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' ',
}

# принимаем строку и сразу преобразуем её в верхний регистр
s = input().upper()

# идём по всем символам строки
for c in s:
    # идём по всем цифрам и значениям для них в словаре
    for digit, values in keyboard.items():
        if c in values:
            # ищем, сколько раз нам надо нажать эту цифру
            cnt = values.index(c) + 1
            print(cnt * digit, end='')
            break
"""
