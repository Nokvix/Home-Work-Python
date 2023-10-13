def main_func():
    n = int(input("Введите количество элементов в списке: "))
    list_items = []
    shift = int(input("Сдвиг: "))
    for _ in range(n):
        list_items.append(input("Введите элемент списка: "))
    print(f"Изначальный список: {list_items}")
    result = move_list(list_items, shift)
    print(f"Сдвинутый список: {result}")


def move_list(list_items, shift):
    supporting_list = []
    for i in range(shift):
        supporting_list.append(list_items[i])
    for i in range(len(list_items)):
        supporting_list[i % shift], list_items[(i + shift) % len(list_items)] = list_items[
            (i + shift) % len(list_items)], supporting_list[i % shift]
    return list_items


main_func()
