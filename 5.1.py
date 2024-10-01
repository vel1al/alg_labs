import math as m

#Составить программу для вычисления площади разных геометрических фигур.
#Даны 3 различных массива целых чисел (размер каждого не превышает 15). В каждом массиве найти сумму элементов и среднеарифметическое значение.

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

def task2_func(arr):
    sum, count = 0, 0
    for i in arr:
        sum += i
        count += 1

    print(f"сумма: {sum}, среднеарифметическое: {sum/count}")

def task2_cycle():
    arr = []
    n = int(input(f"размер массива: "))
    for i in range(n):
        a = int(input(f"{i} элемент: "))

    task2_func(arr)
def task2():
    for _ in range(3):
        task2_cycle()