'''1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с.
2. Cоставить программу вычисления площади выпуклого четырехугольника, заданного
длинами четырех сторон и диагонали.'''

import math as m

def b_is_in_dig(value, a, b, c) -> bool:
    return str(a) in str(value) and str(b) in str(value) and str(c) in str(value)

def task1():
    n = int(input("заданное N: "))
    a = float(input("заданное a: "))
    b = float(input("заданное b: "))
    c = float(input("заданное c: "))

    count = 0
    for dig in range(100, n + 1):
        if(b_is_in_dig(dig, a, b, c)):
            count += 1

    print("количество", count)

def task2():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))

    dg = float(input("dg: "))

    p1 = (a + b + dg) / 2
    p2 = (c + d + dg) / 2

    area = round(m.sqrt(p1*(p1-a)*(p1-b)*(p1-dg)) + m.sqrt(p2*(p2-d)*(p2-d)*(p2-dg)), 2)
    print("площадь:", area)