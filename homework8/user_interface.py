import load_and_safe_data as l_s_d
import print_data
import add_data
import delete_data
import search_data
import choosing_action_for_user_interface as action_user
import removing_repetitions as del_rep_rec
import sorting_phone_book as sort_book
import logger


def work_phone_directory():

    data = l_s_d.loading_data_from_phone_directory()
    logger.log_entry("справочник запущен")
    
    while True:

        action = action_user.choosing_start_work_action()

        match action[0]:
            case 1:
                logger.log_entry(action[1])
                print_data.print_all_list_in_terminal(data)
            case 2:
                logger.log_entry(action[1])
                data.append(add_data.input_data_in_phone_directory())
            case 3:
                logger.log_entry(action[1])
                data = submenu_to_delete(data)
            case 4:
                logger.log_entry(action[1])
                print_data.print_all_list_in_terminal(\
                    search_data.search_data_in_telephone_directory(\
                        data, add_data.input_data_in_phone_directory("search")))
            case 5:
                logger.log_entry(action[1])
                data = sort_book.sorting_data(data)
            case 6:
                logger.log_entry(action[1])
                data = l_s_d.loading_data_from_phone_directory()
            case 7:
                logger.log_entry(action[1])
                submenu_to_saving_data(data)
            case 8:
                logger.log_entry(action[1])
                if submenu_to_exit_from_directory(data) == False: 
                    return True


def submenu_to_delete(data: list) -> list:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_to_delete()
        
        match action[0]:
            case 1:
                logger.log_entry(action[1])
                data = delete_data.delet_data_from_list(data)
                return data
            case 2:
                logger.log_entry(action[1])
                data = del_rep_rec.delet_repeat_data(data)
                return data
            case 3:
                logger.log_entry(action[1])
                return data


def submenu_to_saving_data(data: list) -> bool:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_to_saving_data()
        
        match action[0]:
            case 1:
                logger.log_entry(action[1])
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
            case 2:
                logger.log_entry(action[1])
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data), "column")
            case 3:
                logger.log_entry(action[1])
                return False
        return True


def submenu_to_exit_from_directory(data: list) -> bool:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_exit_from_directory()

        match action[0]:
            case 1:
                logger.log_entry(action[1])
                return False
            case 2:
                logger.log_entry(action[1])
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data),\
                    action_user.choosing_action_for_safe()[0])
                print("данные сохранены")
                return False
            case 3:
                logger.log_entry(action[1])
                return True