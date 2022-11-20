text = 'съешь ещё этих мягких французских БУЛОК'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) 

for c in text:
    print(c)