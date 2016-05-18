af = 123
# create a function that doubles it's input
# double af with it

def double(input):
    return input * 2

print(double(af))

def test(expected, actual):
    if expected == actual:
        print('check')
    else:
        print('JAJ')

test(double(2), 4)
test(double(0), 0)
test(double('Bela'), 'BelaBela')
test(double(1.234), 1.234*2)
