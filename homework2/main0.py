'''
1. Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.

Пример:
0,56 -> 11
'''

def separation(real_number_string):
    
    if real_number_string.find(","):
        real_number_string = real_number_string.replace(",", ".")

    if real_number_string.find(".") == -1:
        real_number_string += ".0"

    list_string_integer_and_fractional_part = real_number_string.split(".") 
    integer_part_number = abs(int(list_string_integer_and_fractional_part[0]))
    fractional_part_number = int(list_string_integer_and_fractional_part[1])

    return [integer_part_number, fractional_part_number]

def summa_nambers(namber):
    symma = 0
    while namber:
        symma += namber%10
        namber = namber//10
    return symma

real_number_string = input("Введите вещественное число: ")

print(f"Сумма целой части числа {real_number_string}: {summa_nambers(separation(real_number_string)[0])}")
print(f"Сумма дробной части числа {real_number_string}: {summa_nambers(separation(real_number_string)[1])}")

all_summa = summa_nambers(separation(real_number_string)[0]) + summa_nambers(separation(real_number_string)[1])
print(f"Сумма всех цифр числа {real_number_string}: {all_summa}")