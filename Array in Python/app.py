from array import array

arr1 = array('i', [5, -9, 8, -1, 10])  # i : signed int
arr2 = array('I', [5, 9, 8, 1, 10])  # i : unsigned int
arr3 = array('u', ['a', 'b', 'c'])  # i : unsigned int

print(arr1)
print(arr2)
print(arr3)


print(arr1.buffer_info())  # address, size

print(arr1.typecode)

arr1.reverse()
print(arr1)

for i in arr1:
    print(i)

for i in range(arr1.buffer_info()[1]):
    print(arr1[i])

for i in range(len(arr1)):
    print(arr1[i])

print(arr1[2])


arr4 = array(arr1.typecode, [])

arr5 = array(arr1.typecode, [num for num in arr1])
print(arr5)
