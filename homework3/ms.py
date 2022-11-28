resalt_list = list()

list_positive_fibonacci = [1, 2, 3, 4]

for count in range(1, len(list_positive_fibonacci), 1):
        
    if count%2:
        flag_znak = 1
    else:
        flag_znak = -1
        
    resalt_list.append((flag_znak*list_positive_fibonacci[count-1]))

print(resalt_list)
    
for count in range(0, int(len(resalt_list)/2), 1):

    byffer = resalt_list[count]
    resalt_list[count] = resalt_list[len(resalt_list)-count-1]
    resalt_list[len(resalt_list)-count-1] = byffer