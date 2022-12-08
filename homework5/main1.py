'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
ход друг после друга. Первый ход определяется жеребьёвкой. За один ход 
можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом""
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

'''
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
Ответ:

Первый игрок должен взять 20 конфет (или 2021 % 29 = 20) и затем поддерживать 
общую сумму взятых конфет на протяжении всех ходов игры 
вторым игроком и им самим (первым игроком) равной 29 конфетам

Насколько понимаю это идея для супер бота которого невозможно обыграть
'''

import random
from pathlib import Path

def entering_name_and_choosing_order_game():

    print("Введите через нажатие клавиши 'Enter' имена двух игроков")
    print("Если хотите сыграть с 'тупым' ботом введи вместо одного из имен 'stupid bot'")
    print("Если хотите сыграть с 'умным' ботом введи вместо одного из имен 'smart bot'")

    player_names = ["",""]
    
    count = 0

    while True:
        
        player_names[count] = input("Имя одного из 2-х игкора: ")
        
        try:
            count += 1
        
        except Exception:
            print("Повторите ввод")
            continue

        if count >1:
            break
    
    game_for_dictionary = {'player1': '','player2': ''}  
    
    if random.randint(0, 100) >= 50:
        game_for_dictionary['player1'] = player_names[0]
        game_for_dictionary['player2'] = player_names[1]
    else:
        game_for_dictionary['player1'] = player_names[1]
        game_for_dictionary['player2'] = player_names[0]
    

    game_for_dictionary["Account " + str(player_names[0])] = 0
    game_for_dictionary["Account " + str(player_names[1])] = 0

    game_for_dictionary["Status " + str(player_names[0])] = ""
    game_for_dictionary["Status " + str(player_names[1])] = ""

    game_for_dictionary["Step this game for end"] = 0

    return game_for_dictionary

def take_input(player_names: str, candies_remained: int):
    
    while True:
        player_answer = input(f"Сколько конфет возьмете {player_names}: ")
        
        try:
            player_answer = int(player_answer)
        
        except Exception:
            print("Повторите ввод количества конфет")
            continue
        

        if (1 <= player_answer <= 28) and (player_answer <= candies_remained): 
            break
        else:
            print("Можно взять от 1 до 28 конфет и не больше чем осталось")
    
    return player_answer

def print_resalt_one(count_step_game: int, quantity_candy: int , game_for_dictionary: dict):
    
    print("\n")
    print(f"Номер хода: {count_step_game}")
    print("----------------------------------")
    print(f"Всего конфет лежит на столе: {quantity_candy}")
    print("----------------------------------")
    print(f"Конфет у {game_for_dictionary['player1']}:", int(game_for_dictionary["Account " + str(game_for_dictionary['player1'])]))
    print("----------------------------------")
    print(f"Конфет у {game_for_dictionary['player2']}:", int(game_for_dictionary["Account " + str(game_for_dictionary['player2'])]))
    print("----------------------------------")
    print("\n")

def print_resalt_two(game_for_dictionary: dict):
    
    print("\n")
    print("После жеребьевки определено что первым ходит:")
    print(game_for_dictionary['player1'])
    print("----------------------------------")
    print("Вторым ходит:")
    print(game_for_dictionary['player2'])
    print("----------------------------------")
    print("\n")

def print_resalt_three(game_for_dictionary: dict):
    
    print("\n")
    print("----------------------------------")
    if game_for_dictionary["Status " + str(game_for_dictionary['player1'])] == "Win":
        print(f"Выйграл {game_for_dictionary['player1']} за ходов:", int(game_for_dictionary["Step this game for end"]))
        print(f"Проиграл {game_for_dictionary['player2']}")
        print(f"{game_for_dictionary['player2']} отдаст {game_for_dictionary['player1']}", int(game_for_dictionary["Account " + str(game_for_dictionary['player2'])]), "конфет")
    else:
        print(f"Выйграл {game_for_dictionary['player2']} за ходов:", int(game_for_dictionary["Step this game for end"]))
        print(f"Проиграл {game_for_dictionary['player1']}")
        print(f"{game_for_dictionary['player1']} отдаст {game_for_dictionary['player2']}", int(game_for_dictionary["Account " + str(game_for_dictionary['player1'])]), "конфет")

def print_resalt_for(results_all_games: str):

    if not results_all_games:
        print("\n")
        print("\n")
        print('СОХРАНЕННЫХ РЕЗУЛЬТАТОВ ИГР НЕТ')
        print("\n")
        print("\n")
    else:
        print("\n")
        print(f"\tВСЕГО СОХРАНЕННО ИГР: {len(results_all_games)}")
        print("\n")
        print("\tРЕЗУЛЬТАТЫ ПОСЛЕДНЕЙ СОХРАНЕННОЙ ИГРЫ:")
        print("\n")
        print("\t", "'"+ results_all_games[len(results_all_games)-1].split("Status ")[1].split(",")[0])
        print("\n")
        print("\t", "'"+ results_all_games[len(results_all_games)-1].split("Status ")[2].split(",")[0])
        print("\n")

file_name_read_and_write = "log_for_game_in_main1.txt"
relative_file_directory_for_read_and_write = Path(file_name_read_and_write)

with open(relative_file_directory_for_read_and_write, 'r') as data:
    
    results_all_games = list()
    
    for line in data:
        results_all_games.append(line)

    for count in range(0, len(results_all_games), 1):
        results_all_games[count] = results_all_games[count].replace('\n', '')

print_resalt_for(results_all_games)

game_for_dictionary = entering_name_and_choosing_order_game()

print_resalt_two(game_for_dictionary)

count_step_game = 1

#для тестирования
#quantity_candy = 50
quantity_candy = 2021

previous_answer_human = 0
    
previous_answer_player = 0

flag_for_smart_bot = "Wait"

while True:

    print_resalt_one(count_step_game, quantity_candy, game_for_dictionary)

    if count_step_game%2 == 0:
        name_games = game_for_dictionary['player2']
    else:
        name_games = game_for_dictionary['player1']

    if name_games == "stupid bot":
        if quantity_candy >= 28:
            player_answer = random.randint(1, 28)
        else:
            player_answer = random.randint(1, quantity_candy)
        print(f"stupid bot взял {player_answer} конфет")

    elif name_games == "smart bot" and count_step_game == 1:
        player_answer = quantity_candy % 29
        flag_for_smart_bot = "Win"
        print(f"smart bot взял {player_answer} конфет")
    
    elif name_games == "smart bot" and flag_for_smart_bot == "Win":
        if quantity_candy >= 28:
            player_answer = 29 - previous_answer_human
        else:
            player_answer = quantity_candy
        print(f"smart bot взял {player_answer} конфет")
    
    elif name_games == "smart bot" and flag_for_smart_bot == "Wait":
        if quantity_candy % 29 <= 28:
            player_answer = quantity_candy % 29
            flag_for_smart_bot = "Win"
        elif quantity_candy % 29 == 0 or quantity_candy % 29 > 28:
            if quantity_candy >= 28:
                player_answer = random.randint(1, 28)
            else:
                player_answer = random.randint(1, quantity_candy)
        print(f"smart bot взял {player_answer} конфет")
    
    else:
        player_answer = take_input(name_games, quantity_candy)
        previous_answer_human = player_answer
    
    previous_answer_player = player_answer

    game_for_dictionary["Account " + str(name_games)] += player_answer

    quantity_candy -= player_answer

    if quantity_candy == 0:

        if game_for_dictionary['player1'] == str(name_games):
            game_for_dictionary["Status " + str(name_games)] = "Win"
            game_for_dictionary["Status " + str(game_for_dictionary['player2'])] = "Loss"
        
        if game_for_dictionary['player2'] == str(name_games):
            game_for_dictionary["Status " + str(name_games)] = "Win"
            game_for_dictionary["Status " + str(game_for_dictionary['player1'])] = "Loss"

        break

    count_step_game += 1

    game_for_dictionary["Step this game for end"] = count_step_game


print_resalt_three(game_for_dictionary)


file_name_read_and_write = "log_for_game_in_main1.txt"
relative_file_directory_for_read_and_write = Path(file_name_read_and_write)


with open(relative_file_directory_for_read_and_write, 'a', encoding='utf-8') as data_out:
    data_out.write(f"{str(game_for_dictionary)}\n")