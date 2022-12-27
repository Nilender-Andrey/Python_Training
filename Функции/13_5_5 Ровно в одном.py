# Напишите функцию is_one_away(word1, word2),
# которая принимает в качестве аргументов два слова word1 и word2
# и возвращает значение True если слова имеют одинаковую длину
# и отличаются ровно в 1 символе и False в противном случае.

# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))


#  оптимальное решение:
# объявление функции
def is_one_away(word1, word2):
    return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
