'''
1. Напишите программу, которая принимает на вход число N 
и выдаёт последовательность из N членов.

Пример:
Для N = 5: 1, -3, 9, -27, 81
'''

'''
my_list = list()

n = int(input("Введите N: "))

for i in range(0, n+1, 1):
    my_list.append( (-3)**i )

print(my_list)
'''

'''
i = int(input('Введите число N: '))
y = 1
while i >= 1:
    print(int(y))
    y = y * (-3)
    i = i - 1
'''

i = int(input('Введите число N: '))
y = 1
while i:
    print(int(y))
    y = y * (-3)
    i = i - 1

'''
while k:=int(input('--> ')) <= 0:
    pass
'''