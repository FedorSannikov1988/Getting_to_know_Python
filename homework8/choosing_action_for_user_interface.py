import validation_input_data as v_i_d

def choosing_start_work_action()-> list():

    dictionary_for_choosing_start_work_action = \
        {1: 'просмотреть все записи в справочнике',\
            2: 'добавить запись в справочник',\
                3: 'меню удаление запис(-и)(-ей) из справочника',\
                    4: 'найти запись в справочнике',\
                        5: 'сортировать записи',\
                            6: 'загрузить данные (данные загруженные или добавленные ранее во время сессии будут утеряны)',\
                                7: 'меню сохранения данных',\
                                    8: 'меню выхода из справочника'} 

    print("\n")
    print("\t       ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_choosing_start_work_action[1]}")
    print(f"\t 2 -  {dictionary_for_choosing_start_work_action[2]}")
    print(f"\t 3 -  {dictionary_for_choosing_start_work_action[3]}")
    print(f"\t 4 -  {dictionary_for_choosing_start_work_action[4]}")
    print(f"\t 5 -  {dictionary_for_choosing_start_work_action[5]}")
    print(f"\t 6 -  {dictionary_for_choosing_start_work_action[6]}")
    print(f"\t 7 -  {dictionary_for_choosing_start_work_action[7]}")
    print(f"\t 8 -  {dictionary_for_choosing_start_work_action[8]}")
    print("")
    
    byffer = v_i_d.validation_human_answer(8, 1)
    
    return [byffer , dictionary_for_choosing_start_work_action[byffer]]

def choosing_action_for_safe() -> list():

    dictionary_for_choosing_action_for_safe =\
        {1: 'в столбик', 2: 'в сторочку'}

    print("\n")
    print("\t     В КАКОМ ФОРМАТЕ СОХРАНИТЬ ДАННЫЕ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_choosing_action_for_safe[1]}")
    print("\t пример:")
    print("\t Фамилия1")
    print("\t Имя1")
    print("\t Отчество1")
    print("\t Телефон1")
    print("\t","-"*10)
    print("\t Фамилия2")
    print("\t Имя2")
    print("\t Отчество2")
    print("\t Телефон2")
    print("\t","-"*41)
    print(f"\t 2 -  {dictionary_for_choosing_action_for_safe[2]}")
    print("\t пример:")
    print("\t Фамилия1;Имя1;Отчество1;Телефон1")
    print("\t Фамилия2;Имя2;Отчество2;Телефон2")

    human_answer_namber = v_i_d.validation_human_answer(2, 1)

    if human_answer_namber == 1:
        return ["column", dictionary_for_choosing_action_for_safe[human_answer_namber]]
    elif human_answer_namber == 2:
        return ["line", dictionary_for_choosing_action_for_safe[human_answer_namber]]

def choosing_action_for_submenu_to_saving_data() -> list():
    
    dictionary_for_choosing_action_for_submenu_to_saving_data = \
        {1: 'сохранить данные в формате: line',\
             2: 'сохранить данные в формате: column',\
                3: 'вернуться в основное меню',}
    
    print("\n")
    print("\t\t  МЕНЮ СОХРАНЕНИЯ ДАННЫХ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_choosing_action_for_submenu_to_saving_data[1]}")
    print(f"\t 2 -  {dictionary_for_choosing_action_for_submenu_to_saving_data[2]}")
    print(f"\t 3 -  {dictionary_for_choosing_action_for_submenu_to_saving_data[3]}")
    print("")

    byffer = v_i_d.validation_human_answer(3, 1)

    return [byffer , dictionary_for_choosing_action_for_submenu_to_saving_data[byffer]]

def choosing_action_for_submenu_exit_from_directory() -> list():
    
    dictionary_for_choosing_action_for_submenu_exit_from_directory = \
        {1: 'выйти из справочника без сохранения изминений и удаления повторов в телефонной книге',\
             2: 'выйти из справочника с сохранением изминений в телефонной книге',\
                3: 'вернуться в основное меню',}
    
    print("\n")
    print("\t\t\tМЕНЮ ВЫХОДА")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 - {dictionary_for_choosing_action_for_submenu_exit_from_directory[1]}")
    print(f"\t 2 - {dictionary_for_choosing_action_for_submenu_exit_from_directory[2]}")
    print(f"\t 3 - {dictionary_for_choosing_action_for_submenu_exit_from_directory[3]}")
    print("\t","-"*41)
    print("\t Примечание к пункту 2:")
    print("\t При выходе из справочника данные автоматически сохраняются.")
    print("\t Пользователю предоставляеся выбор в каком формате line или")
    print("\t column данные будут сохранены. Так же происходит удаление")
    print("\t повторяющихся записей.")
    print("")
    
    byffer = v_i_d.validation_human_answer(3, 1)
    
    return [byffer , dictionary_for_choosing_action_for_submenu_exit_from_directory[byffer]]

def choosing_action_for_submenu_to_delete() -> list():

    dictionary_for_choosing_action_for_submenu_to_delete = \
        {1: 'удалить запис(-и)(-ь) из справочника',\
             2: 'удалить повторяющиеся записи',\
                3: 'вернуться в основное меню',}

    print("\n")
    print("\t\t   МЕНЮ УДАЛЕНИЯ ДАННЫХ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_choosing_action_for_submenu_to_delete[1]}")
    print(f"\t 2 -  {dictionary_for_choosing_action_for_submenu_to_delete[2]}")
    print(f"\t 3 -  {dictionary_for_choosing_action_for_submenu_to_delete[3]}")
    print("")
    
    byffer = v_i_d.validation_human_answer(3, 1)

    return [byffer, dictionary_for_choosing_action_for_submenu_to_delete[byffer]]

def choosing_action_for_delet_data_from_list() -> list():
    
    dictionary_for_delet_data_from_list = \
        {1: 'удалить записи по их порядковому номеру',\
            2: 'удалить записи по Ф.И.О.'}
    
    print("\n")
    print("\t ПРОЦЕДУРА УДАЛЕНИЯ ДАННЫХ:")
    print("\t---------------------------")
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_delet_data_from_list[1]}")
    print(f"\t 2 -  {dictionary_for_delet_data_from_list[2]}") 
    
    human_answer_namber = v_i_d.validation_human_answer(2, 1)
    
    return [human_answer_namber, dictionary_for_delet_data_from_list[human_answer_namber]]

def choosing_action_for_delete_FIO() -> list():
    
    dictionary_for_delete_FIO = {1: 'удалить', 2: 'не удалить'}

    print("\n")
    print("\t УДАЛИТЬ ЭТИ ДАННЫЕ:")
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_delete_FIO[1]}")
    print(f"\t 2 -  {dictionary_for_delete_FIO[2]}")

    human_answer_namber = v_i_d.validation_human_answer(2, 1)

    return [human_answer_namber, dictionary_for_delete_FIO[human_answer_namber]]

def choosing_action_for_sorting_data_choice_number_one() -> list():
    
    dictionary_for_sorting_data_choice_number_one = \
        {1: 'фамилии', 2: 'имени', 3: 'отчеству', 4: 'номеру телефона'}

    print("\n")
    print("\t\t   СОРТИРОВАТЬ ЗАПИСИ ПО")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_sorting_data_choice_number_one[1]}")
    print(f"\t 2 -  {dictionary_for_sorting_data_choice_number_one[2]}")
    print(f"\t 3 -  {dictionary_for_sorting_data_choice_number_one[3]}")
    print(f"\t 4 -  {dictionary_for_sorting_data_choice_number_one[4]}")
    print("\n")

    human_answer_namber = v_i_d.validation_human_answer(4, 1)

    return [human_answer_namber, dictionary_for_sorting_data_choice_number_one[human_answer_namber]]

def choosing_action_for_sorting_data_choice_number_two() -> list():
    
    dictionary_for_sorting_data_choice_number_two = \
        {1: 'убыванию', 2: 'возрастанию'}

    print("\n")
    print("\t\t ВОЗРАСТАНИЮ ИЛИ УБЫВАНИЮ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print(f"\t 1 -  {dictionary_for_sorting_data_choice_number_two[1]}")
    print(f"\t 2 -  {dictionary_for_sorting_data_choice_number_two[2]}")
    print("\n")
    
    human_answer_namber = v_i_d.validation_human_answer(2, 1)

    return [human_answer_namber, dictionary_for_sorting_data_choice_number_two[human_answer_namber]]