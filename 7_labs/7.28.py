'''см. таблицу Склад фруктов
На складе имеются запасы фруктов.
В онлайн магазин поступил заказ, на банкет необходимо доставить заказ:
1. Апельсины, 4 кг
2. Груша, 3 кг
3. Арбуз, 23 кг
4. Авокадо, 2 кг
5. Дыня, 9 кг
Все данные из таблицы “Склад фруктов” должны храниться в вашем коде в
виде словаря
1. Создайте функцию input_fruit Пользователь вводит НАЗВАНИЕ_ФРУКТА,
КОЛ-ВО_ФРУКТОВ, сделайте возврат данных из функции в виде кортежа
(название, кол-во)
2. Cоздайте цикл со счетчиком (кол-во позиций в заявке) который вызывает
функцию input_fruit и оформляет заявку на необходимое кол-во фруктов.
Расчитайте цену заказа:
Ночной тариф, все товары *2 кроме Авокадо и груши
3. Выведите результирующий список в виде словаря в консоль: Вывести с
указанием наименования, веса и ценой заявки.
Вывести остатки на складе(Название и вес)'''

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

    order = {}

    night_exceptions = ['Авокадо', 'Груша']
    required = [('Апельсин', 4), ('Груша', 3), ('Арбуз', 23), ('Авокадо', 2), ('Дыня', 9)]
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
                price = sklad[sklad_number][fruit_tuple[0]]['price']
                if(fruit_tuple[0] not in night_exceptions):
                    price *= 2

                order.setdefault(fruit_tuple[0], {'weight': 0, 'total': 0})
                order[fruit_tuple[0]]['total'] += fruit_tuple[1] * price
                order[fruit_tuple[0]]['weight'] += fruit_tuple[1]

                sklad[sklad_number][fruit_tuple[0]]['stored'] -= fruit_tuple[1]
            else:
                print(f"{fruit_tuple[0]} осталось {sklad[sklad_number][fruit_tuple[0]]['stored']}")
        else:
            print("фрукт отсуствует на 1 и 2 складе")


    print(f"\nзаказ:{order}\nостаток на складе:{sklad}")