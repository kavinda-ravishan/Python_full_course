from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def Name(self):
        pass


class Laptop(Computer):
    def Name(self):
        print('my laptop')


lap = Laptop()
lap.Name()
