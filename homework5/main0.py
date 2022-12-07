'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

from pathlib import Path

file_name_read = "file_for_read_text_main0.txt"
relative_file_directory_for_read = Path(file_name_read)

with open(relative_file_directory_for_read, 'r', encoding='utf-8') as data:
    text_in_file = data.read()

def my_function_search_in_line_text_and_clear(line: str, search_text: str) -> str:
    
    list_string = list(line.split(" "))
    
    resalt_list = list()
    
    for count in range(0, len(list_string), 1):
        
        if list_string[count].count(search_text) == 0:
            resalt_list.append(list_string[count])
    
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

'''
можно было вставить create_line в my_function_search_in_line_text_and_clear
но время поджимает ...
'''

def create_line(resalt_list: list) -> str:
        
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

print("Текст из файла:")
print(text_in_file)

search_text = "абв"

clear_text_my_function = my_function_search_in_line_text_and_clear(text_in_file, search_text)
print("Почистил строку с помощью my_function_search_in_line_text_and_clear:")
print(clear_text_my_function)

clear_list_filter = list(filter(lambda x: not search_text in x, text_in_file.split(" ")))
#clear_list_filter = list(filter(lambda x: search_text in x, text_in_file.split(" ")))
print("Почистил строку с помощью filter и create_line:")
print(create_line(clear_list_filter))

list_for_clear_list = text_in_file.split(" ")

clear_list = [list_for_clear_list[count] for count in range(0, len(list_for_clear_list), 1)\
     if not (search_text in list_for_clear_list[count])]

print("Почистил строку с помощью list comprehension и create_line:")
print(create_line(clear_list))

file_name_write = "file_for_write_text_main0.txt"
relative_file_directory_for_write = Path(file_name_write)

with open(relative_file_directory_for_write, 'a', encoding='utf-8') as data:
    data.write(str(f"{create_line(clear_list)}\n"))