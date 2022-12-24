def clearing_line_from_bot_telegrams(line: str, search_text: str) -> str:
    
    list_string = list(line.split(" "))
    
    resalt_list = list()
    
    for count in range(0, len(list_string), 1):
        
        if list_string[count].count(search_text) == 0:
            resalt_list.append(list_string[count])
    
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

'''
как будет время напишу лучше (без дублей):
'''
def print_answer_for_bot_v1(data_in: list) -> str:

        if data_in == []: 
            ansver = "по вашему запросу данные не найдены"
        else:
            ansver = ""
            for count_one in data_in:
                for count_two in count_one:
                    ansver += str(count_two) + " "
                ansver += "\n"
        
        return ansver

'''
время появилось:
'''
def print_answer_for_bot_v2(data_in: list) -> str:

        if data_in == []: 
            ansver = "по вашему запросу данные не найдены"
        else:
            ansver = ""
            left_border = 0
            right_border = 1
            
            ansver += str(data_in[left_border][0]) \
                + " " + str(data_in[left_border][1]) + \
                    " " + str(data_in[left_border][2])
            
            if len(data_in) > 1:
                while True:
                    if data_in[left_border][0] == data_in[left_border+right_border][0] \
                        and data_in[left_border][1] == data_in[left_border+right_border][1]:
                        
                        ansver += " " + str(data_in[left_border+right_border][2])
                        right_border +=1
                        if left_border+right_border == len(data_in): break
                    
                    else:
                        left_border += right_border
                        right_border = 1
                        ansver += "\n"
                        ansver += str(data_in[left_border][0]) \
                            + " " + str(data_in[left_border][1]) + \
                                " " + str(data_in[left_border][2])
                        if left_border+right_border == len(data_in): break
        
        return ansver