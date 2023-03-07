# And this is a Cartesian point. But imagine you want to initialize it from polar coordinates
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    # this is kind of like a God object, but for initializes, you end up with an initialise
    # that this takes like ten arguments and you have to be really explicit in the documentation about how
    # these arguments can be assigned and what not. You don't really want this.
    # def __init__(self, x,y, system = CoordinateSystem.C) -> None:
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = x
    #         self.y = y
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = x * cos(y)
    #         self.y = x * sin(y)
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)
