'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование list comprehension

Функция create_list(namber) взятя из домашнего задания №2 задача №4 (homework2/main3.py)

Было:
'''

def create_list_v1(namber):
    
    resalt_list = list()
    
    for count in range(-namber, namber+1, 1):
        resalt_list.append(count)
    
    return resalt_list

'''
Стало после использования list comprehension:
'''

def create_list_v2(namber):
    return [count for count in range(-namber, namber+1, 1)]

namber = 4

print("create_list_v1(namber)")
print(create_list_v1(namber))

print("create_list_v2(namber)")
print(create_list_v2(namber))