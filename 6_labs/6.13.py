#1. Дан одномерный массив целых чисел. Проверить, есть ли в нем одинаковые
#элементы. Вывести эти элементы и их индексы.
#2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
#меньшие 15 их удвоенными значениями. Вывести на экран монитора
#преобразованный массив.

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr_unique, arr_unique_indexes, arr_repeat = [], [], []
    for i in range(N):
        if (arr[i] not in arr_unique):
            arr_unique.append(arr[i])
            arr_unique_indexes.append(i)
        else:
            str = f"элемент {arr[i]} под индексами {i} и {arr_unique_indexes[arr_unique.index(arr[i])]}"
            arr_repeat.append(str)

    for str in arr_repeat:
        print(str)

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