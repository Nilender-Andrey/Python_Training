# На вход программе подается строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru

s = input()
print("YES" if s.endswith(".com") or s.endswith(".ru") else "NO")

# еще вариант:
s = input().lower()
print("YES" if (s[-4::] == ".com") or (s[-3::] == ".ru") else "NO")

# Улучшенный вариант:

print('YES' if input().endswith(('.com', '.ru')) else 'NO')
