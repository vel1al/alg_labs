#1. Составить программу для нахождения чисел из интервала [М, N], имеющих наибольшее
#количество делителей.
#2. Cоставить программу вычисления площади выпуклого четырехугольника, заданного
#длинами четырех сторон и диагонали

import math as m

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