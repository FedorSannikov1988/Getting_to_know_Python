import loading_data_in_file
import safe_data_in_file
import print_data
import add_data
import delete_data
import search_data

def choosing_action():

    print("\n")
    print("\t        ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 - просмотреть все записи в справочнике")
    print("\t 2 - добавить запись в справочник")
    print("\t 3 - удалить запись из справочника")
    print("\t 4 - найти запись в справочнике")
    print("\t 5 - выйти из справочника")

    while True:
        human_answer_string = input(f"Какое действие выбираете: ")
        
        if not human_answer_string.isdigit() or int(human_answer_string) > 5 or int(human_answer_string) < 1 :
            print("Повторите ввод действия")
            continue

        try:
            human_answer_namber = int(human_answer_string)
            break
        except ValueError:
            print("Повторите ввод действия")
            continue
    
    return human_answer_namber

def work_phone_directory():
    
    data = loading_data_in_file.loading_data_in_phone_directory()
    
    while True:
        action = choosing_action()
        match action:
            case 1:
                print_data.print_all_list_in_terminal(data)
            case 2:
                input_data = add_data.input_data_in_phone_directory()
                data.append(input_data)
            case 3:
                data = delete_data.delet_data_from_list(data)
            case 4:
                print("Еще не написал")
            case 5:
                safe_data_in_file.input_data_in_phone_directory(data)
                break