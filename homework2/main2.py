'''
3.Задайте список из n чисел последовательности (1 + 1/n)^n 
и выведите на экран их сумму.

Пример:
Для n=4 {1: 2.0 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
'''

def list_numbers_and_summa(namber):
    
    resalt_list = list()
    
    for count in range(1, namber+1, 1):
        resalt_list.append(round((1+(1/count))**count, 2))
    
    return [resalt_list, sum(resalt_list, 0)]


def validation(namber):
    
    natural_number = abs(int(namber))
    
    if natural_number == 0:
        natural_number = 1
    
    return natural_number


namber_string = input("Введите натуральное число N: ")

print(f"Список элементов: {list_numbers_and_summa(validation(namber_string))[0]};")
print(f"Сумма элементов: {list_numbers_and_summa(validation(namber_string))[1]};")