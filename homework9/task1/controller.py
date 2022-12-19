import viev
import check_win as c_w
import move_in_game as m_g
import emoji
from isOdd import isOdd

def playing_in_tic_tac_toe() -> None:

    field_for_game = list(range(1,10,1))
    
    viev.print_playing_field(field_for_game)
    
    count = 0
    
    while True:
        
        if not isOdd(count):
            field_for_game = m_g.make_move_in_game("X", field_for_game)
        else:
            field_for_game = m_g.make_move_in_game("O", field_for_game)
        
        count += 1
        
        if count > 4:
            byffer = c_w.check_win(field_for_game)

            if byffer == "X" or byffer == "O":
                print(f"{emoji.emojize(':beaming_face_with_smiling_eyes:')} Выйграл {byffer}!{emoji.emojize(':beaming_face_with_smiling_eyes:')}")
                
                break
        
        if count == 9:
            print(f"{emoji.emojize(':expressionless_face:')} Ничья!{emoji.emojize(':expressionless_face:')}")
            break
        
        viev.print_playing_field(field_for_game)