
number = 23

for i in range(2, number):
    if(number % i == 0):
        print(f'{number} is not a prime Number')
        break
else:
    print(f'{number} is a prime Number')
