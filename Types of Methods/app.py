class Student():

    # class variables
    school = 'School'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, m1):
        self.m1 = m1

    @classmethod
    def get_school(cls):
        return cls.school

    @classmethod
    def set_school(cls, school):
        cls.school = school

    @staticmethod
    def info():
        print('This is student class')


print(Student.school)

s1 = Student(43, 12, 56)
s2 = Student(67, 98, 56)


print(s1.avg())
print(s2.avg())

print(Student.get_school())

Student.set_school('mySchool')

print(Student.get_school())

Student.info()
