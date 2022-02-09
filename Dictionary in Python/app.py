
d = {'name': 'kavinda', 1: 'one', False: 0, 'pi': 3.14}

print(d['name'])
print(d[1])
print(d[False])

print(d.get('name'))
print(d.get(1))
print(d.get('unknown'))

print(d.get('unknown', 'return value if key dose not exist'))
print(d.get('name', 'return value if key dose not exist'))


keys = ['name', 'age', 'home']
vals = ['kavinda', 25, 'kurunagala']

d = dict(zip(keys, vals))
print(d)

d['language'] = 'sinhala'
print(d)

del d['language']
print(d)


d = {'nums': [1, 2, 3], 'names': ('kavi', 'ravi'), 'd': {'hello': 'world'}}
print(d)
print(d['d']['hello'])

print(d.keys())
print(d.values())
