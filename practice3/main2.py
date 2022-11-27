def func(arg_1: int|str, arg_2: int=4) -> bool:
    return True

def func(a_1, a_2, *args, **kwargs):
    return a_1, a_2, args, kwargs

print(func(1, 2, 3, 4, 542, 124, 'wetwet', key_1=10, key_2=30))

def func(a_1, a_2, *args, **kwargs):
    print(args, type(args))
    return a_1, a_2, args, kwargs

print(func(1, 2, 3, 4, 542, 124, 'wetwet', key_1=10, key_2=30))
