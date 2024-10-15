'''1. Четыре точки заданы своими координатами X(x1, x2, x3), Y(y1, y2, y3), Z(z1, z2, z3), T(t1,t2, t3).
Выяснить, какие из них находятся на минимальном расстоянии
друг от друга и вывести на экран значение этого расстояния. Вычисление расстояния между
двумя точками оформить в виде функции.
2. Напишите программу, которая выводит в одну строчку все делители переданного ей числа,
разделяя их пробелами'''

import math as m

def dist_3d_sqr(x1, y1, z1, x2, y2, z2) -> float:
    return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
def task1():
    points = []
    for point in ["x", "y", "z", "t"]:
        for dim in range(1, 3 + 1):
            cord = int(input(f"{point}{dim}: "))
            points.append(cord)


    dists = []
    points_pairs = []
    points_lits = ["x", "y", "z", "t"]
    for point1 in range(4):
        for point2 in range(point1 + 1, 4):

            points_pairs.append(points_lits[point1] + points_lits[point2])

            x1 = points[3 * point1]
            y1 = points[3 * point1 + 1]
            z1 = points[3 * point1 + 2]
            x2 = points[3 * point2]
            y2 = points[3 * point2 + 1]
            z2 = points[3 * point2 + 2]

            dists.append(dist_3d_sqr(x1, y1, z1, x2, y2, z2))

    min_dist = min(dists)
    for i in range(0, len(dists)):
        if dists[i] == min_dist:
            print(f"{points_pairs[i]}: {min_dist}")

def task2():
    n = int(input("заданное число: "))
    print(1, end=" ")
    for div in range(2, int(m.sqrt(n))):
        if n % div == 0:
            print(div, end=" ")