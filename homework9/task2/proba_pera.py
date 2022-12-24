
ansver = [('Fedor1', 'Sannikov1', 620070), ('Fedor1', 'Sannikov1', 620071), ('Fedor2', 'Sannikov2', 620072), ('Fedor2', 'Sannikov2', 620073), ('Fedor2', 'Sannikov2', 620074)]

#ansver = [('Fedor1', 'Sannikov1', 620070), ('Fedor1', 'Sannikov1', 620071)]

#ansver = [('Fedor1', 'Sannikov1', 620070)]

'''
ansver_str = ""
left_border = 0
right_border = 1

ansver_str += str(ansver[left_border][0]) + " " + str(ansver[left_border][1]) + " " + str(ansver[left_border][2])

if len(ansver) > 1: 
    while True:
        if ansver[left_border][0] == ansver[left_border+right_border][0] \
            and ansver[left_border][1] == ansver[left_border+right_border][1]:
            
            ansver_str += " " + str(ansver[left_border+right_border][2])
            right_border +=1
            if left_border+right_border == len(ansver): break
        
        else:
            left_border += right_border
            right_border = 1
            ansver_str += "\n"
            ansver_str += str(ansver[left_border][0]) + " " + str(ansver[left_border][1]) + " " + str(ansver[left_border][2])
            if left_border+right_border == len(ansver): break

print(ansver_str)
'''