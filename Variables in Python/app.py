x = 10

print(x)

name = '01234'

print(name[0])
print(name[-5])
print(name[4])
print(name[-1])

print(name[0:3])
print(name[1:])
print(name[:3])
print(name[2:100])

name = 'abc'
print(name)
print(len(name))


class Vec2:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __len__(self):
        return 2


vec = Vec2()

print(len(vec))
