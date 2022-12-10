'''
1. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный. 
    
    *Пример:* 
    
    2+2 => 4; 
    
    1+2*3 => 7; 
    
    1-2*3 => -5;
    
    - Добавьте возможность использования скобок, меняющих приоритет операций.
        
        *Пример:* 
        
        1+2*3 => 7; 
        
        (1+2)*3 => 9;
'''

'''
def Summ (num1, num2):
    return num1 + num2
def Minus (num1, num2):
    return num1 - num2
def Multiplication (num1, num2):
    return num1 * num2
def Division (num1, num2):
    return num1/num2


user_string = '1-3*6'

def user_do (user_string ):
    res = ' '
    for i in range (0, len(user_string)):
        if (user_string[i] == '*') or (user_string[i] =='/'):
            if user_string[i] == '*':
                temp_value = str(Multiplication(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
                return res
            if user_string[i] == '/':
                temp_value = str(Division(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
                return res
                res = user_string[:i-1] + temp_value + user_string[i+2:] 
                print(res)
                return res
            if user_string[i] == '-':
                temp_value = str(Minus(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
                return res             

        

user_do(user_string)

user_do(user_do(user_string))
'''

'''
string_for_calculator = input("Введите выражение для калькулятора:")

buffer = 0

for count in range(0, len(string_for_calculator)-1, 1):
    if string_for_calculator[count].isdigit():
        buffer = int(string_for_calculator[count])
    elif string_for_calculator[count] == "+":
        buffer += int(string_for_calculator[count+1])
    elif string_for_calculator[count] == "-":
        buffer -= int(string_for_calculator[count+1])
    elif string_for_calculator[count] == "*":
        buffer *= int(string_for_calculator[count+1])

print(buffer)
'''

'''
import re
#text = input("Введите выражение: ")
text = "23-3"
var = re.findall(r'(-|/|\+|\*|[\d]+)', text)

print(var)
'''

'''
lambda x: (x:=x+1)
'''

import re
text = input("Введите выражение: ")
var = re.findall(r'(-|/|\+|\*|[\d]+)', text)

for count in range(0, len(var)-1):
    if var[count].isdigit():
        buf = int(var[count])
    elif var[count] == "+":
        buf += int(var[count+1])
    elif var[count] == "-":
        buf -= int(var[count+1])
    elif var[count] == "*":
        buf *= int(var[count+1])
    elif var[count] == "/":
        buf /= int(var[count+1])
print("Ответ: " + str(buf))