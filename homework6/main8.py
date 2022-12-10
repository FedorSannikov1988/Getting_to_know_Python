'''
Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
'''

'''
Использование filter и list comprehension

Функция creating_list_float взята
из домашнего задания №3 задача № 5 (homework3/main2.py)

'''

def namber_positive_fibonacci(namber: int) -> int:  

    if namber == 0:
        return 0
    elif namber in [1, 2]:
        return 1
    else:
        return (namber_positive_fibonacci(namber-1) + namber_positive_fibonacci(namber-2))

'''
До использования filter и list comprehension:
'''

def create_list_fibonacci_v1(lenght_fibonacci: int) -> list:

        lenght_fibonacci = abs(lenght_fibonacci)
        
        resalt_negative_list = list()
        
        resalt_positive_list = list()
        
        for count in range(-lenght_fibonacci, 0, 1):
            resalt_negative_list.append(((-1)**(abs(count)+1))*namber_positive_fibonacci(abs(count)))
        
        for count in range(0, lenght_fibonacci + 1, 1):
            resalt_positive_list.append(namber_positive_fibonacci(count))
        
        list_fibonacci = [*resalt_negative_list, *resalt_positive_list]
                
        return list_fibonacci

'''
Стало после использования filter и list comprehension:
'''

def create_list_fibonacci_v2(lenght_fibonacci: int) -> list:

        resalt_positive_list = [namber_positive_fibonacci(count) for count in range(0, abs(lenght_fibonacci)+1, 1)]
       
        resalt_negative_list_backwards_with_zero = [((-1)**(abs(count)+1))*namber_positive_fibonacci(abs(count)) for count in range(0, abs(lenght_fibonacci)+1, 1)]
        
        resalt_negative_list_backwards = list(filter(lambda x: x!=0, resalt_negative_list_backwards_with_zero))

        resalt_negative_list = [resalt_negative_list_backwards[len(resalt_negative_list_backwards)-count-1] for count in range(0, len(resalt_negative_list_backwards), 1)]
        
        return resalt_negative_list + resalt_positive_list

natural_number = int(input("Введите k для которого будет составлен список чисел Фибоначчи в том числе для отрицательных индексов: "))

list_fibonacci_v1 = create_list_fibonacci_v1(natural_number)
print("Последовательность Фиббаначи вариант №1:")
print(list_fibonacci_v1)


list_fibonacci_v2 = create_list_fibonacci_v2(natural_number)
print("Последовательность Фиббаначи вариант №2:")
print(list_fibonacci_v2)