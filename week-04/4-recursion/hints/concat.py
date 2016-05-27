# fill a list with numbers from n to 1

def concat(n):
    if n <= 0:
        return []
    else:
        prevstep = concat(n-1)
        prevstep = [n] + prevstep
        return prevstep


print(concat(3))
