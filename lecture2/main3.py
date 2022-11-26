'''
Чтение данных из файла
'''

way = 'file.txt'

data = open(way, 'r')

for line in data:
    print(line)

data.close()