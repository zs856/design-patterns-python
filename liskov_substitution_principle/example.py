# 下面是一个违背了LSP的例子
class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f"Width: {self.width}, height: {self.height}"


class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    # 因为这里的正方形类的长/宽总是被同时赋予相同的值，
    # 所以use_it输出的预期值和实际值不相等，同时说明正方形类的实现方式违背了LSP
    use_it(sq)
