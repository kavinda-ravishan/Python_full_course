from tkinter.ttk import Style
import numpy as np

# array

arr1 = np.array([1, 2, 3], dtype=np.int16)
print(arr1)

# linspace
arr2 = np.linspace(10, 20, 11, dtype=np.float16)
print(arr2)

# logspace
arr3 = np.logspace(1, 2, num=5, base=10, dtype=np.float16)
print(arr3)

arr4 = np.linspace(1, 2, num=5, dtype=np.float16)
arr5 = np.power(10, arr4)
print(arr5)

# arange
arr6 = np.arange(10)
print(arr6)

# zeros
arr7 = np.zeros(10)
print(arr7)

# ones
arr8 = np.ones(10)
print(arr8)
