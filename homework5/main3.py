'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

'''
нашол протестировал и разобрал две версии алгоритма rle_encoder
версия 1 изящна не думаю что сходу смог бы её возпроизвести
версия 2 топорненькая её я бы выдать смог после дня раздумий 
и кучи компилящий
'''
def rle_encoder_v1(input_string: str) -> str:

    encoding = str()

    i = 0
    
    while i < len(input_string): 
        
        count = 1

        while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:

            count = count + 1
            i = i + 1
        
        encoding += str(count) + input_string[i]
        i = i + 1
    
    return encoding

def rle_encoder_v2(data: str) -> str:

    encoding = ''
    prev_char = ''
    count = 1

    if not data: 
        return ''

    for char in data:

        if char != prev_char:
              
            if prev_char:
                encoding += str(count) + prev_char
            
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        
    return encoding

'''
нашол протестировал и разобрал  rle_dencoder
в приципе не сложно
вынес две "штуки": .isdigit() и char * int(count)
будет время напишу свою функцию заменив char * int(count) 
на цикл for
'''
def rle_decoder_v1(data: str) -> str:

    decode = ''
    count = ''
    
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

from pathlib import Path

file_name_read = "file_for_read_text_for_rle_encoder_main3.txt"
relative_file_directory_for_read = Path(file_name_read)

file_name_write = "file_for_read_text_for_rle_decoder_main3.txt"
relative_file_directory_for_write = Path(file_name_write)

with open(relative_file_directory_for_read, 'r', encoding='utf-8') as data:
    text_in_file = data.read()

print("Считанные данные из файла file_for_read_text_for_rle_encoder_main3.txt:")
print(text_in_file)

print("Теже данные только после RLE сжатия:")
data_rle_encoder = rle_encoder_v1(text_in_file)
print(data_rle_encoder)

print("Теже данные только после RLE восстановления и записанные в файл :")
data_rle_decoder = rle_decoder_v1(data_rle_encoder)
print(data_rle_decoder)

with open(relative_file_directory_for_write, 'a', encoding='utf-8') as data:
    data.write(data_rle_decoder)