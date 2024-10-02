#1. Два простых числа называются «близнецами», если они отличаются друг от друга на 2
#(например, 41 и 43). Напечатать все пары «близнецов» из отрезка [n, 2n], где n — заданное
#натуральное число, большее 2..
#2. Даны две матрицы А и В. Написать программу, меняющую местами максимальные
#элементы этих матриц. Нахождение максимального элемента матрицы оформить в виде
#функции.

import math as m

def b_is_prime(n) -> bool:
    if(abs(n) <= 2):
        return True
    else:
        for div in range(0, int(m.sqrt(abs(n)))):
            if n % div == 0:
                return False

        return True


def task1():
    n = int(input("заданное N: "))
    for pair_left in range(n, 2*n - 1):
        if(b_is_prime(pair_left) and b_is_prime(pair_left + 2)):
            print(pair_left, pair_left + 2)

def max_maxtrix(a):
    max = 0
    for dig in a:
        if dig > max:
            max = dig

    return max

def get_values(n, m) -> []:
    values = []
    for i in range(0, n * m):
        value = int(input(f"заданный элемент {(i // m) + 1} строки {(i % m) + 1} столбца: "))
        values.append(value)

    return values

def print_matrix(arr, n, m):
    for i in range(0, n):
        for j in range(0, m):
            print(arr[i * m + j], end=" ")
        print("\n")


def replace_value(arr, target, new):
    for i in range(0, len(arr)):
        if(arr[i] == target):
            arr[i] = new

def task2():
    n1 = int(input("заданное количество строк 1-й матрицы: "))
    m1 = int(input("заданное количество столбцов 1-й матрицы: "))
    A = get_values(n1, m1)

    n2 = int(input("заданное количество строк 2-й матрицы: "))
    m2 = int(input("заданное количество столбцов 2-й матрицы: "))
    B = get_values(n2, m2)

    print_matrix(A, n1, m1)
    print_matrix(B, n2, m2)

    max_a, max_b = max_maxtrix(A), max_maxtrix(B)

    replace_value(A, max_a, max_b)
    replace_value(B, max_b, max_a)

    print_matrix(A, n1, m1)
    print_matrix(B, n2, m2)
