
win_coordinat = tuple(((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)))

def check_win(game_field: list) -> str|bool:
   
   global win_coordinat

   for item in win_coordinat:
      if game_field[item[0]] == game_field[item[1]] == game_field[item[2]]:
        return game_field[item[0]]
   return False