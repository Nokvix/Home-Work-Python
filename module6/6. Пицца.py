def generate_dictionary():
    for i_order in order_list:
        new_dict = {i_order[1]: int(i_order[2])}
        if i_order[0] in order_dictionary:
            if i_order[1] in order_dictionary[i_order[0]]:
                order_dictionary[i_order[0]][i_order[1]] += int(i_order[2])
            else:
                order_dictionary[i_order[0]][i_order[1]] = int(i_order[2])
        else:
            order_dictionary[i_order[0]] = new_dict


def print_data():
    for i_name in order_dictionary.keys():
        print(i_name, ":", sep="")
        for i_pizza_name in order_dictionary[i_name].keys():
            print("{0}: {1}".format(i_pizza_name, order_dictionary[i_name][i_pizza_name]))


order_quantity = int(input("Введите количество заказов: "))
order_dictionary = dict()
order_list = []
for i_order in range(1, order_quantity + 1):
    order = input("{0}-й заказ (вводите данные через пробел): ".format(i_order)).split()
    order_list.append(order)
order_list.sort()
generate_dictionary()
print_data()
