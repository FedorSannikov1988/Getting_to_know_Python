'''
4. Напишите программу, которая будет преобразовывать 
десятичное число в двоичное.

Пример:
45 -> 101101
3 -> 11
2 -> 10
'''

def conversion_decimal_binary(natural_number: int) -> str:

    string_resalt = str()

    if natural_number < 0:
        natural_number = abs(natural_number)
        simvol = "-0b"
    else:
        simvol = "0b"    
    
    while natural_number > 0:
        string_resalt = str(natural_number%2) + string_resalt
        natural_number = natural_number//2
    
    return(simvol + string_resalt)

natural_number = int(input("Введите натуральное число для преобразования из 10-ой формы записи в 2-ую: "))

print(f"Спомощью встроенной функции способ №1: {bin(natural_number)}")
print(f"Спомощью встроенной функции способ №2: {format(natural_number, '#b')}")
print(f"Спомощью встроенной функции способ №3: {format(natural_number, 'b')}")
print(f"Спомощью моей функции способ №4: {conversion_decimal_binary(natural_number)}")