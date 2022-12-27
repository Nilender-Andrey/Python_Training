# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом и False в противном случае.

# При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

# объявление функции
def is_palindrome(text):
    text = text.lower()
    for c in " ,.!?-":
        text = text.replace(c, "")
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))


# оптимальный вариант:
# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i.isalpha()]
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))


# еще вариант:
# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i not in (',.!?- ')]
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
