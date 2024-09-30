import math as m

#3.1
def lab3_1():
    a = int(input("1-е число: "))
    b = int(input("2-е число: "))
    c = int(input("3-е число: "))

    if(a >= 1 and a <= 3):
        print(a)
    if (b >= 1 and b <= 3):
        print(b)
    if(c >= 1 and c <= 3):
        print(c)

#3.2
def lab3_2():
    year = int(input("номер года: "))

    days = 365
    if(year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0)):
        days += 1
    print("дней:", days)

def lab3_3():
    price = int(input("изначальная сумма: "))

    if price > 1000:
        price *= 0.95
    elif price > 500:
        price *= 0.97

    print("с учётом скидки:", price)

def lab3_4():
    dimension = int(input("номер единицы измерения: "))
    value = int(input("масса : "))

    coefficient = 1
    if dimension == 2:
        coefficient = 10**-6
    elif dimension == 3:
        coefficient = 10**-3
    elif dimension == 4:
        coefficient = 1000
    elif dimension == 5:
        coefficient = 100

    print("кг:", value * coefficient)

def lab3_5():
    a = int(input("1 число: "))
    b = int(input("2 число: "))
    c = int(input("3 число: "))
    d = int(input("4 число: "))

    min = a
    if(a < b):
        if(a < c):
            if(a > d):
                min = d
        else:
            if(c < d):
                min = c
            else:
                min = d
    elif(b < c):
        if(b < d):
            min = b
        else:
            min = d
    elif(c < d):
        min = c
    else:
        min = d

    print("косинус минимального:", m.cos(min))

def lab3_6():
    a = int(input("1 число: "))
    b = int(input("2 число: "))
    c = int(input("3 число: "))

    max = a
    if(b > a):
        if(b > c):
            max = b
        else:
            max = c
    elif(c > a):
        max = c

    print("синус максимального: ", m.sin(max))

def lab3_7():
    a1 = int(input("1-я сторона 1-о треугольника: "))
    b1 = int(input("2-я сторона 1-о треугольника: "))
    c1 = int(input("3-я сторона 1-о треугольника: "))

    a2 = int(input("1-я сторона 2-о треугольника: "))
    b2 = int(input("2-я сторона 2-о треугольника: "))
    c2 = int(input("3-я сторона 2-о треугольника: "))
    
    p1 = (a1+b1+c1) / 2 
    area1 = m.sqrt(p1*(p1 - a1)*(p1 - b1)*(p1 - c1)) 
    p2 = (a2 + b2 + c2) / 2
    area2 = m.sqrt(p2 * (p2 - a2) * (p2 - b2) * (p2 - c2))

    if(abs(area1 - area2) < 10**-6):
        print("ДА")
    else:
        print("НЕТ")

def lab3_8():
    ab = int(input("боковая сторона: "))
    c = int(input("основание: "))

    p = ab + (c/2)
    area = (c/2) * m.sqrt((p - c) * p)
    if(area % 2 == 0):
        area /= 2
    else:
        print("Не могу делить на 2!")

    print("площадь:", area)

def lab3_9():
    number = int(input("месяц: "))

    month = "undefined"
    if(number == 1):
        month = "January"
    elif(number == 2):
        month = "February"
    elif(number == 3):
        month = "March"
    elif(number == 4):
        month = "April"
    elif(number == 5):
        month = "May"
    elif(number == 6):
        month = "June"
    elif(number == 7):
        month = "July"
    elif(number == 8):
        month = "August"
    elif(number == 9):
        month = "September"
    elif(number == 10):
        month = "October"
    elif(number == 11):
        month = "November"
    elif(number == 12):
        month = "December"

    print(month)

def lab3_10():
    convertion_number = int(input("(1 - радианы в градусы. 2 - градусы в радианы): "))
    value = float(input("величина: "))

    if(convertion_number == 2):
        value *= (m.pi / 180)
    elif(convertion_number == 1):
        value *= (180 / m.pi)

    print("результат:", value)

def lab3_11():
    a = int(input("1 число: "))
    b = int(input("2 число: "))
    c = int(input("3 число: "))

    count = 0
    if(a > 0):
        count += 1
    if(b > 0):
        count += 1
    if(c > 0):
        count += 1

    print("положительных:", count)

def lab3_12():
    a = int(input("1 число: "))
    b = int(input("2 число: "))

    result = 0
    if((a * b) > 0):
        result = m.sqrt(a * b)
    else:
        result = (a + b) / 2

    print("результат:", result)

def lab3_13():
    a = int(input("1 сторона: "))
    b = int(input("2 сторона: "))
    c = int(input("3 сторона: "))

    hyp = a
    min = c
    if (b > a):
        if (b > c):
            hyp = b
        else:
            hyp = c
            min = a
    elif (c > a):
        hyp = c
        min = b

    sum = a + b + c
    if(hyp**2 == ((sum - hyp) ** 2 - (sum - hyp - min) * min * 2)):
        area = (sum - hyp - min) * min
        print("площадь:", area)
    else:
        print("НЕТ")

def lab3_14():
    a = int(input("1 сторона: "))
    b = int(input("2 сторона: "))
    c = int(input("3 сторона: "))

    if(a + b > c and a + c > b and b + c > a):
        p = (a + b + c) / 2
        area = m.sqrt(p * (p - a) * (p - b) * (p - c))
        print("площадь:", area)
    else:
        print("НЕТ")

def lab3_15():
    x = int(input("x: "))

    if(x>=0):
        print("f(x):", 0.5 - x ** 0.25)
    else:
        print("f(x):", (m.sin(x ** 2) ** 2) / (x + 1))

def lab4_1_1():
    price = int(input("цена 1кг: "))

    for coefficient in range(1, 11):
        print(f"{coefficient} кг стоит: {coefficient * price}")

def lab4_1_2():
    value = int(input("элемент последовательности: "))
    sum, count = value, 1
    while(value != 0):
        value = int(input("элемент последовательности: "))
        sum += value
        count += 1

    print(f"a){sum}\nb){count}")

def lab4_2_1():
    a = int(input("1 число: "))
    b = int(input("2 число: "))

    sum = b
    for value in range(a, b):
        sum += value

    print("сумма:", sum)

def lab4_2_2():
    value = int(input("элемент последовательности: "))
    sum, count = value, 1
    while(value < 0):
        value = int(input("элемент последовательности: "))
        sum += value
        count += 1

    print("среднее арифметическое положительных:", sum / count)

def lab4_3_1():
    a = int(input("1 число: "))
    b = int(input("2 число: "))

    sum = b ** 2
    for value in range(a, b):
        sum += value ** 2

    print("сумма:", sum)

def lab4_3_2():
    n = input("кол-во чисел в последовательности: ")
    sum, i = 0, 0
    value = int(input(f"элемент последовательности №{i + 1}: "))
    while(value % 2 == 0):
        sum += value
        i += 1

        value = int(input(f"элемент последовательности №{i + 1}: "))

    print("сумма первых четных чисел:", sum)

def lab4_4_1():
    a = int(input("1 число: "))

    sum = 200
    for value in range(a, 200):
        sum += value

    print("среднее арифметическое:", sum / (201 - a))

def lab4_4_2():
    n = input("кол-во чисел в последовательности: ")
    sum, i = 0, 0
    value = float(input(f"элемент последовательности №{i + 1}: "))
    while(value > 0):
        sum += value
        i += 1

        value = float(input(f"элемент последовательности №{i + 1}: "))

    print("сумма первых положительных чисел:", sum)

#5.1 повторяет 2.1

def lab4_5_2():
    N = int(input("степень N: "))

    K = 0
    while(N > 1):
        N /= 2
        K += 1

    print("показатель К:", K)

def lab4_6_1():
    a = int(input("1 число: "))

    sum = 50 ** 2
    for value in range(a, 50):
        sum += value ** 2

    print("сумма:", sum)

def lab4_6_2():
    N = int(input("число N: "))

    K = 1
    while(5 ** K < N):
        K += 1

    print("показатель К:", K)


#7.1 повторяет 1.2

#наибольшее К является бесконечностью. ниже ищеется наименьшее

def lab4_7_2():
    N = int(input("число N: "))

    K = 1
    while(2 ** K < N):
        K += 1

    print("показатель К:", K)

def lab4_8_1():
    n = input("кол-во чисел в последовательности: ")
    sum, i = 0, 0
    value = float(input(f"элемент последовательности №{i + 1}: "))
    while(value % 2 != 0):
        sum += value
        i += 1

        value = float(input(f"элемент последовательности №{i + 1}: "))

    print("сумма первых четных чисел:", sum)

def lab4_8_2():
    N = int(input("число N: "))

    sum, count = 0, 0
    while(N > 0):
        sum += N % 10
        count += 1
        N //= 10

    print(f"количество: {count}, сумма: {sum}")

def lab4_9_1():
    N = int(input("число N: "))

    value = 1
    while(value ** 2 <= N):
        value += 1

    print("число:", value ** 2)

def lab4_9_2():
    N = int(input("число N: "))
    value, shift = 1, 4
    while(value <= N):
        value += shift
        shift += 1

    print("число:", value)

def lab4_10_1():
    sum, i = 0, 0
    while(i < 20):
        mark = int(input(f"оценка {i+1}-о ученика: "))
        sum += mark
        i += 1

    print("средняя оценка:", sum / (i + 1))

def lab4_10_2():
    A = float(input("число А: "))

    sum, K = 1, 1
    while(sum < A):
        K += 1
        sum += 1/K

    print(f"наибольшее К:{K - 1}, сумма:{sum - 1/K}")

#11.1 составитель обезьяна, абсолютно не ясно, как получать исходные данные

def lab4_11_2():
    N = int(input("число N: "))

    K = 1
    while(K ** 2 < N):
        K += 1

    print("показатель К:", K - 1)

#12.1 аналогично 11.1

def lab4_12_2():
    pow = 0
    while(pow <= 20):
        print(2 ** pow)
        pow += 1

def lab4_13_1():
    sum_area, sum_people = 0, 0
    for i in range(0, 12):
        people = int(input(f"количество жителей {i+1}-о района: "))
        area = int(input(f"площадь {i+1}-о района: "))

        sum_people += people
        sum_area += area

    print("средняя плотность населения по области:", sum_people/sum_area)

def lab4_13_2():
    sum, age = 1, 1
    while(sum < 100):
        sum *= 2
        sum += (age + 1)

        age += 1

    print(f"к {age}-у дню рождения")

def lab4_14_1():
    for iter in range(0, 24//3 + 1):
        print(f"{iter*3} часов: {2**iter} клеток")

def lab4_14_2():
    min = float(input("минимальный x: "))
    max = float(input("максимальный x: "))
    step = float(input("шаг x: "))

    while(min <= max):
        print(f"f({min}) = {-0.5 * min + min}")
        min += step

def lab4_15_1():
    sum, distance = 10, 10
    for day in range(2, 7 + 1):
        distance = distance + distance * 0.1
        sum += distance
        print(f"{day}-й день: {distance} км")
    print(f"итого: {sum} км")

def lab4_15_2():
    N = int(input("число N: "))

    prod, sum = 1, 0
    while(N > 0):
        prod *= N % 10
        sum += N % 10
        N //= 10

    print(f"сумма: {sum}, произведение: {prod}")

#далее задания повторяются с предыдущими номерами. 16 лаба - задания 1, 17 - задания 2 и т.д.