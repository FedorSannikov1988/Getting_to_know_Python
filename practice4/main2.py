'''
3. Задайте два числа. Напишите программу, которая 
найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''

a = int(input("Введите 1 число >> "))
b = int(input("Введите 2 число >> "))

def NOK(a,b):
    i = 2 #min(a, b)
    print('i = ', i)
    while True:
        if a%i==0 and b%i==0:
            break
        i += 1
    return i

print(NOK(a,b))