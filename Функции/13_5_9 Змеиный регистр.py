# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку
# в «верблюжьем регистре» и преобразует его в «змеиный регистр».

# объявление функции
def convert_to_python_case(text):
    result = ''
    for i in text:
        if i.isupper():
            result += "_"
        result += i.lower()
    return result[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# еще вариант


def convert_to_python_case(text):
    return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()


txt = input()
print(convert_to_python_case(txt))
