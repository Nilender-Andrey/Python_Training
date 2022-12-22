# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
a = []
for _ in range(n):
    s = input()
    if s not in a:
        a.append(s)
print(*a, sep='\n')

# еще вариант:
s = [input() for _ in range(int(input()))]
print(*[s[i] for i in range(len(s)) if s[:i].count(s[i]) == 0], sep="\n")
