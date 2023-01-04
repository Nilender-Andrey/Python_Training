# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

# шифрует в английском алфавите (символ, сдвиг)
def encryption(symbol, rot):
    char = symbol.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if char not in alphabet:
        return symbol

    index = (alphabet.index(char)+rot) % 26
    result = alphabet[index]

    if symbol == symbol.upper():
        result = result.upper()

    return result


l = input().split()
s = ""

for i in range(len(l)):

    #  считаем знаки являющиеся буквами
    count = 0
    for z in l[i]:
        if z.isalpha():
            count += 1

    for c in l[i]:
        s += encryption(c, count)
    s += " "

print(s)

# слегка оптимизировано


def encryption(symbol, rot):
    char = symbol.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if char not in alphabet:
        return symbol

    index = (alphabet.index(char)+rot) % 26
    result = alphabet[index]

    if symbol == symbol.upper():
        result = result.upper()

    return result


l, s = input().split(), ""

for i in range(len(l)):
    length = len([z for z in l[i] if z.isalpha()])
    s += "".join([encryption(c, length) for c in l[i]])+" "

print(s)
