
a = 45


def function():
    a = 12
    print(a)
    print(globals()['a'])

    x = globals()['a']
    x = 321
    print(x)

    globals()['a'] = 654


def function2():
    print(a)
    print(globals()['a'])


def function3():
    global a
    a = 1234
    print(a)
    print(globals()['a'])


print(a)

function()
function2()
function3()

print(a)
