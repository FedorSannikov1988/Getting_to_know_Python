'''
def choose_an_action(exit_choice=False):
    func_dict = {
        1: lambda: search(),
        2: lambda: print_directory(),
        3: lambda: add_contact(),
        4: lambda: delete_contact(),
        5: lambda: view.print_choose_action_menu(),
        6: lambda: print('hi')
    }
    checking_existence_bd()
    view.print_choose_action_menu()
    while not exit_choice:
        choice = view.input_choose()
        if func_dict.get(choice, None) is not None:
            func_dict[choice]()

clear() - системная комманда
'''

'''
работали в комманде
'''