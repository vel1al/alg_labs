'''1. Создайте функцию input_data которая вызывается для ввода данных в
консоли. Пользователь вводит имя, фамилия, возраст, сделайте возврат
данных из функции в виде словаря.
2. Создайте функцию add_user которая принимает объект в виде словаря и
записывает в list.
3. Создайте цикл со счетчиком в котором функция input_data будет
вызываться 6 раз, данные полученные из функции Input_data должны быть
записаны с помощью функции add_user в list.
4. В результирующем list который содержит 6 словарей, сделайте поиск по
ключам “фамилия” и “имя” найдите совпадение по одному из полей с другими
словарями хранящимися в list:
- есть совпадение: вывести совпадающие записи
- нет совпадений: вывести текст совпадений не найдено'''

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

    users_repeated = []
    for i in range(6):
        user_name, user_lastname, user_age = users[i].values()
        for i2 in range(i, 6):
            user2_name, user2_lastname, user2_age = users[i2].values()

            if (user2_name == user_name or user2_lastname == user_lastname):
                if(users[i] not in users_repeated):
                    users_repeated.append(users[i])

    if(len(users_repeated) > 0):
        print("users с одним и более одинаковыми полями:", users_repeated)
    else:
        print("совпадений не найдено")