'''
5. Реализуйте алгоритм перемешивания списка.
'''

import random

def my_shuffle(list):
    
    for count in range(0, len(list), 1):
        
        index_random = random.randint(0, len(list)-1)
    
        byffer = list[count]
        list[count] = list[index_random]
        list[index_random] = byffer
 
    return list

list_string = ['Один', 'Два', 'Три', 'Четыре', 'Пять']
list_copi_1 = list_string[:]
list_copi_2 = list_string[:]

print(f'Список до перемешывания: {list_string}')

random.shuffle(list_copi_1)

print(f'После перемешывания random.shuffle: {list_copi_1}')
print(f'После перемешывания "моей функцией": {my_shuffle(list_copi_2)}')