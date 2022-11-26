'''
2. Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.

Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

def list_numbers(namber):
    
    byffer = 1
    resalt_list = list()

    for count in range(1, namber+1, 1):
        byffer *= count
        resalt_list.append(byffer)

    return resalt_list


def validation(namber):
    
    natural_number = abs(int(namber))
    
    if natural_number == 0:
        natural_number = 1
    
    return natural_number


namber_string = input("Введите натуральное число N: ")

print(list_numbers(validation(namber_string)))