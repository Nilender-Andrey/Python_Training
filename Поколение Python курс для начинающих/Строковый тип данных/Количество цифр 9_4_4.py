# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.

s = input()
count = 0

for c in s:
    if "0" <= c <= "9":
        count += 1
print(count)

# еще вариант

s = input()
count = 0

for i in range(10):
    count += s.count(str(i))
print(count)
