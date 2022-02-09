import re


lst = [1, 2, 4, 6, 7, 10, 23, 56]


def binSearch(lst, value):
    upper = len(lst) - 1
    lower = 0

    while(upper >= lower):
        # index = int((upper + lower) / 2)
        index = (upper + lower) // 2
        item = lst[index]

        if value < item:
            upper = index - 1
        elif value > item:
            lower = index + 1
        else:
            return index

    return -1


print(binSearch(lst, 7))
