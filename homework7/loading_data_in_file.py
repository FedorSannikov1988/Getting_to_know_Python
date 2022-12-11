from pathlib import Path
import print_data

def loading_data_in_phone_directory() -> list:

    file_name = "phone_directory.csv"
    relative_file_directory = Path(file_name)

    with open(relative_file_directory, 'r', encoding='utf-8') as data_from_file:
        
        data_for_pars = list()        
        
        for line in data_from_file:
            data_for_pars.append(line)
        
        for count in range(0, len(data_for_pars), 1):
            data_for_pars[count] = data_for_pars[count].replace('\n', '')
        
        resalt_data = list()

        for count in range(0, len(data_for_pars), 1):
            resalt_data.append(data_for_pars[count].split(";"))

    return resalt_data

'''
data = loading_data_in_phone_directory()
print(data)
print_data.print_all_list_in_terminal(data)
'''
'''
#data_for_write = ["Фамилию", "Имя", "Отчество", 8900000000]
data = ['Фамилию;Имя;Отчество;8900000000', 'Фамилию;Имя;Отчество;8900000000', 'Иванов;Иван;Иванович;7245963']
print(data)
print(data[0].split(";"))
'''