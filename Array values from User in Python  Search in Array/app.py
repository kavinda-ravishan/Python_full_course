from array import array
from re import search

arr = array('i', [])

n = int(input('Array size : '))

for i in range(n):
    arr.append(int(input('Enter a value : ')))


print(arr)


def SearchArray(arr, value):
    for i, n in enumerate(arr):
        if(n == value):
            return i

    return -1


print(SearchArray(arr, 45))
print(arr.index(45))
