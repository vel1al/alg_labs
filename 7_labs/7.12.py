#На складе имеются запасы фруктов.
#Магазину необходимо оформить заявку на каждый из складов.
#В магазине имеется некоторый товар:
#1. Апельсин, в наличии 12 кг нужно 20
#2. Груша, в наличии 3 кг нужно 10
#3. Арбуз, в наличии 23 кг нужно 35
#4. Авокадо, в наличии 2 кг нужно 8
#5. Дыня, в наличии 0 кг нужно 14
#Все данные из таблицы “Склад фруктов” должны храниться в вашем коде в
#виде словаря
#1. Создайте функцию input_fruit Пользователь вводит НАЗВАНИЕ_ФРУКТА,
#КОЛ-ВО_ФРУКТОВ, сделайте возврат данных из функции в виде кортежа
#(название, кол-во)
#2. Cоздайте цикл со счетчиком (кол-во позиций в заявке) который вызывает
#функцию input_fruit и оформляет заявку на необходимое кол-во фруктов,
#пользователь указывает название фрукта и кол-во, в цикле проверяется
#сколько осталось на складе. А так же проверяется что Одна заявка не может
#быть больше 30кг весом. Если больше оформить как дополнительную заявку
#3. Выведите результирующий список в виде словаря в консоль, Вывести
#заказ с указанием веса каждой заявки и списком необходимых фруктов.

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

    shop = {'Апельсин': {'stored': 12, 'required': 20},
            'Груша': {'stored': 3, 'required': 10},
            'Арбуз': {'stored': 23, 'required': 35},
            'Авокадо': {'stored': 2, 'required': 8},
            'Дыня': {'stored': 0, 'required': 14}}

    orders = []
    order = {1: {'list': [], 'weight': 0}, 2: {'list': [], 'weight': 0}}

    input = [('Дыня', 47), ('Абрикос', 15), ('Апельсин', 12), ('Арбуз', 20), ('Гранат', 18)]

    #for _ in range(5): #недостающих позиций в списке
        #fruit_tuple = input_fruit()

    for fruit_tuple in input:
        sklad_number = 0
        if(fruit_tuple[0] in sklad[1].keys()):
            sklad_number = 1
        elif(fruit_tuple[0] in sklad[2].keys()):
            sklad_number = 2
        if(sklad_number in (1,2)):
            if(sklad[sklad_number][fruit_tuple[0]]['stored'] >= fruit_tuple[1]):
                if(order[sklad_number]['weight'] + fruit_tuple[1] <= 30):
                    order[sklad_number]['list'].append(fruit_tuple[0])
                    order[sklad_number]['weight'] += fruit_tuple[1]
                else:
                    if(order[1]['weight'] > 0 or order[2]['weight'] > 0):
                        orders.append({'sklad': sklad_number, 'order': order[sklad_number]})

                    order_weight = fruit_tuple[1]
                    while(order_weight > 0):
                        if(order_weight > 30):
                            order[sklad_number] = {'list': [fruit_tuple[0]], 'weight': 30}
                            order_weight -= 30
                            orders.append({'sklad': sklad_number, 'order': order[sklad_number]})
                        else:
                            order[sklad_number] = {'list': [fruit_tuple[0]], 'weight': order_weight}
                            order_weight -= 30

                shop.setdefault(fruit_tuple[0], {'stored': 0, 'required': 0})
                shop[fruit_tuple[0]]['stored'] += fruit_tuple[1]
            else:
                print(f"{fruit_tuple[0]} осталось {sklad[sklad_number][fruit_tuple[0]]['stored']}")
        else:
            print("фрукт отсуствует на 1 и 2 складе")

    if(order[1]['weight'] > 0): orders.append({'sklad': 1, 'order': order[1]})
    if(order[2]['weight'] > 0): orders.append({'sklad': 2, 'order': order[2]})

    print(f"склад магазина:{shop}\nзаказ:{orders}")