#print('hello world')

a = 132
b = 1.23
value = None

print(type(a))
print(a)

print(type(b))
print(b)

print(type(value))
value = 12334
print(type(value))
print(value)

s = "hello 'world' !"
print(s)

print(a, '-', b, '-', s)
print('{} - {} - {} - {}'.format(a, b, b, s))
print('{3} - {2} - {1} - {0}'.format(a, b, b, s))
print(f'{a} - {b} - {b} - {s}')

f = False
print(f)

list1 = [1, 2, 3]
list2 = ['1', '2', '3', 'hello']
list3 = ['1', '2', '3', 'hello', 4, 5, 6, 7.5, 8.5]
list4 = ['1', '2', '3', 'hello', 4, 5, 6, 7.5, 8.5, False]

print(list1)
print(list2)
print(list3)
print(list4)