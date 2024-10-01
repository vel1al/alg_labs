#1. Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую
#из своих цифр.
#2. Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний
#элементы. Длину массива и его элементы ввести с клавиатуры. В программе описать
#процедуру для замены элементов массива. Вывести исходные и полученные массивы

#могут возникуть вопросы к делению на нуль. я расценивал так

def b_task1_condition(n) -> bool:
    for div in str(n):
        if(int(div) == 0):
            return False

        if n % int(div) != 0:
            return False

    return True

def task1():
    n = int(input("заданное N: "))

    print("удовлетворяют условию:", end=" ")
    for dig in range(1, n + 1):
        if(b_task1_condition(dig)):
            print(dig, end = " ")

def swap(arr, i, j):
    a1, a2 = arr[i], arr[j]
    arr[i], arr[j] = a2, a1

def task2():
    m = int(input("длинна массива: "))
    arr = []
    for i in range(m):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    print(arr)
    swap(arr, 0, m - 1)
    print(arr)

task2()