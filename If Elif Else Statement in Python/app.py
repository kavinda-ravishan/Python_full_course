import random

for i in range(10):
    random_number = int(random.random()*100)

    print(f'Random number : {random_number}')

    if random_number < 25:
        print("0 < random number < 25")
    elif random_number < 50:
        print("25 <= random number < 50")
    else:
        print("50 <= random number <= 100")
