colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue

print(e)

for e in colors:
    print(e*2) # redred greengreen blueblue

print(e*2)

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True

colors.remove('red') #del colors[0] # удалить элемент
print(colors == ['red', 'green', 'blue', 'gray']) # Fals