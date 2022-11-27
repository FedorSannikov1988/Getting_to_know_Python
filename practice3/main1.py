'''
1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
генератора псевдослучайных чисел (time).
'''
'''
import datetime

a = datetime.datetime.now().microsecond

print(a)
'''

from datetime import datetime

def get_random_number(n):
    now = datetime.now()
    random_number = now.time().second * now.time().minute * now.time().microsecond // now.time().minute
    return random_number % 10**n

print(get_random_number(3))