#1. Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных чисел,
#стоящих рядом.
#2. Дан целочисленный массив размера 10. Создать новый массив, удалив все
#одинаковые элементы, оставив их 1 раз

def task1():
    arr = []
    for i in range(10):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    for i in range(10 - 1):
        if(arr[i] < 0 and arr[i+1] < 0):
            print(f"({arr[i]} {arr[i + 1]})", end=" ")

def task2():
    arr = []
    for i in range(10):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr_unique = []
    for value in arr:
        if(value not in arr_unique):
            arr_unique.append(value)

    print(arr_unique)