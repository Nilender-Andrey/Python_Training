# На вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.

# v.1
"""
s = input()
r = 0

for i in range(len(s)):
    r += int(s[i])
print(r)
"""
# v.2
"""
s = input()
r = 0

for i in s:
    r += int(i)
print(r)
"""

# v.3
print(sum(int(i) for i in input()))
