'''1. Даны катеты двух прямоугольных треугольников. Написать функцию вычисления длины
гипотенузы этих треугольников. Сравнить и вывести какая из гипотенуз больше, а какая
меньше.
2. Преобразовать строку так, чтобы буквы каждого слова в ней были отсортированы по алфавиту.'''

import math as m

def hyp(a, b) -> float:
    return round(m.sqrt(a**2 + b**2), 2)
def task_1():
    a1 = float(input("сторона а1: "))
    b1 = float(input("сторона b1: "))
    a2 = float(input("сторона а2: "))
    b2 = float(input("сторона b2: "))

    hyp1, hyp2 = hyp(a1, b1), hyp(a2, b2)
    if(hyp1 > hyp2):
        print(f"наибольшая: {hyp1}, наименьшая: {hyp2}")
    else:
        print(f"наибольшая: {hyp2}, наименьшая: {hyp1}")

def alpha_sort(word):
    out = ""
    for char in sorted(word):
        out += char

    return out

def task2():
    a = input("входная строка: ")
    for word in a.replace(",", "").replace(".", "").split():
        a = a.replace(word, alpha_sort(word))

    print(a)