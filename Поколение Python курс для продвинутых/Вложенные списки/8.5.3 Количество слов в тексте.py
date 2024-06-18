"""
Напишите программу для определения общего количества различных слов в строке текста.

Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
Знаками препинания .,;:-?! пренебрегаем.

# Ввод:
Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.

# Вывод:
15
"""

# Решение:

print(len(set(item.lower().strip('.,;:-?!') for item in input().split())))


# Через регулярное выражение
"""
import re

print(len(set(re.findall('\w+', input().lower()))))
"""
