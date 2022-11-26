'''
Списки
'''

list1  = [1, 2, 3, 4, 5, 6, 7]

list2  = list1

#list3  = list1[:]
list3  = list1.copy()

print(list3)
print(list3.pop())

print(list3)

print(list3.pop(2))
print(list3)

print(list3.insert(1,11))
print(list3)

print(list3.append(50))
print(list3)

print(list1)