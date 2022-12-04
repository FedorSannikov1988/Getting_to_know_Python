'''
1. Вычислить число c заданной точностью d

Пример:
При d = 0.001, π = 3.141
'''

def input_validation_data(accuracy_calculations: str) -> bool:
    whole_part = int(accuracy_calculations.split('.')[0])
    fractional_part = int(accuracy_calculations.split('.')[1])

    if whole_part == 0 and fractional_part == 1:
        return True
    else:
        return False

def number_after_point(accuracy_calculations: str) -> int:
    return len(accuracy_calculations.split('.')[1])

def my_round_v1(namber_pi: float, number_after_point: int) -> str|float:
    namber_pi_str = str(namber_pi)
    whole_part_str = str(namber_pi_str.split('.')[0])
    fractional_part_str = str(namber_pi_str.split('.')[1])
    
    round_fractional_part_str = ''
    
    for count in range(0, number_after_point, 1):
        round_fractional_part_str += fractional_part_str[count]
    
    return[whole_part_str + "." + round_fractional_part_str , float(whole_part_str + "." + round_fractional_part_str)]

def my_namber_pi(accuracy: int) -> float:

    my_namber_pi: float = 0
    
    for n in range(0, accuracy, 1):
        my_namber_pi += (1/16**n)*((4/((8*n)+1))-(2/((8*n)+4))-(1/((8*n)+5))-(1/((8*n)+6)))
    
    return(my_namber_pi)

import math
math.pi

ACCURACY_FOR_MY_NAMBER_PI = 10000

print("Введите точность вычисления числа Пи в следующем формате при d = 0.001 Пи = 3.141")
accuracy_calculations = input("d = ")

if input_validation_data(accuracy_calculations):
    print(f"Вариант №1: число Пи с заданной точностью равно {round(math.pi, number_after_point(accuracy_calculations))}")
    print(f"Вариант №1.1: число Пи с заданной точностью равно {round(my_namber_pi(ACCURACY_FOR_MY_NAMBER_PI), number_after_point(accuracy_calculations))}")
    for_format = "." + str(number_after_point(accuracy_calculations)) + "f"
    print(f"Вариант №2: число Пи с заданной точностью равно {format(math.pi, for_format)}")
    print(f"Вариант №3: число Пи с заданной точностью равно {my_round_v1(math.pi, number_after_point(accuracy_calculations))[0]}")
    print(f"Вариант №3.3: число Пи с заданной точностью равно {my_round_v1(my_namber_pi(ACCURACY_FOR_MY_NAMBER_PI), number_after_point(accuracy_calculations))[0]}")
else:
    print("Введенное значение вычисления точности числа Пи не соответсвует формату ввода")