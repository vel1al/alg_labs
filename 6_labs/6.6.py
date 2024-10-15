'''1. Дан одномерный массив из 10 целых чисел. Найти максимальный элемент и
сравнить с ним остальные элементы. Вывести количество меньших максимального и
больших максимального элемента.

странное задание, очевидно, что все элементы будут меньше максимального.


2. Одномерный массив из 10-и целых чисел заполнить с клавиатуры, определить
сумму тех чисел, которые > 5'''

def task1():
    arr = []
    for i in range(10):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    max_value = arr[0]
    for value in arr:
        if(value > max_value):
            max_value = value

    bigger, smaller = 0, 0
    for value in arr:
        if(value > max_value):
            bigger += 1
        elif(value < max_value):
            smaller += 1

    print(f"{arr} - максимальный элемент: {max_value}, меньше: {smaller}, больше: {smaller}")

def task2():
    arr = []
    for i in range(10):
        value = int(input(f"{i + 1} элемент массива: "))
        arr.append(value)

    target_sum = 0
    for value in arr:
        if(value > 5):
            target_sum += value

    print(f"искомая сумма: {target_sum}")