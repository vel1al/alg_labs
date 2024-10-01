#1. Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т.
#д. Через сколько таких действий получится нуль?
#2. Даны 3 различных массива целых чисел. В каждом массиве найти произведение элементов
#и среднеарифметическое значение.

def digs_sum(n) -> int:
    sum = 0
    for dig in str(n):
        sum += int(dig)

    return sum

def task1():
    n = int(input("заданное N: "))

    count = 0
    while(n > 0):
        n -= digs_sum(n)
        count += 1

    print(count)

def task2_func(arr):
    prod, sum, count = 1, 0, 0
    for i in arr:
        prod *= i
        sum += i
        count += 1

    print(f"произведение: {prod}, среднеарифметическое: {round(sum/count, 2)}")

def task2_cycle():
    arr = []
    n = int(input(f"размер массива: "))
    for i in range(n):
        a = int(input(f"{i + 1} элемент: "))
        arr.append(a)

    task2_func(arr)
def task2():
    for _ in range(3):
        task2_cycle()

task2()