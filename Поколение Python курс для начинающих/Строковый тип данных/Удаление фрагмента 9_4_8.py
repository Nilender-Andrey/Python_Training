# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.

s = input()
l = s.find("h")
r = s.rfind("h")

print(s[0:l]+s[r+1:])
