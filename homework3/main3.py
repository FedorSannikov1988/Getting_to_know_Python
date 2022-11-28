'''
4. Напишите программу, которая будет преобразовывать 
десятичное число в двоичное.

Пример:
45 -> 101101
3 -> 11
2 -> 10
'''

import copy

def conversion_decimal_binary(natural_number: int) -> str|int:

    string_resalt = str()
    
    copi_natural_number_one = copy.deepcopy(natural_number)
    copi_natural_number_two = copy.deepcopy(natural_number)

    if natural_number < 0:
        copi_natural_number_one = abs(copi_natural_number_one)
        copi_natural_number_two = abs(copi_natural_number_two)
        simvol = "-0b"
        flag_znak = -1
    else:
        simvol = "0b"
        flag_znak = 1

    count_digit_nambers = 0
    
    while copi_natural_number_one > 0:
        copi_natural_number_one = copi_natural_number_one//2
        count_digit_nambers += 1
        
    int_resalt = 0
    
    for count in range(0, count_digit_nambers, 1):
        int_resalt += ((copi_natural_number_two%2)*(10**count))
        string_resalt = (str(copi_natural_number_two%2) + string_resalt)
        copi_natural_number_two = (copi_natural_number_two//2)

    #tuple_resalt = tuple([simvol+string_resalt, flag_znak*int_resalt])
    
    return (simvol+string_resalt, flag_znak*int_resalt)

natural_number = int(input("Введите натуральное число для преобразования из 10-ой формы записи в 2-ую: "))

print(f"Спомощью встроенной функции способ №1: {bin(natural_number)}")
print(f"Спомощью встроенной функции способ №2: {format(natural_number, '#b')}")
print(f"Спомощью встроенной функции способ №3: {format(natural_number, 'b')}")
print(f"Спомощью моей функции способ №4: {conversion_decimal_binary(natural_number)[0]}")
print(f"Спомощью моей функции способ №5: {conversion_decimal_binary(natural_number)[1]}")