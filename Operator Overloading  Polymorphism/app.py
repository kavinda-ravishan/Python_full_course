
a = 1
b = 2

print(a+b)
print(int.__add__(a, b))


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec2):
        return Vec2(self.x + vec2.x, self.y + vec2.y)

    def __sub__(self, vec2):
        return Vec2(self.x - vec2.x, self.y - vec2.y)

    def __mul__(self, vec2):
        return Vec2(self.x * vec2.x, self.y * vec2.y)

    def __gt__(self, vec2):
        return True if (self.x + self.y) > (vec2.x + vec2.y) else False

    def __str__(self):
        return f'{self.x}, {self.y}'


vec1 = Vec2(1, 3)
vec2 = Vec2(2, 4)

result = vec1 + vec2
result = Vec2.__add__(vec1, vec2)
print(result.x, result.y)
result = vec1 - vec2
print(result.x, result.y)
result = vec1 * vec2
print(result.x, result.y)

print(vec1 > vec2)
print(vec1 < vec2)

print(vec1)
print(vec2)
