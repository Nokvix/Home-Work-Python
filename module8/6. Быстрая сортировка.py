import random


def quick_sort(sort_list):
    sorted_list = []
    if len(sort_list) <= 1:
        return sort_list
    smaller_numbers, equal_numbers, larger_numbers = split_list(sort_list)
    if len(smaller_numbers) > 0:
        sorted_list.extend(quick_sort(smaller_numbers))
    sorted_list.extend(equal_numbers)
    if len(larger_numbers) > 0:
        sorted_list.extend(quick_sort(larger_numbers))
    return sorted_list


def split_list(curr_list):
    support_element = curr_list[-1]
    smaller_numbers = []
    equal_numbers = []
    larger_numbers = []
    for number in curr_list:
        if number > support_element:
            larger_numbers.append(number)
        elif number < support_element:
            smaller_numbers.append(number)
        else:
            equal_numbers.append(number)
    return smaller_numbers, equal_numbers, larger_numbers


# list_numbers = [5, 8, 9, 4, 2, 9, 1, 8]
random_list = [random.randint(1, 100) for _ in range(20)]
print("Изначальный список:", random_list)
print("Отсортированный список:", quick_sort(random_list))
