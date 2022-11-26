'''
Перезапись всех данных в файле
'''

colors = ['red2', 'green2', 'blue2']

data = open('file.txt', 'w')
data.writelines(f'{colors}\n')
data.close()