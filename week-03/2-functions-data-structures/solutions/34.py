numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def summacska(input):
    summa = input[0]
    for i in range(1,len(input)):
        summa += input[i]
    return summa

print(summacska(numbers))
print(summacska([1,2]))

def test(expected, actual):
    if expected == actual:
        print('check')
    else:
        print('JAJ')

test(summacska(numbers), 49)
test(summacska([2,2]), 4)
test(summacska([2234,34532,53445,34535]), 2234+34532+53445+34535)
test(summacska(['sum','macska']), 'summacska')
# SKIP test(summacska(['sum',123]), 'sum123')
