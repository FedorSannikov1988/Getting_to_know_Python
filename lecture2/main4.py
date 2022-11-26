'''
Чтение данных из файла
'''

way_for_file = 'file.txt'

with open(way_for_file, 'r') as data:
    for line in data:
        print(line)