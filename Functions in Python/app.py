
def great():
    print('hello')
    print('good morning')


def add(a, b):
    return a + b


def add_sub(a, b):
    c = a + b
    d = a-b
    return c, d


def main():
    great()
    x = add(1, 2)
    print(x)
    a, b = add_sub(3, 1)
    print(a, b)


if __name__ == '__main__':
    main()
