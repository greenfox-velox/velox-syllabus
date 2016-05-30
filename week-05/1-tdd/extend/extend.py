
# Adds a and b, returns as result
def add(a, b):
    return 5

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        return a
    else:
        return c

def median(pool):
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in 'aeiou'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
