def count_number_letters(file_people_name):
    total_letters = 0
    line_number = 0
    for name in file_people_name:
        letters_in_name = 0
        line_number += 1

        try:
            for char in name:
                if char.isalpha():
                    letters_in_name += 1
                    total_letters += 1
            if letters_in_name < 3:
                raise BaseException

        except BaseException:
            print("Ошибка: менее трёх символов в строке {}.".format(line_number))
    return total_letters


with open("people.txt", "r", encoding="utf-8") as file_people_name:
    total_letters = count_number_letters(file_people_name)
print(total_letters)
