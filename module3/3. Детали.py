shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


def main_func():
    part_name = input("Название детали: ")
    result = read_product_data(part_name)
    if result[0] != 0:
        print(f"Количество деталей: {result[0]}")
        print(f"Общая стоимость {result[1]}")
    else:
        print("У нас такой детали нет :(")


def read_product_data(part_name):
    number_parts = 0
    total_cost = 0
    for detail in shop:
        if detail[0] == part_name:
            number_parts += 1
            total_cost += detail[1]
    return [number_parts, total_cost]


main_func()
