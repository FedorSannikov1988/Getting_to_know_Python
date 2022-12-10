'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование map и list comprehension

Функция creating_list_float взята
из домашнего задания №3 задача № 3 (homework3/main2.py)

Было:
'''

def creating_list_float_v1\
    (list_float_random_number: list, rounding: int=4) -> list:
    
    resalt_list = list()

    for count in range(0, len(list_float_random_number), 1):
        resalt_list.append(round(( \
            list_float_random_number[count] \
                - int(list_float_random_number[count])), rounding))

    return resalt_list

'''
Стало после использования map и list comprehension:
'''

def creating_list_float_v2\
    (list_float_random_number: list, rounding: int=4) -> list:

    return [round(list_float_random_number[count]- \
        list(map(int, list(list_float_random_number)))[count], rounding) \
        for count in range(0 , len(list_float_random_number), 1)]

data = [1.1, 1.2, 3.1, 5, 10.01]
print(data)

print("creating_list_float_v1")
print(creating_list_float_v1(data))
print("creating_list_float_v2")
print(creating_list_float_v2(data))