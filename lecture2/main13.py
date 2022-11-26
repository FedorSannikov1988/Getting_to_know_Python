'''
Cловари
'''

#dictionary_1 = {}
dictionary_1 = \
{
'up': '↑',
'left': '←',
'down': '↓',
'right': '→'
}
#print(dictionary_1) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
#print(dictionary_1['left']) # ←

dictionary_2 = {'one': '1','two': '2','theer': '3','for': '4'}
print(dictionary_2)

del dictionary_2['theer']
print(dictionary_2)

dictionary_2['one'] = '_1*'
print(dictionary_2)

for item in dictionary_2:
    print('{}: {}'.format(item, dictionary_2[item]))

for item in dictionary_2:
    print(item)

for item in dictionary_2.values():
    print(item)

for item in dictionary_2:
    print(dictionary_2[item])

print(dictionary_2.values())