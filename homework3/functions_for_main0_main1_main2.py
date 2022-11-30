'''
Вынесенные функции
'''

import random

def creating_list_random_number\
    (quantity_random_number: int, min_val: int, max_val: int) -> list:  
    
    quantity_random_number = abs(quantity_random_number)

    if quantity_random_number == 0:
        quantity_random_number = 1

    if min_val > max_val:
        max_val = min_val + 1

    resalt_list = list()

    for _ in range(0, quantity_random_number, 1):
        resalt_list.append(random.randint(min_val, max_val))
    
    return resalt_list

def creating_list_float_random_number\
    (quantity_random_number: int, min_val: float, max_val: float, rounding: int=4) -> list:  

    quantity_random_number = abs(quantity_random_number)

    if quantity_random_number == 0:
        quantity_random_number = 1

    if min_val > max_val:
        max_val = min_val + 1

    resalt_list = list()

    for _ in range(0, quantity_random_number, 1):
        resalt_list.append(round(random.uniform(min_val, max_val), rounding))
    
    return resalt_list