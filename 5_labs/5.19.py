'''1. Даны длины сторон треугольника a, b, c. Найти медианы треугольника, сторонами которого
являются медианы исходного треугольника. Для вычисления медианы проведенной к стороне
а, использовать формулу Вычисление медианы оформить в виде функции.
2. Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2). Выяснить и вывести
на экран, сколько точек лежит внутри окружности. Проверку, лежит ли точка внутри
окружности, оформить в виде функции'''

import math as m

def median(base, cat1, cat2) -> float:
    return round(m.sqrt((2*(cat1 ** 2) + 2*(cat2 ** 2) - base**2) / 4), 2)

def task1():
    a = float(input("сторона а: "))
    b = float(input("сторона b: "))
    c = float(input("сторона c: "))

    a2 = median(a, b, c)
    b2 = median(b, a, c)
    c2 = median(c, b, a)

    med2_a = median(a2, b2, c2)
    med2_b = median(b2, a2, c2)
    med2_c = median(c2, b2, a2)

    print(f"медиана к медиане к a: {med2_a}, медиана к медиане к b: {med2_b}, медиана к медиане к c: {med2_c}")

def b_is_nearly_equal(a, b, tol = 0.001) -> bool:
    return abs(a - b) < tol

def b_is_in_round(a, b, r, p1, p2) -> bool:
    dist = (p1 - a) ** 2 + (p2 - b) ** 2

    return b_is_nearly_equal(dist, r ** 2)

def task2():
    x0 = float(input("x0: "))
    y0 = float(input("y0: "))
    r = float(input("r: "))

    p1 = float(input("Px: "))
    p2 = float(input("Py: "))
    f1 = float(input("Fx: "))
    f2 = float(input("Fy: "))
    l1 = float(input("Lx: "))
    l2 = float(input("Ly: "))

    if(b_is_in_round(x0, y0, r, p1, p2)):
        print("точка P лежит в окружности")
    if(b_is_in_round(x0, y0, r, f1, f2)):
        print("точка F лежит в окружности")
    if(b_is_in_round(x0, y0, r, l1, l2)):
        print("точка L лежит в окружности")