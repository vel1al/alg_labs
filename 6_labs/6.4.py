'''1. Дан массив целых чисел. Найти максимальный элемент массива и его
порядковый номер.
2. Дан одномерный массив целого типа. Получить другой массив, состоящий только
из нечетных чисел исходного массива или сообщить, что таких чисел нет.
Полученный массив вывести в порядке убывания элементов.'''

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    max_value, max_index = arr[0], 0
    for i in range(N):
        if(arr[i] > max_value):
            max_value = arr[i]
            max_index = i

    print(f"максимальный элемент {max_value} под индексом {max_index}")

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
        if(value % 2 != 0):
            arr2.append(value)

    if(len(arr2) > 0):
        sort_arr(arr2)  ##или sorted(arr2)
        print("arr2")
    else:
        print("нечётные элементы отсуствуют")
