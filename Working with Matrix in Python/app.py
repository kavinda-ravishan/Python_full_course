import numpy as np

arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr_flat = arr.flatten()
print(arr_flat)

arr3 = arr_flat.reshape(-1, 2, 5)
print(arr3)

mat = np.matrix(arr)
print(mat)

mat = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(mat)
print(np.diagonal(mat))
print(mat.min())

mat1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
mat2 = np.matrix('1 2 3; 4 5 6; 7 8 9')

print(mat1 * mat2)
print(mat1 @ mat2)
