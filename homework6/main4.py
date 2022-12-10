'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование list comprehension

Функция creating_list_random_number и creating_list_float_random_number взяты 
из домашнего задания №3 задача с 1-ой по 3-ю (homework3/functions_for_main0_main1_main2.py)

Было:
'''

import random

def creating_list_random_number_v1\
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

def creating_list_float_random_number_v1\
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

'''
Стало после использования list comprehension:
'''

def creating_list_random_number_v2\
    (quantity_random_number: int, min_val: int, max_val: int) -> list:  
    
    quantity_random_number = abs(quantity_random_number)

    if quantity_random_number == 0:
        quantity_random_number = 1

    if min_val > max_val:
        max_val = min_val + 1
    
    return [random.randint(min_val, max_val) for _ in range(0, quantity_random_number, 1)]

def creating_list_float_random_number_v2\
    (quantity_random_number: int, min_val: float, max_val: float, rounding: int=4) -> list:  

    quantity_random_number = abs(quantity_random_number)

    if quantity_random_number == 0:
        quantity_random_number = 1

    if min_val > max_val:
        max_val = min_val + 1
    
    return [round(random.uniform(min_val, max_val), rounding) for _ in range(0, quantity_random_number, 1)]

print("creating_list_random_number_v1")
print(creating_list_random_number_v1(5, 0, 5))

print("creating_list_random_number_v2")
print(creating_list_random_number_v2(5, 0, 5))

print("creating_list_float_random_number_v1")
print(creating_list_float_random_number_v1(5, 0, 5))

print("creating_list_float_random_number_v2")
print(creating_list_float_random_number_v2(5, 0, 5))