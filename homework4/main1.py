'''
2. Задайте натуральное число N.
Напишите программу, которая составит 
список простых множителей числа N.
'''

def definition_prime_numbers(check_namber: int) -> bool:
    
    count: int = 2
    
    if check_namber == 0 or check_namber == 1 :
        return False
    elif check_namber == count:
        return True
    
    while check_namber > count:
        if check_namber%count == 0:
            return False
        count += 1
    else:
        return True

def find_simple_multiplier(check_namber: int) -> list():

    count: int = 2

    resalt_list = list()
    
    while check_namber > 1:
        
        if definition_prime_numbers(count) and check_namber%count == 0:
            resalt_list.append(count)
            check_namber = check_namber//count
        else:
            count +=1
   
    return resalt_list

print("Задайте натуральное число N:")
natural_number = abs(int(input("N = ")))
print(f"Вы задали {natural_number}")

if definition_prime_numbers(natural_number):
    print(f"Число {natural_number} является простым")
else:
    print(f"Cписок простых множителей числа {natural_number}: {find_simple_multiplier(natural_number)}")