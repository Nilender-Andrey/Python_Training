# На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.

# v.1.
'''
num = int(input())

for i in range(2, num+1):
    if num % i == 0:
        print(i)
        break
'''
# v.2.

i = 2
num = int(input())

while num % i != 0:
    i += 1

print(i)
