from pickletools import pystring
import numpy as np


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 1, 3, 8, 5])

arr1 += 5

print(arr1)

arr3 = arr1 + arr2

print(arr3)

print(np.sin(arr1))
print(np.max(arr1))

arr4 = np.concatenate([arr1, arr2], axis=0)

print(arr4)


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1

print(arr1)
print(arr2)

arr2[0] = 12
print(arr1)
print(arr2)

if id(arr1) == id(arr2):
    print('same id')
else:
    print('id not same')


# shallow copy
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.view()

print(arr1)
print(arr2)

arr2[0] = 12
print(arr1)
print(arr2)

if id(arr1) == id(arr2):
    print('same id')
else:
    print('id not same')


# deep copy
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.copy()

print(arr1)
print(arr2)

arr2[0] = 12
print(arr1)
print(arr2)

if id(arr1) == id(arr2):
    print('same id')
else:
    print('id not same')
