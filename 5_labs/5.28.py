#1. Натуральное число, в записи которого n цифр, называется числом Армстронга, если сумма
#его цифр, возведенная в степень n, равна самому числу. Найти все числа Армстронга от 1 до
#к.
#2. Составить программу, которая изменяет последовательность слов в строке на обратную.

def digs_sum(n) -> int:
    sum = 0
    for dig in str(n):
        sum += int(dig)

    return sum

def b_is_armstrong(a) -> bool:
    dis_count = len(str(a))
    return (digs_sum(a) ** dis_count) == a

def task1():
    n = int(input("заданное N: "))
    for value in range(1, n + 1):
        if(b_is_armstrong(value)):
            print(value)

def flip_arr(arr) -> str:
    output = ""
    for i in range(len(arr) - 1, -1, -1):
        word = arr[i]
        if ',' in word or "." in word:
            word = word[len(word) - 1] + word[:len(word) - 1] + " "
        else:
            word += " "

        output += word

    return output
def task2():
    string = input("входная строка: ")
    print("с обратной последовательностью:", flip_arr(string.split()))