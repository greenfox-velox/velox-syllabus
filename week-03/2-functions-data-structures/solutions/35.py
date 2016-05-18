# create a function that returns it's input factorial

def factorial(input_number):
    factorta = 1
    for i in range(1,input_number+1):
        factorta *= i
    return factorta

print(factorial(5))

def test(expected, actual):
    if expected == actual:
        print('check')
    else:
        print('JAJ')

test(factorial(5), 120)
test(factorial(10), 3628800)
test(factorial(11), 39916800)
test(factorial(0), 1)
