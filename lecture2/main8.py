
def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for count in range(0, 25):
    list.append(fib(count))

print(list)