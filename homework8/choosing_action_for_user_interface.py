import validation_input_data as v_i_d

def choosing_start_work_action() -> None:

    print("\n")
    print("\t       ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  просмотреть все записи в справочнике")
    print("\t 2 -  добавить запись в справочник")
    print("\t 3 -  меню удаление запис(-и)(-ей) из справочника")
    print("\t 4 -  найти запись в справочнике")
    print("\t 5 -  сортировать записи")
    print("\t 6 -  загрузить данные (данные загруженные")
    print("\t      или добавленные ранее во время сессии")
    print("\t      будут утеряны)")
    print("\t 7 -  меню сохранения данных")
    print("\t 8 -  меню выхода из справочника")
    print("")
      
    return v_i_d.validation_human_answer(8, 1)

def choosing_action_for_safe() -> None:

    print("\n")
    print("\t     В КАКОМ ФОРМАТЕ СОХРАНИТЬ ДАННЫЕ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 - в столбик")
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
    print("\t 2 - в сторочку")
    print("\t пример:")
    print("\t Фамилия1;Имя1;Отчество1;Телефон1")
    print("\t Фамилия2;Имя2;Отчество2;Телефон2")

    human_answer_namber = v_i_d.validation_human_answer(2, 1)

    if human_answer_namber == 1:
        return "column"
    elif human_answer_namber == 2:
        return "line"

def choosing_action_for_submenu_to_delete() -> None:

    print("\n")
    print("\t\t   МЕНЮ УДАЛЕНИЯ ДАННЫХ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  удалить запис(-и)(-ь) из справочника")
    print("\t 2 -  удалить повторяющиеся записи")
    print("\t 3 -  вернуться в основное меню")
    print("")
    
    return v_i_d.validation_human_answer(3, 1)

def choosing_action_for_submenu_to_saving_data() -> None:
    
    print("\n")
    print("\t\t  МЕНЮ СОХРАНЕНИЯ ДАННЫХ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  сохранить данные в формате: line")
    print("\t 2 -  сохранить данные в формате: column")
    print("\t 3 -  вернуться в основное меню")
    print("")

    return v_i_d.validation_human_answer(3, 1)

def choosing_action_for_submenu_exit_from_directory() -> None:
    
    print("\n")
    print("\t\t\tМЕНЮ ВЫХОДА")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 - выйти из справочника без сохранения")
    print("\t     изминений и удаления повторов")
    print("\t     в телефонной книге")
    print("\t 2 - выйти из справочника с сохранением")
    print("\t     изминений в телефонной книге")
    print("\t 3 - вернуться в основное меню")
    print("\t","-"*41)
    print("\t Примечание к пункту 2:")
    print("\t При выходе из справочника данные автоматически сохраняются.")
    print("\t Пользователю предоставляеся выбор в каком формате line или")
    print("\t column данные будут сохранены. Так же происходит удаление")
    print("\t повторяющихся записей.")
    print("")
    
    return v_i_d.validation_human_answer(3, 1)