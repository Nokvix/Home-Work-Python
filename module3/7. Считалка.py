def main_func():
    n = int(input("Количество человек: "))
    k = int(input("Какое число в считалке? "))
    people = list(range(1, n + 1))
    print(f"Значит, выбывает каждый {k}-й человек\n")
    counting(k, people)


def counting(k, people):
    index = 0
    while len(people) > 1:
        print(f"Текущий круг людей: {people}")
        print(f"Начало счёта с номера {people[index % len(people)]}")
        index = (index + k - 1) % len(people)
        print(f"Выбывает человек под номером {people[index]}\n")
        value = people[index]
        people.remove(value)
    print(f"Остался человек под номером {people[0]}")


main_func()
