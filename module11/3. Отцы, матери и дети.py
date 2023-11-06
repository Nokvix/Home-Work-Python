class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = []
        for child in children:
            if self.age - child.age >= 16:
                self.children.append(child)
            else:
                print(f'{self.name} не может быть родителем {child.name}, так как их разница в возрасте меньше 16 лет')

    def tell_us_about_yourself(self):
        print(
            f'Моё имя: {self.name}. Мне {self.age} лет. У меня {len(self.children)} детей'
        )

    def soothe_child(self, child):
        child.is_calm = False

    def feed_child(self, child):
        child.is_hungry = False


class Child:
    def __init__(self, name, age, is_calm, is_hungry):
        self.name = name
        self.age = age
        self.is_calm = is_calm
        self.is_hungry = is_hungry
