#1. Вычислить площадь правильного шестиугольника со стороной а, используя подпрограмму
#вычисления площади треугольника.
#2. Пользователь вводит две стороны трех прямоугольников. Вывести их площади.

import math as m

def area_r_tri(a) -> float:
    return round((a**2 * m.sqrt(3)) / 4, 2)

def area_6cr(a) -> float:
    area = 0
    for _ in range(6):
        area += area_r_tri(a)

    return area
def area_4cr(a, b) -> float:
    return a * b

def task2_cycle():
    a = float(input("сторона а: "))
    b = float(input("сторона b: "))

    print(f"площадь: {area_4cr(a, b)}")
def task2():
    for _ in range(3):
        task2_cycle()