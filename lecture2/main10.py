t = ()
print(type(t)) # tuple

t = (1,)
print(type(t)) # tuple

t = (1)
print(type(t)) # int

t = (28, 9, 1990)
print(type(t)) # tuple

colors = ['red', 'green', 'blue']

#список
print("список")
print(colors) # ['red', 'green', 'blue']

#сделали из списка кортеж !
t = tuple(colors)
print("кортеж")
print(t)