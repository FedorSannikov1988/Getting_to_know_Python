import search_data
import print_data
import add_data

def delet_data_from_list(data: list):

    print_data.print_all_list_in_terminal(data)

    print("\n")
    print("\t ПРОЦЕДУРА УДАЛЕНИЯ ДАННЫХ:")
    print("\t---------------------------")
    print("\t Выберите действие:")
    print("\t 1 -  удалить запись по номеру")
    print("\t 2 -  удалить записи по Ф.И.О.")   

    '''
    while True: надо обернуть 
    в функцию как будет время
    '''
    
    human_answer_namber = validation_human_answer(2, 1)
    
    if human_answer_namber == 1:
        return delete_selected_lines(data)
    
    if human_answer_namber == 2:
        return delete_FIO(data)

def delete_selected_lines(data_in: list):
    
    while True:
        text = "\tВведите через пробел номера строк \nкоторые необходимо удалить после чего нажмите 'Enter'\n"
        human_answer_string = input(f"{text}")
        try:
            human_answer_namber = list(map(int, list(human_answer_string.split())))
            break
        except ValueError:
            print("Повторите ввод")
            continue
    
    function = lambda x: x <= len(data_in)
    human_answer_namber = list(filter(function, human_answer_namber))

    data_out = []
    
    for count in range(0, len(data_in), 1):
        if human_answer_namber.count(int(count+1)) == 0:
            data_out.append(data_in[count])
    
    return data_out

def delete_FIO(data_in: list):

    data_for_delete = search_data.search_data_in_telephone_directory(data_in, add_data.input_data_in_phone_directory("search"))

    print_data.print_all_list_in_terminal(data_for_delete)

    print("\n")
    print("\t УДАЛИТЬ ЭТИ ДАННЫЕ:")
    print("\t Выберите действие:")
    print("\t 1 -  удалить")
    print("\t 2 -  не удалять") 

    '''
    надо писать функцию но время 
    сдачи поджиает
    '''

    human_answer_namber = validation_human_answer(2, 1)

    if human_answer_namber == 1:
         data_out = list()
         [data_out.append(element) for element in data_in if element not in data_for_delete]
         return data_out
    else:
        return data_in

def validation_human_answer(max_answer: int, min_answer: int):

        while True:
            human_answer_string = input(f"Какое действие выбираете: ")
            
            if not human_answer_string.isdigit() or int(human_answer_string) > max_answer or int(human_answer_string) < min_answer:
                print("Повторите ввод действия")
                continue
            try:
                human_answer_namber = int(human_answer_string)
                break
            except ValueError:
                print("Повторите ввод действия")
                continue
        return human_answer_namber