# На вход программе подается число nn, а затем n строк, содержащих целые числа в порядке возрастания. 
# Из данных строк формируются списки чисел. 
# Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

'''
3
1 2 3 4
5 6 7
10 11 17

Ответ:
1 2 3 4 5 6 7 10 11 17
'''

# решение по материалам:
def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    return result


res = []
for _ in range(int(input())):
    list_1 =[int(i) for i in input().split()]
    res = quick_merge(res, list_1)
    
print(*res)

# оптимальное решение:
n=int(input())
def quick_merge(n):
    return sorted([int(i) for i in range(n) for i in input().split()])
print(*quick_merge(n))  

# sorted возвращает отсортированный список указанного итерируемого объекта.