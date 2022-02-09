class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(
            f"Name : {self.name}, Roll No : {self.rollno}, Laptop brand : {self.lap.brand}"
        )
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(f"Brand : {self.brand}, CPU : {self.cpu}, RAM : {self.ram}")


s1 = Student("kavinda", 1)
s2 = Student("ravishan", 2)

s1.show()

s2.lap.brand = "dell"
s2.show()

lap = s1.lap
lap1 = s1.Laptop()
print(f"{lap1.brand}, {lap1.cpu}, {lap1.ram}")
print(f"{id(lap1)}\n{id(s1.lap)}\n{id(lap)}")

lap2 = s2.lap
lap2.ram = 12

print(f"{lap2.brand}, {lap2.cpu}, {lap2.ram}")
print(f"{id(lap2)}\n{id(s2.lap)}")

lap3 = Student.Laptop()
print(f"{id(lap3)}")


lap.show()
lap1.show()
lap2.show()
lap3.show()


s1.lap.show()
s2.lap.show()
