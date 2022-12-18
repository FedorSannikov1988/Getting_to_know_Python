import validation_input_data as v_i_d
import  choosing_action_for_user_interface as action_user
import logger

def sorting_data(data: list) -> list:

    selecting_item_to_sort = action_user.choosing_action_for_sorting_data_choice_number_one()
    logger.log_entry(selecting_item_to_sort[1])

    selection_sort_order = action_user.choosing_action_for_sorting_data_choice_number_two()
    logger.log_entry(selection_sort_order[1])

    match selection_sort_order[0]:
            case 1: flag_sort_order = False
            case 2: flag_sort_order = True

    data = sorted(data, key=lambda list_for_sort: list_for_sort[selecting_item_to_sort[0]-1], reverse = flag_sort_order)
    
    return data