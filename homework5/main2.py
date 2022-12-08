'''
3. Создайте программу для игры в ""Крестики-нолики"".
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

def create_line(resalt_list: list) -> str:
        
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

def playing_field_list(data):
    
    print() 
    print("\t     |     |") 
    print(f"\t  {data[0]}  |  {data[1]}  |  {data[2]}") 
    print("\t_____|_____|_____") 
    
    print("\t     |     |") 
    print(f"\t  {data[3]}  |  {data[4]}  |  {data[5]}") 
    print("\t_____|_____|_____")

    print("\t     |     |") 
    print(f"\t  {data[6]}  |  {data[7]}  |  {data[8]}")
    print("\t     |     |")


def take_input(move, field):

   while True:

      player_answer = input(f"Куда поместить {move}: ")
      
      try:
         player_answer = int(player_answer)
      
      except Exception:
         print("Повторите ввод номера клетки")
         continue
      
      if 1 <= player_answer <= 9:

        if str(field[player_answer-1]) != "X" and str(field[player_answer-1]) != "O":

            field[player_answer-1] = move
            break
        else:
            print("Клеточка занята")
      else:
         print("Введите число от 1 до 9")
   
   return field

def check_win(board):
   
   win_coordinat = tuple(((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)))

   for item in win_coordinat:
      if board[item[0]] == board[item[1]] == board[item[2]]:
        return board[item[0]]
   return False

from pathlib import Path

file_name_read_and_write = "log_for_game_in_main2.txt"
relative_file_directory_for_read_and_write = Path(file_name_read_and_write)

with open(relative_file_directory_for_read_and_write, 'r', encoding='utf-8') as data:
    
    results_all_games = list()
    
    for line in data:
        results_all_games.append(line)

    for count in range(0, len(results_all_games), 1):
        results_all_games[count] = results_all_games[count].replace('\n', '')

if not results_all_games:
    print("\n")
    print("\n")
    print('\tСОХРАНЕННЫХ РЕЗУЛЬТАТОВ ИГР НЕТ')
    print("\n")
    print("\n")
else:
    print("\n")
    print("\n")
    print("\tРЕЗУЛЬТАТЫ ПОСЛЕДНЕЙ СОХРАНЕННОЙ ИГРЫ:")
    playing_field_list(results_all_games[len(results_all_games)-1].split(" "))
    print("__________________________")

field_for_game = list(range(1,10,1))
playing_field_list(field_for_game)
count = 0

while True:

    if count%2 == 0:
        field_for_game = take_input("X", field_for_game)
    else:
        field_for_game = take_input("O", field_for_game)
    
    count += 1

    if count > 4:
        
        byffer = check_win(field_for_game)

        if byffer:
            print(f"{byffer} выйграл !")
            break
    
    if count == 9:
        print("Ничья!")
        break

    playing_field_list(field_for_game)

with open(relative_file_directory_for_read_and_write, 'a', encoding='utf-8') as data_out:
    data_out.write(f"{create_line(field_for_game)}\n")