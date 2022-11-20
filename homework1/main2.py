'''
3.Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
находится эта точка.

Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

namber_quarter = ['1-ая четверть', '2-ая четверть', '3-я четверть', '4-ая четверть']
x_koordinata = float(input('Введите значение координаты Х: '))
y_koordinata = float(input('Введите значение координаты Y: '))

if ( (x_koordinata != 0) and (y_koordinata != 0) ):
    if   ( (x_koordinata > 0) and (y_koordinata > 0)  ): byffer = 0
    elif ( (x_koordinata < 0) and (y_koordinata > 0)  ): byffer = 1
    elif ( (x_koordinata < 0) and (y_koordinata < 0)  ): byffer = 2
    elif ( (x_koordinata > 0) and (y_koordinata < 0)  ): byffer = 3
    print(f'Введенные координаты X={x_koordinata} и Y={y_koordinata} соответствуют: {namber_quarter[byffer]}')
elif (x_koordinata == 0 ):
    print('Введенное Вами значение координаты Х равно нулю. Будьте внимательнее.')
elif (y_koordinata == 0 ):
    print('Введенное Вами значение координаты Y равно нулю. Будьте внимательнее.')