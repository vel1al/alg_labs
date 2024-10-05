#1. Дан массив целых чисел. Найти сумму элементов с четными номерами и
#произведение элементов с нечетными номерами. Вывести сумму и произведение.
#2. Переставить в одномерном массиве минимальный элемент и максимальный

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    target_sum, target_prod = 0, 1
    for i in range(N):
        if(i % 2 == 0):
            target_sum += arr[i]
        else:
            target_prod *= arr[i]

    print(f"искомая сумма: {target_sum}, искоммое произведение: {target_prod}")

def task2():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    min_value, max_value = arr[0], arr[0]
    min_index, max_index = 0, 0
    for i in range(N):
        if(arr[i] > max):
            max = arr[i]
            max_index = i
        elif(arr[i] < min):
            min = arr[i]
            min_index = i

    arr[max_index] = min
    arr[min_index] = max
    print(arr)