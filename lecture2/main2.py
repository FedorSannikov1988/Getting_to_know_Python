'''
Запись данных в файл
Автоматическое закрытие файла
'''

colors = ['red3', 'green3', 'blue3']

with open('file.txt', 'a') as data:
    data.write(f'{colors}\t')