import sys

sys.setrecursionlimit(50)

count = 0


def say_hello():
    global count
    count += 1
    print("hello", count)
    say_hello()


# say_hello()


print(sys.getrecursionlimit())


def factorial(num: int) -> int:

    fac = 1

    for i in range(2, num+1):
        fac *= i

    return fac


def factorial_rec(num: int) -> int:

    if num == 1:
        return 1
    return num * factorial(num-1)


print(1*2*3*4)

print(factorial(4))
print(factorial_rec(4))
