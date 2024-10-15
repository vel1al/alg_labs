'''1. Составить программу для нахождения чисел из интервала [М, N], имеющих наибольшее
количество делителей.
2.Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, p2). Выяснить,
какие из них находятся на максимальном расстоянии друг от друга и вывести на экран
значение этого расстояния. Вычисление расстояния между двумя точками оформить в виде
функции.'''

def divs(n) -> []:
    output = [1]
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            output.append(div)

    return output

def task1():
    m = int(input("заданное M: "))
    n = int(input("заданное N: "))

    max_count, master_value = 0, []
    for dig in range(m, n + 1):
        divs_count = len(divs(dig))

        if(divs_count > max_count):
            max_count = divs_count

            master_value.clear()
            master_value.append(dig)

        elif(divs_count == max_count):
            master_value.append(dig)


    if(len(master_value) > 1):
        print(f"числа {master_value} имеют {max_count} делителей")
    else:
        print(f"число {master_value[0]} имеет {max_count} делителей")


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