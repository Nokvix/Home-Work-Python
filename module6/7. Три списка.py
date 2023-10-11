def solution_without_sets_problem_1():
    matching_numbers = []
    for number in array_1:
        if number in array_2 and number in array_3:
            matching_numbers.append(number)
    string = "Решение без множеств: "
    print_data(matching_numbers, string)


def solution_without_sets_problem_2():
    numbers_without_repetition = []
    for number in array_1:
        if number not in array_2 and number not in array_3:
            numbers_without_repetition.append(number)
    string = "Решение без множеств: "
    print_data(numbers_without_repetition, string)


def set_solution_problem_1():
    matching_numbers = sorted(set_1 & set_2 & set_3)
    string = "Решение с множествами: "
    print_data(matching_numbers, string)


def set_solution_problem_2():
    numbers_without_repetition = sorted(set_1 - set_2 - set_3)
    string = "Решение с множествами: "
    print_data(numbers_without_repetition, string)


def print_data(number_list, string):
    print("{0}".format(string), end="")
    for number in number_list:
        print(number, end=" ")
    print()


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)

print("Задача 1:")
solution_without_sets_problem_1()
set_solution_problem_1()
print("Задача 2")
solution_without_sets_problem_2()
set_solution_problem_2()
