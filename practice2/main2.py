'''   
3. Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другой.
'''

text1 = 'Я люблю Пайтон'
text2 = 'Я'
print(text1.count(text2))

if text1.count(text2) == 0:
    print('Не входит !')
else:
    print('Входит')

text3 = "Я люблю Пайтон"
text4 = "Я"
print(text3.find(text4))

if text3.find(text4) == -1:
    print("Не входит !")
else:
    print("Входит")