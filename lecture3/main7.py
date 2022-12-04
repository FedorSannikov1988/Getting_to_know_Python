def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
print(".split()")
print(data)

data = list(map(int, data))
print("select(int, data)")
print(data)

data = where(lambda e: not e % 2, data)
print("where(lambda e: not e % 2, data)")
print(data)

data = list(map(lambda e: (e, e**2), data))
print("list(select(lambda e: (e, e**2), data))")
print(data)