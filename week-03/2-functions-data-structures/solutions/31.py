ae = 'Jozsi'
# create a function that greets ae

def greet(name="Valaki"):
    return 'hello, '+str(name)

print(greet(ae))

def test(expected, actual):
    if expected == actual:
        print('check')
    else:
        print('JAJ')

test(greet(ae), 'hello, Jozsi')
test(greet('Bela'), 'hello, Bela')
test(greet(''), 'hello, ')
test(greet('Feco'), 'hello, Feco')
test(greet(), 'hello, Valaki')
test(greet(0), 'hello, 0')
test(greet(666), 'hello, 666')
test(greet('Esmeralda'), 'hello, Esmeralda')
test(greet('Esmer/+alda'), 'hello, Esmer/+alda')
test(greet('\nEsmeralda'), 'hello, \nEsmeralda')
test(greet('\nárvíztűrő'), 'hello, \nárvíztűrő')
test(greet('Béla Bácsi'), 'hello, Béla Bácsi')
