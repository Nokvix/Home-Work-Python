from math import sqrt


def get_sqrt(number):
    try:
        if number < 0:
            raise ValueError
        return sqrt(number)
    except ValueError:
        print("Число {} отрицательное. Действительного корня из отрицательного числа нет!\n".format(number))
    except Exception as exs:
        print(type(exs), "\n", exs)


while True:
    user_number = float(input("Введите число для вычисления квадратного корня\n"
                              "Если хотите закончить вычисления, то введите -1\n"
                              "Число: "))
    print()
    if user_number == -1:
        break
    else:
        result = get_sqrt(user_number)
        if result:
            print(result)
