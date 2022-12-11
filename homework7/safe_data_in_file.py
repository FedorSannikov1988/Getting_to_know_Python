from pathlib import Path

def input_data_in_phone_directory(data_for_write: list):
    
    file_name = "phone_directory.csv"
    relative_file_directory = Path(file_name)

    with open(relative_file_directory, 'w', encoding='utf-8') as data:
        for count in range(0, len(data_for_write), 1):
            data.write("{};{};{};{}\n".format(data_for_write[count][0], \
                data_for_write[count][1], data_for_write[count][2], data_for_write[count][3]))

#data_for_write = ["Фамилию", "Имя", "Отчество", 8900000000]
#input_data_in_phone_directory(data_for_write)