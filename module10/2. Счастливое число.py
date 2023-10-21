import random

total_amount = 0
with open("out_file.txt", "w", encoding="utf=8") as file_numbers:
    try:
        while total_amount < 777:
            random_number = random.randint(1, 13)
            user_number = int(input("Введите число: "))

            if random_number == 13:
                raise Exception("Вас постигла неудача!")

            total_amount += user_number
            file_numbers.write(str(user_number) + "\n")

    except Exception:
        print("Вас постигла неудача!")
    else:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")
