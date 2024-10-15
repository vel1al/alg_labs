'''1. Найти наибольший элемент списка, который делиться на 2 без остатка и вывести
его на экран.
2. Дан одномерный массив целого типа. Получить другой массив, состоящий только
из четных чисел исходного массива, меньше 10, или сообщить, что таких чисел нет.
Полученный массив вывести в порядке возрастания элементов.'''

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    max_value = None
    for value in arr:
        if(value % 2 == 0):
            if(value > max_value):
                max_value = value

    if(max_value):
        print("максимальный элемент кратный 2:",max_value)
    else:
        print("элементы кратных 2 отсуствуют")

#не знаю, разрешено юзать sorted() или нет. добавил сортировку пузырьком, чтобы вопросов точно не возникало.
def sort_arr(arr):
    bswapped = True

    while bswapped:
        bswapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

def task2():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr2 = []
    for value in arr:
        if(value % 2 == 0 and value < 10):
            arr2.append(value)

    if(len(arr2) > 0):
        sort_arr(arr2) ##или sorted(arr2)
        print("полученный массив:", arr2)
    else:
        print("чётных элементов меньше 10 нет")