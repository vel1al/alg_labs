'''1. Создайте функцию input_data которая вызывается для ввода данных в консоли.
Пользователь вводит имя, фамилия, возраст, сделайте возврат данных из функции
в виде словаря.
2. Создайте функцию add_user которая принимает объект в виде словаря и
записывает в list.
3. Создайте цикл со счетчиком в котором функция input_data будет вызываться 5
раз, данные полученные из функции Input_data должны быть записаны с помощью
функции add_user в list.
4. Вывести получившийся список словарей в консоли.'''

def input_data() -> dict:
    name = input("имя: ")
    lastname = input("фамилия: ")
    age = int(input("возраст: "))

    return dict(name=name, lastname=lastname, age=age)

def add_user(list, user: dict):
    list.append(user)

def main():
    users = []

    for _ in range(5):
        user = input_data()
        add_user(users, user)

    print("список users:",users)