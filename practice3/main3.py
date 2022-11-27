'''
2. Задайте список. Напишите программу, которая определит, 
присутствует ли в заданном списке строк некое число.
['213213', 'dsf653', 'dsf', 'fdh76']
num = 3
Вывод: '213213', 'dsf653'
'''

def task2(sp: list, number: int) -> list:
    result = []
    for item in sp:
        if isinstance(item, str) and str(number) in item:
            result.append(item)
    return result if result else [-1]

lst1 = ['23232323', 'dfsdfgsdg564654', 'sdfg34', '3423424', '9878', 3455, 'df5']
print(*task2(lst1, 1))