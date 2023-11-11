class Property:
    def __init__(self, worth):
        self.worth = worth

    def count_rent(self):
        return self.worth


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_rent(self):
        return round(1 / 1000 * self.worth, 2)

    def print_rent(self):
        print(f'Налог за квартиру {self.count_rent()}')


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_rent(self):
        return round(1 / 200 * self.worth, 2)

    def print_rent(self):
        print(f'Налог за машину {self.count_rent()}')


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_rent(self):
        return round(1 / 500 * self.worth, 2)

    def print_rent(self):
        print(f'Налог за дачу {self.count_rent()}')


def main():
    user_money = int(input('Введите количество денег, которое у вас есть: '))
    total_rent = 0
    all_property = [
        Car(int(input('Введите стоимость машины: '))),
        Apartment(int(input('Введите стоимость квартиры: '))),
        CountryHouse(int(input('Введите стоимость дачи: ')))
    ]
    for prop in all_property:
        prop.print_rent()
        total_rent += prop.count_rent()
    total_rent = round(total_rent, 2)
    print(f'Итоговая сумма: {total_rent}')

    if user_money >= total_rent:
        print('Денег на налоги хватает')
    else:
        dif = total_rent - user_money
        print(f'На налоги не хватает {dif} руб')


if __name__ == '__main__':
    main()
