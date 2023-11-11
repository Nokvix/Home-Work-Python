from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self, *args):
        pass


class Circle(Shape):

    def area(self, radius):
        return round(pi * radius ** 2, 2)


class Rectangle(Shape):
    def area(self, side1, side2):
        return side1 * side2


class Triangle(Shape):
    def area(self, base, height):
        return base / 2 * height


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

print(circle.area(5))
print(rectangle.area(5, 6))
print(triangle.area(5, 3))
