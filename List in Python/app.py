from time import process_time_ns


nums = [1, 2, 3, 4]

print(nums)


mylist = [25, 'kavinda', 1.8, False]

print(mylist)
print(mylist[1])
print(mylist[-1])
print(mylist[1][0:4])
print(mylist[1:3])


mylist[0:2] = [27, 'kvn']
print(mylist)

listoflist = [[1, 2, 3], ['a', 'b']]
print(listoflist)

listoflist.append('end')
listoflist.insert(1, 123)
print(listoflist)

listoflist.remove(123)
print(listoflist)

listoflist.pop(-1)
print(listoflist)

print(nums)
del nums[2:]
print(nums)

nums.extend([5, 6, 7])
print(nums)

print(min(nums))
print(sum(nums))
