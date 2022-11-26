'''
Добавление данных в файл
'''

colors = ['red1', 'green1', 'blue1']

data = open('file.txt', 'a')
#data.writelines(f'{colors}\n')
#data.write(f'{colors}\n')
data.write(f'{colors}\t')
data.close()