#1. Найдите сумму и произведение элементов списка. Результаты вывести на экран.
#2. В массиве действительных чисел все нулевые элементы заменить на среднее
#арифметическое всех элементов массива.

def task1():
    N = int(input("кол-во элементов массива: "))
    arr = []
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    target_sum, target_prod = 0, 1
    for i in range(N):
        target_sum += arr[i]
        target_prod *= arr[i]

    print(f"искомая сумма: {target_sum}, искоммое произведение: {target_prod}")


def task2():
    N = int(input("кол-во элементов массива: "))
    arr, sum = [], 0
    for i in range(N):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

        sum += value

    swap = sum / N
    for i in range(N):
        if(arr[i] == 0):
            arr[i] = swap