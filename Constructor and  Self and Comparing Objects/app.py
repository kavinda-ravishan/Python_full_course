
class Computer():

    def __init__(self, name):
        print(id(self))
        self.name = name

    def print2computers(self, computer):
        print(f'{self.name} and {computer.name}')


computer1 = Computer('kavinda')
print(id(computer1))

computer2 = Computer('ravishan')
print(id(computer2))

print(computer1.name)
print(computer2.name)

computer1.print2computers(computer2)
Computer.print2computers(computer1, computer2)
