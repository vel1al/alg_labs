#1. Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т.
#д. Через сколько таких действий получится нуль?
#2. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых
#представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.

def digs_sum(n) -> int:
    sum = 0
    for dig in str(n):
        sum += int(dig)

    return sum

def task1():
    n = int(input("заданное N: "))

    count = 0
    while(n > 0):
        n -= digs_sum(n)
        count += 1

    print(count)

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
def task2():
    n = int(input("число n: "))
    for dig in range(1, n + 1):
        if(b_is_palidrom(str(bin(dig)))[2::]):
            if(b_is_prime(dig)):
                print(dig)