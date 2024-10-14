#1. Создайте функцию input_fruit которая вызывается для ввода данных в
#консоли. Пользователь вводит НАЗВАНИЕ_ФРУКТА, КОЛ-ВО_ФРУКТОВ,
#сделайте возврат данных из функции в виде кортежа (название, кол-во)
#2. Cоздайте бесконечный цикл while который вызывает функцию input_fruit до
#тех пор пока кол-во полученных яблок и апельсин в сумме не станет больше
#или равно 20
#3. Выведите результирующий список в виде словаря в консоль

def input_fruit() -> tuple:
    name = input("название фрукта: ")
    count = int(input("количество: "))

    return (name, count)

def main():
    fruits = {}

    while (fruits.get("Яблоко", 0) + fruits.get("Апельсин", 0)) <= 20:
        fruit_tuple = input_fruit()
        fruits.setdefault(fruit_tuple[0], 0)
        fruits[fruit_tuple[0]] += fruit_tuple[1]

    print(fruits)