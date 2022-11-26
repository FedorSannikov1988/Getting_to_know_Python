'''
2. Для натурального n создать последовательности 3n + 1.
    
Пример:
Для n = 6: 4, 7, 10, 13, 16, 19
'''

'''
lst = []
n = int(input("Write count: "))
for n in range(1,n+1):
    lst.append(3*n+1 )
    
print(lst)
'''

n = int(input('Введите n:'))
print('Для n=', end=' ')
for i in range(1, n+1):
    print(3*i + 1, end=', ')