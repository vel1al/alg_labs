#1. Найти наименьший нечетный элемент списка и вывести его на экран.
#2. Даны массивы A и B одинакового размера 10. Поменять местами их содержимое
#и вывести вначале элементы преобразованного массива A, а затем — элементы
#преобразованного массива B

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    min_value = None
    for value in arr:
        if(value % 2 == 1):
            if(value < min_value or min_value == None):
                min_value = value

    if(min_value):
        print("минимальный нечётный элемент:",min_value)
    else:
        print("нечётные элементы отсутствуют отсуствуют")

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

    print(A,B)