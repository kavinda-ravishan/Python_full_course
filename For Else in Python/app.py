nums1 = [1, 3, 6, 7, 11]
nums2 = [1, 3, 5, 7, 10]

for num in nums1:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")


for num in nums2:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")
