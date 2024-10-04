#1. Дан одномерный массив, состоящей из N целочисленных элементов. Ввести
#массив с клавиатуры. Найти максимальный элемент. Вывести массив на экран в обратном порядке
#2. В массиве действительных чисел все нулевые элементы заменить на среднее арифметиеское всех элементов массива.

def task1():
    N = int(input("кол-во элементов массива: "))
    max, arr = 0, []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

        if(value > max):
            max = value

    print("максимальный элемент:", max)
    for i in range(N - 1, -1, -1):
        print(arr[i])

def task2_alg(arr):
    sum, count = 0, 0
    for i in arr:
        sum += i
        count += 1

    rep = sum / count
    for i in range(count):
        if(arr[i] == 0):
            arr[i] = rep
def task2():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    task2_alg(arr)
    print(arr)

task2()