class Computer():

    def config(self):
        print('Core i7, 16GB RAM, Windows 10')


computer = Computer()
print(type(computer))

computer.config()

Computer.config(computer)
