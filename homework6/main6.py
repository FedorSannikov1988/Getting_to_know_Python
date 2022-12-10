'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование list comprehension

Функция multiplication_couple_elements взята
из домашнего задания №3 задача № 2 (homework3/main1.py)

Было:
'''

def multiplication_couple_elements_v1\
    (list_for_multiplication_couple_elements: list) -> list:

    if len(list_for_multiplication_couple_elements) == 0:
        return print("в массиве для умножения нет элементов")
        
    if len(list_for_multiplication_couple_elements)%2 == 0:
        length_resalt_list = int(len(list_for_multiplication_couple_elements)/2)
    else: 
        length_resalt_list = ((len(list_for_multiplication_couple_elements)//2)+1)

    resalt_list = list()
    
    for count in range(0, length_resalt_list, 1):
        resalt_list.append(list_for_multiplication_couple_elements[count] \
            * list_for_multiplication_couple_elements \
                [len(list_for_multiplication_couple_elements)-count-1])
    
    return resalt_list

'''
Стало после использования list comprehension:
'''

def multiplication_couple_elements_v2\
    (list_for_multiplication_couple_elements: list) -> list:

    if len(list_for_multiplication_couple_elements) == 0:
        return print("в массиве для умножения нет элементов")
        
    if len(list_for_multiplication_couple_elements)%2 == 0:
        length_resalt_list = int(len(list_for_multiplication_couple_elements)/2)
    else: 
        length_resalt_list = ((len(list_for_multiplication_couple_elements)//2)+1)

    return[list_for_multiplication_couple_elements[count]*\
        list_for_multiplication_couple_elements\
            [len(list_for_multiplication_couple_elements)-count-1] for count in range(0, length_resalt_list, 1)]

data1 = [2, 3, 4, 5, 6] #=> [12, 15, 16];
data2 =[2, 3, 5, 6] #=> [12, 15]

print(data1)
print(data2)

print("multiplication_couple_elements_v1")
print(multiplication_couple_elements_v1(data1))
print(multiplication_couple_elements_v1(data2))

print("multiplication_couple_elements_v2")
print(multiplication_couple_elements_v2(data1))
print(multiplication_couple_elements_v2(data2))