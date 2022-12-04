'''
1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).
'''

file_name = "main0.txt"

'''
with open(file_name, 'r') as data:
    string_data = data.read().split(' ')
print(string_data)
'''
with open(file_name, 'r') as data:
    string_data = data.read()
print(string_data)
string_data = string_data.split(' ')
print(string_data)

list_nums = list()
for i in range(0, len(string_data), 1):
    list_nums.append(int(string_data[i]))
print(list_nums)

print(f"Минимум из файла: {min(list_nums)} | Максимум из файла: {max(list_nums)}")