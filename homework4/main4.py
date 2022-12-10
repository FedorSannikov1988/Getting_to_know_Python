'''
5. Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов 
(складываются числа, у которых "х" в одинаковых степенях). 
Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 
'''

from pathlib import Path
import functions_for_main3_main4 as my_function

file_name_one = "create_file_one_with_polynomial.txt"
home_directory = Path.home()
absolut_file_directory = Path(home_directory, "Desktop", "getting to know Python", "homework4", file_name_one)

with open(absolut_file_directory, 'r') as data_in_file:
    
    polynomial_one = list()
    
    for line in data_in_file:
        polynomial_one.append(line)

    for count in range(0, len(polynomial_one), 1):
        polynomial_one[count] = polynomial_one[count].replace('\n', '')

file_name_two = "create_file_two_with_polynomial.txt"
relative_file_directory = Path(file_name_two)

with open(relative_file_directory, 'r') as data_in_file:

    polynomial_two = list()

    for line in data_in_file:
        polynomial_two.append(line)
    
    for count in range(0, len(polynomial_two), 1):
        polynomial_two[count] = polynomial_two[count].replace('\n', '')

def search_coefficients_polynomial(polynomial: str) -> list:
    
    elements_polynomial = polynomial.replace(' +', '').replace(' = 0', '').split(' ')

    resalt_dictionary = {}

    for count in range(0, len(elements_polynomial), 1):
        if elements_polynomial[count].count('*x^') == 1:
            resalt_dictionary[int(elements_polynomial[count].split('*x^')[1])] = int(elements_polynomial[count].split('*x^')[0])
        elif elements_polynomial[count].count('*x') == 1:
            resalt_dictionary[1] = int(elements_polynomial[count].replace('*x', ''))
        else:
            resalt_dictionary[0] = int(elements_polynomial[count])

    return resalt_dictionary

def dictionary_to_do_int_list(dictionary) -> list:

    resalt_list = list()

    for count in range(0, max(list(dictionary.keys()))+1, 1):
        if count in dictionary:
            resalt_list.append(dictionary[count])
        else:
            resalt_list.append(0)

    resalt_list.reverse()

    return resalt_list

'''
не использую def sum_list_items(list_one: list, list_two: list) но жалко удалять 
'''

def sum_list_items(list_one: list, list_two: list) -> list:

    if len(list_one) > len(list_two):
        main_list = list_one[:]
    elif len(list_one) < len(list_two):
        main_list = list_two[:]
    else:
        main_list = list_one[:]

    for count in range(0, min(len(list_one), len(list_two)), 1):
        main_list[count] = list_one[count] + list_two[count]
    
    return main_list

def sum_dictionary_items(dictionary_one, dictionary_two):

    a = (dictionary_one, dictionary_two)

    resultdict = {}
    
    for dictionary in a:
        for key in dictionary:
            try:
                resultdict[key] += dictionary[key]
            except KeyError:
                resultdict[key] = dictionary[key]    
    
    return resultdict

'''
делал polynomial_one[0] для цикла но под конец устал и поэтому работал только с 0 элеменотом списка 
однако тестировал на разных строчках из файла да и в задаче не говорилось что нужно считать все строки 
с многочленами что бы получить суммарный многочлен для каждой строки
'''

item1 = 1 #номер строки в файле №1
item2 = 1 #номер строки в файле №2

print("Многочлен считанный из файла: create_file_one_with_polynomial.txt")
print(polynomial_one[item1])

print("Многочлен считанный из файла: create_file_two_with_polynomial.txt")
print(polynomial_two[item2])

coefficients_polynomial_one = search_coefficients_polynomial(polynomial_one[item1])
coefficients_polynomial_two = search_coefficients_polynomial(polynomial_two[item2])

polynomial_three = \
    my_function.generate_polynomial(dictionary_to_do_int_list(sum_dictionary_items(\
        coefficients_polynomial_one, coefficients_polynomial_two)))

print("Итоговый сгенерированный многочлен:")
print(polynomial_three)

file_name_three = "create_file_three_with_polynomial.txt"
relative_file_directory = Path(file_name_three)

with open(relative_file_directory, 'a') as data:
    data.write(str(f"{polynomial_three}\n"))