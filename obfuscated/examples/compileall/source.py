# программа для подсчета площади прямоугольного треугольника
def square_triangle_area(width, height):
    return height * width / 2


print("Эта программа считает площадь прямоугольного треугольника.")
print("Введите значение длины: ")

w = int(input())

print("Введите значение высоты: ")
h = int(input())

print("Площадь прямоугольного треугольника = " + str(square_triangle_area(w, h)))

input()
