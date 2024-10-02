#1. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых
#представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
#2. Составить программу для вычисления площади разных геометрических фигур.

import math as m

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