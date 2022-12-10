'''
#list comprehension, lambda:

list_two = [count for count in range(0, 11, 2)]

list_three = [count for count in range(0, 11, 1) if count%2 == 0]

list_for = [(count,count) for count in range(0, 11, 1) if count%2 == 0]

print(list_two)
print(list_three)
print(list_for)

function = lambda x: x+x

list_one = [function(count) for count in range(0, 11, 1) if count%2 == 0]

list_two = [(function(count)) for count in range(0, 11, 1) if count%2 == 0]

list_three = [(function(count), count) for count in range(0, 11, 1) if count%2 == 0]

list_for = [[function(count), count] for count in range(0, 11, 1) if count%2 == 0]

print(list_one)
print(list_two)
print(list_three)
print(list_for)
'''

# zip, enumerate:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
print(users)

id = [1, 2, 3, 4, 5]
salary = [100, 200, 300, 400]

data1 = list(zip(users, id))
data2 = list(zip(users, id, salary))

data3 = list(enumerate(users))
data4 = list(enumerate(id))

print("---")
print(data1)
print(data2)
print("---")
print(data3)
print(data4)
print("---")


'''
#map:

list_one = [count for count in range(1, 20, 1)]
print(list_one)

list_two = list(map(lambda x:x+0.1, list_one))
print(list_two)

list_three = list(map(int, list_one))
print(list_three)
'''

'''
#filter:

data = [count for count in range(0, 11, 1)]
print(data)

#filter_one = list(filter(lambda x: x%2==0, data))
filter_one = list(filter(lambda x: x%2, data))
print(filter_one)
'''