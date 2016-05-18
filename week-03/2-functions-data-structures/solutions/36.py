numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def revert(input):
    reverse = []
    for i in range(len(input)-1, -1, -1):
        reverse += [input[i]]
    return reverse

print(revert(numbers))

def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print('JAJ!', message)

test(revert(numbers), [7,6,5,4,3], 'it should revert the list')
test(revert([1]), [1], 'it should revert lists with 1 item')
test(revert([]), [], 'it should revert empty lists')
