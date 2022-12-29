# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной
# скобочной последовательностью и False в противном случае.

# Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка.

# объявление функции
def is_correct_bracket(text):
    count = 0
    for c in text:
        count += c == "("
        count -= c == ")"
        if count < 0:
            return False
    return count == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# еще вариант:

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text


txt = input()
print(is_correct_bracket(txt))
