'''1. Найти максимальный элемент численного массива и поменять его местами с
минимальным.
2. Программа заполняет одномерный массив из 10 целых чисел числами,
считанными с клавиатуры. Определить среднее арифметическое всех чисел
массива. Заменить элементы массива большие среднего арифметического на'''
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