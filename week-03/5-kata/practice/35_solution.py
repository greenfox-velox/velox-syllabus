# create a function that returns it's input factorial

# 1

def factorial1(num):
    output = 1
    i = 1
    while i <= num:
        output *= i
        i += 1
    return output

print(factorial1(6))

# 2

def factorial2(num):
    output = 1
    for n in range(1, num + 1):
        output *= n
    return output

print(factorial2(7))

# 3
def factorial3(num):
    if num == 1:
        return 1
    else:
        return factorial3(num - 1) * num

print(factorial3(3))







