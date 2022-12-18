import search_data
import print_data
import add_data
import logger
import choosing_action_for_user_interface as action_user

def delet_data_from_list(data: list) -> list():

    print_data.print_all_list_in_terminal(data)

    byffer_for_choice = action_user.choosing_action_for_delet_data_from_list()

    logger.log_entry(byffer_for_choice[1])

    if byffer_for_choice[0] == 1:
        return delete_selected_lines(data)
    
    if byffer_for_choice[0] == 2:
        return delete_FIO(data)

def delete_selected_lines(data_in: list) -> list():
    
    while True:
        text = "\tВведите через пробел номера строк \nкоторые необходимо удалить после чего нажмите 'Enter'\n"
        human_answer_string = input(f"{text}")
        try:
            human_answer_namber = list(map(int, list(human_answer_string.split())))
            break
        except ValueError:
            print("Повторите ввод")
            continue
    
    function = lambda x: 1 <= x <= len(data_in)
    human_answer_namber = list(filter(function, human_answer_namber))
    logger.log_entry(str(human_answer_namber))

    data_out = []
    
    for count in range(0, len(data_in), 1):
        if human_answer_namber.count(int(count+1)) == 0:
            data_out.append(data_in[count])
    
    return data_out

def delete_FIO(data_in: list) -> list():

    data_for_delete = search_data.search_data_in_telephone_directory(data_in, add_data.input_data_in_phone_directory("search"))

    print_data.print_all_list_in_terminal(data_for_delete)

    logger.log_entry(str(data_for_delete))

    byffer_for_choice = action_user.choosing_action_for_delete_FIO()

    logger.log_entry(byffer_for_choice[1])

    if byffer_for_choice[0] == 1:
         data_out = list()
         [data_out.append(element) for element in data_in if element not in data_for_delete]
         return data_out
    else:
        return data_in