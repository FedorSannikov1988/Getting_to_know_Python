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
    logger.log_entry("вход (загрузка данных) в справочник")
    
    while True:
        
        action = action_user.choosing_start_work_action()
        
        match action:
            case 1:
                print_data.print_all_list_in_terminal(data)
                logger.log_entry("просмотрены все записи")
            case 2:
                data.append(add_data.input_data_in_phone_directory())
                logger.log_entry("добавлена запись")
            case 3:
                data = submenu_to_delete(data)
            case 4:
                print_data.print_all_list_in_terminal(\
                    search_data.search_data_in_telephone_directory(\
                        data, add_data.input_data_in_phone_directory("search")))
                logger.log_entry("произведен поиск данных")
            case 5:
                data = sort_book.sorting_data(data)
                logger.log_entry("произведена сортировка данных")
            case 6:
                data = l_s_d.loading_data_from_phone_directory()
                logger.log_entry("произведена загрузка данных")
            case 7:
                submenu_to_saving_data(data)
            case 8:
                if submenu_to_exit_from_directory(data) == False: return True

def submenu_to_delete(data: list) -> list:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_to_delete()
        
        match action:
            case 1:
                data = delete_data.delet_data_from_list(data)
                logger.log_entry("удалена запись")
            case 2:
                data = del_rep_rec.delet_repeat_data(data)
                logger.log_entry("удалены повторяющиеся записи")
            case 3: 
                break
        return data

def submenu_to_saving_data(data: list) -> bool:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_to_saving_data()
        
        match action:
            case 1:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
                logger.log_entry("данные сохранены в формате line")
            case 2:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data), "column")
                logger.log_entry("данные сохранены в формате column")
            case 3:
                return False
        return True

def submenu_to_exit_from_directory(data: list) -> bool:
    
    while True:
        
        action = action_user.choosing_action_for_submenu_exit_from_directory()
        
        match action:
            case 1:
                print("данные не сохранены")
                logger.log_entry("выход из справочника без сохранения данных")
                return False
            case 2:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data),\
                    action_user.choosing_action_for_safe())
                logger.log_entry("выход из справочника с сохранением данных")
                print("данные сохранены")
                return False
            case 3: 
                return True