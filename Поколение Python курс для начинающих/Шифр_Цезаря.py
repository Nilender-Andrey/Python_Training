def get_language():
    while True:
        print("Язык русский(ru) или английский(en)")
        language = input().lower()

        if language == "ru":
            return 32, "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        elif language == "en":
            return 26, 'abcdefghijklmnopqrstuvwxyz'
        else:
            print("Такого варианта нет")


def get_encrypt():
    while True:
        print("Шифрование(Y) или дешифрование(N)?")
        is_encrypt = input().lower()

        if is_encrypt == "y" or is_encrypt == "n":
            return is_encrypt == "y"
        else:
            print("Такого варианта нет")


def get_rot():
    while True:
        print("Шаг сдвига(число)")
        shift = input()

        if shift.isdigit():
            return int(shift)
        else:
            print("Необходимо число")


def encryption(symbol, rot, power, alphabet):
    char = symbol.lower()

    if char not in alphabet:
        return symbol

    index = (alphabet.index(char)+rot) % power
    result = alphabet[index]

    if symbol == symbol.upper():
        result = result.upper()

    return result


def main():
    print("Введите исходный текст")
    text = input()

    is_encrypt = get_encrypt()
    power, alphabet = get_language()
    rot = get_rot()*[-1, 1][is_encrypt]

    result = ""
    for c in text:
        result += encryption(c, rot, power, alphabet)

    return result


print(main())
