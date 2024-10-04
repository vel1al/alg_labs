#1. Дан одномерный массив, состоящий из N целочисленных элементов.
#Ввести массив с клавиатуры. Найти минимальный элемент. Вывести индекс минимального элемента на экран.
#Дан массив целых чисел. Переписать все положительные элементы во второй массив, соатльные - в третий.

def task1():
    N = int(input("кол-во элементов массива: "))
    min = int(input("1 элемент массива: "))
    arr = [min]
    for i in range(1, N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

        if(value < min):
            min = value

    print("минимальный элемент:", min)
    print("индекс минимального элемента:", arr.index(min))

def task2():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr2, arr3 = [], []
    for val in arr:
        if(val > 0):
            arr2.append(val)
            arr3.append(val)

    print("2-й массив:", arr2)
    print("3-й массив:", arr3)

task1()