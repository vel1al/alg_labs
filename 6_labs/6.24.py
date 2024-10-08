#1. В одномерном числовом массиве D длиной n вычислить сумму элементов с
#нечетными индексами. Вывести на экран массив D, полученную сумму.
#2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
#меньшие 15 их удвоенными значениями. Вывести на экран монитора
#преобразованный массив.

def task1():
    N = int(input("кол-во элементов массива: "))
    D = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        D.append(value)

    target_sum = 0
    for i in range(N):
        if(i % 2 == 1):
            target_sum += D[i]

    print(D, target_sum)

def task2():
    arr = []
    for i in range(8):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    print("исходный массив:", arr)

    for i in range(8):
        if(arr[i] < 15):
            arr[i] = arr[i] * 2

    print("модифицированный массив:", arr)