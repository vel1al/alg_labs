#1. Два натуральных числа называются «дружественными», если каждое из них равно сумме
#всех делителей (кроме его самого) другого (например, числа 220 и 284). Найти все пары
#«дружественных» чисел, которые не больше данного числа N.
#2. Даны длины сторон треугольника a, b, c. Найти медианы треугольника, сторонами которого
#являются медианы исходного треугольника. Для вычисления медианы проведенной к стороне
#а, использовать формулу Вычисление медианы оформить в виде функции

import math as m

def divs_sum(n) -> int:
    sum = 1
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            sum += div

    return sum

def b_is_friendly(a, b) -> bool:
    divs_a, divs_b = divs_sum(a), divs_sum(b)

    return a == divs_b and b == divs_a

def task1():
    n = int(input("заданное N: "))
    for pair_left in range(1, n + 1):
        for pair_right in range(pair_left + 1, n + 1):
            if(b_is_friendly(pair_left, pair_right)):
                print(f"пара: {pair_left} и {pair_right}")

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