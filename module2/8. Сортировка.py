def main_func():
    list_numbers = [1, 4, -3, 0, 10]
    print(sort_list(list_numbers))
    # print(sorted(list_numbers))  # Второй способ (быстрее чем пузырьковая сортировка)


def sort_list(list_numbers):  # Пузырьковая сортировка
    for _ in range(len(list_numbers)):
        for i in range(len(list_numbers) - 1):
            if list_numbers[i] > list_numbers[i + 1]:
                list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
    return list_numbers


main_func()
