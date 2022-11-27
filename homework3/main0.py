'''
1. Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов 
списка, стоящих на нечётной идексах.

Пример:
[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
'''

import functions_for_main0_main1_main2 as my_function

def sum_odd_elements\
    (list_for_summ: list) -> int:

    if len(list_for_summ) == 0:
        return print("в массиве для суммирования нет элементов")
    
    summa: int = 0

    for count in range(1, len(list_for_summ), 2):
        summa += list_for_summ[count]
    
    return summa

quantity_random_number = int(input("Введите количество элементов списка: "))

min_val = int(input("Введите нижний предел генерации случайных чисел: "))

max_val = int(input("Введите верхний предел генерации случайных чисел: "))

list_random_number = \
    my_function.creating_list_random_number(quantity_random_number, min_val, max_val)

print(f"Список для суммирования нечетных элементов: {list_random_number}")

print(f"Сумма нечетных элементов: {sum_odd_elements(list_random_number)}")