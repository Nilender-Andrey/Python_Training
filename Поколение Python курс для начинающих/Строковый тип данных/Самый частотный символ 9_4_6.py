# На вход программе подается строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# Если таких символов несколько, следует вывести последний по порядку символ.

s = input()
max_c = s[0]

for c in s:
    if s.count(c) >= s.count(max_c):
        max_c = c

print(max_c)

# еще вариант:

# разворачиваем строку, чтобы выполнить условие 3
# key задает функцию для работы max
# max перебирает посимвольно и подставляет символ в key-функцию
# из результатов выбирается первый max и возвращается соответствующий ему символ
a = input()[::-1]
z = max(a, key=a.count)
print(z)
