# ISP = interface segregation principle
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def print(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionalPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        """Not supported

        Args:
            document (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("Printer cannot scan")


# 下面是对打印机类的更细粒度的实现
class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        pass


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


# 然后我们可以更进一步做抽象
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def print(self, document):
        self.scanner.scan(document)
