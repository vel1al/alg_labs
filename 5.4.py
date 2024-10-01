import math as m

#Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
#Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2). Выяснить и вывести на экран, сколько точек лежит внутри окружности. Проверку, лежит ли точка внутри окружности, оформить в виде функции.

def b_is_palidrom(word) -> bool:
    return word == word[-1::]

def b_is_prime(n) -> bool:
    if(abs(n) <= 2):
        return True
    else:
        for div in range(0, int(m.sqrt(abs(n)))):
            if n % div == 0:
                return False

        return True

def task1():
    n = int(input("число n: "))
    for dig in range(1, n + 1):
        if(b_is_palidrom(str(bin(dig)))[2::]):
            if(b_is_prime(dig)):
                print(dig)

def b_is_nearly_equal(a, b, tol = 0.001):
    return abs(a - b) < tol

def b_is_in_round(a, b, r, p1, p2):
    dist = (p1 - a) ** 2 + (p2 - b) ** 2

    return b_is_nearly_equal(dist, r ** 2)

def task2():
    x0 = float(input("x0: "))
    y0 = float(input("y0: "))
    r = float(input("r: "))

    p1 = float(input("Px: "))
    p2 = float(input("Py: "))
    f1 = float(input("Fx: "))
    f2 = float(input("Fy: "))
    l1 = float(input("Lx: "))
    l2 = float(input("Ly: "))

    if(b_is_in_round(x0, y0, r, p1, p2)):
        print("точка P лежит в окружности")
    if(b_is_in_round(x0, y0, r, f1, f2)):
        print("точка F лежит в окружности")
    if(b_is_in_round(x0, y0, r, l1, l2)):
        print("точка L лежит в окружности")