# На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.

s = input()
count = 0
for c in s:
    if c != c.upper():
        count += 1
print(count)

# еще вариант
s = input()
count = 0
for c in s:
    if "a" <= c <= "z" or "а" <= c <= "я":
        count += 1
print(count)

# еще вариант
s = input()
count = 0
for i in range(len(s)):
    if s[i] in "abcdefghijklmnopqrstuvwxyz":
        count += 1
print(count)

# еще вариант
print(sum(s.islower() for s in input()))
