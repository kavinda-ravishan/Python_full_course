

def linearSearch(lst, val):
    for i, num in enumerate(lst):
        if num == val:
            return i
    return -1


lst = [5, 8, 4, 6, 9, 2]

print(linearSearch(lst, 9))


def printlst():
    lst = []  # local var
    print(lst)  # print local var
    print(globals()['lst'])  # print global var


printlst()
