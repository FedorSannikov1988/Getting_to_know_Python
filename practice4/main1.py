'''
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    1) с помощью математических формул нахождения корней квадратного уравнения
    2) с помощью дополнительных библиотек Python (scipy)
'''

from sympy.solvers import solve
from sympy import Symbol

def fun(a,b,c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)
    
print('Корни уравнения:', *fun(1, -16, 28))

'''
import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
'''