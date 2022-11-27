'''
Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.

Пример:
Для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

def namber_positive_fibonacci(namber: int) -> int:
    if namber == 0:
        return 0
    elif namber in [1, 2]:
        return 1
    else:
        return (namber_positive_fibonacci(namber-1) + namber_positive_fibonacci(namber-2))

def create_list_positive_fibonacci(lenght_fibonacci: int) -> list:

    lenght_fibonacci = abs(lenght_fibonacci)

    resalt_list = list()
    
    for count in range(0, lenght_fibonacci + 1, 1):
        resalt_list.append(namber_positive_fibonacci(count))
    
    return resalt_list

def create_list_negative_fibonacci(list_positive_fibonacci: list) -> list:
   
    resalt_list = list()
    
    for count in range(0, len(list_positive_fibonacci)-1, 1):
        
        if count%2:
            flag_znak = 1
        else:
            flag_znak = -1
        
        resalt_list.insert(count,(flag_znak*list_positive_fibonacci[len(list_positive_fibonacci)-count-1]))

    return resalt_list

def create_list_fibonacci(lenght_fibonacci: int) -> list:
   
    list_fibonacci = list()
    
    list_positive_fibonacci = create_list_positive_fibonacci(lenght_fibonacci)
    
    #list_fibonacci = create_list_negative_fibonacci(list_positive_fibonacci) + list_positive_fibonacci
    list_fibonacci = [*create_list_negative_fibonacci(list_positive_fibonacci), *list_positive_fibonacci]

    return list_fibonacci

natural_number = int(input("Введите k для которого будет составлен список чисел Фибоначчи в том числе для отрицательных индексов: "))

list_fibonacci = create_list_fibonacci(natural_number)

print(list_fibonacci)

with open('file_create_main4.txt', 'a') as data:
    data.write(str(f"{list_fibonacci}\n"))