from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size


# 场景：我们在开发过程中需要不断对产品的过滤器添加新的需求
# 但根据OCP的原则，当一个类已经被写好并测试后，就不应该对其进行修改，
# 所以把下面的第一个过滤器当作一个错误示范
class ProductFilter:
    def fileter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def fileter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# 基于OCP我们可以把这个过滤器以更好的形式进行实现，如下
# Specification
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
    products = [apple, tree, house]
    pf = ProductFilter()
    print("Green products (old):")
    for p in pf.fileter_by_color(products, Color.GREEN):
        print(f"- {p.name} is green")

    bf = BetterFilter()
    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f"- {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f"- {p.name} is large")

    print("Large blue items:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f"- {p.name} is large and blue")

    # 下面这个写法是Large blue的另一种实现，需要实现Specification的__and__方法
    print("Large blue items:")
    large_blue = large & ColorSpecification((Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f"- {p.name} is large and blue")
