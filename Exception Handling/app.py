
from cmath import inf
from functools import cache


a = 1
b = 0
c = 0

try:
    c = a/b
except ZeroDivisionError as e:
    print(e)
    c = inf
except TypeError as e:
    print(e)
    pass
except Exception as e:
    print(e)
    pass
finally:
    print('done')

print(c)
