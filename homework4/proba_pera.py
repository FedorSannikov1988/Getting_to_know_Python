'''
откудато содрал но чательно протестировал
'''

a = (
      {'Петя': 6, 'Вася': 8, 'Дима': 11, 'Юля': 3},
      {'Петя': 5, 'Вася': 36, 'Дима': 4, 'Юля': 8},
      {'Петя': 54, 'Вася': 21, 'Дима': 22, 'Юля': 39},
      {'Петя': 61, 'Вася': 48, 'Дима': 71, 'Юля': 73}
    )

resultdict = {}

for dictionary in a:
  for key in dictionary:
    try:
      resultdict[key] += dictionary[key] 
    except KeyError:                        
      resultdict[key] = dictionary[key]   

print(resultdict)