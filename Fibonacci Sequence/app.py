
def fib(count: int) -> list:
    '''
    Fibonacci series
    ================
    This function returns list of fibonacci series.

    How to use:
    -----------
    >>> lst = fib(5)
    '''

    lst = [0, 1]

    for i in range(count-2):
        lst.append(lst[i]+lst[i+1])

    return lst


print(fib(5))
