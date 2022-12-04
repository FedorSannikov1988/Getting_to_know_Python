'''
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.

Ввод: [1, 1, 2, 3, 4, 4, 4]

Вывод: [2, 3]
'''

def find_not_repeating_elements_in_list(list_elements: list) -> list():

    relalt_list = list()

    for element in list_elements:
        if list_elements.count(element) == 1:
            relalt_list.append(element)
    
    return relalt_list

def string_list_in_int_list(string_list_numbers: list) -> list():

    int_list_numbers = list()

    split_string_list_numbers  = string_list_numbers.split(" ")   
    
    while True:
        if split_string_list_numbers.count("") != 0:
            split_string_list_numbers.remove("")
        else:
            break

    for element in split_string_list_numbers:
        int_list_numbers.append(int(element))
    
    return int_list_numbers

string_list_numbers = input("Введите список элементов через пробел:")

numbers = string_list_in_int_list(string_list_numbers)

print(f"Вы ввели: {numbers}")

print("Cписок не повторяющихся элементов в веденной последовательности:")

print(find_not_repeating_elements_in_list(numbers))

sort_relalt_list = find_not_repeating_elements_in_list(numbers)
sort_relalt_list.sort()

print("Отсортированный список не повторяющихся элементов в веденной последовательности:")
print(sort_relalt_list)