'''
Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.

Пример:
Для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

import copy

def namber_positive_fibonacci(namber: int) -> int:  

    if namber == 0:
        return 0
    elif namber in [1, 2]:
        return 1
    else:
        return (namber_positive_fibonacci(namber-1) + namber_positive_fibonacci(namber-2))


def create_list_fibonacci(lenght_fibonacci: int) -> list:

        lenght_fibonacci = abs(lenght_fibonacci)
        
        resalt_negative_list = list()
        
        resalt_positive_list = list()
        
        for count in range(-lenght_fibonacci, 0, 1):
            resalt_negative_list.append(((-1)**(abs(count)+1))*namber_positive_fibonacci(abs(count)))
        
        for count in range(0, lenght_fibonacci + 1, 1):
            resalt_positive_list.append(namber_positive_fibonacci(count))
        
        list_fibonacci = [*resalt_negative_list, *resalt_positive_list]
                
        return list_fibonacci


def create_list_fibonacci_v2(lenght_fibonacci: int) -> list:

        lenght_fibonacci = abs(lenght_fibonacci)

        resalt_negative_list = list()

        resalt_positive_list = list()

        resalt_list = list()

        for count in range(0, lenght_fibonacci + 1, 1):
            resalt_positive_list.append(namber_positive_fibonacci(count))

        #resalt_negative_list = copy.deepcopy(resalt_positive_list)
        resalt_negative_list = resalt_positive_list[:]

        resalt_negative_list.pop(0)
        
        for count in range(0, len(resalt_negative_list), 1):

            if count%2:
                flag_znak = -1
            else:
                flag_znak = 1

            resalt_negative_list[count] = flag_znak*resalt_negative_list[count]
        
        byffer: int = 0

        lengt_negative_list = len(resalt_negative_list)
        
        for count in range(0, int(lengt_negative_list/2), 1):

            byffer = resalt_negative_list[count]
            resalt_negative_list[count] = resalt_negative_list[lengt_negative_list-count-1]
            resalt_negative_list[lengt_negative_list-count-1] = byffer
        
        #resalt_list = [*resalt_negative_list, *resalt_positive_list]
        resalt_list = resalt_negative_list + resalt_positive_list

        return resalt_list


natural_number = int(input("Введите k для которого будет составлен список чисел Фибоначчи в том числе для отрицательных индексов: "))


list_fibonacci = create_list_fibonacci(natural_number)
print("Последовательность Фиббаначи вариант №1:")
print(list_fibonacci)


list_fibonacci_v2 = create_list_fibonacci_v2(natural_number)
print("Последовательность Фиббаначи вариант №2:")
print(list_fibonacci_v2)


with open('file_create_main4.txt', 'a') as data:
    data.write(str("Fibonacci v1:\n"))
    data.write(str(f"{list_fibonacci}\n"))
    data.write(str("Fibonacci v2:\n"))
    data.write(str(f"{list_fibonacci_v2}\n"))