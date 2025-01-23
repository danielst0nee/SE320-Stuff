"""First practice with classes"""
from math import pi


class Circle:
    """ Circle class with some attributes and behvaiors """

    def __init__(self, radius: float) -> None:
        """initializes circle class"""
        self.radius = radius

    def circumference(self) -> float:
        """calculates circle circumference"""
        return self.radius * 2 * pi

    def area(self):
        """calculates circle area"""
        return self.radius ** 2 * pi


my_circle = Circle(1)
print(f"Area: {my_circle.area()}")
print(my_circle)
