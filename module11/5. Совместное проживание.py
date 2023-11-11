from random import randint


class House:
    food = 50
    money = 0

    def print_info(self):
        return f'Еда: {self.food}, деньги: {self.money}'


class Person:
    satiety = 50
    is_dead = False

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def print_info(self):
        return f'Имя: {self.name}, сытость: {self.satiety}'

    def eat(self):
        self.satiety += 1
        self.house.food -= 1

    def work(self):
        self.satiety -= 1
        self.house.money += 1

    def play(self):
        self.satiety -= 1

    def shop_for_food(self):
        self.house.food += 1
        self.house.money -= 1

    def person_dead(self):
        if self.satiety < 0:
            self.is_dead = True


def daily_action(person, house, dice_points):
    if person.satiety < 0:
        person.person_dead()
    elif person.satiety < 20:
        person.eat()
    elif house.food < 10:
        person.shop_for_food()
    elif house.money < 50:
        person.work()
    elif dice_points == 1:
        person.work()
    elif dice_points == 2:
        person.eat()
    else:
        person.play()


house = House()
person_1 = Person('Артём', house)
person_2 = Person('Ваня', house)
for day in range(365):
    dice_points = randint(1, 6)
    daily_action(person_1, house, dice_points)
    daily_action(person_2, house, dice_points)
    if person_1.is_dead:
        print(f'{person_1.name} умер на {day} дне')
        break
    if person_2.is_dead:
        print(f'{person_2.name} умер на {day} дне')
        break
else:
    print('Эксперимент прошёл успешно. Все остались живы\n'
          '\nДанные по первому жителю:\n'
          f'{person_1.print_info()}\n'
          '\nДанные по второму жителю:\n'
          f'{person_2.print_info()}\n'
          '\nДанные по дому:\n'
          f'{house.print_info()}')
