'''На складе имеются запасы фруктов.
Магазину необходимо оформить заявку на каждый из складов.
В магазине имеется некоторый товар:
1. Апельсин, в наличии 12 кг нужно 20
2. Груша, в наличии 3 кг нужно 10
3. Арбуз, в наличии 23 кг нужно 35
4. Авокадо, в наличии 2 кг нужно 8
5. Дыня, в наличии 0 кг нужно 14
Все данные из таблицы “Склад фруктов” должны храниться в вашем коде в
виде словаря
1. Создайте функцию input_fruit Пользователь вводит НАЗВАНИЕ_ФРУКТА,
КОЛ-ВО_ФРУКТОВ, сделайте возврат данных из функции в виде кортежа
(название, кол-во)
2. Cоздайте цикл со счетчиком (кол-во позиций в заявке) который вызывает
функцию input_fruit и оформляет заявку на необходимое кол-во фруктов,
пользователь указывает название фрукта и кол-во, в цикле проверяется
сколько осталось на складе. А так же проверяется что Одна заявка не может
быть больше 30кг весом. Если больше оформить как дополнительную заявку
3. Выведите результирующий список в виде словаря в консоль, Вывести
заказ с указанием веса каждой заявки и списком необходимых фруктов.'''

def input_fruit() -> tuple:
    name = input("название фрукта: ")
    count = int(input("количество: "))

    return (name, count)


def main():
    sklad = {1: {'Абрикос': {'stored': 30, 'price': 120},
                 'Авокадо': {'stored': 19, 'price': 90},
                 'Алыча': {'stored': 32, 'price': 67},
                 'Апельсин': {'stored': 67, 'price': 129},
                 'Арбуз': {'stored': 129, 'price': 19}},
             2: {'Гранат': {'stored': 36, 'price': 56},
                 'Грейпфрут': {'stored': 23, 'price': 78},
                 'Груша': {'stored': 57, 'price': 20},
                 'Дыня': {'stored': 48, 'price': 45},
                 'Инжир': {'stored': 12, 'price': 54},
                 'Кешью': {'stored': 31, 'price': 73}}}

    orders = []
    order = {1: {}, 2: {}}

    required = [('Апельсин', 8), ('Груша', 7), ('Арбуз', 12), ('Авокадо', 6), ('Дыня', 14)]
    for fruit_tuple in required:

    #for _ in range(5): #недостающих позиций в списке
        #fruit_tuple = input_fruit()
        sklad_number = 0
        if(fruit_tuple[0] in sklad[1].keys()):
            sklad_number = 1
        elif(fruit_tuple[0] in sklad[2].keys()):
            sklad_number = 2
        if(sklad_number in (1,2)):
            if(sklad[sklad_number][fruit_tuple[0]]['stored'] >= fruit_tuple[1]):
                order_weight = sum([fruit for fruit in order[sklad_number].values()])
                if(order_weight + fruit_tuple[1] <= 30):
                    order[sklad_number].setdefault(fruit_tuple[0], 0)
                    order[sklad_number][fruit_tuple[0]] += fruit_tuple[1]

                else:
                    order1_weight = sum([fruit for fruit in order[1].values()])
                    order2_weight = sum([fruit for fruit in order[2].values()])
                    if(order1_weight > 0 or order2_weight > 0):
                        orders.append({'sklad': sklad_number, 'order': order[sklad_number]})

                    current_weight = fruit_tuple[1]
                    while(current_weight > 0):
                        if(current_weight > 30):
                            order[sklad_number] = {fruit_tuple[0]: 30}
                            current_weight -= 30

                            orders.append({'sklad': sklad_number, 'order': order[sklad_number]})
                        else:
                            order[sklad_number] = {fruit_tuple[0]: current_weight}
                            break

                sklad[sklad_number][fruit_tuple[0]]['stored'] -= fruit_tuple[1]
            else:
                print(f"{fruit_tuple[0]} осталось {sklad[sklad_number][fruit_tuple[0]]['stored']}")
        else:
            print("фрукт отсуствует на 1 и 2 складе")

    order1_weight = sum([fruit for fruit in order[1].values()])
    order2_weight = sum([fruit for fruit in order[2].values()])
    if(order1_weight > 0): orders.append({'sklad': 1, 'order': order[1]})
    if(order2_weight > 0): orders.append({'sklad': 2, 'order': order[2]})

    print(f"\nзаказ:{orders}")