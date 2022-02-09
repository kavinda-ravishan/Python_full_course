x = [1, 2, 3, 4, 5, 6]

it = iter(x)

print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))

print('----------------')

for n in it:
    print(n)

print('----------------')

# write iterator


class Numbers:

    def __init__(self, start, stop, step=1):
        self.index = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.stop:
            index = self.index
            self.index += self.step
            return index
        else:
            raise StopIteration


topTen = Numbers(1, 10)

print(topTen.__next__())
print(next(topTen))

for num in topTen:
    print(num)
