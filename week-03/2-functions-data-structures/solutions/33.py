ag = 'kuty'
# write a function that gets a string as an input
# and appends an 'a' character to its end

def add_a(input):
    return str(input) + 'a'

print(add_a(ag))
print(add_a('cic'))
print(add_a('burgony'))
print(add_a('krumpl'))
print(add_a('bek'))

def test(expected, actual):
    if expected == actual:
        print('check')
    else:
        print('JAJ')

test(add_a('cic'), 'cica')
test(add_a('burgony'), 'burgonya')
test(add_a('krumpl'), 'krumpla')
test(add_a('bek'), 'beka')
test(add_a(0), '0a')
