t = tuple(['red', 'green', 'blue'])

print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range

for e in t:
    print(e) # red green blue

#t[0] = 'black' # TypeError: 'tuple' object does not supportitem assignment