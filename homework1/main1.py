'''
Напишите программу для проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
 ⋀ - and 
 ⋁ - or 
 ¬ - not
'''

def left_expression(X, Y, Z):
    return (not (X or Y or Z))


def right_expression(X, Y, Z):
    return (not (X) and not (Y) and not (Z))


def output_screen(X, Y, Z):
    return (print(f'¬({X} ⋁ {Y} ⋁ {Z}) = {left_expression(X, Y, Z)};   ¬{X} ⋀ ¬{Y} ⋀ ¬{Z} = {right_expression(X, Y, Z)};   Равенство левой и правой части: {left_expression(X, Y, Z) == right_expression(X, Y, Z)}.'))


def validation_rezalt(bool_list_resalt):
    for count in range(0,len(bool_list_resalt),1):
        if (bool_list_resalt[count] == False):
            print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z НЕ верно для всех значений предикат')
            break
    else:
        print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для всех значений предикат')
    
    return


bool_list = [True, False]
bool_list_resalt = list()


print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print(end='\n')


for X in bool_list:
    for Y in bool_list:
        for Z in bool_list:
            output_screen(X, Y, Z)
            bool_list_resalt.append( (left_expression(X, Y, Z) == right_expression(X, Y, Z)) )


print(end='\n')
print('Итог:')
validation_rezalt(bool_list_resalt)