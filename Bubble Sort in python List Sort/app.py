
lst = [5, 4, 3, 2, 1, 0]


def bubbleSort(lst):

    size = len(lst)

    for i in range(size-1):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


print(lst)
print(bubbleSort(lst))
