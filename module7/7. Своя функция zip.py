# 1 часть задания
def zip_inbuilt():
    string = "abcd"
    tuple_numbers = (10, 20, 30, 40)
    zipped_tuples = zip(string, tuple_numbers)
    print(zipped_tuples)
    for tpl in zipped_tuples:
        print(tpl)


# 2 часть задания
def create_object():
    data_type = int(input("Введите номер типа данных:\n"
                          "1. Список\n"
                          "2. Кортеж\n"
                          "3. Строка\n"
                          "Выбор: "))
    while True:
        if data_type == 1:
            new_list = input("Введите через пробел данные, которые хотите добавить в список: ").split()
            return new_list
        elif data_type == 2:
            new_tuple = tuple(input("Введите через пробел данные, которые хотите добавить в кортеж: ").split())
            return new_tuple
        elif data_type == 3:
            new_string = input("Введите строку: ")
            return new_string
        else:
            print("Команда не распознана, попробуйте ещё раз")


def my_zip_function():
    object_1 = create_object()
    object_2 = create_object()
    zipped_objects = ((object_1[index], object_2[index]) for index in range(min(len(object_1), len(object_2))))
    print(zipped_objects)
    for element in zipped_objects:
        print(element)


my_zip_function()
