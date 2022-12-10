'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование list comprehension

Функция coordinates_point_entry() взятя из домашнего задания №1 задача №5 (homework1/main4.py)

Было:
'''

def coordinates_point_entry_v1():
    somvol = None
    array = list()
    for count in range(0,2,1):
        if (count == 0): somvol = 'X'
        else: somvol = 'X'
        array.append(float(input(f"Введите координату {somvol} = ")))
    return array

'''
Стало после использования list comprehension:
'''

def coordinates_point_entry_v2():
    return [float(input(f"Введите координату {count} = ")) for count in ['X', 'Y']]

print("coordinates_point_entry_v1():")
print(coordinates_point_entry_v1())

print("coordinates_point_entry_v2():")
print(coordinates_point_entry_v2())