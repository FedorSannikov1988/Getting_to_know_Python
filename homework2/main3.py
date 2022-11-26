'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных индексах. 
Индексы вводятся одной строкой, через пробел.

n = 3
[-3, -2, -1, 0, 1, 2, 3]
--> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0
'''

def validation_namber(namber):
    
    natural_number = abs(int(namber))
    
    if natural_number == 0:
        natural_number = 1
    
    return natural_number

def validation_index(array_index, array_element):
    
    max_index = len(array_element) - 1
    
    for count in range(0, len(array_index), 1):
        if array_index[count] > max_index:
            array_index[count] = max_index
        elif array_index[count] < 0:
            array_index[count] = 0

    return array_index

def create_list(namber):
    
    resalt_list = list()
    
    for count in range(-namber, namber+1, 1):
        resalt_list.append(count)
    
    return resalt_list


def input_index_multiplying_element(text):
    
    string = input(text)

    resalt_list = list()
    
    for count in range(0, len(string.split()), 1):
        resalt_list.append(int(string.split()[count]))
    
    return resalt_list


def multiplying_element_list(index, element):
    
    byffer = 1

    for count in range(0, len(index), 1):
        byffer = byffer * element[index[count]]
    
    return byffer


namber_string = input("Введите натуральное положительное число N: ")
print(f"Считаем что Вы ввели число: {validation_namber(namber_string)}")


nambers = create_list(validation_namber(namber_string))
print(nambers)


indexing = input_index_multiplying_element("Введите индексы элементов которые необходимо перемножить: ")
print(f"Введенные значения индексов: {indexing}")


indexing = validation_index(indexing, nambers)


print(f"Значения индесов после валидации/проверки: {indexing}")
print(f"Произведение элементов: {multiplying_element_list(indexing, nambers)}")