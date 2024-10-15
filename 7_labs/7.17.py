'''1. Создайте функцию input_fruit которая вызывается для ввода данных в
консоли. Пользователь вводит НАЗВАНИЕ_ФРУКТА, КОЛ-ВО_ФРУКТОВ,
сделайте возврат данных из функции в виде кортежа (название, кол-во)
2. Cоздайте бесконечный цикл while который вызывает функцию input_fruit
в зависимости от наименования фрукта, помещать данные в разные
переменные
sklad_1 (Абрикос, Авокадо, Алыча, Апельсин, Арбуз)
sklad_2 (Гранат, Грейпфрут, Груша, Дыня, Инжир, Кешью)
Прервать цикл когда на одном из складов будет 50 фруктов
3. Выведите результирующий список в виде словаря в консоль, Каждый склад
ввести отдельным словарем.'''

def input_fruit() -> tuple:
    name = input("название фрукта: ")
    count = int(input("количество: "))

    return (name, count)

def main():
    sklad_1, sklad_2 = {}, {}
    sklad_1_entry = ('Абрикос', 'Авокадо', 'Алыча', 'Апельсин', 'Арбуз')
    sklad_2_entry = ('Гранат', 'Грейпфрут', 'Груша', 'Дыня', 'Инжир', 'Кешью')

    while sum(sklad_1.values()) < 50 and sum(sklad_2.values()) < 50:
        fruit_tuple = input_fruit()

        if(fruit_tuple[0] in sklad_1_entry):
            sklad_1.setdefault(fruit_tuple[0], 0)
            sklad_1[fruit_tuple[0]] += fruit_tuple[1]
        elif(fruit_tuple[0] in sklad_2_entry):
            sklad_2.setdefault(fruit_tuple[0], 0)
            sklad_2[fruit_tuple[0]] += fruit_tuple[1]

    print(f"sklad_1={sklad_1}\nsklad_2={sklad_2}")