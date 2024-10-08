#1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на
#экран эти значения.
#2. Дан одномерный массив целого типа. Получить другой массив, состоящий только
#из нечетных чисел исходного массива или сообщить, что таких чисел нет.
#Полученный массив вывести в порядке убывания элементов

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr_unique, arr_repeat = [], []
    for value in arr:
        if(value not in arr_unique):
            arr_unique.append(value)
        else:
            arr_repeat.append(value)

    if(len(arr_repeat) > 0):
        print(arr_repeat)
    else:
        print("повторяющиеся элементы отсутствуют")

#не знаю, разрешено юзать sorted() или нет. добавил сортировку пузырьком, чтобы вопросов точно не возникало.
def sort_arr(arr):
    bswapped = True

    while bswapped:
        bswapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
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
        if(value % 2 == 1 and value < 10):
            arr2.append(value)

    if(len(arr2) > 0):
        sort_arr(arr2) #или sorted(arr2, reverse = true)
        print("полученный массив:", arr2)
    else:
        print("нечётных элементов меньше 10 нет")