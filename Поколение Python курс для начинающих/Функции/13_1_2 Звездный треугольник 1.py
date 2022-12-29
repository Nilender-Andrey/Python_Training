# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10.

# объявление функции
def draw_triangle():
    for i in range(1, 11):
        print("*"*i)


# основная программа
draw_triangle()  # вызов функции

# еще вариант:


def draw_triangle():
    print("\n".join(["*"*i for i in range(1, 11)]))


draw_triangle()
