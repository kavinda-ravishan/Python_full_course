def sum(a=None, b=None, c=None):

    a = a if a else 0
    b = b if b else 0
    c = c if c else 0

    return a + b + c


print(sum())
print(sum(3))
print(sum(3, 6))
print(sum(3, 6, 9))


class Entity:

    def sum(self, a=None, b=None, c=None):

        print('Entity')
        a = a if a else 0
        b = b if b else 0
        c = c if c else 0

        return a + b + c


class SubClass(Entity):

    def sum(self, a=None, b=None, c=None):

        print('SubClass')
        a = a if a else 0
        b = b if b else 0
        c = c if c else 0

        return a + b + c


e = Entity()
print(e.sum())
print(e.sum(3))
print(e.sum(3, 6))
print(e.sum(3, 6, 9))

s = SubClass()
print(s.sum())
print(s.sum(3))
print(s.sum(3, 6))
print(s.sum(3, 6, 9))
