class Water:
    text = 'Вода'

    def __add__(self, other):
        match other:
            case Air():
                return Storm()
            case Fire():
                return Vapour()
            case Earth():
                return Dirt()
            case _:
                return UnknownElement()


class Air:
    text = 'Воздух'

    def __add__(self, other):
        match other:
            case Water():
                return Storm()
            case Fire():
                return Lightning()
            case Earth():
                return Dust()
            case _:
                return UnknownElement()


class Fire:
    text = 'Огонь'

    def __add__(self, other):
        match other:
            case Air():
                return Lightning()
            case Water():
                return Vapour()
            case Earth():
                return Lava()
            case _:
                return UnknownElement()


class Earth:
    text = 'Земля'

    def __add__(self, other):
        match other:
            case Air():
                return Dust()
            case Fire():
                return Lava()
            case Water():
                return Dirt()
            case _:
                return UnknownElement()


class Storm:
    text = 'Шторм'


class Vapour:
    text = 'Пар'


class Dirt:
    text = 'Грязь'


class Lightning:
    text = 'Молния'


class Dust:
    text = 'Пыль'


class Lava:
    text = 'Лава'


class UnknownElement:
    text = 'Неизвестный элемент'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
result_1 = water + air
result_2 = air + fire
result_3 = fire + earth
print(result_1.text)
print(result_2.text)
print(result_3.text)
