'''1. Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую
из своих цифр.
2. Даны длины сторон треугольника a, b, c. Найти медианы треугольника, сторонами которого
являются медианы исходного треугольника. Для вычисления медианы проведенной к стороне
а, использовать формулу Вычисление медианы оформить в виде функции'''

import math as m

def b_task1_condition(n) -> bool:
    for div in str(n):
        if(int(div) == 0):
            return False

        if n % int(div) != 0:
            return False

    return True

def task1():
    n = int(input("заданное N: "))

    print("удовлетворяют условию:", end=" ")
    for dig in range(1, n + 1):
        if(b_task1_condition(dig)):
            print(dig, end = " ")

def median(base, cat1, cat2) -> float:
    return round(m.sqrt((2*(cat1 ** 2) + 2*(cat2 ** 2) - base**2) / 4), 2)

def task2():
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