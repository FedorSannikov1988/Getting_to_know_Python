'''
2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''

import functions_for_main0_main1_main2 as my_function

quantity_random_number = int(input("Введите количество элементов списка: "))

min_val = int(input("Введите нижний предел генерации случайных чисел: "))

max_val = int(input("Введите верхний предел генерации случайных чисел: "))

list_random_number = \
    my_function.creating_list_random_number(quantity_random_number, min_val, max_val)

print(f"Список для попарного перемножения элементов: {list_random_number}")

def multiplication_couple_elements\
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

print(multiplication_couple_elements(list_random_number))