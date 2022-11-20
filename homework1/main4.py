'''
5.Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

import math
from math import sqrt

def coordinates_point_entry():
    somvol = None
    array = list()
    for count in range(0,2,1):
        if (count == 0): somvol = 'X'
        else: somvol = 'Y'
        array.append(float(input(f"Введите координату {somvol} = ")))
    return array

def distance_calculation(point_a, point_b):
    #distance = ((((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2)) ** (0.5))
    #distance = math.sqrt( ((point_a[0] - point_b[0])**2) + ((point_a[1] - point_b[1])**2) ) 
    distance = sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2)) 
    return distance

print('Введите координаты точки А:')
point_a = coordinates_point_entry()
print('Введите координаты точки B:')
point_b = coordinates_point_entry()

distance = round(distance_calculation(point_a, point_b), 3)
print('Расстояние между точками А и B:')
print(distance)