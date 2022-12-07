w = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 8, 9]

def create_line(resalt_list: list) -> str:
        
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

print(w)

print(create_line(w))