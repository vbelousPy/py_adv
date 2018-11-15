from random import random

import arrow as arrow


class Factory:

    def build(self):
        pass


class MonitorFactory(Factory):
    def build(self):
        return Monitor()


class KeyboardFactory(Factory):
    def build(self):
        return Keyboard()


class PCFactory(Factory):
    def build(self):
        return PC()


class ComputerParts:

    def __init__(self, vendor="", release_date="", ) -> None:
        self.vendor = self.__class__.__name__ + "_Factory" if vendor == "" else vendor
        self.release_date = arrow.utcnow().to('local').format(
            'YYYY-MM-DD HH:mm:ss') if release_date == "" else release_date

    def __str__(self) -> str:
        returned_str = str()
        for k, v in self.__dict__.items():
            returned_str += "{}: {}; ".format(str(k).capitalize(), str(v))
        return returned_str


class Monitor(ComputerParts):

    def __init__(self, vendor="", release_date="", model="Chinese fake", diagonal=21) -> None:
        super().__init__(vendor, release_date)
        self.model = model
        self.diagonal = diagonal


class Keyboard(ComputerParts):
    keyboard_types = ["PC", "Bluetooth"]

    def __init__(self, vendor="", release_date="") -> None:
        super().__init__(vendor, release_date)
        self.keyboard_type = self.keyboard_types[int(random() * len(self.keyboard_types))]


class PC(ComputerParts):
    pc_types = ["Mini tower", "Tower"]

    def __init__(self, vendor="", release_date="") -> None:
        super().__init__(vendor, release_date)
        self.pc_type = self.pc_types[int(random() * len(self.pc_types))]


class Compus:
    __instance = None
    factory_list = [MonitorFactory(), KeyboardFactory(), PCFactory()]
    stock_balance = None

    def __init__(self) -> None:
        if self.stock_balance is None:
            self.stock_balance = list()

    def __new__(cls):
        if Compus.__instance is None:
            Compus.__instance = object.__new__(cls)
        return Compus.__instance

    def start_work(self):
        for i in range(int(random() * 20)):
            self.stock_balance.append(self.factory_list[int(random() * len(self.factory_list))].build())

    def print_balance(self):
        for i in self.stock_balance:
            print(i)


compus = Compus()
compus.start_work()
compus.print_balance()
print("---------------------------------------- CHECK SINGLETON --------------------------------------------")
new_compus = Compus()
new_compus.print_balance()
