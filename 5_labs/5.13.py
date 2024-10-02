#1. Натуральное число, в записи которого n цифр, называется числом Армстронга, если сумма
#его цифр, возведенная в степень n, равна самому числу. Найти все числа Армстронга от 1 до n.
#2. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать
#координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало
#координат с точкой, минимальный. Вычисления оформить в виде функции.

import math as m

def digs_sum(n) -> int:
    sum = 0
    for dig in str(n):
        sum += int(dig)

    return sum

def b_is_armstrong(a) -> bool:
    dis_count = len(str(a))
    return (digs_sum(a) ** dis_count) == a

def task1():
    n = int(input("заданное N: "))
    for value in range(1, n + 1):
        if(b_is_armstrong(value)):
            print(value)

def angle_cos(point_x, point_y) -> float:
    return point_x / m.sqrt(point_x ** 2 + point_y ** 2)

def task2():
    x1 = float(input("сторона x1: "))
    x2 = float(input("сторона x2: "))
    y1 = float(input("сторона y1: "))
    y2 = float(input("сторона y2: "))
    z1 = float(input("сторона z1: "))
    z2 = float(input("сторона z2: "))

    cos_x = angle_cos(x1, x2)
    cos_y = angle_cos(y1, y2)
    cos_z = angle_cos(z1, z2)

    if(cos_y > cos_x):
        if(cos_y > cos_z):
            print("координаты:", y1, y2)
        else:
            print("координаты:", z1, z2)
    elif(cos_z > cos_x):
        print("координаты:", z1, z2)
    else:
        print("координаты:", x1, x2)

task2()