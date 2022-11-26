'''
Множества
'''

a = {1, 2, 3, 5, 8}

b = {'2', '5', 8, 13, 21}

c = ['2', '5', 8, 13, 21]

print(type(a)) # set
print(a)

print(type(b)) # set
print(b)

print(type(c))
print(c)

a = {1, 2, 3, 5, 8}

b = set([2, 5, 8, 13, 21])

c = set((2, 5, 8, 13, 21))

print(type(a)) # set
print(a)

print(type(b)) # set
print(b)

print(type(c)) # set
print(c)

a = {1, 1, 1, 1, 1}
print(type(a))
print(a) # {1}

a = {0, 0, 5, 0, -1}
print(type(a))
print(a)