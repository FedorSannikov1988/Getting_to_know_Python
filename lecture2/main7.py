
def concatenatio_1(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio_1('p', 'r', 'i', 'v', 'e', 't')) 
print(concatenatio_1('a', '*', 'd', '2', '$'))

def concatenatio_2(*params):
    res: int = 0
    for item in params:
        res += item
    return res

print(concatenatio_2(1, 2, 3, 4)) 