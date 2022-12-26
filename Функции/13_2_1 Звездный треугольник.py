# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;

# а затем выводит его.

# Примечание. Гарантируется, что основание треугольника – нечетное число.


# объявление функции
def draw_triangle(fill, base):
    base += 1
    print(*[fill*min(i, base-i) for i in range(1, base)], sep="\n")


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
