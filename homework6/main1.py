'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование lambda и list comprehension

Функция list_numbers_and_summa взятя из домашнего задания №2 задача №3 (homework2/main2.py)

Было:
'''

def list_numbers_and_summa_v1(namber):
    
    resalt_list = list()
    
    for count in range(1, namber+1, 1):
        resalt_list.append(round((1+(1/count))**count, 2))
    
    return [resalt_list, sum(resalt_list, 0)]

'''
Стало после использования lambda и list comprehension:
'''

def list_numbers_and_summa_v2(namber):
    
    function = lambda x: round((1+(1/x))**x, 2)
    
    return [[function(count) for count in range(1, namber+1, 1)],\
        sum([function(count) for count in range(1, namber+1, 1)], 0)]


def list_numbers_and_summa_v3(namber):
    
    function = lambda x: (x:= round((1+(1/x))**x, 2))
    
    return [[function(count)  for count in range(1, namber+1, 1)],\
        sum([function(count) for count in range(1, namber+1, 1)], 0)]

namber = 4

namber = 4

print("list_numbers_and_summa_v1(namber)")
print(list_numbers_and_summa_v1(namber))

print("list_numbers_and_summa_v2(namber)")
print(list_numbers_and_summa_v2(namber))

print("list_numbers_and_summa_v3(namber)")
print(list_numbers_and_summa_v3(namber))