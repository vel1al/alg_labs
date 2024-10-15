'''1. Составить программу для вычисления площади разных геометрических фигур.
2.Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, p2). Выяснить,
какие из них находятся на максимальном расстоянии друг от друга и вывести на экран
значение этого расстояния. Вычисление расстояния между двумя точками оформить в виде
функции.'''

import math as m

def area_tri1(a, b, c) -> float:
    p = (a+b+c)/2
    return round(m.sqrt(p*(p-a)*(p-b)*(p-c)), 2)

def area_tri2(a, h) -> float:
    return (a * h) / 2

def area_rnd(r) -> float:
    return m.pi*(r**2)

def area_sqr(a) -> float:
    return a**2

def area_tr(a, b, h) -> float:
    return ((a + b) / 2) * h

def dist_2d_sqr(x1, y1, x2, y2) -> float:
    return (x2 - x1) ** 2 + (y2 - y1) ** 2
def task2():
    points = []
    for point in ["x", "y", "z", "t"]:
        for dim in range(1, 2 + 1):
            cord = int(input(f"{point}{dim}: "))
            points.append(cord)


    dists = []
    points_pairs = []
    points_lits = ["x", "y", "z", "t"]
    for point1 in range(4):
        for point2 in range(point1 + 1, 4):

            points_pairs.append(points_lits[point1] + points_lits[point2])

            x1 = points[2 * point1]
            y1 = points[2 * point1 + 1]
            x2 = points[2 * point2]
            y2 = points[2 * point2 + 1]

            dists.append(dist_2d_sqr(x1, y1, x2, y2))

    max_dist = max(dists)
    for i in range(0, len(dists)):
        if dists[i] == max_dist:
            print(f"{points_pairs[i]}: {max_dist}")