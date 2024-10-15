'''1. Создайте функцию input_fruit которая вызывается для ввода данных в
консоли. Пользователь вводит НАЗВАНИЕ_ФРУКТА, КОЛ-ВО_ФРУКТОВ,
сделайте возврат данных из функции в виде кортежа (название, кол-во)
2. Cоздайте бесконечный цикл while который вызывает функцию input_fruit
прервать цикл если будет введен фрукт “Фейхоа”
3. Выведите результирующий список в виде словаря в консоль, не добавлять
в результирующий список “Фейхоа”.'''

def input_fruit() -> tuple:
    name = input("название фрукта: ")
    count = int(input("количество: "))

    return (name, count)

def main():
    fruits = {}

    while True:
        fruit_tuple = input_fruit()
        if(fruit_tuple[0] == "Фейхоа"):
            break

        fruits.setdefault(fruit_tuple[0], 0)
        fruits[fruit_tuple[0]] += fruit_tuple[1]

    print(fruits)