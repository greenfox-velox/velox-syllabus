numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens


def filter_odds(input):
    evens = []
    for item in input:
        if item % 2 == 0:
            evens += [item]
    return evens

print(filter_odds(numbers))
