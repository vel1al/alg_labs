'''1. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых
представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
2. Составить программу, которая изменяет последовательность слов в строке на обратную.'''

import math as m

def b_is_palidrom(word) -> bool:
    return word == word[-1::]

def b_is_prime(n) -> bool:
    if(abs(n) <= 2):
        return True
    else:
        for div in range(0, int(m.sqrt(abs(n)))):
            if n % div == 0:
                return False

        return True
def task1():
    n = int(input("число n: "))
    for dig in range(1, n + 1):
        if(b_is_palidrom(str(bin(dig)))[2::]):
            if(b_is_prime(dig)):
                print(dig)

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