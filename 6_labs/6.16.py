#1. Дан одномерный массив, состоящий из N целочисленных элементов. Ввести
#массив с клавиатуры. Найти максимальный элемент. Вывести массив на экран в
#обратном порядке.
#2. В массиве действительных чисел все нулевые элементы заменить на среднее
#арифметическое всех элементов массива.

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    max = arr[0]
    for value in arr:
        if (value > max):
            max = value

    print("максимальный элемент:", max)
    for i in range(N - 1, -1, -1):
        print(arr[i])

def task2():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = float(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    sum = 0
    for i in arr:
        sum += i

    average = sum / N
    for i in range(N):
        if (arr[i] == 0):
            arr[i] = average

    print(f"среднее арифметическое: {average}, модифицированный массив: {arr}")