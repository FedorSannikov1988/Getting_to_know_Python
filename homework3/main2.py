'''
3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.

Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

def creating_list_float\
    (list_float_random_number: list, rounding: int=4) -> list:
    
    resalt_list = list()

    for count in range(0, len(list_float_random_number), 1):
        resalt_list.append(round(( \
            list_float_random_number[count] \
                - int(list_float_random_number[count])), rounding))

    return resalt_list

import functions_for_main0_main1_main2 as my_function

quantity_random_number = int(input("Введите количество элементов списка: "))

min_val = abs(float(input("Введите нижний предел генерации случайных чисел: ")))
print(f"Считаем что Вы ввели: {min_val}")

max_val = abs(float(input("Введите верхний предел генерации случайных чисел: ")))
print(f"Считаем что Вы ввели: {max_val}")

rounding = int(input("Введите количество символов после запятой для генерируемого числа: "))

list_float_random_number = \
    my_function.creating_list_float_random_number(quantity_random_number, min_val, max_val, rounding)

print(f"Созданный список: {list_float_random_number}")

list_float = creating_list_float(list_float_random_number, rounding)

print(f"Массив 'дробных частей': {list_float}")

difference_built_in_function = round(max(list_float) - min(list_float), rounding)

'''
если будет время напишу свои функци max и min
'''

print(f"Максимальное значение дробной части элементов массива: {max(list_float)}")

print(f"Минимальное значение дробной части элементов массива: {min(list_float)}")

print(f"Разница между максимальным и минимальным значением дробной части элементов исходного массива: {difference_built_in_function}")