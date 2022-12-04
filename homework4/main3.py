'''
4.Задана натуральная степень k. Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
'''

import random
from pathlib import Path
import functions_for_main3_main4 as my_function

def generate_coefficients_polynomial(quantity: int) -> list():

    relalt_list = list()

    for _ in range(0, quantity+1, 1):
        relalt_list.append(random.randint(0, 100))
    
    return relalt_list

print("Задайте натуральную степень k:")
natural_degree = abs(int(input("k = ")))
if natural_degree == 0: natural_degree = 1
print(f"Вы задали: {natural_degree}")

print("Сгенерированный многочлен #1:")
polynomial_one = my_function.generate_polynomial(generate_coefficients_polynomial(natural_degree))
print(polynomial_one)

print("Сгенерированный многочлен #2:")
polynomial_two = my_function.generate_polynomial(generate_coefficients_polynomial(natural_degree))
print(polynomial_two)

file_name_one = "create_file_one_with_polynomial.txt"
home_directory = Path.home()
absolut_file_directory = Path(home_directory, "Desktop", "getting to know Python", "homework4", file_name_one)

with open(absolut_file_directory, 'a') as data:
    data.write(str(f"{polynomial_one}\n"))

file_name_two = "create_file_two_with_polynomial.txt"
relative_file_directory = Path(file_name_two)

with open(relative_file_directory, 'a') as data:
    data.write(str(f"{polynomial_two}\n"))