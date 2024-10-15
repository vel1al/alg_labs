'''1. Создайте функцию которая вызывается для ввода данных в консоли.
Пользователь вводит имя, фамилия, возраст, сделайте возврат данных из функции
в виде словаря.
2. Создайте функцию которая принимает объект в виде словаря и записывает в
list.
Должен получиться list с названием users содержащий в себе последовательность
словарей типа user'''

def collect_data() -> dict:
    name = input("имя: ")
    lastname = input("фамилия: ")
    age = int(input("возраст: "))

    return dict(name=name, lastname=lastname, age=age)

def append_user(list, user: dict):
    list.append(user)

def main():
    users = []

    user = collect_data()
    append_user(users, user)
    print("список users:",users)