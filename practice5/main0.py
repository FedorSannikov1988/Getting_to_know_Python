'''
1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
--> 'Я люблю абвЖвау иабв Питон'
--> 'Я люблю Питон'
# включений, filter, map
'''

'''
string = 'Я люблю абвЖвау иабв Питон'.split(" ")
print(string)

z = "абв"
filter_one = list(filter(lambda x: not z in x, string))
#filter_one = list(filter(lambda x: z in x, string))
print(filter_one)
'''

a = 'Я люблю абвЖвау иабв Питон'.split(' ')
print(a)
b = 'абв'
list1 = [a[i] for i in range(len(a)) if not (b in a[i])]
print(list1)