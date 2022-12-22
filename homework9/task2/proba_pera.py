ansver1 = [('Fedor1', 'Sannikov1', 620070), ('Fedor1', 'Sannikov1', 620071)]
ansver2 = [('Fedor1', 'Sannikov1', 620070)]

text = ""

for count_one in ansver2:
    for count_two in count_one:
        text += str(count_two) + " "
    text += "\n"

print(text)