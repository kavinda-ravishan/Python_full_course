def function1(a, b):
    print(f'a : {a}, b : {b}')


function1(2, 3)
function1(b=3, a=2)


def function2(a=0, b=0):
    print(f'a : {a}, b : {b}')


function2()
function2(1)
function2(1, 2)


def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num

    return sum


print(add())
print(add(1, 2, 3))
