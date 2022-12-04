'''
List Comprehension
'''

list_one = list()

for count in range(0 , 11):
    if count%2 == 0:
        list_one.append(count)

print("Вариант №1:")
print(list_one)

list_two = [count for count in range(0, 11, 2)]

list_three = [count for count in range(0, 11, 1) if count%2 == 0]

list_for = [(count,count) for count in range(0, 11, 1) if count%2 == 0]

print("Вариант №2:")
print(list_two)

print("Вариант №3 (c if):")
print(list_three)

print("Вариант №4 (c if):")
print(list_for)

print("Вариант №5 (а здесь float):")
print([count/2 for count in range(0, 11, 2)])

'''
[exp for item in iterable]

[exp for item in iterable (if conditional)]
'''