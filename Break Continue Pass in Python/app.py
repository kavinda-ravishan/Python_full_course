# x = int(input("How many : "))
x = 12

candy_count = 10
i = 1
while i <= x:
    if candy_count <= 0:
        print("out of stock.")
        break

    candy_count -= 1
    print(f"{i} Candy, {candy_count}")

    i += 1


for j in range(1, 50):
    if (j % 3 != 0) or (j % 5 != 0):
        continue

    print(j)


for j in range(10):
    if j % 2 != 0:
        pass
    else:
        print(j)
