
def update(x):
    print(f'function : {x}, id : {id(x)}')
    x = 123
    print(f'function : {x}, id : {id(x)}')


def update_lst(lst):
    print(f'function : {lst[0]}, id : {id(lst)}')
    lst[0] = 123
    print(f'function : {lst[0]}, id : {id(lst)}')


x = 10
print(f'Main : {x}, id : {id(x)}')
update(x)
print(f'Main : {x}, id : {id(x)}')

print()

lst = [10]
print(f'Main : {lst[0]}, id : {id(lst)}')
update_lst(lst)
print(f'Main : {lst[0]}, id : {id(lst)}')
