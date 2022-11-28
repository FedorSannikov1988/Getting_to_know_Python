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

natural_number = int(input("Введите k для которого будет составлен список чисел Фибоначчи в том числе для отрицательных индексов: "))

list_fibonacci = create_list_fibonacci(natural_number)
print("Последовательность Фиббаначи:")
print(list_fibonacci)

with open('file_create_main4.txt', 'a') as data:
    data.write(str("Fibonacci:\n"))
    data.write(str(f"{list_fibonacci}\n"))