from random import randint


class Unit:
    health = 100
    impact_force = 20
    is_dead = False

    def __init__(self, unit_name):
        self.name = unit_name

    def attack(self, unit):
        unit.health -= 20
        if unit.health == 0:
            unit.is_dead = True
            print('Победил {attacking_unit}'.format(attacking_unit=self.name))
        else:
            print(
                'Провёл атаку {attacking_unit}. У {unit} осталось {health} здоровья'
                .format(attacking_unit=self.name,
                        unit=unit.name,
                        health=unit.health)
            )


unit_1 = Unit('Воин 1')
unit_2 = Unit('Воин 2')

while not (unit_1.is_dead or unit_2.is_dead):
    action = randint(0, 100)
    if action % 2 == 0:
        unit_1.attack(unit_2)
    else:
        unit_2.attack(unit_1)
