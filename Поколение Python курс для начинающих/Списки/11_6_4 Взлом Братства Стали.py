# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, и любезно соглашается помочь им в решении их проблем. 
# Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. 
# Известно, что программисты Братства никогда не оставляют комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. 
# Помогите писцу Ибсену удалить все комментарии из программы.

# На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, не считая первой. 
# Далее следует n строк кода.

'''
#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)
'''

''' результат
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)
'''

num = int(input().split("#")[1])

for _ in range(num):
    l = input().split("#")
    if len(l):
        l=l[0].rstrip() 
    print("".join(l))

# еще вариант

n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# еще вариант

n = input().split('#')
for _ in range(int(n[1])):
    print(input().split('#')[0].rstrip())