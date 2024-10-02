#1. Вычислить площадь правильного шестиугольника со стороной а, используя подпрограмму
#вычисления площади треугольника.
#2. Напишите функцию, которая переводит переданное ей неотрицательное целое число в 10-
#значный восьмеричный код, сохранив лидирующие нули.

import math as m

def area_r_tri(a) -> float:
    return round((a**2 * m.sqrt(3)) / 4, 2)

def area_6cr(a) -> float:
    area = 0
    for _ in range(6):
        area += area_r_tri(a)

    return area

def task2():
    n = int(input("заданное число: "))
    oct_view = oct(n)[2::]

    output = "0" * (10 - len(oct_view)) + oct_view
    print("10-значная восьмеричная запись:", output)