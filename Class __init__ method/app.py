
class Computer():

    def __init__(self, processor, ram, memory):
        self.processor = processor
        self.ram = ram
        self.memory = memory

    def config(self, name):
        self.name = name
        print(f'{name} : {self.processor}, {self.ram}GB RAM, {self.memory}GB Memory.')


computer1 = Computer("Core i7", 16, 500)
computer2 = Computer("Core i5", 8, 500)


computer1.config('Computer 1')
Computer.config(computer2, 'Computer 2')
