import validation_input_data as v_i_d

def sorting_data(data: list) -> list:
    
    '''
    можно изящнее но нет времени
    '''

    print("\n")
    print("\t\t   СОРТИРОВАТЬ ЗАПИСИ ПО")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  фамилии")
    print("\t 2 -  имени")
    print("\t 3 -  отчеству")
    print("\t 4 -  номеру телефона")
    print("\n")

    selecting_item_to_sort = v_i_d.validation_human_answer(4, 1)

    print("\n")
    print("\t\t ВОЗРАСТАНИЮ ИЛИ УБЫВАНИЮ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  убывание")
    print("\t 2 -  возрастанию")
    print("\n")

    if v_i_d.validation_human_answer(2, 1) == 1:
        flag_sort_order = False
    else:
        flag_sort_order = True

    data = sorted(data, key=lambda list_for_sort: list_for_sort[selecting_item_to_sort-1], reverse = flag_sort_order)
    
    return data