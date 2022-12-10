'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование map

Функция create_list(namber) взятя из домашнего задания №2 задача №4 (homework2/main3.py)

Было:
'''

def input_index_multiplying_element_v1(text):
    
    string = input(text)

    resalt_list = list()
    
    for count in range(0, len(string.split()), 1):
        resalt_list.append(int(string.split()[count]))
    
    return resalt_list

'''
Стало после использования map:
'''

def input_index_multiplying_element_v2(text):
    return list(map(int, list(input(text).split())))

text = "4 5 6 7"
print(text)


'''
При тестировании не забудь нажать 'Enter'
'''

print("input_index_multiplying_element_v1(text)")
print(input_index_multiplying_element_v1(text))

print("input_index_multiplying_element_v2(text)")
print(input_index_multiplying_element_v2(text))