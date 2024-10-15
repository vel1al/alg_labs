'''1. Создайте функцию input_data которая вызывается для ввода данных в
консоли. Пользователь вводит имя, фамилия, возраст, сделайте возврат
данных из функции в виде словаря.
2. Создайте функцию add_user которая принимает объект в виде словаря и
записывает в list.
3. Создайте цикл со счетчиком в котором функция input_data будет
вызываться 6 раз, данные полученные из функции Input_data должны быть
записаны с помощью функции add_user в list.
4. В результирующем list который содержит 6 словарей, сделайте поиск по
ключу “возраст” и выведите запись из list с самым большим возрастом.'''

def input_data() -> dict:
    name = input("имя: ")
    lastname = input("фамилия: ")
    age = int(input("возраст: "))

    return dict(name=name, lastname=lastname, age=age)

def add_user(list, user: dict):
    list.append(user)

def main():
    users = []

    for _ in range(6):
        user = input_data()
        add_user(users, user)

    max_age_user = users[0]
    for user in users:
        if(max_age_user.get("age") < user.get("age")):
            max_age_user = user

    print("user с максимальным age:", max_age_user)