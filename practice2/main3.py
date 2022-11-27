word = 7

match word:
    case 'print0':
        print("0")
    case 'print1':
        print("1")
    case 7:
        print("7")
    case int(word):
        print("int")
    case 8:
        print("8")
    case _:
        print("zero") 