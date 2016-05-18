def greet(name):
    return "hello, "+name


def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print(message)



test(greet(''), 'hello, ', 'it should greet people')
