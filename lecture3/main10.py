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