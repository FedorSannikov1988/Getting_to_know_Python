'''
Списки
'''

list1  = [1, 2, 3, 4, 5]

list2  = list1

list3  = list1[:]

for count1 in list1:
    print(count1)

print()

for count2 in list2:
    print(count2)

print()

list1[0] = 111
list2[1] = 222

for count1 in list1:
    print(count1)

print()

for count2 in list2:
    print(count2)

print()

for count3 in list3:
    print(count3)