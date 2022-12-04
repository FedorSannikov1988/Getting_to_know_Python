data = [count for count in range(0, 11, 1)]
print(data)

#filter_one = list(filter(lambda x: x%2==0, data))
filter_one = list(filter(lambda x: not x%2, data))
print(filter_one)