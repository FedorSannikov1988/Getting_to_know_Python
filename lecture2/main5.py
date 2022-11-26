
def f0(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def f1():
    print("Вызвана функция из другого файла")
    return 1

def f2(x):
    return x**2

'Задание значений по умолчанию'

def new_string_1(symbol, count = 1):
    return symbol * count

def new_string_2(symbol = '*', count = 1):
    return symbol * count