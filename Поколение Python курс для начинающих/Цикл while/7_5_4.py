# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = 5678  # int(input())
count, total, first_num = 0, 0, 0
multiplication = 1
last_num = num % 10

while num:
    first_num = num % 10
    total += first_num
    multiplication *= first_num
    count += 1
    num //= 10

# print(total, count, multiplication, total/count, first_num, first_num+last_num, sep="\n")

print(total)              # 26
print(count)              # 4
print(multiplication)     # 1680
print(total/count)        # 6.5
print(first_num)          # 5
print(first_num+last_num)  # 13
