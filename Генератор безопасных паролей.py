from random import sample

chars = ["0123456789", 
         "abcdefghijklmnopqrstuvwxyz",
         "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
         "!#$%&*+-=?@^_"]

questions = ["Включать ли цифры 0123456789?", 
             "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?",
             "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?", 
             "Включать ли символы !#$%&*+-=?@^_?"]


num = int(input("Количество паролей для генерации: "))
length = int(input("Длину одного пароля: "))

print("Настройки, 'Y'- да, 'N' - нет")

res_chars = []
for i in range(len(questions)):

    if input(questions[i]+" ").upper() == "Y":
        res_chars.extend(chars[i])
   
if input("Исключать ли неоднозначные символы il1Lo0O? ").upper() == "Y":
      for c in "il1Lo0O":
          if c in res_chars:
              del res_chars[res_chars.index(c)]
  
  
def generate_password(num, length):
  for _ in range(num):
    print(*sample(res_chars, length), sep="")

generate_password(num, length)
