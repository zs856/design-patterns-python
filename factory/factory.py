# So a factory is essentially the implementation of the idea of the single responsibility principle or
# the separation of concerns.
# And that is the idea that once you get too many factory methods inside a class, it might make sense
# to actually move them out of the class or at least to try and group them somehow into a separate entity.
from math import *


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:
        # Now, the interesting thing is that it doesn't really matter whether these factory methods are static
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p, p2)
