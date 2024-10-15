'''1. Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его площадь, если угол
между сторонами длиной X и У — прямой. Использовать две подпрограммы для вычисления
площадей: прямоугольного треугольника и прямоугольника.
2. Напишите программу, которая переводит переданное ей неотрицательное целое число в
10-значный восьмеричный код, сохранив лидирующие нули.'''

import math as m

def area_tri_right(a, b) -> float:
    return (a * b) / 2

def area_4cr_right(a, b) -> float:
    return a * b

def task1():
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    t = float(input("t: "))

    area = area_4cr_right(x, y) + area_tri_right(round(m.sqrt(z ** 2 - (t - y) ** 2), 2), abs(t - y))
    print("площадь:", area)

def task2():
    n = int(input("заданное число: "))
    oct_view = oct(n)[2::]

    output = "0" * (10 - len(oct_view)) + oct_view
    print("10-значная восьмеричная запись:", output)