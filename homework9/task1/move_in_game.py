def make_move_in_game(move: str, game_field: list) -> list:

   while True:

      player_answer = input(f"Номер клетки для {move}: ")
      
      try:
        player_answer = int(player_answer)
      
      except ValueError:
        print("Повторите ввод номера клетки")
        continue
      
      if 1 <= player_answer <= 9:

        if str(game_field[player_answer-1]) != "X" and str(game_field[player_answer-1]) != "O":
            game_field[player_answer-1] = move
            break
        else:
            print("Клетка занята")
      else:
         print("Введите число от 1 до 9")

   return game_field