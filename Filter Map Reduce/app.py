from functools import reduce

numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evenlist = list(filter(lambda num: num % 2 == 0, numlist))


def is_odd(num):
    return num % 2 != 0


oddlist = list(filter(is_odd, numlist))

print(evenlist)
print(oddlist)


doublelist = list(map(lambda num: num*2, numlist))

print(doublelist)

sumvalue = reduce(lambda sum, num: sum + num, numlist)

print(sumvalue)
