def add_to_dictionary(contacts):
    name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").title().split()
    telephone_number = int(input("Введите номер телефона: "))
    full_name = (name, surname)
    if full_name in contacts:
        print("Такой человек уже есть в словаре контактов")
    else:
        contacts[full_name] = telephone_number


def find_in_dictionary(contacts):
    surname = input("Введите фамилию для поиска: ").title()
    flag = False
    for full_name, telephone_number in contacts.items():
        name_dict, surname_dict = full_name
        if surname == surname_dict:
            flag = True
            print(name_dict, surname_dict, telephone_number)
    if not flag:
        print("Такого контакта в словаре нет")
    print()


def main():
    contacts = dict()
    while True:
        action = int(input("Выберите номер действия:\n"
                           "\t1. Добавить контакт\n"
                           "\t2. Найти человека\n"
                           "Действие: "))
        if action == 1:
            add_to_dictionary(contacts)
            print("Текущий словарь контактов: {0}\n".format(contacts))
        elif action == 2:
            find_in_dictionary(contacts)


main()
