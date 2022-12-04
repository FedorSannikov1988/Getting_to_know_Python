def generate_polynomial(coefficients_polynomial: list) -> str():

    relalt_list: str = ''
    
    for item in range(0, len(coefficients_polynomial), 1):

        if coefficients_polynomial[item] == 0:
            relalt_list += ''
        elif (len(coefficients_polynomial)-item-1) == 1:
            relalt_list += str(coefficients_polynomial[item]) + '*x' + ' + '
        elif (len(coefficients_polynomial)-item-1) == 0:
            relalt_list += str(coefficients_polynomial[item]) + ' '
        else:
            relalt_list += str(coefficients_polynomial[item]) + '*x^' + str(len(coefficients_polynomial)-item-1) + ' + '

    relalt_list = relalt_list + '= 0'
    
    return relalt_list.replace('+ = 0', '= 0')