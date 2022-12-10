'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование list comprehension

Функция sum_odd_elements взята
из домашнего задания №3 задача № 1 (homework3/main0.py)

Было:
'''

def sum_odd_elements_v1\
    (list_for_summ: list) -> int:

    if len(list_for_summ) == 0:
        return print("в массиве для суммирования нет элементов")
    
    summa: int = 0

    for count in range(1, len(list_for_summ), 2):
        summa += list_for_summ[count]
    
    return summa

'''
Стало после использования list comprehension c if:
'''

def sum_odd_elements_v2\
    (list_for_summ: list) -> int:

    if len(list_for_summ) == 0:
        return print("в массиве для суммирования нет элементов")
    
    return sum([list_for_summ[count] for count in range(0, len(list_for_summ), 1) if count%2 != 0])


data = [2, 3, 5, 9, 3, 7, 6, 4]

print(data)

print("sum_odd_elements_v1")
print(sum_odd_elements_v1(data))

print("sum_odd_elements_v2")
print(sum_odd_elements_v2(data))