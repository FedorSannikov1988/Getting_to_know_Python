'''
переменная со ссылкой на функцию 
'''

def mult(x):
    return x**2

mult_copi = mult

print(type(mult))
print(type(mult_copi))

print(mult(2))
print(mult_copi(2))