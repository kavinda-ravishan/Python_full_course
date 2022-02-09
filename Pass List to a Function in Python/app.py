
lst = [2, 4, 1, 5, 7]


def even_odd(lst: list) -> tuple:

    e, o = 0, 0
    for num in lst:
        if num % 2 == 0:
            e += 1
        else:
            o += 1

    return e, o


even, odd = even_odd(lst)

print('{even}, {odd}'.format(even=even, odd=odd))
