def power_two(x):
    return x**2

def summa(x):
    return x+x

def summa_v2(x, y):
    return x+y

copy_summa_v2 = summa_v2

improved_clone_summa_v2 = lambda x, y: x+y

def mult(x):
    return x*x

def mult_v2(x, y):
    return x*y

copy_mult_v2 = mult_v2

improved_clone_mult_v2 = lambda x, y: x*y

def math(function, variable):
    return function(variable)

def math_v2(function, variable1, variable2):
    return function(variable1, variable2)

print(" ----- ")
print(math_v2(summa_v2, 1, 6))
print(math_v2(copy_summa_v2, 1, 6))
print(math_v2(improved_clone_summa_v2, 1, 6))

print(" ----- ")
print(math_v2(mult_v2, 1.5, 6))
print(math_v2(copy_mult_v2, 1.5, 6))
print(math_v2(improved_clone_mult_v2, 1.5, 6))

print(" ----- ")
#print(math(summa, 3))
#print(math(power_two, 3))