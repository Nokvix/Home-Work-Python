rollers = []
legs = []


def main_func():
    number_rollers = int(input("Количество роликов: "))
    for i_rollers in range(number_rollers):
        rollers.append(int(input(f"Размер пары {i_rollers + 1}: ")))
    number_people = int(input("Количество людей: "))
    for i_person in range(number_people):
        legs.append(int(input(f"Размер ноги человека {i_person + 1}: ")))
    print(f"Наибольшее количество людей, которые могут взять ролики: {people_take_rollers()}")


def people_take_rollers():
    result = 0
    for roller in rollers:
        if roller in legs:
            result += 1
            rollers.remove(roller)
            legs.remove(roller)
    return result


main_func()
