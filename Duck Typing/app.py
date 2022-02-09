class PyCharm:
    def execute(self):
        print("PyCharm run")


class VSCode:
    def execute(self):
        print("VSCode run")


class Laptop:
    def code(self, ide):
        ide.execute()


lap = Laptop()
ide1 = PyCharm()
ide2 = VSCode()

lap.code(ide1)
lap.code(ide2)
