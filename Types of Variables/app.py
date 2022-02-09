class Car():

    class_type = "car"

    def __init__(self, com, mil):
        self.com = com
        self.mil = mil


c1 = Car("BMW", 80)
c2 = Car("TOYOTA", 100)

print(c1.com, c1.mil, c1.class_type)
print(c2.com, c2.mil, c2.class_type)

Car.class_type = "jeep"

print(c1.com, c1.mil, c1.class_type)  # jeep
print(c2.com, c2.mil, c2.class_type)  # jeep

c1.class_type = "van"

print(c1.com, c1.mil, c1.class_type)  # van
print(c2.com, c2.mil, c2.class_type)  # jeep
