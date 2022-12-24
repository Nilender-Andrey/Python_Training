# На вход программе подается строка, содержащая английский текст.
# Слова текста разделены символом пробела.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
# Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'

l = input().lower().split()

print("Общее количество артиклей:",
      l.count("a")+l.count("an")+l.count("the"))

# еще вариант:
text = input().lower().split()
articles = ['a', 'the', 'an']
total = 0
for i in text:
    if i in articles:
        total += 1
print(f"Общее количество артиклей: {total}")
