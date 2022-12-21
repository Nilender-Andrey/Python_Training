# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.

n = int(input())
s = ""
for _ in range(n):
    s += input()
print(list(s))

# еще вариант:

n = int(input())
l = []
for i in range(n):
    l += input()
print(l)

# еще вариант:
n = int(input())
sp = []
for _ in range(n):
    sp.extend(input())
print(sp)
