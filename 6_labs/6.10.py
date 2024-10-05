#1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на
#экран это значение, иначе сообщение об их отсутствии.
#2. Дан одномерный массив из 15 элементов. Элементам массива меньше 10
#присвоить нулевые значения, а элементам больше 20 присвоить 1. Вывести на экран
#монитора первоначальный и преобразованный массивы в строчку

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    arr_unique, arr_repeated = [], []
    for value in arr:
        if(value not in arr_unique):
            arr_unique.append(value)
        else:
            arr_repeated.append(value)

    if(len(arr_repeated) > 0):
        print("повторяющиеся элементы:", arr_repeated)
    else:
        print("повторяющиеся элементы отсуствуют")

def task2():
    arr = []
    for i in range(15):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    print("исходный массив:", end=" ") #идк, что означает "преобразованный массивы в строчку"
    for i in range(15):
        print(arr[i], end=" ")

    for i in range(15):
        if(arr[i] < 10):
            arr[i] = 0
        elif(arr[i] > 20):
            arr[i] = 1

    print("преобразованный массив:", end=" ")
    for i in range(15):
        print(arr[i], end=" ")