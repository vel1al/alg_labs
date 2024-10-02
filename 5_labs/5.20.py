#1. Составить программу, которая изменяет последовательность слов в строке на обратную.
#2. Напишите программу, которая выводит в одну строчку все делители переданного ей числа,
#разделяя их пробелами.

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
def task1():
    string = input("входная строка: ")
    print("с обратной последовательностью:", flip_arr(string.split()))

def task2():
    n = int(input("заданное число: "))
    print(1, end=" ")
    for div in range(2, int(m.sqrt(n))):
        if n % div == 0:
            print(div, end=" ")