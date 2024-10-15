'''На складе имеются фрукты в кол-ве штук:
sklad_1 (Абрикос=50, Авокадо=50, Алыча=50, Апельсин=50, Арбуз=50)
sklad_2 (Гранат=20, Грейпфрут=4, Груша=10, Дыня=10, Инжир=20, Кешью=100)
1. Создайте функцию input_fruit Пользователь вводит НАЗВАНИЕ_ФРУКТА,
КОЛ-ВО_ФРУКТОВ, сделайте возврат данных из функции в виде кортежа
(название, кол-во)
2. Cоздайте бесконечный цикл while который вызывает функцию input_fruit
и оформляет заявку на необходимое кол-во фруктов, пользователь указывает
название фрукта и кол-во, в цикле проверяется сколько осталось на складе..
Сообщать пользователю сколько осталось данного фрукта, если пользователь
запросил больше чем было на складе
Остановить приём заявок когда будет больще 4 наименования в заказе
3. Выведите результирующий список в виде словаря в консоль, Каждый склад
ввести отдельным словарем. Вывести исходное кол-во на складе. Вывести
остаток на складе. Вывести заказ.'''

def input_fruit() -> tuple:
    name = input("название фрукта: ")
    count = int(input("количество: "))

    return (name, count)

def append_fruit(fruits, fruit):
    fruits.setdefault(fruit[0], 0)
    fruits[fruit[0]] += fruit[1]

def print_default_dict(sklad, order):
    default_dict = {}
    for stored_fruit in sklad.keys():
        append_fruit(default_dict, (stored_fruit, sklad[stored_fruit] + order.get(stored_fruit, 0)))

    print(default_dict)

#поведение, если введён фрукт, не находящийся ни в одном складе, не задано.
def main():
    sklad_1 = {'Абрикос': 50, 'Авокадо': 50, 'Алыча': 50, 'Апельсин': 50, 'Арбуз': 50}
    sklad_2 = {'Гранат': 20, 'Грейпфрут': 4, 'Груша': 10, 'Дыня': 10, 'Инжир': 20, 'Кешью': 100}
    order = {}

    while len(order.keys()) < 4:
        fruit_tuple = input_fruit()

        if (fruit_tuple[0] in sklad_1.keys()):
            if(sklad_1[fruit_tuple[0]] >= fruit_tuple[1]):
                append_fruit(order, fruit_tuple)
                append_fruit(sklad_1, (fruit_tuple[0], -fruit_tuple[1]))
            else:
                print(f"{fruit_tuple[0]} осталось {sklad_1[fruit_tuple[0]]}")
        if (fruit_tuple[0] in sklad_2.keys()):
            if (sklad_2[fruit_tuple[0]] >= fruit_tuple[1]):
                append_fruit(order, fruit_tuple)
                append_fruit(sklad_2, (fruit_tuple[0], -fruit_tuple[1]))
            else:
                print(f"{fruit_tuple[0]} осталось {sklad_2[fruit_tuple[0]]}")

    print("исходные:")
    print_default_dict(sklad_1, order)
    print_default_dict(sklad_2, order)
    print(f"остаток:\n{sklad_1}\n{sklad_2}\nзаказ:\n{order}")