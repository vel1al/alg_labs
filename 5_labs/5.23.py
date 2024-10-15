'''1. Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую
из своих цифр.
2. Пользователь вводит две стороны трех прямоугольников. Вывести их площади.'''

def b_task1_condition(n) -> bool:
    for div in str(n):
        if(int(div) == 0):
            return False

        if n % int(div) != 0:
            return False

    return True

def task1():
    n = int(input("заданное N: "))

    print("удовлетворяют условию:", end=" ")
    for dig in range(1, n + 1):
        if(b_task1_condition(dig)):
            print(dig, end = " ")

def area_4cr(a, b) -> float:
    return a * b

def task2_cycle():
    a = float(input("сторона а: "))
    b = float(input("сторона b: "))

    print(f"площадь: {area_4cr(a, b)}")
def task2():
    for _ in range(3):
        task2_cycle()