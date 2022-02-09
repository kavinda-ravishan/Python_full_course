
def TopTen(start, stop, step=1):
    n = start
    while(n <= stop):
        yield n
        n += step


topTen = TopTen(1, 20, 2)

print(topTen.__next__())
print(next(topTen))

for num in topTen:
    print(num)
