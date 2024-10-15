'''1. Дан одномерный массив, состоящий из N вещественных элементов. Ввести
массив с клавиатуры. Найти и вывести минимальный по модулю элемент. Вывести
массив на экран в обратном порядке.
2. Даны массивы A и B одинакового размера 10. Вывести исходные массивы.
Поменять местами их содержимое и вывести в начале элементы преобразованного
массива A, а затем — элементы преобразованного массива B.'''

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = float(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    min = arr[0]
    for value in arr:
        if(abs(value) < abs(min)):
            min = value

    print("минимальный элемент:", min)
    for i in range(N - 1, -1, -1):
        print(arr[i])

def task2():
    A, B = [], []
    for i in range(10):
        value = float(input(f"{i + 1} элемент массива A: "))
        A.append(value)
    for i in range(10):
        value = float(input(f"{i + 1} элемент массива B: "))
        B.append(value)

    print(A, B)

    C = A.copy()
    A = B
    B = C

    print(A, B)