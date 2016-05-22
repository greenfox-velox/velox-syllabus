def multiply(a, b):
    return a * -b




def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print(message)



test(multiply(1, 2), 2, 'it should multiply numbers')

