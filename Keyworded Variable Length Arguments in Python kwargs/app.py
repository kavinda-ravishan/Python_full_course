def pearson(**data):
    for key in data.keys():
        print(key, data[key])

    for key, value in data.items():
        print(key, value)


pearson(name='kavinda', age=25, height=1.98)
