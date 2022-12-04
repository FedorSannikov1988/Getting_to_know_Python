function = lambda x: x+x

list_one = [function(count) for count in range(0, 11, 1) if count%2 == 0]

list_two = [(function(count)) for count in range(0, 11, 1) if count%2 == 0]

list_three = [(function(count), count) for count in range(0, 11, 1) if count%2 == 0]

list_for = [[function(count), count] for count in range(0, 11, 1) if count%2 == 0]

print(list_one)
print(list_two)
print(list_three)
print(list_for)