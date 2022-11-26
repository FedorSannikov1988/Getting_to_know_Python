word = "-"

match word:
    case 'print0':
        print("0")
    case 'print1':
        print("1")
    case int(word):
        print("int")
    case _:
        print("zero")

        