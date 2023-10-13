import random

original_list = [random.randint(0, 100) for _ in range(10)]
print("Оригинальный список: {0}".format(original_list))
new_list = [
    (original_list[index], original_list[index + 1]) for index in range(0, len(original_list), 2)]
print("Новый список: {0}".format(new_list))
