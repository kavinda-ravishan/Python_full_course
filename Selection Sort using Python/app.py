lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def selection_sort(lst: list) -> list:

    for i in range(len(lst)-1):
        min_index = i
        for j in range(i, len(lst)-1):

            if lst[min_index] > lst[j+1]:
                min_index = j+1

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


print(selection_sort(lst))
