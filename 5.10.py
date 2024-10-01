#1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с.
#2. Составить программу, которая изменяет последовательность слов в строке на обратную.

def b_is_in_dig(value, a, b, c) -> bool:
    return str(a) in str(value) and str(b) in str(value) and str(c) in str(value)

def task1():
    n = int(input("заданное N: "))
    a = float(input("заданное a: "))
    b = float(input("заданное b: "))
    c = float(input("заданное c: "))

    count = 0
    for dig in range(100, n + 1):
        if(b_is_in_dig(dig, a, b, c)):
            count += 1

    print("количество", count)

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