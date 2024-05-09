'''
На вход программе подается строка текста из натуральных чисел. 
Из неё формируется список чисел. 
Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа. 
'''

# Решение
num_list = list(map(int, input().split()))
r = 0

for i in range(1, len(num_list)):
    r += num_list[i] > num_list[i-1]

print(r)

# Решение 2

num_list = list(map(int, input().split()))
print(sum([num_list[i] > num_list[i-1] for i in range(1, len(num_list))]))
