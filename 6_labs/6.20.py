'''1. Найти максимальный элемент численного массива и поменять его местами с
минимальным.
2. Программа заполняет одномерный массив из 10 целых чисел числами,
считанными с клавиатуры. Определить среднее арифметическое всех чисел
массива. Заменить элементы массива большие среднего арифметического на 1'''

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    min_value, max_value = arr[0], arr[0]
    min_index, max_index = 0, 0
    for i in range(N):
        if(arr[i] > max_value):
            max_value = arr[i]
            max_index = i
        elif(arr[i] < min_value):
            min_value = arr[i]
            min_index = i

    arr[max_index] = min_value
    arr[min_index] = max_value
    print(arr)

def task2():
    arr = []
    for i in range(10):
        value = float(input(f"{i + 1} элемент массива A: "))
        arr.append(value)

    sum = 0
    for value in arr:
        sum += value
    average = sum / 10

    for i in range(10):
        if(arr[i] > average):
            arr[i] = 1

    print(f"среднее арифметическое: {average}, модифицированный массив: {arr}")